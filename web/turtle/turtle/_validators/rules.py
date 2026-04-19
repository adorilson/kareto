import math

from browser import document, window

from _validators import (
    collect_segments,
    segments_to_path_points,
    unique_points,
    compute_turn_angles_from_segments,
    compute_signed_turn_angles_from_segments,
    point_dist,
    fail
    )


def run_rules_test(test_case):
    msg = test_case.get('msg', 'Não está pronto.')
    close_eps = float(test_case.get('closeEps', 5))
    point_eps = float(test_case.get('pointEps', close_eps))
    rules = test_case.get('rules', [])

    segments = collect_segments(test_case)
    if not segments:
        window.console.log('No segments found for rules test.')
        fail(msg)

    strict_segments = test_case.get('strictSegments')
    if strict_segments is not None:
        strict_segments = int(strict_segments)
        if len(segments) != strict_segments:
            window.console.log(f'Strict segments: found {len(segments)}, expected {strict_segments}.')
            fail(msg)

    points = segments_to_path_points(segments, point_eps)
    uniq = unique_points(points, point_eps)
    lengths = [math.hypot(x2 - x1, y2 - y1) for x1, y1, x2, y2 in segments]
    turns = compute_turn_angles_from_segments(segments, close_loop=True, eps=point_eps)
    signed_turns = compute_signed_turn_angles_from_segments(segments, close_loop=True, eps=point_eps)

    xs = [p[0] for p in uniq] or [0]
    ys = [p[1] for p in uniq] or [0]
    bbox_w = max(xs) - min(xs)
    bbox_h = max(ys) - min(ys)

    metrics = {
        'segments': len(segments),
        'uniquePoints': len(uniq),
        'closed': point_dist(points[0], points[-1]) <= close_eps if points else False,
        'sideMean': sum(lengths) / len(lengths) if lengths else 0,
        'sideMin': min(lengths) if lengths else 0,
        'sideMax': max(lengths) if lengths else 0,
        'sideStd': (math.sqrt(sum((l - (sum(lengths) / len(lengths))) ** 2 for l in lengths) / len(lengths)) if lengths else 0),
        'bboxWidth': bbox_w,
        'bboxHeight': bbox_h,
        'bboxRatio': (bbox_w / bbox_h) if bbox_h != 0 else 0,
        'turnMean': sum(turns) / len(turns) if turns else 0,
        'turnMin': min(turns) if turns else 0,
        'turnMax': max(turns) if turns else 0,
        'turnMeanSigned': sum(signed_turns) / len(signed_turns) if signed_turns else 0,
        'turnMinSigned': min(signed_turns) if signed_turns else 0,
        'turnMaxSigned': max(signed_turns) if signed_turns else 0,
        'turnDir': ('right' if (sum(signed_turns) / len(signed_turns)) > 1e-6 else 'left' if (sum(signed_turns) / len(signed_turns)) < -1e-6 else 'none') if signed_turns else 'none',
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

    for rule in rules:
        if not _rule_ok(rule, metrics):
            window.console.log(f'Rule failed: {rule}')
            fail(rule.get('msg', msg))

