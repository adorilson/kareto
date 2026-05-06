
import ast
import math

from browser import window, document


def validate_code(code: str, filename):
    ast.parse(code, filename)

    return True, "OK"


def run_tests(test_cases):
    window.console.log('Running tests...')

    world = test_cases.get('world')
    def _nectar_zero(girassol):
        try:
            return int(getattr(girassol, "nectares", -1)) == 0
        except (TypeError, ValueError):
            return False

    todos = all(
        getattr(girassol, "_hidden") or _nectar_zero(girassol)
        for girassol in world.girassois
    )

    if not todos:
        window.console.log('Test not passed: At least one girassol is not hidden.')
        raise AssertionError('Algum nectar não foi coletado.')
