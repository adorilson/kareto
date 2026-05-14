
import ast
import math

from browser import window, document


def validate_code(code: str, filename):
    ast.parse(code, filename)

    return True, "OK"


class CodeRulesError(AssertionError):
    pass

#common
def fail(msg):
    raise CodeRulesError(msg) from None


def _count_code_lines(code):
    count = 0
    for line in code.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith('#'):
            continue
        count += 1
    return count


#common
def collect_code_metrics(code):
    tree = ast.parse(code, '<string>')

    for_count = 0
    while_count = 0
    for node in ast.walk(tree):
        if isinstance(node, ast.For):
            for_count += 1
        if isinstance(node, ast.While):
            while_count += 1

    loop_count = for_count + while_count

    return {
        'codeForCount': for_count,
        'codeWhileCount': while_count,
        'codeLoopCount': loop_count,
        'codeLineCount': _count_code_lines(code),
    }


#common
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


#common
def run_code_rules_test(test_case, code_metrics=None):
    code_rules = test_case.get('codeRules', [])
    if not code_rules:
        return

    msg = test_case.get('msg', 'Não está pronto.')
    if code_metrics is None:
        code_metrics = collect_code_metrics(document['editoraux'].value)

    for rule in code_rules:
        if not _rule_ok(rule, code_metrics):
            window.console.log(f'Code rule failed: {rule}')
            fail(rule.get('msg', msg))


def run_tests(test_cases):
    if not test_cases:
        window.console.log('No test cases provided.')
        return

    def _nectar_zero(girassol):
        try:
            return int(getattr(girassol, "nectares", -1)) == 0
        except (TypeError, ValueError):
            return False

    window.console.log('Running tests...')

    world = test_cases.get('world') if isinstance(test_cases, dict) else None
    if world is None:
        window.console.log('Test not passed: missing world in test cases.')
        raise AssertionError('Configuração de teste inválida: mundo não encontrado.')
    todos = all(
        getattr(girassol, "_hidden") or _nectar_zero(girassol)
        for girassol in world.girassois
    )

    if not todos:
        window.console.log('Test not passed: At least one girassol is not hidden.')
        raise AssertionError('Algum nectar não foi coletado.')

    if isinstance(test_cases, dict):
        run_code_rules_test(test_cases)
