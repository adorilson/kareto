if (allTraceData === undefined) {
 var allTraceData = {};
 }
 allTraceData["item_assign"] = {"code": "fruit = [\"banana\", \"apple\", \"cherry\"]\n\nfruit[0] = \"pear\"\nfruit[-1] = \"orange\"\n\n", "trace": [{"line": 1, "event": "step_line", "func_name": "<module>", "globals": {}, "ordered_globals": [], "stack_to_render": [], "heap": {}, "stdout": ""}, {"line": 3, "event": "step_line", "func_name": "<module>", "globals": {"fruit": ["REF", 1]}, "ordered_globals": ["fruit"], "stack_to_render": [], "heap": {"1": ["LIST", "banana", "apple", "cherry"]}, "stdout": ""}, {"line": 4, "event": "step_line", "func_name": "<module>", "globals": {"fruit": ["REF", 1]}, "ordered_globals": ["fruit"], "stack_to_render": [], "heap": {"1": ["LIST", "pear", "apple", "cherry"]}, "stdout": ""}, {"line": 4, "event": "return", "func_name": "<module>", "globals": {"fruit": ["REF", 1]}, "ordered_globals": ["fruit"], "stack_to_render": [], "heap": {"1": ["LIST", "pear", "apple", "orange"]}, "stdout": ""}]}