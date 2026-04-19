import math

from browser import document, window

# PRIVATE API

def _get_animate_to(line, attr_name):
    value = None
    for animate in line.getElementsByTagName('animate'):
        if animate.getAttribute('attributeName') == attr_name:
            value = animate.getAttribute('to')
    return value


# PUBLIC API

def fail(msg):
    raise AssertionError(msg) from None


def point_dist(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])


def unique_points(points, eps):
    uniq = []
    for pt in points:
        if all(point_dist(pt, other) > eps for other in uniq):
            uniq.append(pt)
    return uniq


def compute_turn_angles_from_segments(segments, close_loop=True, eps=5):
    if len(segments) < 2:
        return []

    segs = [list(seg) for seg in segments]
    for i in range(len(segs) - 1):
        x1, y1, x2, y2 = segs[i]
        nx1, ny1, nx2, ny2 = segs[i + 1]
        end = (x2, y2)
        start_next = (nx1, ny1)
        end_next = (nx2, ny2)
        if point_dist(end, start_next) <= eps:
            continue
        if point_dist(end, end_next) <= eps:
            segs[i + 1] = [nx2, ny2, nx1, ny1]

    turns = []
    end_idx = len(segs) - 1
    pair_count = len(segs) if close_loop and len(segs) > 2 else end_idx
    for i in range(pair_count):
        a = segs[i]
        b = segs[(i + 1) % len(segs)]
        v1x, v1y = a[2] - a[0], a[3] - a[1]
        v2x, v2y = b[2] - b[0], b[3] - b[1]
        n1 = math.hypot(v1x, v1y)
        n2 = math.hypot(v2x, v2y)
        if n1 == 0 or n2 == 0:
            continue
        cosang = (v1x * v2x + v1y * v2y) / (n1 * n2)
        cosang = max(-1.0, min(1.0, cosang))
        angle = math.degrees(math.acos(cosang))
        turns.append(angle)

    return turns


def compute_signed_turn_angles_from_segments(segments, close_loop=True, eps=5):
    if len(segments) < 2:
        return []

    segs = [list(seg) for seg in segments]
    for i in range(len(segs) - 1):
        x1, y1, x2, y2 = segs[i]
        nx1, ny1, nx2, ny2 = segs[i + 1]
        end = (x2, y2)
        start_next = (nx1, ny1)
        end_next = (nx2, ny2)
        if point_dist(end, start_next) <= eps:
            continue
        if point_dist(end, end_next) <= eps:
            segs[i + 1] = [nx2, ny2, nx1, ny1]

    turns = []
    end_idx = len(segs) - 1
    pair_count = len(segs) if close_loop and len(segs) > 2 else end_idx
    for i in range(pair_count):
        a = segs[i]
        b = segs[(i + 1) % len(segs)]
        v1x, v1y = a[2] - a[0], a[3] - a[1]
        v2x, v2y = b[2] - b[0], b[3] - b[1]
        n1 = math.hypot(v1x, v1y)
        n2 = math.hypot(v2x, v2y)
        if n1 == 0 or n2 == 0:
            continue
        dot = v1x * v2x + v1y * v2y
        cross = v1x * v2y - v1y * v2x
        angle = math.degrees(math.atan2(cross, dot))
        turns.append(angle)

    return turns


def get_line_points(line):
    x1 = float(line.getAttribute('x1') or 0)
    y1 = float(line.getAttribute('y1') or 0)
    x2 = _get_animate_to(line, 'x2') or line.getAttribute('x2') or 0
    y2 = _get_animate_to(line, 'y2') or line.getAttribute('y2') or 0
    return x1, y1, float(x2), float(y2)


def collect_segments(test_case):
    lines = list(document.select('#turtle-canvas g:nth-child(3) line'))
    non_zero_only = bool(test_case.get('nonZeroOnly', True))
    min_len = float(test_case.get('minLen', 0.5))
    if non_zero_only:
        filtered = []
        for line in lines:
            x1, y1, x2, y2 = get_line_points(line)
            if math.hypot(x2 - x1, y2 - y1) > min_len:
                filtered.append((x1, y1, x2, y2))
        lines = filtered
    else:
        lines = [(get_line_points(line)) for line in lines]

    last_n = test_case.get('lastN')
    if last_n is not None:
        last_n = int(last_n)
        if last_n > 0 and len(lines) >= last_n:
            lines = lines[-last_n:]

    return lines


def segments_to_path_points(segments, eps):
    if not segments:
        return []

    x1, y1, x2, y2 = segments[0]
    points = [(x1, y1), (x2, y2)]
    current = (x2, y2)

    for seg in segments[1:]:
        a = (seg[0], seg[1])
        b = (seg[2], seg[3])

        if point_dist(a, current) <= eps:
            points.append(b)
            current = b
        elif point_dist(b, current) <= eps:
            points.append(a)
            current = a
        else:
            points.append(a)
            points.append(b)
            current = b

    return points


def run(test_cases):
    mode = test_cases.get('type') or test_cases.get('mode')
    if mode == 'hexagon':
        from _validators import shapes
        shapes.run_hexagon_test(test_cases)
        return
    if mode == 'triangle':
        from _validators import shapes
        shapes.run_triangle_test(test_cases)
        return
    if mode == 'rectangle':
        from _validators import shapes
        shapes.run_rectangle_test(test_cases)
        return
    if mode == 'turtle_shape':
        from _validators import shapes
        shapes.run_shape_test(test_cases)
        return
    if mode == 'turtle_glasses':
        from _validators import shapes
        shapes.run_glasses_test(test_cases)
        return
    if mode == 'turtle_rules':
        from _validators import rules
        rules.run_rules_test(test_cases)
        from _validators import parser
        parser.run_code_rules_test(test_cases)
        return
    if mode == 'turtle_config':
        from _validators import parser
        parser.run_code_requirements_test(test_cases)
        return
    if mode == 'turtle_sequence':
        from _validators import parser
        parser.run_turtle_sequence_test(test_cases)
        return
    if mode == 'turtle_random_colors_triangle':
        from _validators import parser
        parser.run_random_colors_triangle_test(test_cases)
        return
    if mode == 'turtle_envelope':
        from _validators import parser
        parser.run_envelope_test(test_cases)
        return



