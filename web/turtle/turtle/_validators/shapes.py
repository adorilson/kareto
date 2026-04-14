import math

from browser import window, document

from _validators import (
    get_line_points,
    collect_segments,
    point_dist,
    unique_points,
    compute_turn_angles_from_segments,
    segments_to_path_points,
    fail
    )

# PRIVATE API

def _add_unique_point(points, new_point, eps):
    nx, ny = new_point
    for px, py in points:
        if math.hypot(nx - px, ny - py) <= eps:
            return points
    points.append((nx, ny))
    return points


# Not used. Future use.
def _assert_is_isosceles_triangle(segments):
    lengths = [math.hypot(x2 - x1, y2 - y1) for x1, y1, x2, y2 in segments]
    return len(set(round(length, 2) for length in lengths)) == 2


def _assert_triangle_side_lengths(segments, side, side_tol, msg):
    lengths = [math.hypot(x2 - x1, y2 - y1) for x1, y1, x2, y2 in segments]
    if any(abs(length - side) > side_tol for length in lengths):
        window.console.log(f'Lengths: {lengths}')
        fail(msg)


# PUBLIC API

def run_hexagon_test(test_case):
    msg = test_case.get('msg', 'Não está pronto.')
    close_eps = float(test_case.get('closeEps', 5))
    ratio = float(test_case.get('ratio', 1.3))

    lines = list(document.select('#turtle-canvas g:nth-child(3) line'))
    if len(lines) < 6:
        window.console.log(f'Found only {len(lines)} lines, expected at least 6.')
        fail(msg)

    lines = lines[-6:]
    points = [get_line_points(line) for line in lines]
    lengths = [math.hypot(x2 - x1, y2 - y1) for x1, y1, x2, y2 in points]

    if len(lengths) != 6:
        window.console.log(f'Expected 6 line segments, found {len(lengths)}.')
        fail(msg)

    sorted_lengths = sorted(lengths)
    small_mean = sum(sorted_lengths[:4]) / 4
    if small_mean <= 0:
        fail(msg)

    if not all(length >= ratio * small_mean for length in sorted_lengths[4:]):
        window.console.log(f'Lengths: {lengths}')
        fail(msg)

    start_x, start_y, _, _ = points[0]
    _, _, end_x, end_y = points[-1]
    final_eps = round(math.hypot(end_x - start_x, end_y - start_y), 2)
    if final_eps > close_eps:
        window.console.log(f'Start point: ({start_x}, {start_y})')
        window.console.log(f'End point: ({end_x}, {end_y})')
        window.console.log(f'Final distance from start to end: {final_eps}px')
        fail(msg)


def run_triangle_test(test_case):
    msg = test_case.get('msg', 'Não está pronto.')
    side = float(test_case.get('side', 150))
    close_eps = float(test_case.get('closeEps', 5))
    side_tol = float(test_case.get('sideTol', side * 0.08))
    base_eps = float(test_case.get('baseEps', 5))
    min_height_ratio = float(test_case.get('minHeightRatio', 0.5))

    lines = list(document.select('#turtle-canvas g:nth-child(3) line'))
    if len(lines) < 3:
        window.console.log(f'Found only {len(lines)} lines, expected at least 3.')
        fail(msg)

    lines = lines[-3:]
    points = []
    segments = []
    for line in lines:
        x1, y1, x2, y2 = get_line_points(line)
        segments.append((x1, y1, x2, y2))
        _add_unique_point(points, (x1, y1), close_eps)
        _add_unique_point(points, (x2, y2), close_eps)

    if len(points) != 3:
        window.console.log(f'Expected 3 unique points, found {len(points)}.')
        fail(msg)

    _assert_triangle_side_lengths(segments, side, side_tol, msg)

    start_x, start_y, _, _ = segments[0]
    _, _, end_x, end_y = segments[-1]
    final_eps = round(math.hypot(end_x - start_x, end_y - start_y), 2)
    if final_eps > close_eps:
        window.console.log(f'Final distance from start to end: {final_eps}px')
        fail(msg)

    points_sorted = sorted(points, key=lambda p: p[1])
    top = points_sorted[0]
    bottom = points_sorted[1:]
    if abs(bottom[0][1] - bottom[1][1]) > base_eps:
        window.console.log(f'Bottom Y values: {bottom[0][1]}, {bottom[1][1]}')
        fail(msg)

    height = min(bottom[0][1], bottom[1][1]) - top[1]
    if height < side * min_height_ratio:
        window.console.log(f'Height: {height}px')
        fail(msg)


def run_rectangle_test(test_case):
    msg = test_case.get('msg', 'Não está pronto.')
    sides = int(test_case.get('sides') or test_case.get('edges') or 0)
    close_eps = float(test_case.get('closeEps', 5))
    ratio = test_case.get('ratio')
    side = test_case.get('side')

    if sides < 3:
        window.console.log(f'Invalid polygon sides: {sides}.')
        fail(msg)

    side = float(side) if side is not None else None
    side_tol = float(test_case.get('sideTol', side * 0.08 if side is not None else 0))
    ratio = float(ratio) if ratio is not None else None

    lines = list(document.select('#turtle-canvas g:nth-child(3) line'))
    if len(lines) < sides:
        window.console.log(f'Found only {len(lines)} lines, expected at least {sides}.')
        fail(msg)

    lines = lines[-sides:]
    segments = []
    for line in lines:
        x1, y1, x2, y2 = get_line_points(line)
        segments.append((x1, y1, x2, y2))

    lengths = [math.hypot(x2 - x1, y2 - y1) for x1, y1, x2, y2 in segments]

    if side is not None:
        if any(abs(length - side) > side_tol for length in lengths):
            window.console.log(f'{any(abs(length - side) > side_tol for length in lengths)=}')
            fail(msg)

    if ratio is not None:
        sorted_lengths = sorted(lengths)
        if sorted_lengths[0] <= 0:
            window.console.log(f'Invalid length found: {sorted_lengths[0]}')
            fail(msg)
        min_len = min(sorted_lengths)
        max_len = max(sorted_lengths)
        if max_len < ratio * min_len:
            window.console.log(f'{max_len < ratio * min_len=}')
            fail(msg)

    start_x, start_y, _, _ = segments[0]
    _, _, end_x, end_y = segments[-1]
    final_eps = round(math.hypot(end_x - start_x, end_y - start_y), 2)
    if final_eps > close_eps:
        window.console.log(f'Start point: ({start_x}, {start_y})')
        window.console.log(f'End point: ({end_x}, {end_y})')
        window.console.log(f'Final distance from start to end: {final_eps}px')
        fail(msg)


def run_shape_test(test_case):
    msg = test_case.get('msg', 'Não está pronto.')
    shape = str(test_case.get('shape', 'polygon'))
    close_eps = float(test_case.get('closeEps', 5))
    point_eps = float(test_case.get('pointEps', close_eps))

    segments = collect_segments(test_case)
    if not segments:
        window.console.log('No segments found for shape test.')
        fail(msg)

    if shape != 'polygon':
        window.console.log(f'Unsupported shape: {shape}')
        fail(msg)

    sides = int(test_case.get('sides', 0))
    if sides < 3:
        window.console.log(f'Invalid polygon sides: {sides}.')
        fail(msg)

    strict = bool(test_case.get('strict', False))
    if strict and len(segments) != sides:
        window.console.log(f'Strict mode: found {len(segments)} segments, expected exactly {sides}.')
        fail(msg)

    if len(segments) < sides:
        window.console.log(f'Found only {len(segments)} segments, expected at least {sides}.')
        fail(msg)

    segments = segments[-sides:]
    lengths = [math.hypot(x2 - x1, y2 - y1) for x1, y1, x2, y2 in segments]

    side = test_case.get('side')
    side = float(side) if side is not None else None
    side_tol = float(test_case.get('sideTol', side * 0.08 if side is not None else 0))
    if side is not None:
        if any(abs(length - side) > side_tol for length in lengths):
            window.console.log(f'Lengths: {lengths}')
            fail(msg)

    equal_sides = bool(test_case.get('equalSides', False))
    ratio = test_case.get('ratio')
    ratio = float(ratio) if ratio is not None else None
    if equal_sides:
        if not lengths or min(lengths) <= 0:
            fail(msg)
        max_len = max(lengths)
        min_len = min(lengths)
        target_ratio = ratio if ratio is not None else 1.1
        if max_len > target_ratio * min_len:
            window.console.log(f'Lengths: {lengths}')
            fail(msg)

    start_x, start_y, _, _ = segments[0]
    _, _, end_x, end_y = segments[-1]
    final_eps = round(math.hypot(end_x - start_x, end_y - start_y), 2)
    if final_eps > close_eps:
        window.console.log(f'Final distance from start to end: {final_eps}px')
        fail(msg)

    points = segments_to_path_points(segments, point_eps)
    uniq = unique_points(points, point_eps)
    if len(uniq) < sides:
        window.console.log(f'Unique points: {len(uniq)}, expected at least {sides}.')
        fail(msg)

    turn_mean = test_case.get('turnMean')
    turn_tol = float(test_case.get('turnTol', 8))
    if turn_mean is not None:
        turns = compute_turn_angles_from_segments(segments, close_loop=True, eps=point_eps)
        if not turns:
            fail(msg)
        mean_turn = sum(turns) / len(turns)
        if abs(mean_turn - float(turn_mean)) > turn_tol:
            window.console.log(f'Turn mean: {mean_turn}, expected: {turn_mean}')
            fail(msg)



def run_glasses_test(test_case):
    msg_lens_size = test_case.get('msgLensSize', 'O tamanho das lentes deve ser diferente do original.')
    msg_lens_gap = test_case.get('msgLensGap', 'A distancia entre as lentes deve ser diferente da original.')

    base_size = float(test_case.get('size', 100))
    size_tol = float(test_case.get('sizeTol', 8))
    require_size_change = bool(test_case.get('requireSizeChange', True))
    base_gap = float(test_case.get('gap', 150))
    gap_tol = float(test_case.get('gapTol', 8))
    min_gap = float(test_case.get('minGap', 10))
    max_gap = float(test_case.get('maxGap', 400))
    gap_axis = str(test_case.get('gapAxis', 'edge'))
    require_gap_change = bool(test_case.get('requireGapChange', True))
    close_eps = float(test_case.get('closeEps', 5))

    lines = list(document.select('#turtle-canvas g:nth-child(3) line'))
    non_zero_lines = []
    for line in lines:
        x1, y1, x2, y2 = get_line_points(line)
        if math.hypot(x2 - x1, y2 - y1) > 0.5:
            non_zero_lines.append(line)

    if len(non_zero_lines) < 8:
        window.console.log(f'Found only {len(non_zero_lines)} non-zero lines, expected at least 8.')
        raise AssertionError(msg_lens_size) from None

    segments = [(get_line_points(line), line) for line in non_zero_lines]
    candidates = []
    split_tol = float(test_case.get('splitTol', 0))

    def _get_point_index(points, point, eps):
        px, py = point
        for i, (ex, ey) in enumerate(points):
            if math.hypot(px - ex, py - ey) <= eps:
                return i
        points.append(point)
        return len(points) - 1

    def _share_endpoint(a, b, eps):
        ax1, ay1, ax2, ay2 = a
        bx1, by1, bx2, by2 = b
        return (
            math.hypot(ax1 - bx1, ay1 - by1) <= eps or
            math.hypot(ax1 - bx2, ay1 - by2) <= eps or
            math.hypot(ax2 - bx1, ay2 - by1) <= eps or
            math.hypot(ax2 - bx2, ay2 - by2) <= eps
        )

    # Try a split by midpoint X to separate left/right lenses first
    midpoints = [((x1 + x2) / 2) for (x1, y1, x2, y2), _ in segments]
    midpoints_sorted = sorted(midpoints)
    if midpoints_sorted:
        mid = midpoints_sorted[len(midpoints_sorted) // 2]
        window.console.log(f'Glasses mid split: mid={mid}, splitTol={split_tol}')
        left_lines = []
        right_lines = []
        for (x1, y1, x2, y2), _ in segments:
            mx = (x1 + x2) / 2
            if mx <= mid - split_tol:
                left_lines.append((x1, y1, x2, y2))
            elif mx >= mid + split_tol:
                right_lines.append((x1, y1, x2, y2))

        window.console.log(f'Glasses split counts: left={len(left_lines)}, right={len(right_lines)}')

        def _lens_from_lines(lines_set):
            if len(lines_set) < 4:
                return None

            local_segments = list(lines_set)
            best_candidate = None

            # Try all 4-line combinations to find a valid square-like loop.
            for a in range(len(local_segments) - 3):
                for b in range(a + 1, len(local_segments) - 2):
                    for c in range(b + 1, len(local_segments) - 1):
                        for d in range(c + 1, len(local_segments)):
                            subset = [
                                local_segments[a],
                                local_segments[b],
                                local_segments[c],
                                local_segments[d],
                            ]

                            points = []
                            counts = []
                            lengths = []
                            for x1, y1, x2, y2 in subset:
                                idx1 = _get_point_index(points, (x1, y1), close_eps)
                                while len(counts) <= idx1:
                                    counts.append(0)
                                counts[idx1] += 1

                                idx2 = _get_point_index(points, (x2, y2), close_eps)
                                while len(counts) <= idx2:
                                    counts.append(0)
                                counts[idx2] += 1

                                lengths.append(math.hypot(x2 - x1, y2 - y1))

                            if len(points) != 4:
                                continue
                            if any(count != 2 for count in counts):
                                continue

                            best_candidate = {
                                'points': points,
                                'mean_len': sum(lengths) / len(lengths),
                            }
                            return best_candidate

            return best_candidate

        def _drop_bridge(lines_set, mid_x, target=4):
            if len(lines_set) <= target:
                return list(lines_set)
            # Drop the lines whose midpoints are closest to the split axis (likely the bridge).
            mids = [(abs((x1 + x2) / 2 - mid_x), i) for i, (x1, y1, x2, y2) in enumerate(lines_set)]
            mids_sorted = sorted(mids, key=lambda item: item[0])
            drop_count = max(0, len(lines_set) - target)
            drop_idx = {i for _, i in mids_sorted[:drop_count]}
            return [line for i, line in enumerate(lines_set) if i not in drop_idx]

        left_candidate = _lens_from_lines(left_lines)
        if left_candidate is None and len(left_lines) > 4:
            left_candidate = _lens_from_lines(_drop_bridge(left_lines, mid))

        right_candidate = _lens_from_lines(right_lines)
        if right_candidate is None and len(right_lines) > 4:
            right_candidate = _lens_from_lines(_drop_bridge(right_lines, mid))
        window.console.log(f'Glasses split candidates: left={left_candidate is not None}, right={right_candidate is not None}')
        if left_candidate:
            candidates.append(left_candidate)
        if right_candidate:
            candidates.append(right_candidate)

        def _bbox(points_set):
            xs_set = [p[0] for p in points_set]
            ys_set = [p[1] for p in points_set]
            return min(xs_set), max(xs_set), min(ys_set), max(ys_set)

        def _points_from_lines(lines_set):
            pts = []
            for x1, y1, x2, y2 in lines_set:
                pts.append((x1, y1))
                pts.append((x2, y2))
            return pts

        def _try_bbox_validation(left_points, right_points, label):
            if len(left_points) < 4 or len(right_points) < 4:
                return False

            lminx, lmaxx, lminy, lmaxy = _bbox(left_points)
            rminx, rmaxx, rminy, rmaxy = _bbox(right_points)

            left_mean = (abs(lmaxx - lminx) + abs(lmaxy - lminy)) / 2
            right_mean = (abs(rmaxx - rminx) + abs(rmaxy - rminy)) / 2

            window.console.log(
                f'Lens sizes (bbox-{label}): left={left_mean}px, right={right_mean}px, '
                f'base={base_size}px, tol={size_tol}px'
            )

            if require_size_change:
                if abs(left_mean - base_size) <= size_tol and abs(right_mean - base_size) <= size_tol:
                    return False

            left_center = ((lminx + lmaxx) / 2, (lminy + lmaxy) / 2)
            right_center = ((rminx + rmaxx) / 2, (rminy + rmaxy) / 2)

            if gap_axis == 'euclidean':
                gap = math.hypot(right_center[0] - left_center[0], right_center[1] - left_center[1])
            elif gap_axis == 'center':
                gap = abs(right_center[0] - left_center[0])
            else:
                gap = rminx - lmaxx

            window.console.log(f'Lens gap (bbox-{label}): {gap}px, base gap: {base_gap}px, axis: {gap_axis}')
            if gap < min_gap or gap > max_gap:
                return False
            if require_gap_change and abs(gap - base_gap) <= gap_tol:
                return False

            return True

        if len(candidates) < 2:
            cleaned_left = _drop_bridge(left_lines, mid)
            cleaned_right = _drop_bridge(right_lines, mid)
            left_points = _points_from_lines(cleaned_left)
            right_points = _points_from_lines(cleaned_right)
            if _try_bbox_validation(left_points, right_points, 'split'):
                return

    # Build connected components of lines that share endpoints as fallback
    if len(candidates) < 2:
        visited = [False] * len(segments)
        for i, (seg_i, _) in enumerate(segments):
            if visited[i]:
                continue
            stack = [i]
            component = []
            visited[i] = True
            while stack:
                idx = stack.pop()
                component.append(segments[idx][0])
                for j, (seg_j, _) in enumerate(segments):
                    if visited[j]:
                        continue
                    if _share_endpoint(segments[idx][0], seg_j, close_eps):
                        visited[j] = True
                        stack.append(j)

            if len(component) < 4:
                continue

            points = []
            counts = []
            lengths = []
            for x1, y1, x2, y2 in component:
                idx1 = _get_point_index(points, (x1, y1), close_eps)
                while len(counts) <= idx1:
                    counts.append(0)
                counts[idx1] += 1

                idx2 = _get_point_index(points, (x2, y2), close_eps)
                while len(counts) <= idx2:
                    counts.append(0)
                counts[idx2] += 1

                lengths.append(math.hypot(x2 - x1, y2 - y1))

            if len(points) != 4:
                continue
            if any(count != 2 for count in counts):
                continue

            mean_len = sum(lengths) / len(lengths)
            candidates.append({
                'points': points,
                'mean_len': mean_len,
            })

    if len(candidates) < 2:
        window.console.log(f'Found only {len(candidates)} lens candidates, expected 2.')

        # Fallback: split by point X and use bounding boxes.
        point_split_tol = float(test_case.get('pointSplitTol', 0))
        all_points = []
        for (x1, y1, x2, y2), _ in segments:
            all_points.append((x1, y1))
            all_points.append((x2, y2))

        xs = sorted(p[0] for p in all_points)
        if not xs:
            raise AssertionError(msg_lens_size) from None
        mid_x = xs[len(xs) // 2]

        left_points = [p for p in all_points if p[0] < mid_x - point_split_tol]
        right_points = [p for p in all_points if p[0] > mid_x + point_split_tol]

        if len(left_points) < 4 or len(right_points) < 4:
            window.console.log(f'Point split counts: left={len(left_points)}, right={len(right_points)}')
            raise AssertionError(msg_lens_size) from None

        def _bbox(points_set):
            xs_set = [p[0] for p in points_set]
            ys_set = [p[1] for p in points_set]
            return min(xs_set), max(xs_set), min(ys_set), max(ys_set)

        lminx, lmaxx, lminy, lmaxy = _bbox(left_points)
        rminx, rmaxx, rminy, rmaxy = _bbox(right_points)

        left_mean = (abs(lmaxx - lminx) + abs(lmaxy - lminy)) / 2
        right_mean = (abs(rmaxx - rminx) + abs(rmaxy - rminy)) / 2

        window.console.log(f'Lens sizes (bbox): left={left_mean}px, right={right_mean}px, base={base_size}px, tol={size_tol}px')
        if require_size_change:
            if abs(left_mean - base_size) <= size_tol and abs(right_mean - base_size) <= size_tol:
                raise AssertionError(msg_lens_size) from None

        left_center = ((lminx + lmaxx) / 2, (lminy + lmaxy) / 2)
        right_center = ((rminx + rmaxx) / 2, (rminy + rmaxy) / 2)

        if gap_axis == 'euclidean':
            gap = math.hypot(right_center[0] - left_center[0], right_center[1] - left_center[1])
        elif gap_axis == 'center':
            gap = abs(right_center[0] - left_center[0])
        else:
            gap = rminx - lmaxx
        window.console.log(f'Lens gap (bbox): {gap}px, base gap: {base_gap}px, axis: {gap_axis}')
        if gap < min_gap or gap > max_gap:
            raise AssertionError(msg_lens_gap) from None
        if require_gap_change and abs(gap - base_gap) <= gap_tol:
            raise AssertionError(msg_lens_gap) from None

        return

    best_pair = None
    best_gap = -1
    for i in range(len(candidates)):
        for j in range(i + 1, len(candidates)):
            ci = candidates[i]
            cj = candidates[j]
            cix = sum(p[0] for p in ci['points']) / len(ci['points'])
            ciy = sum(p[1] for p in ci['points']) / len(ci['points'])
            cjx = sum(p[0] for p in cj['points']) / len(cj['points'])
            cjy = sum(p[1] for p in cj['points']) / len(cj['points'])
            gap = math.hypot(cjx - cix, cjy - ciy)
            if gap > best_gap:
                best_gap = gap
                best_pair = (ci, cj)

    if not best_pair:
        window.console.log('Could not find two non-overlapping lens candidates.')
        raise AssertionError(msg_lens_size) from None

    left_lens, right_lens = best_pair
    left_mean = left_lens['mean_len']
    right_mean = right_lens['mean_len']

    window.console.log(f'Lens sizes: left={left_mean}px, right={right_mean}px, base={base_size}px, tol={size_tol}px')
    if require_size_change:
        if abs(left_mean - base_size) <= size_tol and abs(right_mean - base_size) <= size_tol:
            raise AssertionError(msg_lens_size) from None

    def _bbox_from_points(points_set):
        xs_set = [p[0] for p in points_set]
        ys_set = [p[1] for p in points_set]
        return min(xs_set), max(xs_set), min(ys_set), max(ys_set)

    lminx, lmaxx, lminy, lmaxy = _bbox_from_points(left_lens['points'])
    rminx, rmaxx, rminy, rmaxy = _bbox_from_points(right_lens['points'])

    left_center = ((lminx + lmaxx) / 2, (lminy + lmaxy) / 2)
    right_center = ((rminx + rmaxx) / 2, (rminy + rmaxy) / 2)

    if gap_axis == 'euclidean':
        gap = math.hypot(right_center[0] - left_center[0], right_center[1] - left_center[1])
    elif gap_axis == 'center':
        gap = abs(right_center[0] - left_center[0])
    else:
        gap = rminx - lmaxx
    window.console.log(f'Lens gap: {gap}px, base gap: {base_gap}px, axis: {gap_axis}')
    if gap < min_gap or gap > max_gap:
        raise AssertionError(msg_lens_gap) from None
    if require_gap_change and abs(gap - base_gap) <= gap_tol:
        raise AssertionError(msg_lens_gap) from None
