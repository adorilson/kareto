import sys
import types
from pathlib import Path

import pytest


WEB_DIR = Path(__file__).resolve().parents[1]
if str(WEB_DIR) not in sys.path:
    sys.path.insert(0, str(WEB_DIR))

if "browser" not in sys.modules:
    browser = types.SimpleNamespace()
    browser.window = types.SimpleNamespace(
        console=types.SimpleNamespace(log=lambda *args, **kwargs: None)
    )
    browser.document = {}
    sys.modules["browser"] = browser

import validators


def test_collect_code_metrics_counts_loops_and_lines():
    code = """
# comment line

for i in range(3):
    print(i)
"""
    metrics = validators.collect_code_metrics(code)
    assert metrics["codeLoopCount"] == 1
    assert metrics["codeLineCount"] == 2


def test_run_code_rules_test_passes():
    code = """
for i in range(2):
    print(i)
"""
    metrics = validators.collect_code_metrics(code)
    test_case = {
        "codeRules": [
            {"metric": "codeLoopCount", "op": ">=", "value": 1},
            {"metric": "codeLineCount", "op": "<=", "value": 3},
        ]
    }
    validators.run_code_rules_test(test_case, code_metrics=metrics)


def test_run_code_rules_test_fails():
    code = """
print("hi")
"""
    metrics = validators.collect_code_metrics(code)
    test_case = {
        "codeRules": [
            {
                "metric": "codeLoopCount",
                "op": ">=",
                "value": 1,
                "msg": "Use loop.",
            }
        ]
    }
    with pytest.raises(validators.CodeRulesError, match="Use loop\."):
        validators.run_code_rules_test(test_case, code_metrics=metrics)
