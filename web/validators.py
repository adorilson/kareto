
import ast
import math

from browser import window, document


def validate_code(code: str, filename):
    ast.parse(code, filename)

    return True, "OK"


def run_tests(test_cases):
    window.console.log('Running tests...')

    world = test_cases.get('world')
    todos = all(getattr(girassol, "_hidden") for girassol in world.girassois)

    if not todos:
        window.console.log('Test not passed: At least one girassol is not hidden.')
        raise AssertionError('Algum nectar não foi coletado.')
