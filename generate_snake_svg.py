import random
from collections import deque

COLS = 47  # cols 0 to 46 (x = 51 to 787)
ROWS = 11  # rows 0 to 10 (y = 53 to 213)
CELL_SIZE = 16
OFFSET_X = 51
OFFSET_Y = 53

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)
DIRECTIONS = [RIGHT, DOWN, LEFT, UP]

def get_neighbors(pos):
    c, r = pos
    res = []
    for dc, dr in DIRECTIONS:
        nc, nr = c + dc, r + dr
        if 0 <= nc < COLS and 0 <= nr < ROWS:
            res.append((nc, nr))
    return res

def bfs_path(start, target, obstacles):
    queue = deque([[start]])
    visited = set(obstacles)
    visited.add(start)
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == target:
            return path
        for neighbor in get_neighbors(node):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])
    return None

def flood_fill_count(start, obstacles):
    queue = deque([start])
    visited = set(obstacles)
    visited.add(start)
    count = 0
    while queue:
        node = queue.popleft()
        count += 1
        for neighbor in get_neighbors(node):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return count

def simulate_round(seed, round_num, target_foods=11, grow_per_food=4):
    rng = random.Random(seed)
    
    start_row = rng.randint(3, 7)
    start_col = rng.randint(8, 16)
    snake = deque([
        (start_col, start_row),
        (start_col - 1, start_row),
        (start_col - 2, start_row),
        (start_col - 3, start_row)
    ])
    
    foods_eaten = 0
    history = []
    
    def pick_food(current_snake):
        body_set = set(current_snake)
        candidates = [(c, r) for c in range(2, COLS - 2) for r in range(1, ROWS - 1) if (c, r) not in body_set]
        if not candidates:
            candidates = [(c, r) for c in range(COLS) for r in range(ROWS) if (c, r) not in body_set]
        return rng.choice(candidates)
    
    food = pick_food(snake)
    score = 0
    grow_pending = 0
    max_steps = 220
    step_count = 0
    crash_pos = None
    
    while step_count < max_steps:
        head = snake[0]
        history.append({
            'round': round_num,
            'snake': list(snake),
            'food': food,
            'score': score,
            'status': 'playing'
        })
        step_count += 1
        
        # Trigger crash when target foods reached
        if foods_eaten >= target_foods:
            neighbors = get_neighbors(head)
            body_list = list(snake)
            crash_move = None
            for n in neighbors:
                if n in body_list[3:]:
                    crash_move = n
                    break
            if crash_move:
                crash_pos = crash_move
                break
            best_n = None
            min_dist = 999
            for n in neighbors:
                if n != snake[1]:
                    d = min(abs(n[0] - b[0]) + abs(n[1] - b[1]) for b in body_list[4:])
                    if d < min_dist:
                        min_dist = d
                        best_n = n
            if best_n is None:
                best_n = neighbors[0]
            next_head = best_n
            if next_head in body_list:
                crash_pos = next_head
                break
            snake.appendleft(next_head)
            snake.pop()
            continue
            
        obstacles = set(list(snake)[:-1]) if grow_pending == 0 else set(snake)
        path = bfs_path(head, food, obstacles)
        
        chosen_move = None
        if path and len(path) > 1:
            candidate_move = path[1]
            sim_obstacles = set(list(snake)[1:]) | {candidate_move}
            space = flood_fill_count(candidate_move, sim_obstacles)
            if space > len(snake) // 2:
                chosen_move = candidate_move
        
        if chosen_move is None:
            best_space = -1
            best_move = None
            for n in get_neighbors(head):
                if n not in obstacles:
                    sp = flood_fill_count(n, obstacles | {n})
                    if sp > best_space:
                        best_space = sp
                        best_move = n
            chosen_move = best_move
            
        if chosen_move is None:
            neighbors = [n for n in get_neighbors(head) if n != snake[1]]
            chosen_move = neighbors[0] if neighbors else head
            if chosen_move in snake:
                crash_pos = chosen_move
                break
                
        snake.appendleft(chosen_move)
        if chosen_move == food:
            foods_eaten += 1
            score += 10
            grow_pending += grow_per_food
            food = pick_food(snake)
            
        if grow_pending > 0:
            grow_pending -= 1
        else:
            snake.pop()
            
    if crash_pos is None:
        crash_pos = snake[0]
        
    crash_steps = 18  # Hold Game Over for 18 ticks (~2.16s)
    for _ in range(crash_steps):
        history.append({
            'round': round_num,
            'snake': list(snake),
            'food': food,
            'score': score,
            'status': 'crash',
            'crash_pos': crash_pos
        })
        
    return history

def generate_svg():
    print("Simulating 3 rounds with true random food placements...")
    r1 = simulate_round(4242, 1, target_foods=11)
    r2 = simulate_round(8484, 2, target_foods=12)
    r3 = simulate_round(9999, 3, target_foods=11)
    
    ticks = r1 + r2 + r3
    N = len(ticks)
    duration_s = N * 0.12
    print(f"Total steps: {N}, Duration: {duration_s:.2f}s")
    
    # Precalculate keyTimes string (format to 4 decimal places)
    key_times = ";".join(f"{i / (N - 1):.4f}".rstrip('0').rstrip('.') if i > 0 and i < N - 1 else ("0" if i == 0 else "1") for i in range(N))
    
    # Maximum snake length
    max_len = max(len(t['snake']) for t in ticks)
    print(f"Max snake length across all rounds: {max_len}")
    
    # Collect all unique scores across all ticks
    unique_scores = sorted(set(t['score'] for t in ticks))
    print(f"Unique scores: {unique_scores}")
    
    # Color palette for snake segments (tail: dark green, head: neon lime green)
    def get_segment_base_color(idx, total):
        ratio = idx / max(1, total - 1)
        r = int(0 + ratio * 0)
        g = int(90 + ratio * 165)
        b = int(50 + ratio * 86)
        return f"#{r:02x}{g:02x}{b:02x}"
        
    segment_colors = [get_segment_base_color(i, max_len) for i in range(max_len)]
    
    lines = []
    lines.append('<svg width="900" height="250" viewBox="0 0 900 250" xmlns="http://www.w3.org/2000/svg">')
    lines.append('  <defs>')
    lines.append('    <radialGradient id="bg" cx="50%" cy="50%" r="75%">')
    lines.append('      <stop offset="0%" stop-color="#0a1a3e"/>')
    lines.append('      <stop offset="60%" stop-color="#07071a"/>')
    lines.append('      <stop offset="100%" stop-color="#050512"/>')
    lines.append('    </radialGradient>')
    lines.append('    <pattern id="g" width="16" height="16" patternUnits="userSpaceOnUse">')
    lines.append('      <path d="M16 0H0V16" fill="none" stroke="#00f0ff" stroke-width="0.35" opacity="0.06"/>')
    lines.append('    </pattern>')
    lines.append('    <linearGradient id="rgb" gradientUnits="userSpaceOnUse" x1="12" y1="125" x2="888" y2="125">')
    lines.append('      <stop offset="0%" stop-color="#00f0ff"><animate attributeName="stop-color" values="#00f0ff;#d946ef;#00ffcc;#00f0ff" dur="5s" repeatCount="indefinite"/></stop>')
    lines.append('      <stop offset="33%" stop-color="#d946ef"><animate attributeName="stop-color" values="#d946ef;#00f0ff;#ff73fa;#d946ef" dur="5s" repeatCount="indefinite"/></stop>')
    lines.append('      <stop offset="66%" stop-color="#00ffcc"><animate attributeName="stop-color" values="#00ffcc;#ff73fa;#00f0ff;#00ffcc" dur="5s" repeatCount="indefinite"/></stop>')
    lines.append('      <stop offset="100%" stop-color="#00f0ff"><animate attributeName="stop-color" values="#00f0ff;#d946ef;#00ffcc;#00f0ff" dur="5s" repeatCount="indefinite"/></stop>')
    lines.append('      <animateTransform attributeName="gradientTransform" type="rotate" from="0 450 125" to="360 450 125" dur="4.5s" repeatCount="indefinite"/>')
    lines.append('    </linearGradient>')
    lines.append('    <filter id="gl" x="-25%" y="-25%" width="150%" height="150%">')
    lines.append('      <feGaussianBlur stdDeviation="3.5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>')
    lines.append('    </filter>')
    lines.append('    <filter id="no" x="-10%" y="-18%" width="120%" height="136%">')
    lines.append('      <feGaussianBlur stdDeviation="5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>')
    lines.append('    </filter>')
    lines.append('    <filter id="fg" x="-50%" y="-50%" width="200%" height="200%">')
    lines.append('      <feGaussianBlur stdDeviation="4" result="g"/><feMerge><feMergeNode in="g"/><feMergeNode in="SourceGraphic"/></feMerge>')
    lines.append('    </filter>')
    lines.append('    <clipPath id="cl"><rect x="12" y="12" width="876" height="226" rx="16"/></clipPath>')
    lines.append('  </defs>')
    lines.append('')
    lines.append('  <rect x="12" y="12" width="876" height="226" rx="16" fill="none" stroke="url(#rgb)" stroke-width="5" opacity="0.32" filter="url(#no)"/>')
    lines.append('  <rect x="12" y="12" width="876" height="226" rx="16" fill="url(#bg)"/>')
    lines.append('  <rect x="12" y="12" width="876" height="226" rx="16" fill="url(#g)"/>')
    lines.append('')
    lines.append('  <path d="M22 42 L22 22 L42 22" stroke="#00f0ff" stroke-width="2" fill="none" opacity=".85"/>')
    lines.append('  <path d="M878 42 L878 22 L858 22" stroke="#00f0ff" stroke-width="2" fill="none" opacity=".85"/>')
    lines.append('  <path d="M22 208 L22 228 L42 228" stroke="#d946ef" stroke-width="2" fill="none" opacity=".85"/>')
    lines.append('  <path d="M878 208 L878 228 L858 228" stroke="#d946ef" stroke-width="2" fill="none" opacity=".85"/>')
    lines.append('')
    lines.append('  <text x="32" y="32" font-family="\'Fira Code\',ui-monospace,monospace" font-size="11" font-weight="700" letter-spacing="2" fill="#00f0ff" opacity="0.95">// NOKIA SNAKE ARCADE &#183; RIOON7337</text>')
    lines.append('')
    
    # Round Indicators in center
    for rnd in [1, 2, 3]:
        rnd_op = ";".join("1" if t['round'] == rnd else "0" for t in ticks)
        lines.append(f'  <text x="450" y="32" text-anchor="middle" font-family="\'Fira Code\',ui-monospace,monospace" font-size="11" font-weight="700" letter-spacing="2" fill="#00f0ff" opacity="0">')
        lines.append(f'    <animate attributeName="opacity" values="{rnd_op}" keyTimes="{key_times}" dur="{duration_s:.2f}s" calcMode="discrete" repeatCount="indefinite"/>')
        lines.append(f'    [ ROUND 0{rnd} / 03 &#183; RANDOM FOOD ]')
        lines.append(f'  </text>')
        
    # Score Counters on right
    for s_val in unique_scores:
        s_op = ";".join("1" if t['score'] == s_val else "0" for t in ticks)
        lines.append(f'  <text x="868" y="32" text-anchor="end" font-family="\'Fira Code\',ui-monospace,monospace" font-size="11" font-weight="700" letter-spacing="2" fill="#ff73fa" opacity="0">')
        lines.append(f'    <animate attributeName="opacity" values="{s_op}" keyTimes="{key_times}" dur="{duration_s:.2f}s" calcMode="discrete" repeatCount="indefinite"/>')
        lines.append(f'    SCORE: <tspan fill="#00ff88">{s_val:03d}</tspan>')
        lines.append(f'  </text>')
        
    lines.append('  <g clip-path="url(#cl)">')
    
    # Food animation values
    food_cx = ";".join(str(OFFSET_X + t['food'][0] * CELL_SIZE + 7) for t in ticks)
    food_cy = ";".join(str(OFFSET_Y + t['food'][1] * CELL_SIZE + 7) for t in ticks)
    food_op = ";".join("0" if t['status'] == 'crash' else "1" for t in ticks)
    food_ring_op = ";".join("0" if t['status'] == 'crash' else "0.4" for t in ticks)
    
    lines.append('    <!-- Glowing Food -->')
    lines.append('    <circle r="6" fill="#d946ef" filter="url(#fg)">')
    lines.append(f'      <animate attributeName="cx" values="{food_cx}" keyTimes="{key_times}" dur="{duration_s:.2f}s" calcMode="discrete" repeatCount="indefinite"/>')
    lines.append(f'      <animate attributeName="cy" values="{food_cy}" keyTimes="{key_times}" dur="{duration_s:.2f}s" calcMode="discrete" repeatCount="indefinite"/>')
    lines.append(f'      <animate attributeName="opacity" values="{food_op}" keyTimes="{key_times}" dur="{duration_s:.2f}s" calcMode="discrete" repeatCount="indefinite"/>')
    lines.append('      <animate attributeName="r" values="5;7;5" dur="0.8s" repeatCount="indefinite"/>')
    lines.append('    </circle>')
    lines.append('    <circle r="9" fill="none" stroke="#ff73fa" stroke-width="1" opacity="0.4">')
    lines.append(f'      <animate attributeName="cx" values="{food_cx}" keyTimes="{key_times}" dur="{duration_s:.2f}s" calcMode="discrete" repeatCount="indefinite"/>')
    lines.append(f'      <animate attributeName="cy" values="{food_cy}" keyTimes="{key_times}" dur="{duration_s:.2f}s" calcMode="discrete" repeatCount="indefinite"/>')
    lines.append(f'      <animate attributeName="opacity" values="{food_ring_op}" keyTimes="{key_times}" dur="{duration_s:.2f}s" calcMode="discrete" repeatCount="indefinite"/>')
    lines.append('      <animate attributeName="r" values="8;12;8" dur="0.8s" repeatCount="indefinite"/>')
    lines.append('    </circle>')
    
    # Snake Segments: from tail (idx 0) to head (idx max_len - 1)
    print("Generating snake segments...")
    for seg_i in range(max_len):
        base_color = segment_colors[seg_i]
        seg_xs = []
        seg_ys = []
        seg_ops = []
        seg_fills = []
        
        for tick_idx, t in enumerate(ticks):
            s = t['snake']
            L = len(s)
            offset_from_head = (max_len - 1) - seg_i
            
            if offset_from_head < L:
                pos = s[offset_from_head]
                px = OFFSET_X + pos[0] * CELL_SIZE
                py = OFFSET_Y + pos[1] * CELL_SIZE
                seg_xs.append(str(px))
                seg_ys.append(str(py))
                
                if t['status'] == 'crash':
                    seg_ops.append("0.9" if (tick_idx % 2 == 0) else "0.5")
                    seg_fills.append("#ff0033" if (tick_idx % 2 == 0) else "#ff3344")
                else:
                    seg_ops.append("1")
                    seg_fills.append(base_color)
            else:
                head_pos = s[0]
                px = OFFSET_X + head_pos[0] * CELL_SIZE
                py = OFFSET_Y + head_pos[1] * CELL_SIZE
                seg_xs.append(str(px))
                seg_ys.append(str(py))
                seg_ops.append("0")
                seg_fills.append(base_color)
                
        val_x = ";".join(seg_xs)
        val_y = ";".join(seg_ys)
        val_op = ";".join(seg_ops)
        val_fill = ";".join(seg_fills)
        
        lines.append(f'    <rect width="14" height="14" rx="2" fill="{base_color}" stroke="#002b11" stroke-width="0.5">')
        lines.append(f'      <animate attributeName="x" values="{val_x}" keyTimes="{key_times}" dur="{duration_s:.2f}s" calcMode="discrete" repeatCount="indefinite"/>')
        lines.append(f'      <animate attributeName="y" values="{val_y}" keyTimes="{key_times}" dur="{duration_s:.2f}s" calcMode="discrete" repeatCount="indefinite"/>')
        lines.append(f'      <animate attributeName="opacity" values="{val_op}" keyTimes="{key_times}" dur="{duration_s:.2f}s" calcMode="discrete" repeatCount="indefinite"/>')
        lines.append(f'      <animate attributeName="fill" values="{val_fill}" keyTimes="{key_times}" dur="{duration_s:.2f}s" calcMode="discrete" repeatCount="indefinite"/>')
        lines.append('    </rect>')
        
    # Head Eyes
    print("Generating head eyes...")
    eye1_cx = []
    eye1_cy = []
    eye2_cx = []
    eye2_cy = []
    eye_ops = []
    
    for t in ticks:
        s = t['snake']
        head = s[0]
        hx = OFFSET_X + head[0] * CELL_SIZE
        hy = OFFSET_Y + head[1] * CELL_SIZE
        
        if t['status'] == 'crash':
            eye1_cx.append(str(hx))
            eye1_cy.append(str(hy))
            eye2_cx.append(str(hx))
            eye2_cy.append(str(hy))
            eye_ops.append("0")
        else:
            eye_ops.append("1")
            neck = s[1] if len(s) > 1 else (head[0] - 1, head[1])
            dc = head[0] - neck[0]
            dr = head[1] - neck[1]
            
            if dc > 0:  # Moving right
                eye1_cx.append(str(hx + 10))
                eye1_cy.append(str(hy + 3))
                eye2_cx.append(str(hx + 10))
                eye2_cy.append(str(hy + 9))
            elif dc < 0:  # Moving left
                eye1_cx.append(str(hx + 4))
                eye1_cy.append(str(hy + 3))
                eye2_cx.append(str(hx + 4))
                eye2_cy.append(str(hy + 9))
            elif dr < 0:  # Moving up
                eye1_cx.append(str(hx + 3))
                eye1_cy.append(str(hy + 4))
                eye2_cx.append(str(hx + 9))
                eye2_cy.append(str(hy + 4))
            else:  # Moving down
                eye1_cx.append(str(hx + 3))
                eye1_cy.append(str(hy + 10))
                eye2_cx.append(str(hx + 9))
                eye2_cy.append(str(hy + 10))
                
    lines.append('    <!-- Head Eyes -->')
    lines.append('    <circle r="1.8" fill="#ffffff">')
    lines.append(f'      <animate attributeName="cx" values="{";".join(eye1_cx)}" keyTimes="{key_times}" dur="{duration_s:.2f}s" calcMode="discrete" repeatCount="indefinite"/>')
    lines.append(f'      <animate attributeName="cy" values="{";".join(eye1_cy)}" keyTimes="{key_times}" dur="{duration_s:.2f}s" calcMode="discrete" repeatCount="indefinite"/>')
    lines.append(f'      <animate attributeName="opacity" values="{";".join(eye_ops)}" keyTimes="{key_times}" dur="{duration_s:.2f}s" calcMode="discrete" repeatCount="indefinite"/>')
    lines.append('    </circle>')
    lines.append('    <circle r="1.8" fill="#ffffff">')
    lines.append(f'      <animate attributeName="cx" values="{";".join(eye2_cx)}" keyTimes="{key_times}" dur="{duration_s:.2f}s" calcMode="discrete" repeatCount="indefinite"/>')
    lines.append(f'      <animate attributeName="cy" values="{";".join(eye2_cy)}" keyTimes="{key_times}" dur="{duration_s:.2f}s" calcMode="discrete" repeatCount="indefinite"/>')
    lines.append(f'      <animate attributeName="opacity" values="{";".join(eye_ops)}" keyTimes="{key_times}" dur="{duration_s:.2f}s" calcMode="discrete" repeatCount="indefinite"/>')
    lines.append('    </circle>')
    
    # Dizzy Stars & GAME OVER Effect
    print("Generating Dizzy Stars and Game Over effect...")
    crash_group_op = ";".join("1" if t['status'] == 'crash' else "0" for t in ticks)
    
    star1_x = []
    star1_y = []
    star2_x = []
    star2_y = []
    star3_x = []
    star3_y = []
    
    for t in ticks:
        cpos = t.get('crash_pos', t['snake'][0])
        cx = OFFSET_X + cpos[0] * CELL_SIZE + 7
        cy = OFFSET_Y + cpos[1] * CELL_SIZE + 7
        star1_x.append(str(cx - 12))
        star1_y.append(str(cy - 12))
        star2_x.append(str(cx + 14))
        star2_y.append(str(cy - 5))
        star3_x.append(str(cx - 5))
        star3_y.append(str(cy + 12))
        
    lines.append('    <!-- Dizzy Stars & Game Over Effect -->')
    lines.append('    <g>')
    lines.append(f'      <animate attributeName="opacity" values="{crash_group_op}" keyTimes="{key_times}" dur="{duration_s:.2f}s" calcMode="discrete" repeatCount="indefinite"/>')
    lines.append('      <!-- Star 1 -->')
    lines.append('      <text font-size="15" fill="#ffd700" text-anchor="middle" dominant-baseline="middle">')
    lines.append(f'        <animate attributeName="x" values="{";".join(star1_x)}" keyTimes="{key_times}" dur="{duration_s:.2f}s" calcMode="discrete" repeatCount="indefinite"/>')
    lines.append(f'        <animate attributeName="y" values="{";".join(star1_y)}" keyTimes="{key_times}" dur="{duration_s:.2f}s" calcMode="discrete" repeatCount="indefinite"/>')
    lines.append('        <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="1s" repeatCount="indefinite"/>')
    lines.append('        &#9733;')
    lines.append('      </text>')
    lines.append('      <!-- Star 2 -->')
    lines.append('      <text font-size="11" fill="#ff73fa" text-anchor="middle" dominant-baseline="middle">')
    lines.append(f'        <animate attributeName="x" values="{";".join(star2_x)}" keyTimes="{key_times}" dur="{duration_s:.2f}s" calcMode="discrete" repeatCount="indefinite"/>')
    lines.append(f'        <animate attributeName="y" values="{";".join(star2_y)}" keyTimes="{key_times}" dur="{duration_s:.2f}s" calcMode="discrete" repeatCount="indefinite"/>')
    lines.append('        <animateTransform attributeName="transform" type="rotate" from="360" to="0" dur="0.7s" repeatCount="indefinite"/>')
    lines.append('        &#9733;')
    lines.append('      </text>')
    lines.append('      <!-- Star 3 -->')
    lines.append('      <text font-size="13" fill="#00f0ff" text-anchor="middle" dominant-baseline="middle">')
    lines.append(f'        <animate attributeName="x" values="{";".join(star3_x)}" keyTimes="{key_times}" dur="{duration_s:.2f}s" calcMode="discrete" repeatCount="indefinite"/>')
    lines.append(f'        <animate attributeName="y" values="{";".join(star3_y)}" keyTimes="{key_times}" dur="{duration_s:.2f}s" calcMode="discrete" repeatCount="indefinite"/>')
    lines.append('        <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="1.3s" repeatCount="indefinite"/>')
    lines.append('        &#9733;')
    lines.append('      </text>')
    lines.append('      <!-- Dizzy Spiral Particles -->')
    lines.append('      <text x="450" y="125" text-anchor="middle" font-family="\'Fira Code\',monospace" font-size="24" font-weight="900" fill="#ff0033" letter-spacing="5" filter="url(#gl)">')
    lines.append('        GAME OVER')
    lines.append('      </text>')
    lines.append('      <text x="450" y="148" text-anchor="middle" font-family="\'Fira Code\',monospace" font-size="11" font-weight="700" fill="#ff73fa" letter-spacing="2">')
    lines.append('        // SELF-COLLISION CRASH //')
    lines.append('      </text>')
    lines.append('    </g>')
    lines.append('  </g>')
    lines.append('</svg>')
    
    svg_content = "\n".join(lines)
    with open('snake.svg', 'w', encoding='utf-8') as f:
        f.write(svg_content)
    print(f"snake.svg successfully written! Size: {len(svg_content) / 1024:.2f} KB, Lines: {len(lines)}")

if __name__ == '__main__':
    generate_svg()
