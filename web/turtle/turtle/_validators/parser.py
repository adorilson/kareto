import ast
import math

from browser import document, window

from _validators import get_line_points, fail

# PRIVATE API
def _is_turtle_constructor(call):
    if isinstance(call.func, ast.Attribute):
        return isinstance(call.func.value, ast.Name)and call.func.value.id == 'turtle' and call.func.attr == 'Turtle'
    if isinstance(call.func, ast.Name):
        return call.func.id == 'Turtle'
    return False


def _get_literal_str(node):
    if isinstance(node, ast.Constant)and isinstance(node.value, str):
        return node.value
    return None


def _get_literal_number(node):
    if isinstance(node, ast.Constant)and isinstance(node.value, (int, float)):
        return float(node.value)
    return None


def _extract_color_list(tree, var_name):
    colors = None
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name)and target.id == var_name:
                    value = node.value
                    if isinstance(value, (ast.List, ast.Tuple)):
                        entries = []
                        for elt in value.elts:
                            entries.append(_get_literal_str(elt))
                        colors = entries
    return colors


def collect_turtle_call_metrics(code):
    tree = ast.parse(code, '<string>')

    turtle_names = set()
    forward_values = []
    right_values = []
    left_values = []

    for node in ast.walk(tree):
        if isinstance(node, ast.Assign)and isinstance(node.value, ast.Call):
            if _is_turtle_constructor(node.value):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        turtle_names.add(target.id)

        if isinstance(node, ast.Call)and isinstance(node.func, ast.Attribute):
            if isinstance(node.func.value, ast.Name)and node.func.value.id in turtle_names:
                method = node.func.attr
                if method in {'forward', 'fd'} and node.args:
                    forward_values.append(_get_literal_number(node.args[0]))
                if method == 'right' and node.args:
                    right_values.append(_get_literal_number(node.args[0]))
                if method == 'left' and node.args:
                    left_values.append(_get_literal_number(node.args[0]))

    forward_literal = [val for val in forward_values if val is not None]
    right_literal = [val for val in right_values if val is not None]
    left_literal = [val for val in left_values if val is not None]

    return {
        'codeForwardCount': len(forward_values),
        'codeForwardLiteralCount': len(forward_literal),
        'codeForwardUnique': len(set(forward_literal)),
        'codeRightCount': len(right_values),
        'codeRightLiteralCount': len(right_literal),
        'codeLeftCount': len(left_values),
        'codeLeftLiteralCount': len(left_literal),
        'codeTurnCount': len(right_values) + len(left_values),
    }


def _rule_ok(rule, metrics_lookup):
    metric = rule.get('metric')
    op = rule.get('op')
    if isinstance(op, str):
        op = op.replace('&gt;', '>').replace('&lt;', '<').replace('&amp;', '&').strip()
    value = rule.get('value')
    tol = float(rule.get('tol', rule.get('eps', 0)))
    min_val = rule.get('min')
    max_val = rule.get('max')

    if metric not in metrics_lookup:
        window.console.log(f'Unknown metric: {metric}')
        return False

    actual = metrics_lookup[metric]

    if op == 'approx':
        return abs(actual - float(value)) <= tol
    if op == 'between':
        if min_val is None or max_val is None:
            return False
        return float(min_val) <= actual <= float(max_val)
    if op == '==':
        return actual == value
    if op == '!=':
        return actual != value
    if op == '>':
        return actual > float(value)
    if op == '>=':
        return actual >= float(value)
    if op == '<':
        return actual < float(value)
    if op == '<=':
        return actual <= float(value)

    window.console.log(f'Unknown op: {op}')
    return False


# PUBLIC API

def run_code_rules_test(test_case):
    code_rules = test_case.get('codeRules', [])
    if not code_rules:
        return

    msg = test_case.get('msg', 'Não está pronto.')
    code_metrics = collect_turtle_call_metrics(document['editoraux'].value)
    for rule in code_rules:
        if not _rule_ok(rule, code_metrics):
            window.console.log(f'Code rule failed: {rule}')
            fail(rule.get('msg', msg))




def run_code_requirements_test(test_case):
    msg_color = test_case.get('msgColor', 'A cor da linha deve ser diferente de vermelho.')
    msg_shape = test_case.get('msgShape', 'O formato da tartaruga deve ser diferente do padrao classic.')
    msg_size = test_case.get('msgSize', 'O tamanho do quadrado deve ser diferente de 100.')
    require_color = bool(test_case.get('requireColorChange', True))
    require_shape = bool(test_case.get('requireShapeChange', True))
    require_size = bool(test_case.get('requireSquareSizeChange', True))

    code = document['editoraux'].value
    tree = ast.parse(code, '<string>')

    turtle_names = set()
    color_values = []
    shape_values = []
    forward_values = []

    for node in ast.walk(tree):
        if isinstance(node, ast.Assign)and isinstance(node.value, ast.Call):
            if _is_turtle_constructor(node.value):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        turtle_names.add(target.id)

        if isinstance(node, ast.Call)and isinstance(node.func, ast.Attribute):
            if isinstance(node.func.value, ast.Name)and node.func.value.id in turtle_names:
                method = node.func.attr
                if method in {'color', 'pencolor'} and node.args:
                    color_values.append(_get_literal_str(node.args[0]))
                if method == 'shape' and node.args:
                    shape_values.append(_get_literal_str(node.args[0]))
                if method in {'forward', 'fd'} and node.args:
                    forward_values.append(_get_literal_number(node.args[0]))

    if require_color:
        if not color_values or all(value is None or value == 'red' for value in color_values):
            fail(msg_color)

    if require_shape:
        if not shape_values or all(value is None or value == 'classic' for value in shape_values):
            fail(msg_shape)

    if require_size:
        if not forward_values or all(value is None or abs(value - 100) < 1e-6 for value in forward_values):
            fail(msg_size)


def run_turtle_sequence_test(test_case):
    msg_shape = test_case.get('msgShape', 'A forma da tartaruga deve ser diferente do padrao classic.')
    msg_colors = test_case.get('msgColors', 'A ordem das cores deve ser diferente da original.')
    msg_pensize = test_case.get('msgPensize', 'A largura da linha deve ser diferente de 5.')
    msg_squares = test_case.get('msgSquares', 'A tartaruga deve desenhar dois quadrados.')

    code = document['editoraux'].value
    tree = ast.parse(code, '<string>')

    turtle_names = set()
    color_values = []
    shape_values = []
    pensize_values = []
    forward_values = []
    turn_values = []

    for node in ast.walk(tree):
        if isinstance(node, ast.Assign)and isinstance(node.value, ast.Call):
            if _is_turtle_constructor(node.value):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        turtle_names.add(target.id)

        if isinstance(node, ast.Call)and isinstance(node.func, ast.Attribute):
            if isinstance(node.func.value, ast.Name)and node.func.value.id in turtle_names:
                method = node.func.attr
                if method in {'color', 'pencolor'} and node.args:
                    color_values.append(_get_literal_str(node.args[0]))
                if method == 'shape' and node.args:
                    shape_values.append(_get_literal_str(node.args[0]))
                if method == 'pensize' and node.args:
                    pensize_values.append(_get_literal_number(node.args[0]))
                if method in {'forward', 'fd'} and node.args:
                    forward_values.append(_get_literal_number(node.args[0]))
                if method in {'right', 'left'} and node.args:
                    turn_values.append(_get_literal_number(node.args[0]))

    if not shape_values or all(value is None or value == 'classic' for value in shape_values):
        fail(msg_shape)

    required_colors = ['blue', 'black', 'red', 'pink']
    if len(color_values)< 4:
        fail(msg_colors)
    first_four = color_values[:4]
    if any(value is None for value in first_four):
        fail(msg_colors)
    if set(first_four)!= set(required_colors):
        fail(msg_colors)
    if first_four == required_colors:
        fail(msg_colors)

    if not pensize_values or all(value is None or abs(value - 5)< 1e-6 for value in pensize_values):
        fail(msg_pensize)

    forward_count = sum(1 for value in forward_values if value is not None)
    turn_count = sum(1 for value in turn_values if value is not None and abs(value - 90)< 1e-6)
    if forward_count < 8 or turn_count < 8:
        fail(msg_squares)



def run_random_colors_triangle_test(test_case):
    msg_colors = test_case.get('msgColors', 'A lista de cores deve conter mais cores e nao pode incluir vermelho.')
    msg_pensize = test_case.get('msgPensize', 'A largura da linha deve ser alterada.')

    min_colors = int(test_case.get('minColors', 5))
    forbidden = set(test_case.get('forbidColors', ['red']))
    colors_var = test_case.get('colorsVar', 'cores')

    code = document['editoraux'].value
    tree = ast.parse(code, '<string>')

    colors = _extract_color_list(tree, colors_var)
    if not colors:
        fail(msg_colors)
    if any(color is None for color in colors):
        fail(msg_colors)
    if len(colors)< min_colors:
        fail(msg_colors)
    if forbidden.intersection(colors):
        fail(msg_colors)

    turtle_names = set()
    pensize_values = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign)and isinstance(node.value, ast.Call):
            if _is_turtle_constructor(node.value):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        turtle_names.add(target.id)

        if isinstance(node, ast.Call)and isinstance(node.func, ast.Attribute):
            if isinstance(node.func.value, ast.Name)and node.func.value.id in turtle_names:
                if node.func.attr == 'pensize' and node.args:
                    pensize_values.append(_get_literal_number(node.args[0]))

    if not pensize_values or all(value is None for value in pensize_values):
        fail(msg_pensize)

    triangle_case = {
        'side': float(test_case.get('side', 100)),
        'sideTol': float(test_case.get('sideTol', 8)),
        'closeEps': float(test_case.get('closeEps', 5)),
        'baseEps': float(test_case.get('baseEps', 6)),
        'minHeightRatio': float(test_case.get('minHeightRatio', 0.5)),
        'msg': test_case.get('msgTriangle', 'A tartaruga deve ter desenhado um triangulo apontando para cima.')
    }

    from _validators import shapes
    shapes.run_triangle_test(triangle_case)


def run_envelope_test(test_case):
    msg_size = test_case.get('msgSize', 'O envelope deve ser maior do que o original.')
    msg_shape = test_case.get('msgShape', 'Use formas diferentes para a aba e o corpo.')
    msg_color = test_case.get('msgColor', 'O envelope deve ser colorido.')
    msg_flap = test_case.get('msgFlap', 'A aba do envelope deve ser menor que o corpo.')

    require_size = bool(test_case.get('requireSize', True))
    require_shape = bool(test_case.get('requireShape', True))
    require_color = bool(test_case.get('requireColor', True))
    require_flap_ratio = bool(test_case.get('requireFlapRatio', True))
    require_orientation = bool(test_case.get('requireOrientation', True))

    min_scale = float(test_case.get('minScale', 1.05))
    flap_ratio = float(test_case.get('flapRatio', 0.9))
    top_tol = float(test_case.get('topTol', 3))
    align_tol = float(test_case.get('alignTol', 3))

    code = document['editoraux'].value
    tree = ast.parse(code, '<string>')

    turtle_names = set()
    shape_values = []
    color_values = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign)and isinstance(node.value, ast.Call):
            if _is_turtle_constructor(node.value):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        turtle_names.add(target.id)

        if isinstance(node, ast.Call)and isinstance(node.func, ast.Attribute):
            if isinstance(node.func.value, ast.Name)and node.func.value.id in turtle_names:
                method = node.func.attr
                if method == 'shape' and node.args:
                    shape_values.append(_get_literal_str(node.args[0]))
                if method in {'color', 'pencolor'} and node.args:
                    color_values.append(_get_literal_str(node.args[0]))

    unique_shapes = {value for value in shape_values if value}
    if require_shape and len(unique_shapes)< 2:
        fail(msg_shape)

    if require_color and (not color_values or all(value is None or value == 'black' for value in color_values)):
        fail(msg_color)

    lines = list(document.select('#turtle-canvas g:nth-child(3) line'))
    non_zero_lines = []

    for line in lines:
        x1, y1, x2, y2 = get_line_points(line)
        if math.hypot(x2 - x1, y2 - y1)> 0.5:
            non_zero_lines.append(line)

    if len(non_zero_lines)< 7:
        window.console.log(f'Found only {len(non_zero_lines)} non-zero lines, expected at least 7.')
        fail(msg_size)

    lines = non_zero_lines[-7:]
    flap_lines = lines[:3]
    body_lines = lines[3:]
    window.console.log(f"Flap lines: {'\n'.join(str(line)for line in flap_lines)}")
    window.console.log(f"Body lines: {'\n'.join(str(line)for line in body_lines)}")

    flap_lengths = [math.hypot(x2 - x1, y2 - y1)for x1, y1, x2, y2 in (get_line_points(line)for line in flap_lines)]
    body_lengths = [math.hypot(x2 - x1, y2 - y1)for x1, y1, x2, y2 in (get_line_points(line)for line in body_lines)]
    window.console.log(f'Flap lengths: {flap_lengths}')
    window.console.log(f'Body lengths: {body_lengths}')

    stroke_colors = []
    for line in lines:
        stroke = line.getAttribute('stroke')
        if not stroke:
            style = line.getAttribute('style')or ''
            for item in style.split(';'):
                if ':' in item:
                    key, value = item.split(':', 1)
                    if key.strip().lower()== 'stroke':
                        stroke = value.strip()
                        break
        stroke_colors.append((stroke or 'black').lower())

    window.console.log(f'Envelope stroke colors: {stroke_colors}')
    if require_color:
        unique_colors = set(stroke_colors)
        if len(unique_colors)< 2:
            window.console.log(f'Unique colors found: {unique_colors}')
            fail(msg_color)

    if not flap_lengths or not body_lengths:
        window.console.log(f'Invalid lengths found: flap lengths={flap_lengths}, body lengths={body_lengths}')
        fail(msg_size)

    flap_mean = sum(flap_lengths)/ len(flap_lengths)
    body_mean = sum(body_lengths)/ len(body_lengths)

    if flap_mean <= 0 or body_mean <= 0:
        window.console.log(f'Invalid lengths found: flap mean={flap_mean}, body mean={body_mean}.')
        fail(msg_size)

    min_target = 100 * min_scale
    if require_size and body_mean < min_target:
        window.console.log(f'Body mean length: {body_mean}px, required minimum: {min_target}px')
        fail(msg_size)

    flap_top = get_line_points(flap_lines[0])
    body_top = get_line_points(body_lines[0])

    top_len = flap_lengths[0]
    body_top_len = math.hypot(body_top[2] - body_top[0], body_top[3] - body_top[1])
    other_lens = flap_lengths[1:]

    top_is_horizontal = abs(flap_top[3] - flap_top[1])<= top_tol
    if not top_is_horizontal:
        window.console.log(f'Top flap line is not horizontal: y1={flap_top[1]}, y2={flap_top[3]}, tolerance: {top_tol}px')
        fail(msg_flap)

    if abs(top_len - body_top_len)> top_tol:
        window.console.log(f'Top flap length: {top_len}px, body top length: {body_top_len}px, tolerance: {top_tol}px')
        fail(msg_flap)

    same_dir = (math.hypot(flap_top[0] - body_top[0], flap_top[1] - body_top[1])<= align_tol and
                math.hypot(flap_top[2] - body_top[2], flap_top[3] - body_top[3])<= align_tol)
    swapped_dir = (math.hypot(flap_top[0] - body_top[2], flap_top[1] - body_top[3])<= align_tol and
                   math.hypot(flap_top[2] - body_top[0], flap_top[3] - body_top[1])<= align_tol)
    if not (same_dir or swapped_dir):
        window.console.log(f'Top flap line is not aligned with body top. Flap={flap_top}, Body={body_top}, tolerance: {align_tol}px')
        fail(msg_flap)

    def _line_endpoints(line):
        x1, y1, x2, y2 = get_line_points(line)
        return (x1, y1), (x2, y2)

    def _match_corner(pt, corners):
        for idx, corner in enumerate(corners):
            if math.hypot(pt[0] - corner[0], pt[1] - corner[1]) <= align_tol:
                return idx
        return None

    corners = [(body_top[0], body_top[1]), (body_top[2], body_top[3])]
    corner_hits = set()
    for line in flap_lines[1:]:
        a, b = _line_endpoints(line)
        hit = _match_corner(a, corners)
        if hit is None:
            hit = _match_corner(b, corners)
        if hit is None:
            window.console.log(f'Flap side does not connect to body corner. Line={get_line_points(line)}, corners={corners}')
            fail(msg_flap)
        corner_hits.add(hit)
    if len(corner_hits) < 2:
        window.console.log(f'Flap sides do not connect to both body corners. Hits={corner_hits}, corners={corners}')
        fail(msg_flap)

    def _find_point_off_top(lines_set, top_y):
        for line in lines_set:
            x1, y1, x2, y2 = get_line_points(line)
            if abs(y1 - top_y)> top_tol:
                return (x1, y1)
            if abs(y2 - top_y)> top_tol:
                return (x2, y2)
        return None

    if require_orientation:
        top_y = (flap_top[1] + flap_top[3])/ 2
        flap_off = _find_point_off_top(flap_lines[1:], top_y)
        body_off = _find_point_off_top(body_lines[1:], top_y)

        if flap_off is None or body_off is None:
            window.console.log(f'Could not determine orientation: flap_off={flap_off}, body_off={body_off}')
            fail(msg_flap)

        flap_dir = flap_off[1] - top_y
        body_dir = body_off[1] - top_y
        if flap_dir == 0 or body_dir == 0 or (flap_dir > 0)!= (body_dir > 0):
            window.console.log(f'Flap/body orientation mismatch. flap_off={flap_off}, body_off={body_off}, top_y={top_y}')
            fail(msg_flap)

    if require_flap_ratio:
        if any(length >= body_mean * flap_ratio for length in other_lens):
            window.console.log(f'Flap side lengths: {other_lens}, body mean length: {body_mean}px, flap ratio: {flap_ratio}')
            fail(msg_flap)

