import math

def build_space_invaders_svg():
    TOTAL_DUR = 60.0

    # 1978 Space Invaders Sprite Data (Exact ROM Pixel Matrices)
    SPRITES = {
        "squid_a": [
            "00011000",
            "00111100",
            "01111110",
            "11011011",
            "11111111",
            "00100100",
            "01011010",
            "10100101"
        ],
        "squid_b": [
            "00011000",
            "00111100",
            "01111110",
            "11011011",
            "11111111",
            "01011010",
            "10000001",
            "01000010"
        ],
        "crab_a": [
            "00100000100",
            "00010001000",
            "00111111100",
            "01101110110",
            "11111111111",
            "10111111101",
            "10100000101",
            "00011011000"
        ],
        "crab_b": [
            "00100000100",
            "10010001001",
            "10111111101",
            "11101110111",
            "01111111110",
            "00111111100",
            "01000000010",
            "00100000100"
        ],
        "octo_a": [
            "000011110000",
            "011111111110",
            "111111111111",
            "111001100111",
            "111111111111",
            "000110011000",
            "001101101100",
            "110000000011"
        ],
        "octo_b": [
            "000011110000",
            "011111111110",
            "111111111111",
            "111001100111",
            "111111111111",
            "001111111100",
            "011000000110",
            "000110011000"
        ],
        "ufo": [
            "0000011111100000",
            "0001111111111100",
            "0011111111111110",
            "0110110110110110",
            "1111111111111111",
            "0001110000111000",
            "0000100000010000"
        ],
        "alien_exp": [
            "0001000001000",
            "1000100010001",
            "0100000000010",
            "0010000000100",
            "0010000000100",
            "0100000000010",
            "1000100010001",
            "0001000001000"
        ],
        "cannon": [
            "0000001000000",
            "0000011100000",
            "0000011100000",
            "0111111111110",
            "1111111111111",
            "1111111111111",
            "1111111111111",
            "1111111111111"
        ],
        "cannon_exp": [
            "000100100100100",
            "010010010010010",
            "100100101001001",
            "010001000100010",
            "001010000010100",
            "010001000100010",
            "100100101001001",
            "001001001001000"
        ]
    }

    def matrix_to_path(matrix, px_w=2.0, px_h=2.0):
        rects = []
        for r, row in enumerate(matrix):
            for c, char in enumerate(row):
                if char == '1':
                    rects.append(f"M{c*px_w:.1f} {r*px_h:.1f}h{px_w:.1f}v{px_h:.1f}h-{px_w:.1f}z")
        return " ".join(rects)

    # 3 Waves (Wave 1: 0-20s, Wave 2: 20-40s, Wave 3: 40-60s)
    waves = [
        {
            "id": 1,
            "t_s": 0.0,
            "t_e": 20.0,
            "ufo_t": 7.5,
            "ufo_pts": 300,
            "kills": [
                (2.2, 4, 1, 10),
                (3.8, 3, 2, 10),
                (5.4, 2, 3, 20),
                (7.0, 1, 4, 20),
                (7.5, "ufo", 0, 300),
                (9.2, 0, 5, 30),
                (11.0, 4, 6, 10),
                (12.8, 2, 0, 20),
                (14.5, 1, 7, 20),
                (16.0, 0, 2, 30),
            ],
            "player_hit_t": 17.5,
        },
        {
            "id": 2,
            "t_s": 20.0,
            "t_e": 40.0,
            "ufo_t": 27.8,
            "ufo_pts": 150,
            "kills": [
                (2.0, 4, 3, 10),
                (3.6, 3, 4, 10),
                (5.2, 2, 2, 20),
                (6.8, 1, 5, 20),
                (7.8, "ufo", 0, 150),
                (9.5, 0, 3, 30),
                (11.2, 4, 0, 10),
                (13.0, 3, 6, 10),
                (14.8, 2, 7, 20),
                (16.5, 0, 4, 30),
            ],
            "player_hit_t": 18.0,
        },
        {
            "id": 3,
            "t_s": 40.0,
            "t_e": 60.0,
            "ufo_t": 48.0,
            "ufo_pts": 300,
            "kills": [
                (1.8, 4, 4, 10),
                (3.4, 3, 3, 10),
                (5.0, 2, 5, 20),
                (6.6, 1, 2, 20),
                (8.0, "ufo", 0, 300),
                (9.8, 0, 1, 30),
                (11.5, 4, 7, 10),
                (13.2, 2, 4, 20),
                (15.0, 1, 6, 20),
                (16.8, 0, 6, 30),
            ],
            "player_hit_t": 18.2,
        }
    ]

    COLS_X = [210 + c * 54 for c in range(8)]
    ROWS_Y = [52, 72, 92, 112, 132]

    # Alien Sprites in <defs>
    defs_sprites = []
    for name, mat in SPRITES.items():
        defs_sprites.append(f'    <g id="{name}"><path d="{matrix_to_path(mat, 2.0, 2.0)}" fill="currentColor"/></g>')

    bunker_svg = """
    <g id="bunker">
      <path d="
        M 6 0 H 38 V 4 H 44 V 26 H 32 V 18 H 28 V 14 H 16 V 18 H 12 V 26 H 0 V 4 H 6 Z
      " fill="#00ff88"/>
    </g>
    """

    # Compact Alien Rendering
    # Each alien uses exact transition times: t_start, d_abs, d_abs+0.28, d_abs+0.5, t_end
    def render_wave_aliens_compact(wave_cfg):
        w_id = wave_cfg["id"]
        t_start = wave_cfg["t_s"]
        t_end = wave_cfg["t_e"]
        kills_dict = {}
        for kt, r, c, pts in wave_cfg["kills"]:
            if r != "ufo":
                kills_dict[(r, c)] = kt

        aliens_xml = []
        for r in range(5):
            for c in range(8):
                ax = COLS_X[c]
                ay = ROWS_Y[r]
                sp_type = "squid" if r == 0 else ("crab" if r in [1, 2] else "octo")
                color = "#ffffff" if r == 0 else ("#00f0ff" if r in [1, 2] else "#00ff88")
                pts = 30 if r == 0 else (20 if r in [1, 2] else 10)

                death_t = kills_dict.get((r, c), None)

                if death_t is None:
                    # Alien never dies in this wave
                    k_times = f"0.0;{t_start/TOTAL_DUR:.4f};{t_end/TOTAL_DUR:.4f};1.0"
                    al_node = f"""
        <g transform="translate({ax} {ay})" color="{color}">
          <g>
            <animate attributeName="opacity" values="0;1;0;0" keyTimes="{k_times}" dur="{TOTAL_DUR}s" repeatCount="indefinite"/>
            <use href="#{sp_type}_a"><animate attributeName="display" values="inline;none;inline" dur="0.8s" repeatCount="indefinite"/></use>
            <use href="#{sp_type}_b"><animate attributeName="display" values="none;inline;none" dur="0.8s" repeatCount="indefinite"/></use>
          </g>
        </g>"""
                else:
                    d_abs = t_start + death_t
                    # Alive from t_start to d_abs
                    t0 = 0.0
                    t1 = t_start / TOTAL_DUR
                    t2 = d_abs / TOTAL_DUR
                    t3 = min(1.0, (d_abs + 0.28) / TOTAL_DUR)
                    t4 = min(1.0, (d_abs + 0.60) / TOTAL_DUR)
                    t5 = t_end / TOTAL_DUR

                    al_node = f"""
        <g transform="translate({ax} {ay})" color="{color}">
          <!-- Alien Normal -->
          <g>
            <animate attributeName="opacity" values="0;1;0;0;0" keyTimes="{t0:.4f};{t1:.4f};{t2:.4f};{t5:.4f};1.0" dur="{TOTAL_DUR}s" repeatCount="indefinite"/>
            <use href="#{sp_type}_a"><animate attributeName="display" values="inline;none;inline" dur="0.8s" repeatCount="indefinite"/></use>
            <use href="#{sp_type}_b"><animate attributeName="display" values="none;inline;none" dur="0.8s" repeatCount="indefinite"/></use>
          </g>
          <!-- Explosion Sprite -->
          <g color="#ffd700">
            <animate attributeName="opacity" values="0;0;1;0;0" keyTimes="{t0:.4f};{t2:.4f};{t2:.4f};{t3:.4f};1.0" dur="{TOTAL_DUR}s" repeatCount="indefinite"/>
            <use href="#alien_exp"/>
          </g>
          <!-- Score Popup -->
          <text x="10" y="-3" text-anchor="middle" font-family="'Fira Code', monospace" font-size="9" font-weight="900" fill="#ffd700">
            <animate attributeName="opacity" values="0;0;1;0;0" keyTimes="{t0:.4f};{t2:.4f};{t2:.4f};{t4:.4f};1.0" dur="{TOTAL_DUR}s" repeatCount="indefinite"/>
            +{pts}
          </text>
        </g>"""
                aliens_xml.append(al_node)
        return "\n".join(aliens_xml)

    # Marching Transform per wave
    # 20 steps per wave
    waves_content = []
    for w in waves:
        w_id = w["id"]
        t_s = w["t_s"] / TOTAL_DUR
        t_e = w["t_e"] / TOTAL_DUR
        disp_vals = f"none;inline;none" if w_id == 2 else ("inline;none;none" if w_id == 1 else "none;none;inline")
        disp_keys = f"0.0;{t_s:.4f};{t_e:.4f};1.0" if w_id == 2 else (f"0.0;{t_e:.4f};1.0" if w_id == 1 else f"0.0;{t_s:.4f};1.0")

        # March step keys (every 0.8s, stepping left-right and dropping)
        # Shift values
        step_times = []
        step_shifts = []
        cur_x = -24
        cur_y = 0
        dir_x = 1
        for step in range(24):
            t_rel = step * 0.82
            t_abs = w["t_s"] + t_rel
            if t_abs > w["t_e"]:
                break
            if dir_x == 1:
                cur_x += 10
                if cur_x >= 30:
                    dir_x = -1
                    cur_y += 7
            else:
                cur_x -= 10
                if cur_x <= -30:
                    dir_x = 1
                    cur_y += 7
            step_times.append(f"{t_abs/TOTAL_DUR:.4f}")
            step_shifts.append(f"{cur_x} {cur_y}")

        # pad to 0.0 and 1.0
        if step_times[0] != "0.0000":
            step_times.insert(0, "0.0000")
            step_shifts.insert(0, step_shifts[0])
        if step_times[-1] != "1.0000":
            step_times.append("1.0000")
            step_shifts.append(step_shifts[-1])

        aliens_body = render_wave_aliens_compact(w)
        wave_block = f"""
    <!-- ==================== WAVE {w_id:02d} ALIEN ARMADA ==================== -->
    <g>
      <animate attributeName="display" values="{disp_vals}" keyTimes="{disp_keys}" dur="{TOTAL_DUR}s" repeatCount="indefinite"/>
      <g>
        <animateTransform attributeName="transform" type="translate"
          values="{";".join(step_shifts)}" keyTimes="{";".join(step_times)}" dur="{TOTAL_DUR}s" repeatCount="indefinite"/>
        {aliens_body}
      </g>
    </g>"""
        waves_content.append(wave_block)

    # UFO Flying Saucer
    ufo_xml_list = []
    for w in waves:
        u_t = w["t_s"] + w["ufo_t"]
        u_pts = w["ufo_pts"]
        t_enter = (u_t - 2.8) / TOTAL_DUR
        t_hit = u_t / TOTAL_DUR
        t_exit = (u_t + 0.6) / TOTAL_DUR

        ufo_block = f"""
    <!-- WAVE {w['id']} MYSTERY UFO -->
    <g>
      <animate attributeName="display"
        values="none;inline;none;none"
        keyTimes="0.0;{t_enter:.4f};{t_exit:.4f};1.0"
        dur="{TOTAL_DUR}s" repeatCount="indefinite"/>
      <g>
        <animateTransform attributeName="transform" type="translate"
          values="880 40; 880 40; 430 40; 430 40; -60 40"
          keyTimes="0.0; {t_enter:.4f}; {t_hit:.4f}; {(u_t + 0.3)/TOTAL_DUR:.4f}; 1.0"
          dur="{TOTAL_DUR}s" repeatCount="indefinite"/>
        <!-- UFO Hull -->
        <g color="#ff0044">
          <animate attributeName="opacity" values="1;1;0;0" keyTimes="0.0;{t_hit:.4f};{(u_t + 0.02)/TOTAL_DUR:.4f};1.0" dur="{TOTAL_DUR}s" repeatCount="indefinite"/>
          <use href="#ufo"/>
        </g>
        <!-- UFO Explosion & Points -->
        <g color="#ffd700" opacity="0">
          <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0.0;{t_hit:.4f};{(u_t + 0.02)/TOTAL_DUR:.4f};{(u_t + 0.35)/TOTAL_DUR:.4f};{(u_t + 0.55)/TOTAL_DUR:.4f};1.0" dur="{TOTAL_DUR}s" repeatCount="indefinite"/>
          <use href="#alien_exp" transform="translate(6 0)"/>
          <text x="18" y="-5" text-anchor="middle" font-family="'Fira Code', monospace" font-size="11" font-weight="900" fill="#ffd700">+{u_pts}</text>
        </g>
      </g>
    </g>"""
        ufo_xml_list.append(ufo_block)

    # Lasers
    lasers_xml = []
    for w in waves:
        for kt, r, c, pts in w["kills"]:
            fire_t = (w["t_s"] + kt - 0.20) / TOTAL_DUR
            hit_t = (w["t_s"] + kt) / TOTAL_DUR
            target_y = 42 if r == "ufo" else ROWS_Y[r] + 10
            shoot_x = 430 if r == "ufo" else COLS_X[c] + 12

            l_block = f"""
    <!-- Laser Shot -->
    <line x1="{shoot_x}" y1="196" x2="{shoot_x}" y2="{target_y}" stroke="#ffffff" stroke-width="2.2" stroke-linecap="round" opacity="0">
      <animate attributeName="opacity" values="0;1;0;0" keyTimes="0.0;{fire_t:.4f};{hit_t:.4f};1.0" dur="{TOTAL_DUR}s" repeatCount="indefinite"/>
      <animate attributeName="y1" values="196;196;{target_y};{target_y}" keyTimes="0.0;{fire_t:.4f};{hit_t:.4f};1.0" dur="{TOTAL_DUR}s" repeatCount="indefinite"/>
    </line>"""
            lasers_xml.append(l_block)

    # Alien Bombs dropping
    bombs_xml = []
    for w in waves:
        for bi in range(5):
            bt_start = (w["t_s"] + 1.2 + bi * 3.4) / TOTAL_DUR
            bt_hit = (w["t_s"] + 1.2 + bi * 3.4 + 1.1) / TOTAL_DUR
            bx = 240 + bi * 115
            b_block = f"""
    <!-- Alien Bomb -->
    <path d="M0 0 L2 4 L-2 8 L2 12" stroke="#ff0055" stroke-width="2" fill="none" opacity="0">
      <animate attributeName="opacity" values="0;1;0;0" keyTimes="0.0;{bt_start:.4f};{bt_hit:.4f};1.0" dur="{TOTAL_DUR}s" repeatCount="indefinite"/>
      <animateTransform attributeName="transform" type="translate"
        values="{bx} 80; {bx} 80; {bx} 206; {bx} 206"
        keyTimes="0.0;{bt_start:.4f};{bt_hit:.4f};1.0" dur="{TOTAL_DUR}s" repeatCount="indefinite"/>
    </path>"""
            bombs_xml.append(b_block)

    # Player Tank Trajectory (aiming at targets)
    # Key targets in 60s
    player_keyframes = []
    # start
    player_keyframes.append((0.0, 450))
    for w in waves:
        for kt, r, c, pts in w["kills"]:
            fire_t = w["t_s"] + kt - 0.25
            target_x = 430 if r == "ufo" else COLS_X[c] + 12
            player_keyframes.append((fire_t - 0.4, target_x - 10))
            player_keyframes.append((fire_t, target_x))
            player_keyframes.append((fire_t + 0.3, target_x))
        # hit
        h_t = w["t_s"] + w["player_hit_t"]
        player_keyframes.append((h_t, 380))
        player_keyframes.append((h_t + 1.5, 380))

    player_keyframes.append((60.0, 450))
    # sort and normalize
    player_keyframes = sorted(player_keyframes, key=lambda k: k[0])
    # remove duplicates
    filt_keys = [player_keyframes[0]]
    for k in player_keyframes[1:]:
        if k[0] > filt_keys[-1][0] + 0.05:
            filt_keys.append(k)
    if filt_keys[-1][0] < 60.0:
        filt_keys.append((60.0, filt_keys[-1][1]))

    px_times = [f"{k[0]/TOTAL_DUR:.4f}" for k in filt_keys]
    px_vals = [f"{k[1]:.1f} 0" for k in filt_keys]

    # Player hit explosion timing
    hit_times_keys = []
    hit_normal_vals = []
    hit_exp_vals = []
    for w in waves:
        t0 = w["t_s"]
        th = w["t_s"] + w["player_hit_t"]
        th_end = th + 1.6
        t_end = w["t_e"]
        hit_times_keys.extend([f"{t0/TOTAL_DUR:.4f}", f"{th/TOTAL_DUR:.4f}", f"{th_end/TOTAL_DUR:.4f}"])
        hit_normal_vals.extend(["1", "0", "1"])
        hit_exp_vals.extend(["0", "1", "0"])

    hit_times_keys.append("1.0000")
    hit_normal_vals.append("1")
    hit_exp_vals.append("0")

    # Score timeline calculation
    # Track cumulative score per wave
    score_events = []
    score_events.append((0.0, 0))
    for w in waves:
        sc = 0
        score_events.append((w["t_s"], 0))
        for kt, r, c, pts in w["kills"]:
            sc += pts
            score_events.append((w["t_s"] + kt, sc))
        score_events.append((w["t_e"], sc))

    unique_scores = sorted(list(set(s[1] for s in score_events)))
    score_nodes = []
    for us in unique_scores:
        # find time intervals where score == us
        # construct discrete opacity keyframes
        t_keys = []
        op_vals = []
        curr_state = 0
        for i in range(len(score_events)-1):
            t_cur, sc_cur = score_events[i]
            t_next, _ = score_events[i+1]
            state = 1 if sc_cur == us else 0
            t_keys.append(f"{t_cur/TOTAL_DUR:.4f}")
            op_vals.append(str(state))
        t_keys.append("1.0000")
        op_vals.append(op_vals[-1])

        # clean duplicates in consecutive values
        node = f"""        <text x="0" y="0" fill="#00ff88" opacity="0">
          <animate attributeName="opacity" values="{";".join(op_vals)}" keyTimes="{";".join(t_keys)}" dur="{TOTAL_DUR}s" calcMode="discrete" repeatCount="indefinite"/>
          {us:04d}
        </text>"""
        score_nodes.append(node)

    svg = f"""<svg width="900" height="250" viewBox="0 0 900 250" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Authentic 1978 Space Invaders Arcade Rioon7337">
  <defs>
    <!-- Deep Arcade CRT Black Background -->
    <radialGradient id="bgCrt" cx="50%" cy="50%" r="85%">
      <stop offset="0%" stop-color="#0a0e1c"/>
      <stop offset="60%" stop-color="#05070e"/>
      <stop offset="100%" stop-color="#020308"/>
    </radialGradient>

    <!-- Animated RGB Neon Outer Border -->
    <linearGradient id="rgbInv" gradientUnits="userSpaceOnUse" x1="12" y1="125" x2="888" y2="125">
      <stop offset="0%" stop-color="#00f0ff">
        <animate attributeName="stop-color" values="#00f0ff;#d946ef;#00ffcc;#00f0ff" dur="5s" repeatCount="indefinite"/>
      </stop>
      <stop offset="33%" stop-color="#d946ef">
        <animate attributeName="stop-color" values="#d946ef;#00f0ff;#ff73fa;#d946ef" dur="5s" repeatCount="indefinite"/>
      </stop>
      <stop offset="66%" stop-color="#00ffcc">
        <animate attributeName="stop-color" values="#00ffcc;#ff73fa;#00f0ff;#00ffcc" dur="5s" repeatCount="indefinite"/>
      </stop>
      <stop offset="100%" stop-color="#00f0ff">
        <animate attributeName="stop-color" values="#00f0ff;#d946ef;#00ffcc;#00f0ff" dur="5s" repeatCount="indefinite"/>
      </stop>
      <animateTransform attributeName="gradientTransform" type="rotate" from="0 450 125" to="360 450 125" dur="4.5s" repeatCount="indefinite"/>
    </linearGradient>

    <!-- CRT Arcade Scanline Pattern -->
    <pattern id="scanlines" width="100" height="4" patternUnits="userSpaceOnUse">
      <line x1="0" y1="0" x2="100" y2="0" stroke="#00f0ff" stroke-width="0.3" opacity="0.06"/>
    </pattern>

    <filter id="glowInv" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2.2" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>

    <clipPath id="clipPlayfield">
      <rect x="12" y="12" width="876" height="226" rx="16"/>
    </clipPath>

    <!-- ==================== 1978 ROM SPRITES ==================== -->
{"".join(defs_sprites)}
{bunker_svg}
  </defs>

  <!-- Outer Neon Border Aura -->
  <rect x="12" y="12" width="876" height="226" rx="16" fill="none" stroke="url(#rgbInv)" stroke-width="5" opacity="0.35" filter="url(#glowInv)"/>
  <rect x="12" y="12" width="876" height="226" rx="16" fill="url(#bgCrt)"/>
  <rect x="12" y="12" width="876" height="226" rx="16" fill="url(#scanlines)"/>

  <!-- Main Game Field (Clipped inside rounded bezel) -->
  <g clip-path="url(#clipPlayfield)">

    <!-- ==================== AUTHENTIC 1978 ARCADE HUD HEADER ==================== -->
    <g transform="translate(0 34)" font-family="'Fira Code', 'Press Start 2P', monospace" font-size="11" font-weight="900" letter-spacing="2">
      <!-- Player 1 Score -->
      <text x="50" y="0" fill="#ffffff">SCORE&lt;1&gt;</text>
      <!-- Centered Hi-Score -->
      <text x="450" y="0" text-anchor="middle" fill="#ff0055">HI-SCORE</text>
      <!-- Player 2 Score -->
      <text x="850" y="0" text-anchor="end" fill="#ffffff">SCORE&lt;2&gt;</text>

      <!-- Dynamic P1 Score Value -->
      <g transform="translate(50 14)">
{"".join(score_nodes)}
      </g>

      <!-- Hi-Score Value -->
      <text x="450" y="14" text-anchor="middle" fill="#ffffff">250807</text>
      <!-- P2 Score Value -->
      <text x="850" y="14" text-anchor="end" fill="#00ff88">0000</text>
    </g>

    <!-- Mystery UFOs -->
{"".join(ufo_xml_list)}

    <!-- Alien Armadas (Waves 1, 2, 3) -->
{"".join(waves_content)}

    <!-- Player Lasers -->
{"".join(lasers_xml)}

    <!-- Alien Bombs -->
{"".join(bombs_xml)}

    <!-- 4 Original Green Defense Bunkers -->
    <g transform="translate(180 168)"><use href="#bunker"/></g>
    <g transform="translate(360 168)"><use href="#bunker"/></g>
    <g transform="translate(540 168)"><use href="#bunker"/></g>
    <g transform="translate(720 168)"><use href="#bunker"/></g>

    <!-- ==================== PLAYER LASER CANNON (TANK) ==================== -->
    <g transform="translate(0 200)">
      <!-- Smooth Glide Movement -->
      <animateTransform attributeName="transform" type="translate"
        values="{";".join(px_vals)}" keyTimes="{";".join(px_times)}" dur="{TOTAL_DUR}s" repeatCount="indefinite"/>

      <!-- Normal Green Cannon -->
      <g color="#00ff88">
        <animate attributeName="opacity" values="{";".join(hit_normal_vals)}" keyTimes="{";".join(hit_times_keys)}" dur="{TOTAL_DUR}s" calcMode="discrete" repeatCount="indefinite"/>
        <use href="#cannon"/>
      </g>

      <!-- Destruction Explosion when hit by alien bomb -->
      <g color="#ff0055">
        <animate attributeName="opacity" values="{";".join(hit_exp_vals)}" keyTimes="{";".join(hit_times_keys)}" dur="{TOTAL_DUR}s" calcMode="discrete" repeatCount="indefinite"/>
        <use href="#cannon_exp"/>
      </g>
    </g>

    <!-- ==================== AUTHENTIC 1978 ARCADE BASELINE & FOOTER ==================== -->
    <!-- Green Ground Line -->
    <line x1="12" y1="216" x2="888" y2="216" stroke="#00ff88" stroke-width="2"/>

    <!-- Bottom Arcade Info: Lives Counter & Credit -->
    <g transform="translate(0 230)" font-family="'Fira Code', 'Press Start 2P', monospace" font-size="10" font-weight="900" fill="#00ff88" letter-spacing="2">
      <!-- Player Lives -->
      <g transform="translate(50 -10)">
        <text x="0" y="8" fill="#ffffff">3</text>
        <g transform="translate(18 0)"><use href="#cannon" color="#00ff88" transform="scale(0.8)"/></g>
        <g transform="translate(44 0)"><use href="#cannon" color="#00ff88" transform="scale(0.8)"/></g>
      </g>
      <!-- Center Title -->
      <text x="450" y="0" text-anchor="middle" fill="#00f0ff">// SPACE INVADERS &#183; TAITO 1978 //</text>
      <!-- Credit -->
      <text x="850" y="0" text-anchor="end" fill="#ffffff">CREDIT 00</text>
    </g>

  </g>

  <!-- Cyber Corners -->
  <path d="M22 42 L22 22 L42 22" stroke="#00f0ff" stroke-width="2" fill="none" opacity=".85"/>
  <path d="M878 42 L878 22 L858 22" stroke="#00f0ff" stroke-width="2" fill="none" opacity=".85"/>
  <path d="M22 208 L22 228 L42 228" stroke="#d946ef" stroke-width="2" fill="none" opacity=".85"/>
  <path d="M878 208 L878 228 L858 228" stroke="#d946ef" stroke-width="2" fill="none" opacity=".85"/>

  <!-- Traveling Border Tracer -->
  <rect x="12" y="12" width="876" height="226" rx="16" fill="none" stroke="url(#rgbInv)" stroke-width="1.6"/>
  <rect x="12" y="12" width="876" height="226" rx="16" fill="none" stroke="#00f0ff" stroke-width="2" stroke-linecap="round" opacity="0.9" pathLength="1000" stroke-dasharray="85 915" filter="url(#glowInv)">
    <animate attributeName="stroke-dashoffset" from="0" to="-1000" dur="4s" repeatCount="indefinite"/>
  </rect>
</svg>"""

    with open("space-invaders.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"space-invaders.svg generated! Size: {len(svg)/1024:.2f} KB")

if __name__ == "__main__":
    build_space_invaders_svg()
