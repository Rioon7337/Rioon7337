import random
import math
import xml.etree.ElementTree as ET

def render_pipe(p):
    x = p["x"]
    yc = p["yc"]
    theme = p["theme"]
    t_abs = p["t_abs"]

    # Cap dimensions
    cap_h = 14
    gap_half = 32

    # Top pipe geometry
    top_cap_y = yc - gap_half - cap_h
    top_body_y = 38
    top_body_h = max(6, top_cap_y - top_body_y)

    # Bottom pipe geometry
    bot_cap_y = yc + gap_half
    bot_body_y = bot_cap_y + 11
    bot_body_h = max(6, 215 - bot_body_y)

    if theme == "emerald":
        grad_body = "url(#pipeGrad1)"
        grad_cap = "url(#pipeCapGrad1)"
        color_main = "#00ff88"
    elif theme == "cyan":
        grad_body = "url(#pipeGrad2)"
        grad_cap = "url(#pipeCapGrad2)"
        color_main = "#00f0ff"
    elif theme == "violet":
        grad_body = "url(#pipeGrad3)"
        grad_cap = "url(#pipeCapGrad3)"
        color_main = "#ff73fa"
    elif theme == "gold":
        grad_body = "url(#pipeGradGold)"
        grad_cap = "url(#pipeCapGradGold)"
        color_main = "#ffd700"
    else:  # laser
        grad_body = "#0a142e"
        grad_cap = "#00f0ff"
        color_main = "#00f0ff"

    if theme == "laser":
        xml = f"""      <!-- Laser Gate at X={x} (Center Y={yc}) -->
      <g transform="translate({x} 0)">
        <rect x="0" y="38" width="40" height="{max(8, yc - 75)}" fill="#0a142e" stroke="#00f0ff" stroke-width="1.4"/>
        <rect x="-3" y="{yc - 42}" width="46" height="12" rx="3" fill="#00f0ff" filter="url(#glowFlap)"/>
        <rect x="-3" y="{yc + 30}" width="46" height="12" rx="3" fill="#00f0ff" filter="url(#glowFlap)"/>
        <rect x="0" y="{yc + 42}" width="40" height="{max(8, 210 - (yc + 42))}" fill="#0a142e" stroke="#00f0ff" stroke-width="1.4"/>
        <line x1="20" y1="{yc - 30}" x2="20" y2="{yc + 30}" stroke="#00e5ff" stroke-width="1.8" stroke-dasharray="4 6" opacity="0.6">
          <animate attributeName="opacity" values="0.3;0.8;0.3" dur="0.4s" repeatCount="indefinite"/>
        </line>
        <!-- Bonus Ring -->
        <g transform="translate(20 {yc})" filter="url(#glowFlap)">
          <circle cx="0" cy="0" r="7.5" fill="none" stroke="#00ffcc" stroke-width="1.8"/>
          <circle cx="0" cy="0" r="3" fill="#ffffff"/>
          <circle cx="0" cy="0" r="8" fill="none" stroke="#00ffcc" stroke-width="1.5" opacity="0">
            <animate attributeName="r" values="8;20;26" keyTimes="0;0.5;1" dur="60s" begin="{t_abs:.2f}s" repeatCount="indefinite"/>
            <animate attributeName="opacity" values="1;0.7;0" keyTimes="0;0.5;1" dur="60s" begin="{t_abs:.2f}s" repeatCount="indefinite"/>
          </circle>
        </g>
      </g>"""
    else:
        xml = f"""      <!-- Obstacle {p['idx']+1}: {theme.upper()} at X={x} (Center Y={yc}) -->
      <g transform="translate({x} 0)">
        <!-- Top Pipe -->
        <rect x="0" y="{top_body_y}" width="46" height="{top_body_h}" fill="{grad_body}" stroke="{color_main}" stroke-width="1.2"/>
        <line x1="8" y1="38" x2="8" y2="{top_body_y + top_body_h}" stroke="#ffffff" stroke-width="1.2" opacity="0.45"/>
        <rect x="-3" y="{top_cap_y}" width="52" height="14" rx="2" fill="{grad_cap}" stroke="{color_main}" stroke-width="1.4"/>
        <line x1="4" y1="{top_cap_y + 7}" x2="42" y2="{top_cap_y + 7}" stroke="{color_main}" stroke-width="1.5" stroke-dasharray="4 4"/>

        <!-- Bottom Pipe -->
        <rect x="-3" y="{bot_cap_y}" width="52" height="14" rx="2" fill="{grad_cap}" stroke="{color_main}" stroke-width="1.4"/>
        <rect x="0" y="{bot_body_y}" width="46" height="{bot_body_h}" fill="{grad_body}" stroke="{color_main}" stroke-width="1.2"/>
        <line x1="8" y1="{bot_body_y}" x2="8" y2="210" stroke="#ffffff" stroke-width="1.2" opacity="0.45"/>
        <line x1="4" y1="{bot_cap_y + 7}" x2="42" y2="{bot_cap_y + 7}" stroke="{color_main}" stroke-width="1.5" stroke-dasharray="4 4"/>

        <!-- Bonus Ring -->
        <g transform="translate(23 {yc})" filter="url(#glowFlap)">
          <circle cx="0" cy="0" r="7.5" fill="none" stroke="{color_main}" stroke-width="1.8"/>
          <circle cx="0" cy="0" r="3" fill="#ffffff"/>
          <circle cx="0" cy="0" r="8" fill="none" stroke="{color_main}" stroke-width="1.5" opacity="0">
            <animate attributeName="r" values="8;20;26" keyTimes="0;0.5;1" dur="60s" begin="{t_abs:.2f}s" repeatCount="indefinite"/>
            <animate attributeName="opacity" values="1;0.7;0" keyTimes="0;0.5;1" dur="60s" begin="{t_abs:.2f}s" repeatCount="indefinite"/>
          </circle>
        </g>
      </g>"""
    return xml

def generate_flappy_svg():
    TOTAL_DUR = 60.0
    SPEED = 100.0
    BIRD_X = 180.0
    PIPE_SPACING = 180.0
    FIRST_PIPE_X = 360.0

    rounds_config = [
        {
            "id": 1,
            "label": "ROUND 01 / 03 &#183; RANDOM HAZARDS",
            "seed": 7711,
            "t_start": 0.0,
            "t_end": 20.0,
            "cleared_count": 7,
            "crash_pipe": 7,
            "crash_type": "top_pipe",
        },
        {
            "id": 2,
            "label": "ROUND 02 / 03 &#183; RANDOM HAZARDS",
            "seed": 9922,
            "t_start": 20.0,
            "t_end": 40.0,
            "cleared_count": 8,
            "crash_pipe": 8,
            "crash_type": "bottom_pipe",
        },
        {
            "id": 3,
            "label": "ROUND 03 / 03 &#183; RANDOM HAZARDS",
            "seed": 4433,
            "t_start": 40.0,
            "t_end": 60.0,
            "cleared_count": 7,
            "crash_pipe": 7,
            "crash_type": "laser_gate",
        }
    ]

    pipe_themes = ["emerald", "cyan", "violet", "gold", "laser"]

    rounds_data = []
    for r in rounds_config:
        rng = random.Random(r["seed"])
        num_pipes = r["crash_pipe"] + 1
        pipes = []
        for k in range(num_pipes):
            x = FIRST_PIPE_X + k * PIPE_SPACING
            t_rel = (x - BIRD_X) / SPEED
            t_abs = r["t_start"] + t_rel
            yc = rng.randint(82, 158)
            if k == r["crash_pipe"] and r["crash_type"] == "laser_gate":
                theme = "laser"
            else:
                theme = rng.choice(pipe_themes)
            pipes.append({
                "idx": k,
                "x": x,
                "t_rel": round(t_rel, 3),
                "t_abs": round(t_abs, 3),
                "yc": yc,
                "theme": theme
            })
        rounds_data.append({
            "config": r,
            "pipes": pipes
        })

    # Build keyframes for Bird trajectory
    keyframes = []
    crash_fx_list = []

    for r_idx, r in enumerate(rounds_data):
        cfg = r["config"]
        pipes = r["pipes"]
        t_start = cfg["t_start"]
        t_end = cfg["t_end"]
        crash_type = cfg["crash_type"]
        crash_pipe = pipes[cfg["crash_pipe"]]

        # Spawn at t_start
        keyframes.append((round(t_start, 3), 120.0, 0.0))
        p0 = pipes[0]
        t_mid0 = t_start + (p0["t_abs"] - t_start) * 0.45
        y_mid0 = 120.0 + (p0["yc"] - 120.0) * 0.3
        keyframes.append((round(t_mid0, 3), round(y_mid0, 1), 18.0))
        keyframes.append((round(t_mid0 + 0.35, 3), round(y_mid0 - 12, 1), -30.0))

        # Fly through cleared pipes
        for k in range(cfg["cleared_count"]):
            p = pipes[k]
            keyframes.append((round(p["t_abs"], 3), float(p["yc"]), 0.0))
            if k < len(pipes) - 1:
                p_next = pipes[k+1]
                t_k = p["t_abs"]
                t_next = p_next["t_abs"]
                dt = t_next - t_k
                
                t_fall = t_k + dt * 0.35
                y_fall = min(195.0, p["yc"] + 15.0)
                keyframes.append((round(t_fall, 3), round(y_fall, 1), 32.0))
                
                t_flap = t_k + dt * 0.65
                y_flap = p_next["yc"] + (p_next["yc"] - y_fall) * 0.35
                keyframes.append((round(t_flap, 3), round(y_flap, 1), -35.0))

        # Crash sequence at crash_pipe
        cp = crash_pipe
        t_crash = cp["t_abs"]
        yc_crash = cp["yc"]

        if crash_type == "top_pipe":
            y_hit = yc_crash - 38.0
            angle_hit = -42.0
        elif crash_type == "bottom_pipe":
            y_hit = yc_crash + 38.0
            angle_hit = 45.0
        else: # laser_gate
            y_hit = yc_crash - 10.0
            angle_hit = -15.0

        keyframes.append((round(t_crash, 3), round(y_hit, 1), angle_hit))
        keyframes.append((round(t_crash + 0.15, 3), round(y_hit + 6.0, 1), 75.0))
        keyframes.append((round(t_crash + 0.50, 3), 175.0, 95.0))
        keyframes.append((round(t_crash + 0.90, 3), 204.0, 110.0))
        keyframes.append((round(t_end - 0.10, 3), 204.0, 110.0))

        crash_fx_list.append({
            "round_id": cfg["id"],
            "t_crash": t_crash,
            "t_end": t_end,
            "y_hit": y_hit,
            "crash_type": crash_type
        })

    keyframes.sort(key=lambda k: k[0])
    if keyframes[0][0] != 0.0:
        keyframes.insert(0, (0.0, 120.0, 0.0))
    if keyframes[-1][0] < TOTAL_DUR:
        keyframes.append((TOTAL_DUR, keyframes[-1][1], keyframes[-1][2]))

    # Deduplicate timestamps if any
    clean_kfs = [keyframes[0]]
    for kf in keyframes[1:]:
        if kf[0] > clean_kfs[-1][0] + 0.001:
            clean_kfs.append(kf)
    keyframes = clean_kfs

    anim_t = []
    anim_y = []
    anim_rot = []
    for (t, y, rot) in keyframes:
        kt = t / TOTAL_DUR
        anim_t.append(round(kt, 5))
        anim_y.append(f"0 {y:.1f}")
        anim_rot.append(f"{rot:.1f} 0 0")

    y_values_str = "; ".join(anim_y)
    rot_values_str = "; ".join(anim_rot)
    kt_str = "; ".join(str(kt) for kt in anim_t)

    # Generate Round Status HUD strings
    hud_rounds_xml = []
    for r_idx, r in enumerate(rounds_data):
        cfg = r["config"]
        label = cfg["label"]
        t_s = cfg["t_start"] / TOTAL_DUR
        t_e = cfg["t_end"] / TOTAL_DUR
        
        # Build discrete opacity animation
        if r_idx == 0:
            op_vals = "1;0"
            op_kts = f"0.0;{t_e:.4f};1.0"
        elif r_idx == len(rounds_data) - 1:
            op_vals = "0;1"
            op_kts = f"0.0;{t_s:.4f};1.0"
        else:
            op_vals = "0;1;0"
            op_kts = f"0.0;{t_s:.4f};{t_e:.4f};1.0"
            
        hud_rounds_xml.append(f"""    <text text-anchor="middle" y="0" font-family="'Fira Code', monospace" font-size="10.5" font-weight="800" fill="#00ffcc" letter-spacing="1.5">
      <animate attributeName="opacity" calcMode="discrete" values="{op_vals}" keyTimes="{op_kts}" dur="60s" repeatCount="indefinite"/>
      {label}
    </text>""")

    # Generate Live Dynamic Score Numbers in HUD
    # In each round, score increments with each cleared pipe!
    score_digits_xml = []
    for r_idx, r in enumerate(rounds_data):
        cfg = r["config"]
        pipes = r["pipes"]
        cleared_count = cfg["cleared_count"]
        t_start = cfg["t_start"]
        t_end = cfg["t_end"]

        for sc in range(cleared_count + 1):
            if sc == 0:
                sc_start = t_start
                sc_end = pipes[0]["t_abs"]
            elif sc < cleared_count:
                sc_start = pipes[sc - 1]["t_abs"]
                sc_end = pipes[sc]["t_abs"]
            else:
                sc_start = pipes[sc - 1]["t_abs"]
                sc_end = t_end

            kt_s = sc_start / TOTAL_DUR
            kt_e = sc_end / TOTAL_DUR

            # Ensure valid bounds
            kt_s = max(0.0, min(1.0, kt_s))
            kt_e = max(0.0, min(1.0, kt_e))

            if kt_s >= kt_e:
                continue

            score_str = f"{sc:02d}"
            color = "#ffd700" if sc < 4 else ("#00ff88" if sc < 7 else "#00f0ff")

            # discrete visibility
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

    # Generate Pipe Groups for each round
    pipes_groups_xml = []
    for r_idx, r in enumerate(rounds_data):
        cfg = r["config"]
        r_id = cfg["id"]
        t_s = cfg["t_start"]
        t_e = cfg["t_end"]
        kt_s = t_s / TOTAL_DUR
        kt_e = t_e / TOTAL_DUR

        pipes_code = "\n".join(render_pipe(p) for p in r["pipes"])

        # Travel distance in 20s at 100px/s = 2000px
        # Translation animation across 60s
        if r_idx == 0:
            disp_vals = "inline;none;none"
            disp_kts = f"0.0;{kt_e:.4f};1.0"
            tr_vals = "0 0; -2000 0; -2000 0"
            tr_kts = f"0.0; {kt_e:.4f}; 1.0"
        elif r_idx == 1:
            disp_vals = "none;inline;none;none"
            disp_kts = f"0.0;{kt_s:.4f};{kt_e:.4f};1.0"
            tr_vals = "0 0; 0 0; -2000 0; -2000 0"
            tr_kts = f"0.0; {kt_s:.4f}; {kt_e:.4f}; 1.0"
        else:
            disp_vals = "none;inline"
            disp_kts = f"0.0;{kt_s:.4f};1.0"
            tr_vals = "0 0; 0 0; -2000 0"
            tr_kts = f"0.0; {kt_s:.4f}; 1.0"

        pipes_groups_xml.append(f"""    <!-- ==================== ROUND {r_id:02d} OBSTACLE CORRIDOR ==================== -->
    <g>
      <animate attributeName="display" values="{disp_vals}" keyTimes="{disp_kts}" dur="60s" repeatCount="indefinite"/>
      <animateTransform attributeName="transform" type="translate"
        values="{tr_vals}"
        keyTimes="{tr_kts}"
        dur="60s" repeatCount="indefinite"/>
{pipes_code}
    </g>""")

    # Crash FX and Game Over Overlays for each round
    crash_fx_xml = []
    for c in crash_fx_list:
        r_id = c["round_id"]
        tc = c["t_crash"]
        te = c["t_end"]
        yh = c["y_hit"]
        
        kt_c = tc / TOTAL_DUR
        kt_e = te / TOTAL_DUR
        kt_burst_end = (tc + 0.6) / TOTAL_DUR
        kt_banner_start = (tc + 0.8) / TOTAL_DUR
        kt_banner_end = (te - 0.15) / TOTAL_DUR

        crash_fx_xml.append(f"""    <!-- ROUND {r_id:02d} CRASH FX at ({BIRD_X}, {yh:.1f}) -->
    <g>
      <!-- Shockwave Explosion on Impact -->
      <circle cx="{BIRD_X}" cy="{yh:.1f}" r="12" fill="#ffd700" filter="url(#glowFlap)" opacity="0">
        <animate attributeName="opacity" values="0;0.9;0.5;0;0" keyTimes="0.0;{kt_c:.4f};{(kt_c+0.005):.4f};{kt_burst_end:.4f};1.0" dur="60s" repeatCount="indefinite"/>
        <animate attributeName="r" values="4;18;32" keyTimes="0;0.4;1" dur="60s" begin="{tc:.2f}s" repeatCount="indefinite"/>
      </circle>
      <circle cx="{BIRD_X}" cy="{yh:.1f}" r="6" fill="#ffffff" filter="url(#glowFlap)" opacity="0">
        <animate attributeName="opacity" values="0;1;0;0" keyTimes="0.0;{kt_c:.4f};{(kt_c+0.008):.4f};1.0" dur="60s" repeatCount="indefinite"/>
      </circle>

      <!-- Dizzy Stars around fallen bird on ground -->
      <g transform="translate({BIRD_X} 190)" opacity="0">
        <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0.0;{kt_banner_start:.4f};{(kt_banner_start+0.01):.4f};{kt_banner_end:.4f};{(kt_banner_end+0.01):.4f};1.0" dur="60s" repeatCount="indefinite"/>
        <g fill="#ffd700" filter="url(#glowFlap)">
          <path d="M-12 -6 L-10 -4 L-12 -2 L-14 -4 Z"/>
          <path d="M12 -6 L14 -4 L12 -2 L10 -4 Z"/>
          <path d="M0 -14 L2 -12 L0 -10 L-2 -12 Z"/>
          <animateTransform attributeName="transform" type="rotate" from="0 0 -6" to="360 0 -6" dur="1.2s" repeatCount="indefinite"/>
        </g>
      </g>

      <!-- Full-Screen Cyber Glitch Red Warning Pulse -->
      <rect x="12" y="12" width="876" height="226" rx="16" fill="#ff0055" opacity="0">
        <animate attributeName="opacity" values="0;0;0.35;0.08;0.3;0.05;0;0"
          keyTimes="0.0;{kt_c:.4f};{(kt_c+0.003):.4f};{(kt_c+0.015):.4f};{(kt_c+0.025):.4f};{(kt_c+0.035):.4f};{kt_burst_end:.4f};1.0"
          dur="60s" repeatCount="indefinite"/>
      </rect>

      <!-- Holographic Game Over Alert Banner -->
      <g transform="translate(450 110)" opacity="0">
        <animate attributeName="opacity" values="0;0;1;1;0;0"
          keyTimes="0.0;{kt_banner_start:.4f};{(kt_banner_start+0.005):.4f};{kt_banner_end:.4f};{(kt_banner_end+0.005):.4f};1.0"
          dur="60s" repeatCount="indefinite"/>
        <rect x="-190" y="-22" width="380" height="44" rx="8" fill="#070c20" stroke="#ff0055" stroke-width="1.8" filter="url(#glowFlap)"/>
        <text text-anchor="middle" y="-3" font-family="'Fira Code', monospace" font-size="13" font-weight="900" fill="#ff0055" letter-spacing="2">
          ! CRASH! ROUND {r_id:02d} FAILED !
        </text>
        <text text-anchor="middle" y="14" font-family="'Fira Code', monospace" font-size="9" font-weight="700" fill="#00f0ff" letter-spacing="2">
          REBOOTING NEURAL LINK // NEXT WAVE RANDOMIZED
        </text>
      </g>
    </g>""")

    # Put together the entire SVG document
    svg_content = f"""<svg width="900" height="250" viewBox="0 0 900 250" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Flappy Bird Arcade Matrix Rioon7337">
  <defs>
    <radialGradient id="bgFlap" cx="50%" cy="50%" r="80%">
      <stop offset="0%" stop-color="#0a1a3e"/>
      <stop offset="60%" stop-color="#07071a"/>
      <stop offset="100%" stop-color="#050512"/>
    </radialGradient>

    <pattern id="flapGrid" width="20" height="20" patternUnits="userSpaceOnUse">
      <path d="M20 0H0V20" fill="none" stroke="#00f0ff" stroke-width="0.35" opacity="0.05"/>
    </pattern>

    <!-- Animated Neon Border Gradient -->
    <linearGradient id="rgbFlap" gradientUnits="userSpaceOnUse" x1="12" y1="125" x2="888" y2="125">
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

    <!-- Multi-Stage Pipe Gradients -->
    <linearGradient id="pipeGrad1" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00ff88" stop-opacity="0.95"/>
      <stop offset="25%" stop-color="#00f0ff"/>
      <stop offset="75%" stop-color="#00bd68"/>
      <stop offset="100%" stop-color="#004d2a"/>
    </linearGradient>

    <linearGradient id="pipeGrad2" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00f0ff" stop-opacity="0.95"/>
      <stop offset="30%" stop-color="#38bdf8"/>
      <stop offset="70%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#082f49"/>
    </linearGradient>

    <linearGradient id="pipeGrad3" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ff73fa" stop-opacity="0.95"/>
      <stop offset="30%" stop-color="#d946ef"/>
      <stop offset="70%" stop-color="#9333ea"/>
      <stop offset="100%" stop-color="#3b0764"/>
    </linearGradient>

    <linearGradient id="pipeGradGold" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#fde047" stop-opacity="0.95"/>
      <stop offset="30%" stop-color="#f59e0b"/>
      <stop offset="70%" stop-color="#d97706"/>
      <stop offset="100%" stop-color="#78350f"/>
    </linearGradient>

    <linearGradient id="pipeCapGrad1" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#70ffb0"/>
      <stop offset="35%" stop-color="#00f0ff"/>
      <stop offset="70%" stop-color="#00a855"/>
      <stop offset="100%" stop-color="#003318"/>
    </linearGradient>
    <linearGradient id="pipeCapGrad2" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#7dd3fc"/>
      <stop offset="35%" stop-color="#00e5ff"/>
      <stop offset="70%" stop-color="#0369a1"/>
      <stop offset="100%" stop-color="#0c4a6e"/>
    </linearGradient>
    <linearGradient id="pipeCapGrad3" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#f5d0fe"/>
      <stop offset="35%" stop-color="#ff73fa"/>
      <stop offset="70%" stop-color="#c026d3"/>
      <stop offset="100%" stop-color="#581c87"/>
    </linearGradient>
    <linearGradient id="pipeCapGradGold" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#fef08a"/>
      <stop offset="35%" stop-color="#ffd700"/>
      <stop offset="70%" stop-color="#b45309"/>
      <stop offset="100%" stop-color="#451a03"/>
    </linearGradient>

    <pattern id="groundStripes" width="24" height="24" patternUnits="userSpaceOnUse" patternTransform="rotate(-45)">
      <rect width="12" height="24" fill="#0d1f4a"/>
      <rect x="12" width="12" height="24" fill="#081432"/>
    </pattern>

    <filter id="glowFlap" x="-25%" y="-25%" width="150%" height="150%">
      <feGaussianBlur stdDeviation="3.5" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>

    <filter id="neonOuterFlap" x="-10%" y="-18%" width="120%" height="136%">
      <feGaussianBlur stdDeviation="5" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>

    <filter id="birdGlow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="2.5" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>

    <clipPath id="clipFlap">
      <rect x="12" y="12" width="876" height="226" rx="16"/>
    </clipPath>
  </defs>

  <!-- Outer Neon Aura -->
  <rect x="12" y="12" width="876" height="226" rx="16" fill="none" stroke="url(#rgbFlap)" stroke-width="5" opacity="0.32" filter="url(#neonOuterFlap)"/>
  <rect x="12" y="12" width="876" height="226" rx="16" fill="url(#bgFlap)"/>
  <rect x="12" y="12" width="876" height="226" rx="16" fill="url(#flapGrid)"/>

  <!-- Cyber Corners -->
  <path d="M22 42 L22 22 L42 22" stroke="#00f0ff" stroke-width="2" fill="none" opacity=".85"/>
  <path d="M878 42 L878 22 L858 22" stroke="#00f0ff" stroke-width="2" fill="none" opacity=".85"/>
  <path d="M22 208 L22 228 L42 228" stroke="#d946ef" stroke-width="2" fill="none" opacity=".85"/>
  <path d="M878 208 L878 228 L858 228" stroke="#d946ef" stroke-width="2" fill="none" opacity=".85"/>

  <!-- Arcade HUD Labels -->
  <text x="32" y="32" font-family="'Fira Code', ui-monospace, monospace" font-size="11" font-weight="700" letter-spacing="2" fill="#00f0ff" opacity="0.95">// FLAPPY MATRIX &#183; RIOON7337</text>
  <text x="868" y="32" text-anchor="end" font-family="'Fira Code', ui-monospace, monospace" font-size="11" font-weight="700" letter-spacing="2" fill="#ff73fa" opacity="0.95">HI-SCORE: 250807</text>

  <!-- Dynamic Live Score Display in Center -->
  <g transform="translate(450 32)">
    <rect x="-145" y="-13" width="290" height="18" rx="4" fill="#070c20" stroke="#00f0ff" stroke-width="0.8" opacity="0.85"/>
    <g transform="translate(-70 0)">
{chr(10).join(hud_rounds_xml)}
    </g>
    <g transform="translate(85 0)">
      <text text-anchor="end" x="8" y="0" font-family="'Fira Code', monospace" font-size="10.5" font-weight="800" fill="#00ffcc" filter="url(#glowFlap)">SCORE:</text>
{chr(10).join(score_digits_xml)}
    </g>
  </g>

  <!-- Animated Outer Border & Traveling Tracer -->
  <rect x="12" y="12" width="876" height="226" rx="16" fill="none" stroke="url(#rgbFlap)" stroke-width="1.6"/>
  <rect x="12" y="12" width="876" height="226" rx="16" fill="none" stroke="#00f0ff" stroke-width="2" stroke-linecap="round" opacity="0.9" pathLength="1000" stroke-dasharray="85 915" filter="url(#glowFlap)">
    <animate attributeName="stroke-dashoffset" from="0" to="-1000" dur="4s" repeatCount="indefinite"/>
  </rect>

  <!-- Game Playfield Area -->
  <g clip-path="url(#clipFlap)">
    <!-- Parallax Background Cyber City Skyline -->
    <g opacity="0.22">
      <path d="M0 210 L30 210 L30 150 L60 150 L60 210 L110 210 L110 130 L150 130 L150 210 L220 210 L220 160 L270 160 L270 210 L340 210 L340 120 L380 120 L380 210 L450 210 L450 155 L490 155 L490 210 L560 210 L560 140 L610 140 L610 210 L680 210 L680 125 L730 125 L730 210 L800 210 L800 165 L840 165 L840 210 L900 210 L900 135 L960 135 L960 210 L1020 210 L1020 150 L1060 150 L1060 210 L1140 210 L1140 130 L1200 210" fill="#00f0ff">
        <animateTransform attributeName="transform" type="translate" from="0 0" to="-300 0" dur="16s" repeatCount="indefinite"/>
      </path>
    </g>

    <!-- Parallax Neon Grid Horizon Rays -->
    <g opacity="0.12" stroke="#00f0ff" stroke-width="0.8">
      <line x1="450" y1="210" x2="0" y2="250"/>
      <line x1="450" y1="210" x2="150" y2="250"/>
      <line x1="450" y1="210" x2="300" y2="250"/>
      <line x1="450" y1="210" x2="600" y2="250"/>
      <line x1="450" y1="210" x2="750" y2="250"/>
      <line x1="450" y1="210" x2="900" y2="250"/>
    </g>

    <!-- Floating Cyber Stars -->
    <g fill="#ffffff" opacity="0.35">
      <circle cx="90" cy="55" r="1"><animate attributeName="opacity" values="0.2;0.8;0.2" dur="2.4s" repeatCount="indefinite"/></circle>
      <circle cx="260" cy="80" r="1.2"><animate attributeName="opacity" values="0.8;0.1;0.8" dur="3.1s" repeatCount="indefinite"/></circle>
      <circle cx="420" cy="45" r="0.9"><animate attributeName="opacity" values="0.3;0.9;0.3" dur="2.7s" repeatCount="indefinite"/></circle>
      <circle cx="590" cy="70" r="1.3"><animate attributeName="opacity" values="0.1;0.7;0.1" dur="3.4s" repeatCount="indefinite"/></circle>
      <circle cx="740" cy="50" r="1.1"><animate attributeName="opacity" values="0.7;0.2;0.7" dur="2.2s" repeatCount="indefinite"/></circle>
    </g>

{chr(10).join(pipes_groups_xml)}

    <!-- Dynamic Crash & Game Over FX -->
{chr(10).join(crash_fx_xml)}

    <!-- CONTINUOUS FLIGHT PHYSICS TRAJECTORY (Multi-Round 60-Second Action!) -->
    <g transform="translate({BIRD_X} 0)">
      <g>
        <animateTransform attributeName="transform" type="translate"
          values="{y_values_str}"
          keyTimes="{kt_str}"
          dur="60s" repeatCount="indefinite"/>

        <!-- Dynamic Pitch Rotation -->
        <g>
          <animateTransform attributeName="transform" type="rotate"
            values="{rot_values_str}"
            keyTimes="{kt_str}"
            dur="60s" repeatCount="indefinite"/>

          <!-- Responsive Jet Thrust Particles (Burst when flapping!) -->
          <g filter="url(#glowFlap)">
            <circle cx="-16" cy="3" r="3.2" fill="#00f0ff">
              <animate attributeName="cx" values="-15;-28;-15" dur="0.25s" repeatCount="indefinite"/>
              <animate attributeName="r" values="3.5;1.5;3.5" dur="0.25s" repeatCount="indefinite"/>
              <animate attributeName="opacity" values="0.9;0.1;0.9" dur="0.25s" repeatCount="indefinite"/>
            </circle>
            <circle cx="-20" cy="4" r="2" fill="#d946ef">
              <animate attributeName="cx" values="-18;-34;-18" dur="0.25s" begin="0.08s" repeatCount="indefinite"/>
              <animate attributeName="opacity" values="0.8;0.05;0.8" dur="0.25s" begin="0.08s" repeatCount="indefinite"/>
            </circle>
          </g>

          <!-- The Cyber Flappy Bird Sprite -->
          <g filter="url(#birdGlow)">
            <ellipse cx="0" cy="0" rx="14" ry="11" fill="#facc15" stroke="#ca8a04" stroke-width="1.2"/>
            <path d="M-6 4 Q0 10 8 6 Q1 4 -6 4 Z" fill="#ffffff" opacity="0.95"/>
            <path d="M-6 4 Q0 10 8 6 Q1 4 -6 4 Z" fill="#00f0ff" opacity="0.4"/>
            <circle cx="6" cy="-4" r="5" fill="#ffffff" stroke="#0f172a" stroke-width="1"/>
            <circle cx="7.5" cy="-4" r="2.2" fill="#00f0ff"/>
            <circle cx="8.5" cy="-5" r="0.8" fill="#ffffff"/>
            <path d="M11 -2 L18 1 L11 4 Z" fill="#f97316" stroke="#c2410c" stroke-width="1"/>
            <line x1="11" y1="1" x2="16" y2="1" stroke="#7c2d12" stroke-width="0.8"/>
            <circle cx="4" cy="2" r="2" fill="#ff73fa" opacity="0.75"/>

            <!-- Flapping Cyber Wing -->
            <g transform="translate(-4 0)">
              <ellipse cx="0" cy="0" rx="7.5" ry="4.5" fill="#ffffff" stroke="#ca8a04" stroke-width="1.2">
                <animateTransform attributeName="transform" type="rotate"
                  values="0 0 0; -45 -4 0; 30 -4 0; 0 0 0"
                  dur="0.2s" repeatCount="indefinite"/>
              </ellipse>
            </g>
          </g>
        </g>
      </g>
    </g>

    <!-- Cyber Ground Bar (Scrolling hazard / circuit pattern) -->
    <g>
      <rect x="0" y="210" width="900" height="40" fill="url(#groundStripes)"/>
      <line x1="0" y1="210" x2="900" y2="210" stroke="#00f0ff" stroke-width="2" filter="url(#glowFlap)"/>
      <line x1="0" y1="213" x2="900" y2="213" stroke="#00ff88" stroke-width="1" opacity="0.8"/>
      <!-- Traveling Ground Tracer -->
      <rect x="0" y="209" width="140" height="2" fill="#ffffff" opacity="0.9" filter="url(#glowFlap)">
        <animate attributeName="x" from="900" to="-140" dur="2s" repeatCount="indefinite"/>
      </rect>
    </g>
  </g>
</svg>"""

    with open("flappy-bird.svg", "w", encoding="utf-8") as f:
        f.write(svg_content)

    print("Wrote flappy-bird.svg successfully!")
    # Verify XML
    try:
        ET.fromstring(svg_content)
        print("XML validation PASSED!")
    except Exception as e:
        print("XML validation FAILED:", e)

if __name__ == "__main__":
    generate_flappy_svg()
