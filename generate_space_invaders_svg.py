import random
import math
import xml.etree.ElementTree as ET

def generate_space_invaders_svg():
    TOTAL_DUR = 60.0

    waves_config = [
        {
            "id": 1,
            "label": "WAVE 01 / 03 &#183; RANDOM INVASION",
            "seed": 5511,
            "t_start": 0.0,
            "t_end": 20.0,
            "ufo_time": 8.4,
            "ufo_type": "red",
            "ufo_pts": 300,
            "ufo_x": 420,
            "death_time": 16.2,
            "death_x": 480,
        },
        {
            "id": 2,
            "label": "WAVE 02 / 03 &#183; RANDOM INVASION",
            "seed": 8822,
            "t_start": 20.0,
            "t_end": 40.0,
            "ufo_time": 28.2,
            "ufo_type": "gold",
            "ufo_pts": 500,
            "ufo_x": 490,
            "death_time": 36.4,
            "death_x": 310,
        },
        {
            "id": 3,
            "label": "WAVE 03 / 03 &#183; RANDOM INVASION",
            "seed": 3333,
            "t_start": 40.0,
            "t_end": 60.0,
            "ufo_time": 48.0,
            "ufo_type": "red",
            "ufo_pts": 300,
            "ufo_x": 380,
            "death_time": 56.2,
            "death_x": 560,
        }
    ]

    squid_xs = [180, 245, 310, 375, 440, 505, 570, 635]
    crab_xs  = [178, 243, 308, 373, 438, 503, 568, 633]
    octo_xs  = [176, 241, 306, 371, 436, 501, 566, 631]

    waves_data = []

    for w in waves_config:
        rng = random.Random(w["seed"])
        t_s = w["t_start"]
        t_e = w["t_end"]

        # Pool of 24 aliens
        all_aliens = []
        for col in range(8):
            all_aliens.append(("squid", 0, col, squid_xs[col], 50, 30, "#ff73fa"))
            all_aliens.append(("crab", 1, col, crab_xs[col], 78, 20, "#00f0ff"))
            all_aliens.append(("octo", 2, col, octo_xs[col], 106, 10, "#00ff88"))
        
        # Pick 6 distinct aliens for this wave
        chosen = rng.sample(all_aliens, 6)

        # 6 alien kills + 1 UFO kill = 7 kills per wave
        times = [
            t_s + 1.2,
            t_s + 3.4,
            t_s + 5.8,
            w["ufo_time"],
            t_s + 10.6,
            t_s + 12.8,
            t_s + 14.4
        ]

        kills = []
        al_idx = 0
        for t in times:
            if abs(t - w["ufo_time"]) < 0.05:
                kills.append({
                    "is_ufo": True,
                    "t": round(t, 2),
                    "x": w["ufo_x"],
                    "y": 44,
                    "pts": w["ufo_pts"],
                    "color": "#ffd700" if w["ufo_type"] == "gold" else "#ff0055",
                    "ufo_type": w["ufo_type"]
                })
            else:
                al = chosen[al_idx]
                al_idx += 1
                kills.append({
                    "is_ufo": False,
                    "t": round(t, 2),
                    "species": al[0],
                    "row": al[1],
                    "col": al[2],
                    "x": al[3],
                    "y": al[4],
                    "pts": al[5],
                    "color": al[6]
                })

        # Bombs
        bombs = []
        # Bomb 1: drops at t_s + 2.2, hits bunker at t_s + 3.0
        bombs.append({
            "x": octo_xs[rng.choice([1, 4, 6])],
            "t_drop": round(t_s + 2.2, 2),
            "t_hit": round(t_s + 3.0, 2),
            "hit_y": 156,
            "color": "#ff0055",
            "is_fatal": False
        })
        # Bomb 2: drops at t_s + 6.6, hits ground at t_s + 7.7
        bombs.append({
            "x": octo_xs[rng.choice([2, 5, 7])],
            "t_drop": round(t_s + 6.6, 2),
            "t_hit": round(t_s + 7.7, 2),
            "hit_y": 210,
            "color": "#ff73fa",
            "is_fatal": False
        })
        # Bomb 3: drops near tank, evaded!
        b3_x = w["death_x"] - 50 if w["death_x"] > 400 else w["death_x"] + 50
        bombs.append({
            "x": b3_x,
            "t_drop": round(t_s + 11.2, 2),
            "t_hit": round(t_s + 12.2, 2),
            "hit_y": 210,
            "color": "#ff0055",
            "is_fatal": False
        })
        # Fatal Bomb 4: hits tank!
        bombs.append({
            "x": w["death_x"],
            "t_drop": round(w["death_time"] - 1.0, 2),
            "t_hit": round(w["death_time"], 2),
            "hit_y": 198,
            "color": "#00f0ff",
            "is_fatal": True
        })

        waves_data.append({
            "config": w,
            "kills": kills,
            "bombs": bombs
        })

    # Build Tank Movement Keyframes across all 60s
    tank_keyframes = []
    laser_shots = []

    for w in waves_data:
        cfg = w["config"]
        t_s = cfg["t_start"]
        t_e = cfg["t_end"]
        death_t = cfg["death_time"]
        death_x = cfg["death_x"]

        # Spawn at t_s
        tank_keyframes.append((round(t_s, 2), 380))

        # Maneuvers to each kill shot
        last_x = 380
        last_t = t_s
        for k in w["kills"]:
            tx = k["x"]
            # player tank center is tx+16, so tank left corner is tx
            tank_x = max(180, min(640, tx))
            shot_t = k["t"]
            
            # Arrive slightly before shot
            arr_t = round(shot_t - 0.25, 2)
            if arr_t > last_t + 0.1:
                tank_keyframes.append((arr_t, tank_x))
            tank_keyframes.append((round(shot_t, 2), tank_x))
            last_x = tank_x
            last_t = shot_t

            # Record laser shot
            laser_shots.append({
                "wave_id": cfg["id"],
                "tank_x": tank_x + 16,
                "target_x": k["x"] + 10 if not k["is_ufo"] else k["x"] + 18,
                "target_y": k["y"] + 8,
                "t_shot": round(shot_t - 0.15, 2),
                "t_hit": round(shot_t, 2),
                "color": k["color"],
                "is_ufo": k["is_ufo"]
            })

        # Move to death position
        arr_death = round(death_t - 0.35, 2)
        if arr_death > last_t + 0.1:
            tank_keyframes.append((arr_death, death_x))
        tank_keyframes.append((round(death_t, 2), death_x))

        # Tank destroyed! Stays offscreen or invisible from death_t to t_e
        tank_keyframes.append((round(death_t + 0.05, 2), death_x))
        tank_keyframes.append((round(t_e - 0.05, 2), death_x))

    tank_keyframes.sort(key=lambda k: k[0])
    if tank_keyframes[0][0] != 0.0:
        tank_keyframes.insert(0, (0.0, 380))
    if tank_keyframes[-1][0] < TOTAL_DUR:
        tank_keyframes.append((TOTAL_DUR, tank_keyframes[-1][1]))

    # Deduplicate tank keyframes
    clean_tank = [tank_keyframes[0]]
    for tkf in tank_keyframes[1:]:
        if tkf[0] > clean_tank[-1][0] + 0.001:
            clean_tank.append(tkf)
    tank_keyframes = clean_tank

    tank_x_vals = "; ".join(f"{x} 198" for (t, x) in tank_keyframes)
    tank_kts = "; ".join(str(round(t / TOTAL_DUR, 5)) for (t, x) in tank_keyframes)

    # Tank Opacity (visible while alive, hidden after death in each wave)
    tank_op_pts = []
    for w in waves_data:
        cfg = w["config"]
        t_s = cfg["t_start"]
        death_t = cfg["death_time"]
        t_e = cfg["t_end"]
        tank_op_pts.append((t_s, 1))
        tank_op_pts.append((round(death_t - 0.01, 2), 1))
        tank_op_pts.append((round(death_t, 2), 0))
        tank_op_pts.append((round(t_e - 0.01, 2), 0))
    
    tank_op_pts.sort(key=lambda p: p[0])
    # Deduplicate
    clean_op = [tank_op_pts[0]]
    for p in tank_op_pts[1:]:
        if p[0] > clean_op[-1][0] + 0.001:
            clean_op.append(p)
    tank_op_pts = clean_op

    tank_op_vals = "; ".join(str(v) for (t, v) in tank_op_pts)
    tank_op_kts = "; ".join(str(round(t / TOTAL_DUR, 5)) for (t, v) in tank_op_pts)

    # Wave Status HUD
    hud_waves_xml = []
    for w_idx, w in enumerate(waves_data):
        cfg = w["config"]
        label = cfg["label"]
        t_s = cfg["t_start"] / TOTAL_DUR
        t_e = cfg["t_end"] / TOTAL_DUR
        
        if w_idx == 0:
            op_vals = "1;0"
            op_kts = f"0.0;{t_e:.4f};1.0"
        elif w_idx == len(waves_data) - 1:
            op_vals = "0;1"
            op_kts = f"0.0;{t_s:.4f};1.0"
        else:
            op_vals = "0;1;0"
            op_kts = f"0.0;{t_s:.4f};{t_e:.4f};1.0"
            
        hud_waves_xml.append(f"""    <text text-anchor="middle" y="0" font-family="'Fira Code', monospace" font-size="10.5" font-weight="800" fill="#00ffcc" letter-spacing="1.5">
      <animate attributeName="opacity" calcMode="discrete" values="{op_vals}" keyTimes="{op_kts}" dur="60s" repeatCount="indefinite"/>
      {label}
    </text>""")

    # Dynamic Score per wave
    score_digits_xml = []
    for w in waves_data:
        cfg = w["config"]
        t_s = cfg["t_start"]
        t_e = cfg["t_end"]
        
        running_score = 0
        # Score segments
        score_segs = [(t_s, w["kills"][0]["t"], 0)]
        for ki, k in enumerate(w["kills"]):
            running_score += k["pts"]
            seg_start = k["t"]
            seg_end = w["kills"][ki + 1]["t"] if ki < len(w["kills"]) - 1 else t_e
            score_segs.append((seg_start, seg_end, running_score))

        for (s_start, s_end, sc) in score_segs:
            kt_s = s_start / TOTAL_DUR
            kt_e = s_end / TOTAL_DUR
            if kt_s >= kt_e:
                continue

            score_str = f"{sc:04d}"
            color = "#00f0ff" if sc < 100 else ("#00ff88" if sc < 500 else "#ffd700")

            if kt_s == 0.0:
                op_vals = "1;0"
                op_kts = f"0.0;{kt_e:.4f};1.0"
            elif kt_e == 1.0:
                op_vals = "0;1"
                op_kts = f"0.0;{kt_s:.4f};1.0"
            else:
                op_vals = "0;1;0"
                op_kts = f"0.0;{kt_s:.4f};{kt_e:.4f};1.0"

            score_digits_xml.append(f"""    <text text-anchor="start" x="12" y="0" font-family="'Fira Code', monospace" font-size="11" font-weight="900" fill="{color}">
      <animate attributeName="opacity" calcMode="discrete" values="{op_vals}" keyTimes="{op_kts}" dur="60s" repeatCount="indefinite"/>{score_str}
    </text>""")

    # Generate UFOs XML
    ufos_xml = []
    for w in waves_data:
        cfg = w["config"]
        w_id = cfg["id"]
        u_t = cfg["ufo_time"]
        u_x = cfg["ufo_x"]
        u_type = cfg["ufo_type"]
        pts = cfg["ufo_pts"]

        # UFO crosses over a ~2.2s window
        t_in = u_t - 1.8
        t_out = u_t + 0.8
        kt_in = t_in / TOTAL_DUR
        kt_hit = u_t / TOTAL_DUR
        kt_out = t_out / TOTAL_DUR

        if u_type == "gold":
            ufo_body = """            <g fill="#ffd700">
              <path d="M14 0h16v2h-16z M10 2h24v2h-24z M6 4h32v3h-32z M0 7h44v3h-44z M6 10h8v2h-8z M18 10h8v2h-8z M30 10h8v2h-8z"/>
              <circle cx="12" cy="5" r="1.8" fill="#00f0ff"/>
              <circle cx="22" cy="5" r="2.2" fill="#ffffff"/>
              <circle cx="32" cy="5" r="1.8" fill="#ff73fa"/>
            </g>"""
        else:
            ufo_body = """            <g fill="#ff0055">
              <path d="M12 0h12v2h-12z M8 2h20v2h-20z M4 4h28v3h-28z M0 7h36v3h-36z M6 10h6v2h-6z M16 10h4v2h-4z M24 10h6v2h-6z"/>
              <circle cx="10" cy="5" r="1.5" fill="#ffffff"/>
              <circle cx="18" cy="5" r="1.5" fill="#ffd700"/>
              <circle cx="26" cy="5" r="1.5" fill="#ffffff"/>
            </g>"""

        ufos_xml.append(f"""    <!-- WAVE {w_id:02d} UFO ({u_type.upper()}) at t={u_t}s -->
    <g>
      <animate attributeName="display" values="none;inline;none;none"
        keyTimes="0.0;{kt_in:.4f};{kt_out:.4f};1.0" dur="60s" repeatCount="indefinite"/>
      <g>
        <animateTransform attributeName="transform" type="translate"
          values="920 44; 920 44; {u_x} 44; {u_x} 44; -80 44; -80 44"
          keyTimes="0.0; {kt_in:.4f}; {kt_hit:.4f}; {(kt_hit+0.005):.4f}; {kt_out:.4f}; 1.0"
          dur="60s" repeatCount="indefinite"/>
        <!-- UFO Body -->
        <g filter="url(#glowInv)">
          <animate attributeName="opacity" values="1;1;0;0"
            keyTimes="0.0;{kt_hit:.4f};{(kt_hit+0.002):.4f};1.0" dur="60s" repeatCount="indefinite"/>
{ufo_body}
        </g>
        <!-- UFO Blast Explosion -->
        <g filter="url(#glowInv)" opacity="0">
          <animate attributeName="opacity" values="0;0;1;0.9;0;0"
            keyTimes="0.0;{kt_hit:.4f};{(kt_hit+0.002):.4f};{(kt_hit+0.012):.4f};{(kt_hit+0.025):.4f};1.0" dur="60s" repeatCount="indefinite"/>
          <circle cx="18" cy="6" r="16" fill="#ffd700"/>
          <circle cx="18" cy="6" r="8" fill="#ffffff"/>
          <text x="18" y="-4" text-anchor="middle" font-family="'Fira Code', monospace" font-size="12" font-weight="900" fill="#ffd700">+{pts}</text>
        </g>
      </g>
    </g>""")

    # Generate Alien Armada for each wave
    armada_waves_xml = []
    for w_idx, w in enumerate(waves_data):
        cfg = w["config"]
        w_id = cfg["id"]
        t_s = cfg["t_start"]
        t_e = cfg["t_end"]
        kt_s = t_s / TOTAL_DUR
        kt_e = t_e / TOTAL_DUR

        # Track killed aliens in this wave
        killed_map = {}
        for k in w["kills"]:
            if not k["is_ufo"]:
                killed_map[(k["row"], k["col"])] = k

        # Build Row 1 (Squid), Row 2 (Crab), Row 3 (Octo)
        rows_xml = []
        for row_idx, (species, xs, sprite_a, sprite_b, color, pts) in enumerate([
            ("squid", squid_xs, "#squidA", "#squidB", "#ff73fa", 30),
            ("crab", crab_xs, "#crabA", "#crabB", "#00f0ff", 20),
            ("octo", octo_xs, "#octoA", "#octoB", "#00ff88", 10),
        ]):
            y_base = 50 if row_idx == 0 else (78 if row_idx == 1 else 106)
            aliens_row_xml = []
            for col_idx, x in enumerate(xs):
                if (row_idx, col_idx) in killed_map:
                    k = killed_map[(row_idx, col_idx)]
                    kt_kill = k["t"] / TOTAL_DUR
                    kt_burst_end = (k["t"] + 0.6) / TOTAL_DUR
                    
                    aliens_row_xml.append(f"""        <!-- {species.upper()} {col_idx+1} (Destroyed at t={k['t']}s) -->
        <g transform="translate({x} {y_base})">
          <g>
            <animate attributeName="opacity" values="1;1;0;0"
              keyTimes="0.0;{kt_kill:.4f};{(kt_kill+0.002):.4f};1.0" dur="60s" repeatCount="indefinite"/>
            <use href="{sprite_a}"><animate attributeName="display" values="inline;none;inline" dur="0.7s" repeatCount="indefinite"/></use>
            <use href="{sprite_b}"><animate attributeName="display" values="none;inline;none" dur="0.7s" repeatCount="indefinite"/></use>
          </g>
          <!-- Death Explosion & Score Popup -->
          <g opacity="0">
            <animate attributeName="opacity" values="0;0;1;0.9;0;0"
              keyTimes="0.0;{kt_kill:.4f};{(kt_kill+0.002):.4f};{(kt_kill+0.008):.4f};{kt_burst_end:.4f};1.0" dur="60s" repeatCount="indefinite"/>
            <circle cx="8" cy="8" r="7" fill="#ffd700"/>
            <text x="8" y="-3" text-anchor="middle" font-family="'Fira Code', monospace" font-size="9" font-weight="900" fill="{color}">+{pts}</text>
          </g>
        </g>""")
                else:
                    aliens_row_xml.append(f"""        <!-- {species.upper()} {col_idx+1} (Active) -->
        <g transform="translate({x} {y_base})">
          <use href="{sprite_a}"><animate attributeName="display" values="inline;none;inline" dur="0.7s" repeatCount="indefinite"/></use>
          <use href="{sprite_b}"><animate attributeName="display" values="none;inline;none" dur="0.7s" repeatCount="indefinite"/></use>
        </g>""")

            rows_xml.append(f"""      <!-- ROW {row_idx+1}: {species.upper()} ALIENS -->
      <g fill="{color}" filter="url(#glowInv)">
{chr(10).join(aliens_row_xml)}
      </g>""")

        if w_idx == 0:
            disp_vals = "inline;none;none"
            disp_kts = f"0.0;{kt_e:.4f};1.0"
        elif w_idx == 1:
            disp_vals = "none;inline;none;none"
            disp_kts = f"0.0;{kt_s:.4f};{kt_e:.4f};1.0"
        else:
            disp_vals = "none;inline"
            disp_kts = f"0.0;{kt_s:.4f};1.0"

        armada_waves_xml.append(f"""    <!-- ==================== WAVE {w_id:02d} ALIEN ARMADA ==================== -->
    <g>
      <animate attributeName="display" values="{disp_vals}" keyTimes="{disp_kts}" dur="60s" repeatCount="indefinite"/>
      <!-- Marching Step Transform -->
      <g>
        <animateTransform attributeName="transform" type="translate"
          values="0 0; 28 0; 0 0; -28 0; 0 0; 28 0; 0 0; -28 0; 0 0; 28 0; 0 0; -28 0; 0 0"
          dur="20s" repeatCount="indefinite"/>
{chr(10).join(rows_xml)}
      </g>
    </g>""")

    # Generate Laser Shots XML
    lasers_xml = []
    for s in laser_shots:
        tx = s["tank_x"]
        tgt_x = s["target_x"]
        tgt_y = s["target_y"]
        t_shot = s["t_shot"]
        t_hit = s["t_hit"]
        color = s["color"]
        is_ufo = s["is_ufo"]

        kt_s = t_shot / TOTAL_DUR
        kt_h = t_hit / TOTAL_DUR
        kt_s_tr = max(0.0, kt_s - 0.001)

        width = "3.2" if is_ufo else "2.4"
        dy = tgt_y - 198

        lasers_xml.append(f"""    <!-- Laser shot to ({tgt_x}, {tgt_y}) at t={t_hit}s -->
    <line x1="{tx}" y1="198" x2="{tx}" y2="182" stroke="{color}" stroke-width="{width}" stroke-linecap="round" opacity="0" filter="url(#laserGlow)">
      <animate attributeName="opacity" values="0;0;1;1;0;0"
        keyTimes="0.0;{kt_s:.4f};{(kt_s+0.001):.4f};{kt_h:.4f};{(kt_h+0.002):.4f};1.0" dur="60s" repeatCount="indefinite"/>
      <animateTransform attributeName="transform" type="translate"
        values="0 0; 0 0; {tgt_x - tx} {dy}; {tgt_x - tx} {dy}"
        keyTimes="0.0; {kt_s_tr:.4f}; {kt_h:.4f}; 1.0"
        dur="60s" repeatCount="indefinite"/>
    </line>""")

    # Generate Bombs XML
    bombs_xml = []
    for w in waves_data:
        cfg = w["config"]
        for b in w["bombs"]:
            bx = b["x"]
            t_drop = b["t_drop"]
            t_hit = b["t_hit"]
            hit_y = b["hit_y"]
            color = b["color"]
            is_fatal = b["is_fatal"]

            kt_d = t_drop / TOTAL_DUR
            kt_h = t_hit / TOTAL_DUR
            dy = hit_y - 126

            bombs_xml.append(f"""    <!-- Bomb at x={bx} (t={t_drop}s -> {t_hit}s) -->
    <g stroke="{color}" stroke-width="2" fill="none" filter="url(#laserGlow)">
      <path d="M{bx} 126 L{bx-3} 132 L{bx+3} 138 L{bx} 144" opacity="0">
        <animate attributeName="opacity" values="0;0;1;1;0;0"
          keyTimes="0.0;{kt_d:.4f};{(kt_d+0.001):.4f};{kt_h:.4f};{(kt_h+0.002):.4f};1.0" dur="60s" repeatCount="indefinite"/>
        <animateTransform attributeName="transform" type="translate"
          values="0 0; 0 0; 0 {dy}; 0 {dy}"
          keyTimes="0.0; {kt_d:.4f}; {kt_h:.4f}; 1.0"
          dur="60s" repeatCount="indefinite"/>
      </path>
    </g>""")

    # Tank Explosions & Game Over Banners per wave
    death_fx_xml = []
    for w in waves_data:
        cfg = w["config"]
        w_id = cfg["id"]
        dt = cfg["death_time"]
        dx = cfg["death_x"]
        te = cfg["t_end"]

        kt_d = dt / TOTAL_DUR
        kt_burst = (dt + 0.6) / TOTAL_DUR
        kt_banner_s = (dt + 0.8) / TOTAL_DUR
        kt_banner_e = (te - 0.15) / TOTAL_DUR

        death_fx_xml.append(f"""    <!-- WAVE {w_id:02d} TANK DESTROYED FX at ({dx}, 198) -->
    <g>
      <!-- Mega Plasma Explosion at Tank -->
      <circle cx="{dx+16}" cy="204" r="14" fill="#ffd700" filter="url(#laserGlow)" opacity="0">
        <animate attributeName="opacity" values="0;0;1;0.8;0;0"
          keyTimes="0.0;{kt_d:.4f};{(kt_d+0.002):.4f};{(kt_d+0.008):.4f};{kt_burst:.4f};1.0" dur="60s" repeatCount="indefinite"/>
        <animate attributeName="r" values="5;24;38" keyTimes="0;0.4;1" dur="60s" begin="{dt:.2f}s" repeatCount="indefinite"/>
      </circle>
      <circle cx="{dx+16}" cy="204" r="8" fill="#ffffff" filter="url(#laserGlow)" opacity="0">
        <animate attributeName="opacity" values="0;0;1;0;0"
          keyTimes="0.0;{kt_d:.4f};{(kt_d+0.003):.4f};{(kt_d+0.010):.4f};1.0" dur="60s" repeatCount="indefinite"/>
      </circle>

      <!-- Full-Screen Cyber Glitch Red Warning Pulse -->
      <rect x="12" y="12" width="876" height="226" rx="16" fill="#ff0055" opacity="0">
        <animate attributeName="opacity" values="0;0;0.35;0.08;0.3;0.05;0;0"
          keyTimes="0.0;{kt_d:.4f};{(kt_d+0.003):.4f};{(kt_d+0.015):.4f};{(kt_d+0.025):.4f};{(kt_d+0.035):.4f};{kt_burst:.4f};1.0"
          dur="60s" repeatCount="indefinite"/>
      </rect>

      <!-- Holographic Wave Over / Rebooting Banner -->
      <g transform="translate(450 110)" opacity="0">
        <animate attributeName="opacity" values="0;0;1;1;0;0"
          keyTimes="0.0;{kt_banner_s:.4f};{(kt_banner_s+0.005):.4f};{kt_banner_e:.4f};{(kt_banner_e+0.005):.4f};1.0"
          dur="60s" repeatCount="indefinite"/>
        <rect x="-210" y="-22" width="420" height="44" rx="8" fill="#070c20" stroke="#ff0055" stroke-width="1.8" filter="url(#glowInv)"/>
        <text text-anchor="middle" y="-3" font-family="'Fira Code', monospace" font-size="13" font-weight="900" fill="#ff0055" letter-spacing="2">
          ! CRITICAL HIT - TANK DESTROYED !
        </text>
        <text text-anchor="middle" y="14" font-family="'Fira Code', monospace" font-size="9" font-weight="700" fill="#00ffcc" letter-spacing="2">
          WAVE {w_id:02d} COMPROMISED // REARMING SQUADRON MATRIX...
        </text>
      </g>
    </g>""")

    # Put together complete SVG document
    svg_content = f"""<svg width="900" height="250" viewBox="0 0 900 250" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Space Invaders Arcade Matrix Rioon7337">
  <defs>
    <radialGradient id="bgInv" cx="50%" cy="50%" r="80%">
      <stop offset="0%" stop-color="#0a1a3e"/>
      <stop offset="60%" stop-color="#07071a"/>
      <stop offset="100%" stop-color="#050512"/>
    </radialGradient>

    <pattern id="invGrid" width="20" height="20" patternUnits="userSpaceOnUse">
      <path d="M20 0H0V20" fill="none" stroke="#00f0ff" stroke-width="0.35" opacity="0.05"/>
    </pattern>

    <!-- Animated Neon Border Gradient -->
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

    <!-- Glow Filters -->
    <filter id="glowInv" x="-25%" y="-25%" width="150%" height="150%">
      <feGaussianBlur stdDeviation="3.5" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>

    <filter id="laserGlow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="2.2" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>

    <filter id="neonOuterInv" x="-10%" y="-18%" width="120%" height="136%">
      <feGaussianBlur stdDeviation="5" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>

    <clipPath id="clipInv">
      <rect x="12" y="12" width="876" height="226" rx="16"/>
    </clipPath>

    <!-- Alien Sprites (Pose A and B) -->
    <g id="squidA">
      <path d="M6 0h4v2h-4z M4 2h8v2h-8z M2 4h12v2h-12z M0 6h4v2h-4z M6 6h4v2h-4z M12 6h4v2h-4z M0 8h16v2h-16z M2 10h2v2h-2z M12 10h2v2h-2z M0 12h2v4h-2z M14 12h2v4h-2z M4 12h2v2h-2z M10 12h2v2h-2z" fill="currentColor"/>
    </g>
    <g id="squidB">
      <path d="M6 0h4v2h-4z M4 2h8v2h-8z M2 4h12v2h-12z M0 6h4v2h-4z M6 6h4v2h-4z M12 6h4v2h-4z M0 8h16v2h-16z M4 10h2v2h-2z M10 10h2v2h-2z M2 12h2v4h-2z M12 12h2v4h-2z M6 12h4v2h-4z" fill="currentColor"/>
    </g>

    <g id="crabA">
      <path d="M4 0h2v2h-2z M14 0h2v2h-2z M6 2h2v2h-2z M12 2h2v2h-2z M4 4h12v2h-12z M2 6h4v2h-4z M8 6h4v2h-4z M14 6h4v2h-4z M0 8h20v4h-20z M0 12h4v2h-4z M16 12h4v2h-4z M4 14h2v4h-2z M14 14h2v4h-2z" fill="currentColor"/>
    </g>
    <g id="crabB">
      <path d="M4 0h2v2h-2z M14 0h2v2h-2z M0 2h2v2h-2z M6 2h2v2h-2z M12 2h2v2h-2z M18 2h2v2h-2z M0 4h20v2h-20z M0 6h4v2h-4z M8 6h4v2h-4z M16 6h4v2h-4z M2 8h16v4h-16z M0 12h2v6h-2z M18 12h2v6h-2z" fill="currentColor"/>
    </g>

    <g id="octoA">
      <path d="M8 0h8v2h-8z M2 2h20v2h-20z M0 4h24v2h-24z M0 6h6v2h-6z M10 6h4v2h-4z M18 6h6v2h-6z M0 8h24v4h-24z M4 12h4v2h-4z M16 12h4v2h-4z M2 14h4v2h-4z M10 14h4v2h-4z M18 14h4v2h-4z M0 16h2v4h-2z M6 16h2v4h-2z M16 16h2v4h-2z M22 16h2v4h-2z" fill="currentColor"/>
    </g>
    <g id="octoB">
      <path d="M8 0h8v2h-8z M2 2h20v2h-20z M0 4h24v2h-24z M0 6h6v2h-6z M10 6h4v2h-4z M18 6h6v2h-6z M0 8h24v4h-24z M6 12h12v2h-12z M4 14h2v4h-2z M18 14h2v4h-2z M8 16h2v4h-2z M14 16h2v4h-2z" fill="currentColor"/>
    </g>

    <!-- Player Laser Tank -->
    <g id="playerTank">
      <path d="M14 0h4v6h-4z M6 6h20v4h-20z M2 10h28v6h-28z M0 16h32v4h-32z" fill="#00ff88"/>
      <rect x="14" y="0" width="4" height="4" fill="#ffffff" filter="url(#laserGlow)"/>
    </g>

    <g id="bunkerBase">
      <path d="M4 0h36v6h4v6h4v24h-12v-12h-24v12h-12v-24h4v-6h4z" fill="#00ffcc" opacity="0.85"/>
    </g>
  </defs>

  <!-- Outer Neon Aura -->
  <rect x="12" y="12" width="876" height="226" rx="16" fill="none" stroke="url(#rgbInv)" stroke-width="5" opacity="0.32" filter="url(#neonOuterInv)"/>
  <rect x="12" y="12" width="876" height="226" rx="16" fill="url(#bgInv)"/>
  <rect x="12" y="12" width="876" height="226" rx="16" fill="url(#invGrid)"/>

  <!-- Cyber Corners -->
  <path d="M22 42 L22 22 L42 22" stroke="#00f0ff" stroke-width="2" fill="none" opacity=".85"/>
  <path d="M878 42 L878 22 L858 22" stroke="#00f0ff" stroke-width="2" fill="none" opacity=".85"/>
  <path d="M22 208 L22 228 L42 228" stroke="#d946ef" stroke-width="2" fill="none" opacity=".85"/>
  <path d="M878 208 L878 228 L858 228" stroke="#d946ef" stroke-width="2" fill="none" opacity=".85"/>

  <!-- Arcade HUD Labels -->
  <text x="32" y="32" font-family="'Fira Code', ui-monospace, monospace" font-size="11" font-weight="700" letter-spacing="2" fill="#00f0ff" opacity="0.95">// SPACE INVADERS &#183; RIOON7337</text>
  <text x="868" y="32" text-anchor="end" font-family="'Fira Code', ui-monospace, monospace" font-size="11" font-weight="700" letter-spacing="2" fill="#ff73fa" opacity="0.95">HI-SCORE: 250807</text>

  <!-- Continuous 60s Live Dynamic HUD Display -->
  <g transform="translate(450 32)">
    <rect x="-150" y="-13" width="300" height="18" rx="4" fill="#070c20" stroke="#00f0ff" stroke-width="0.8" opacity="0.85"/>
    <g transform="translate(-75 0)">
{chr(10).join(hud_waves_xml)}
    </g>
    <g transform="translate(80 0)">
      <text text-anchor="end" x="8" y="0" font-family="'Fira Code', monospace" font-size="10.5" font-weight="800" fill="#00ffcc" filter="url(#glowInv)">SCORE:</text>
{chr(10).join(score_digits_xml)}
    </g>
  </g>

  <!-- Animated Border & Traveling Tracer -->
  <rect x="12" y="12" width="876" height="226" rx="16" fill="none" stroke="url(#rgbInv)" stroke-width="1.6"/>
  <rect x="12" y="12" width="876" height="226" rx="16" fill="none" stroke="#00f0ff" stroke-width="2" stroke-linecap="round" opacity="0.9" pathLength="1000" stroke-dasharray="85 915" filter="url(#glowInv)">
    <animate attributeName="stroke-dashoffset" from="0" to="-1000" dur="4s" repeatCount="indefinite"/>
  </rect>

  <!-- Game Playfield Area -->
  <g clip-path="url(#clipInv)">

{chr(10).join(ufos_xml)}

{chr(10).join(armada_waves_xml)}

    <!-- 4 Defense Bunkers (Shields) -->
    <g transform="translate(0 156)" filter="url(#glowInv)">
      <!-- Bunker 1 (x=180) -->
      <g transform="translate(180 0)">
        <use href="#bunkerBase"/>
        <rect x="14" y="6" width="4" height="6" fill="#07071a"/>
      </g>
      <!-- Bunker 2 (x=330) -->
      <g transform="translate(330 0)">
        <use href="#bunkerBase"/>
        <rect x="22" y="4" width="6" height="6" fill="#07071a"/>
        <rect x="30" y="16" width="6" height="4" fill="#07071a"/>
      </g>
      <!-- Bunker 3 (x=480) -->
      <g transform="translate(480 0)">
        <use href="#bunkerBase"/>
        <rect x="18" y="4" width="6" height="6" fill="#07071a"/>
      </g>
      <!-- Bunker 4 (x=630) -->
      <g transform="translate(630 0)">
        <use href="#bunkerBase"/>
        <rect x="20" y="4" width="6" height="6" fill="#07071a"/>
      </g>
    </g>

{chr(10).join(bombs_xml)}

{chr(10).join(lasers_xml)}

    <!-- Dynamic Player Laser Tank Maneuvers (60s Multi-Wave) -->
    <g>
      <animateTransform attributeName="transform" type="translate"
        values="{tank_x_vals}"
        keyTimes="{tank_kts}"
        dur="60s" repeatCount="indefinite"/>
      <g>
        <animate attributeName="opacity" values="{tank_op_vals}" keyTimes="{tank_op_kts}" dur="60s" repeatCount="indefinite"/>
        <use href="#playerTank"/>
      </g>
    </g>

{chr(10).join(death_fx_xml)}

    <!-- Bottom Status Line & Spare Lives Display -->
    <g>
      <line x1="20" y1="224" x2="880" y2="224" stroke="#00f0ff" stroke-width="1.2" opacity="0.7"/>
      <line x1="20" y1="224" x2="880" y2="224" stroke="#00ff88" stroke-width="1.8" stroke-dasharray="12 40" opacity="0.8"/>

      <text x="32" y="238" font-family="'Fira Code', monospace" font-size="9.5" font-weight="700" fill="#00ff88" letter-spacing="1.5">LIVES: 3</text>
      <g transform="translate(90 228) scale(0.55)" fill="#00ff88">
        <use href="#playerTank" x="0"/>
        <use href="#playerTank" x="42"/>
        <use href="#playerTank" x="84"/>
      </g>

      <text x="868" y="238" text-anchor="end" font-family="'Fira Code', monospace" font-size="9.5" font-weight="700" fill="#00f0ff" letter-spacing="1.5">RADAR LOCK ON // CONTINUOUS DEFENSE</text>
    </g>
  </g>
</svg>"""

    with open("space-invaders.svg", "w", encoding="utf-8") as f:
        f.write(svg_content)

    print("Wrote space-invaders.svg successfully!")
    try:
        ET.fromstring(svg_content)
        print("XML validation PASSED!")
    except Exception as e:
        print("XML validation FAILED:", e)

if __name__ == "__main__":
    generate_space_invaders_svg()
