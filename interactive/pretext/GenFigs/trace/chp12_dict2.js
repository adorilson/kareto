if (allTraceData === undefined) {
 var allTraceData = {};
 }
 allTraceData["chp12_dict2"] = {"code": "eng2sp = {'three': 'tres', 'one': 'uno', 'two': 'dos'}\nprint(eng2sp)\n\n", "trace": [{"line": 1, "event": "step_line", "func_name": "<module>", "globals": {}, "ordered_globals": [], "stack_to_render": [], "heap": {}, "stdout": ""}, {"line": 2, "event": "step_line", "func_name": "<module>", "globals": {"eng2sp": ["REF", 1]}, "ordered_globals": ["eng2sp"], "stack_to_render": [], "heap": {"1": ["DICT", ["three", "tres"], ["one", "uno"], ["two", "dos"]]}, "stdout": ""}, {"line": 2, "event": "return", "func_name": "<module>", "globals": {"eng2sp": ["REF", 1]}, "ordered_globals": ["eng2sp"], "stack_to_render": [], "heap": {"1": ["DICT", ["three", "tres"], ["one", "uno"], ["two", "dos"]]}, "stdout": "{'three': 'tres', 'one': 'uno', 'two': 'dos'}\n"}]}