"""
TurtleValidator e validate_code foram by ChatGPT (com alterações necessárias)
Prompt:
Quero fazer uma validação se o código do aluno contém a instrução `import turtle`
e no final tem turtle.done(). Importante levar em conta que antes ou depois disso
o código pode conter comentários.
"""

import ast
import math

from browser import window, document


class TurtleValidator(ast.NodeVisitor):
    def __init__(self):
        self.turtle_aliases = set()

    def visit_Import(self, node):
        for alias in node.names:
            if alias.name == "turtle":
                self.turtle_aliases.add(alias.asname or "turtle")

    def check_last_statement(self, tree):
        if not tree.body:
            return False

        last_stmt = tree.body[-1]

        if not isinstance(last_stmt, ast.Expr):
            return False

        call = last_stmt.value

        if not isinstance(call, ast.Call):
            return False

        func = call.func

        # caso: turtle.done() ou alias.done()
        if isinstance(func, ast.Attribute):
            if isinstance(func.value, ast.Name):
                # garante que vai funcionar mesmo que turtle não tenha sido importado
                is_turtle = func.value.id in self.turtle_aliases.union({"turtle"})
                if is_turtle and func.attr == "done":
                    return True

        return False


def validate_code(code: str, filename):
    tree = ast.parse(code, filename)

    validator = TurtleValidator()
    validator.visit(tree)

    last_ok = validator.check_last_statement(tree)

    if not last_ok:
        raise RuntimeError("Missing 'turtle.done()' at the end")

    return True, "OK"


def DEL_compute_turn_angles(points, close_loop=False):
    if len(points) < 3:
        return []

    pts = list(points)
    if close_loop:
        pts = [pts[-1]] + pts + [pts[0]]

    turns = []
    for i in range(1, len(pts) - 1):
        x0, y0 = pts[i - 1]
        x1, y1 = pts[i]
        x2, y2 = pts[i + 1]
        v1x, v1y = x0 - x1, y0 - y1
        v2x, v2y = x2 - x1, y2 - y1
        n1 = math.hypot(v1x, v1y)
        n2 = math.hypot(v2x, v2y)
        if n1 == 0 or n2 == 0:
            continue
        cosang = (v1x * v2x + v1y * v2y) / (n1 * n2)
        cosang = max(-1.0, min(1.0, cosang))
        angle = math.degrees(math.acos(cosang))
        turns.append(angle)
    return turns


def run_tests(test_cases):
    if not test_cases:
        window.console.log('No test cases provided.')
        return

    window.console.log('Running tests...')

    if isinstance(test_cases, dict):
        from _validators import run
        run(test_cases)
        return


    import svg
    for teste in test_cases:
        selector = teste['selector']
        tag = document.select_one(selector)
        try:
            tag = tag.outerHTML
        except AttributeError as e: #vai ocorrer quando a instrução não tiver sido escrita
            window.console.log(f'Exception: {e}')
            window.console.log(f'Not found an element for the test case: {teste}')
            raise AssertionError(f'{teste["msg"]}') from None
        else:
            assert svg.svg_equal(teste['outerHTML'], tag), f'{teste["msg"]}'

