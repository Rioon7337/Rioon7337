import math

def build_flappy_bird_svg():
    TOTAL_DUR = 60.0
    FPS = 25
    TOTAL_FRAMES = int(TOTAL_DUR * FPS)

    GROUND_Y = 208
    BIRD_X = 180.0
    SPEED = 85.0
    GAP_SIZE = 58.0

    rounds = [
        {
            "id": 1,
            "t_start": 0.0,
            "t_end": 20.0,
            "pipes": [
                {"gap_y": 120, "x": 420},
                {"gap_y": 145, "x": 580},
                {"gap_y": 105, "x": 740},
                {"gap_y": 135, "x": 900},
                {"gap_y": 155, "x": 1060},
                {"gap_y": 115, "x": 1220},
                {"gap_y": 140, "x": 1380}, # Collision here
            ],
            "crash_pipe_idx": 6,
            "score": 6,
            "medal": "bronze"
        },
        {
            "id": 2,
            "t_start": 20.0,
            "t_end": 40.0,
            "pipes": [
                {"gap_y": 130, "x": 420},
                {"gap_y": 100, "x": 580},
                {"gap_y": 140, "x": 740},
                {"gap_y": 110, "x": 900},
                {"gap_y": 150, "x": 1060},
                {"gap_y": 125, "x": 1220},
                {"gap_y": 95,  "x": 1380},
                {"gap_y": 135, "x": 1540}, # Collision here
            ],
            "crash_pipe_idx": 7,
            "score": 8,
            "medal": "silver"
        },
        {
            "id": 3,
            "t_start": 40.0,
            "t_end": 60.0,
            "pipes": [
                {"gap_y": 115, "x": 420},
                {"gap_y": 145, "x": 580},
                {"gap_y": 110, "x": 740},
                {"gap_y": 135, "x": 900},
                {"gap_y": 100, "x": 1060},
                {"gap_y": 140, "x": 1220},
                {"gap_y": 120, "x": 1380},
                {"gap_y": 150, "x": 1540}, # Collision here
            ],
            "crash_pipe_idx": 7,
            "score": 10,
            "medal": "gold"
        }
    ]

    all_bird_y = []
    all_bird_rot = []
    all_wing_state = []
    all_flash_op = []
    all_round_scores = []
    all_game_over_op = []

    for f in range(TOTAL_FRAMES):
        t = f / FPS
        rnd = rounds[0]
        if t >= 40.0:
            rnd = rounds[2]
        elif t >= 20.0:
            rnd = rounds[1]

        t_rel = t - rnd["t_start"]
        pipes = rnd["pipes"]
        crash_idx = rnd["crash_pipe_idx"]

        t_crash = (pipes[crash_idx]["x"] - BIRD_X - 8) / SPEED + 1.5

        # Score calculation
        score = 0
        for i, p in enumerate(pipes):
            px = p["x"] - SPEED * (t_rel - 1.5)
            if t_rel >= 1.5 and px + 48 < BIRD_X:
                score += 1
        score = min(score, rnd["score"])
        all_round_scores.append((t, rnd["id"], score))

        if t_rel < 1.5:
            # Ready hover
            by = 120.0 + 4.5 * math.sin(t_rel * 7.0)
            rot = 0.0
            wing = int((t_rel * 10) % 3)
            flash = 0.0
            gov = 0.0
        elif t_rel < t_crash:
            # Playing
            target_y = 120.0
            for p in pipes:
                px = p["x"] - SPEED * (t_rel - 1.5)
                if px + 50 > BIRD_X:
                    target_y = p["gap_y"]
                    break

            cycle_t = (t_rel - 1.5) % 0.44
            if cycle_t < 0.14:
                frac = cycle_t / 0.14
                by = target_y + 12 - 24 * math.sin(frac * math.pi * 0.5)
                rot = -22.0
                wing = 0 if cycle_t < 0.07 else 1
            else:
                fall_t = (cycle_t - 0.14) / 0.30
                by = target_y - 12 + 24 * (fall_t ** 1.8)
                rot = min(75.0, -22.0 + fall_t * 97.0)
                wing = 2
            flash = 0.0
            gov = 0.0
        elif t_rel < t_crash + 0.45:
            # Falling to ground after impact
            dt = t_rel - t_crash
            start_y = pipes[crash_idx]["gap_y"]
            by = min(GROUND_Y - 10, start_y + dt * 240 + 0.5 * 650 * (dt ** 2))
            rot = min(90.0, 45.0 + dt * 160.0)
            wing = 2
            flash = 0.85 if dt < 0.08 else (0.4 if dt < 0.16 else 0.0)
            gov = 0.0
        else:
            # Dead on ground & Game Over scoreboard
            by = GROUND_Y - 8
            rot = 90.0
            wing = 2
            flash = 0.0
            gov = 1.0

        all_bird_y.append(by)
        all_bird_rot.append(rot)
        all_wing_state.append(wing)
        all_flash_op.append(flash)
        all_game_over_op.append(gov)

    STEP = 2
    sub_times = [round(i * STEP / (TOTAL_FRAMES - 1), 4) for i in range(len(all_bird_y) // STEP)]
    if sub_times[-1] != 1.0:
        sub_times.append(1.0)
    num_pts = len(sub_times)

    key_times_str = ";".join(str(kt) for kt in sub_times)
    bird_y_str = ";".join(f"{all_bird_y[min(i * STEP, len(all_bird_y)-1)]:.1f}" for i in range(num_pts))
    bird_rot_str = ";".join(f"{all_bird_rot[min(i * STEP, len(all_bird_rot)-1)]:.1f} 0 0" for i in range(num_pts))
    flash_op_str = ";".join(f"{all_flash_op[min(i * STEP, len(all_flash_op)-1)]:.2f}" for i in range(num_pts))
    gov_op_str = ";".join(f"{all_game_over_op[min(i * STEP, len(all_game_over_op)-1)]:.1f}" for i in range(num_pts))

    w0_op = ";".join("1" if all_wing_state[min(i*STEP, len(all_wing_state)-1)] == 0 else "0" for i in range(num_pts))
    w1_op = ";".join("1" if all_wing_state[min(i*STEP, len(all_wing_state)-1)] == 1 else "0" for i in range(num_pts))
    w2_op = ";".join("1" if all_wing_state[min(i*STEP, len(all_wing_state)-1)] == 2 else "0" for i in range(num_pts))

    def render_pipe_svg(px, gap_y):
        gap_top = gap_y - GAP_SIZE / 2
        gap_bot = gap_y + GAP_SIZE / 2
        cap_h = 22
        pipe_w = 48
        cap_w = 56
        cap_x = -4

        top_body_h = max(2, gap_top - cap_h - 12)
        top_cap_y = gap_top - cap_h

        bot_cap_y = gap_bot
        bot_body_y = gap_bot + cap_h
        bot_body_h = max(2, GROUND_Y - bot_body_y)

        return f"""
        <g transform="translate({px} 0)">
          <!-- Top Pipe Body -->
          <rect x="0" y="12" width="{pipe_w}" height="{top_body_h:.1f}" fill="#73bf2e" stroke="#153007" stroke-width="1.6"/>
          <rect x="5" y="12" width="6" height="{top_body_h:.1f}" fill="#9de643"/>
          <rect x="36" y="12" width="9" height="{top_body_h:.1f}" fill="#558022"/>
          <!-- Top Pipe Collar / Lip -->
          <rect x="{cap_x}" y="{top_cap_y:.1f}" width="{cap_w}" height="{cap_h}" rx="2" fill="#73bf2e" stroke="#153007" stroke-width="1.6"/>
          <rect x="1" y="{top_cap_y:.1f}" width="7" height="{cap_h}" fill="#9de643"/>
          <rect x="38" y="{top_cap_y:.1f}" width="10" height="{cap_h}" fill="#558022"/>
          <line x1="{cap_x}" y1="{gap_top - 2:.1f}" x2="{cap_x + cap_w}" y2="{gap_top - 2:.1f}" stroke="#153007" stroke-width="1.2"/>

          <!-- Bottom Pipe Collar / Lip -->
          <rect x="{cap_x}" y="{bot_cap_y:.1f}" width="{cap_w}" height="{cap_h}" rx="2" fill="#73bf2e" stroke="#153007" stroke-width="1.6"/>
          <rect x="1" y="{bot_cap_y:.1f}" width="7" height="{cap_h}" fill="#9de643"/>
          <rect x="38" y="{bot_cap_y:.1f}" width="10" height="{cap_h}" fill="#558022"/>
          <line x1="{cap_x}" y1="{bot_cap_y + 2:.1f}" x2="{cap_x + cap_w}" y2="{bot_cap_y + 2:.1f}" stroke="#9de643" stroke-width="1.2"/>
          <!-- Bottom Pipe Body -->
          <rect x="0" y="{bot_body_y:.1f}" width="{pipe_w}" height="{bot_body_h:.1f}" fill="#73bf2e" stroke="#153007" stroke-width="1.6"/>
          <rect x="5" y="{bot_body_y:.1f}" width="6" height="{bot_body_h:.1f}" fill="#9de643"/>
          <rect x="36" y="{bot_body_y:.1f}" width="9" height="{bot_body_h:.1f}" fill="#558022"/>
        </g>"""

    round_corridors = []
    for rnd in rounds:
        r_id = rnd["id"]
        t_s = rnd["t_start"] / TOTAL_DUR
        t_e = rnd["t_end"] / TOTAL_DUR
        disp_vals = f"none;inline;none" if r_id == 2 else ("inline;none;none" if r_id == 1 else "none;none;inline")
        disp_keys = f"0.0;{t_s:.4f};{t_e:.4f};1.0" if r_id == 2 else (f"0.0;{t_e:.4f};1.0" if r_id == 1 else f"0.0;{t_s:.4f};1.0")

        crash_p = rnd["pipes"][rnd["crash_pipe_idx"]]
        t_crash_rel = (crash_p["x"] - BIRD_X - 8) / SPEED + 1.5
        t_crash_abs = rnd["t_start"] + t_crash_rel
        shift_at_crash = SPEED * (t_crash_rel - 1.5)

        t_start_shift = (rnd["t_start"] + 1.5) / TOTAL_DUR
        t_crash_norm = t_crash_abs / TOTAL_DUR

        trans_vals = f"0 0; 0 0; -{shift_at_crash:.1f} 0; -{shift_at_crash:.1f} 0"
        trans_keys = f"0.0; {t_start_shift:.4f}; {t_crash_norm:.4f}; 1.0"

        pipes_xml = "\n".join(render_pipe_svg(p["x"], p["gap_y"]) for p in rnd["pipes"])

        corridor = f"""
    <!-- ==================== ROUND {r_id:02d} PIPES CORRIDOR ==================== -->
    <g>
      <animate attributeName="display" values="{disp_vals}" keyTimes="{disp_keys}" dur="{TOTAL_DUR}s" repeatCount="indefinite"/>
      <g>
        <animateTransform attributeName="transform" type="translate"
          values="{trans_vals}" keyTimes="{trans_keys}" dur="{TOTAL_DUR}s" repeatCount="indefinite"/>
        {pipes_xml}
      </g>
    </g>"""
        round_corridors.append(corridor)

    score_text_anim = []
    for sc in range(11):
        vals = []
        for f in range(0, TOTAL_FRAMES, STEP):
            s = all_round_scores[f][2]
            vals.append("1" if s == sc else "0")
        score_text_anim.append(";".join(vals))

    # Scoreboards per round
    # Round 1: Bronze, Score 06
    # Round 2: Silver, Score 08
    # Round 3: Gold, Score 10 with sparkling star
    scoreboards_xml = """
      <!-- ROUND 1 SCOREBOARD (Bronze Medal, Score 06) -->
      <g>
        <animate attributeName="display" values="inline;none;none" keyTimes="0.0;0.3333;1.0" dur="60s" repeatCount="indefinite"/>
        <!-- Bronze Medal -->
        <g transform="translate(-98 0)">
          <circle cx="0" cy="0" r="16" fill="#cd7f32" stroke="#78350f" stroke-width="1.8"/>
          <circle cx="0" cy="0" r="11" fill="#e09858"/>
          <circle cx="-4" cy="-4" r="2.5" fill="#ffffff" opacity="0.8"/>
        </g>
        <text x="110" y="-10" text-anchor="end" font-family="'Fira Code', monospace" font-size="16" font-weight="900" fill="#181818">06</text>
      </g>

      <!-- ROUND 2 SCOREBOARD (Silver Medal, Score 08) -->
      <g>
        <animate attributeName="display" values="none;inline;none;none" keyTimes="0.0;0.3333;0.6667;1.0" dur="60s" repeatCount="indefinite"/>
        <!-- Silver Medal -->
        <g transform="translate(-98 0)">
          <circle cx="0" cy="0" r="16" fill="#e0e0e0" stroke="#71717a" stroke-width="1.8"/>
          <circle cx="0" cy="0" r="11" fill="#f4f4f5"/>
          <circle cx="-4" cy="-4" r="2.5" fill="#ffffff" opacity="0.9"/>
        </g>
        <text x="110" y="-10" text-anchor="end" font-family="'Fira Code', monospace" font-size="16" font-weight="900" fill="#181818">08</text>
      </g>

      <!-- ROUND 3 SCOREBOARD (Gold Medal, Score 10) -->
      <g>
        <animate attributeName="display" values="none;inline;none" keyTimes="0.0;0.6667;1.0" dur="60s" repeatCount="indefinite"/>
        <!-- Gold Medal -->
        <g transform="translate(-98 0)">
          <circle cx="0" cy="0" r="16" fill="#ffd700" stroke="#b45309" stroke-width="1.8"/>
          <circle cx="0" cy="0" r="11" fill="#fef08a"/>
          <circle cx="-4" cy="-4" r="2.5" fill="#ffffff" opacity="0.95"/>
          <!-- Sparkle -->
          <polygon points="0,-18 3,-12 9,-12 4,-8 6,-2 0,-6 -6,-2 -4,-8 -9,-12 -3,-12" fill="#ffffff" transform="scale(0.5) translate(16 -16)"/>
        </g>
        <text x="110" y="-10" text-anchor="end" font-family="'Fira Code', monospace" font-size="16" font-weight="900" fill="#181818">10</text>
      </g>
    """

    svg = f"""<svg width="900" height="250" viewBox="0 0 900 250" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Original Flappy Bird Arcade Rioon7337">
  <defs>
    <!-- Sky Gradient: Authentic Flappy Bird Daylight Sky -->
    <linearGradient id="skyGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#4ec0ca"/>
      <stop offset="70%" stop-color="#6ad5dd"/>
      <stop offset="100%" stop-color="#82e1e8"/>
    </linearGradient>

    <!-- Animated RGB Neon Outer Border -->
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

    <!-- Dirt Ground Pattern (Iconic diagonal stripes) -->
    <pattern id="flapDirt" width="24" height="24" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">
      <rect width="12" height="24" fill="#ded895"/>
      <rect x="12" width="12" height="24" fill="#d2b450"/>
    </pattern>

    <filter id="cardGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>

    <clipPath id="clipPlayfield">
      <rect x="12" y="12" width="876" height="226" rx="16"/>
    </clipPath>
  </defs>

  <!-- Outer Neon Border Aura -->
  <rect x="12" y="12" width="876" height="226" rx="16" fill="none" stroke="url(#rgbFlap)" stroke-width="5" opacity="0.35" filter="url(#cardGlow)"/>
  <rect x="12" y="12" width="876" height="226" rx="16" fill="url(#skyGrad)"/>

  <!-- Main Game Field (Clipped inside rounded bezel) -->
  <g clip-path="url(#clipPlayfield)">

    <!-- Background Layer 1: Fluffy Pixel Clouds (Slow Parallax) -->
    <g opacity="0.85">
      <g>
        <animateTransform attributeName="transform" type="translate" from="0 0" to="-320 0" dur="25s" repeatCount="indefinite"/>
        <g fill="#ffffff">
          <rect x="40" y="60" width="85" height="22" rx="11"/>
          <rect x="60" y="44" width="45" height="28" rx="14"/>
          <rect x="260" y="85" width="110" height="24" rx="12"/>
          <rect x="290" y="68" width="55" height="32" rx="16"/>
          <rect x="520" y="50" width="95" height="22" rx="11"/>
          <rect x="545" y="36" width="50" height="26" rx="13"/>
          <rect x="760" y="75" width="105" height="24" rx="12"/>
          <rect x="790" y="58" width="50" height="30" rx="15"/>
          <rect x="1000" y="60" width="85" height="22" rx="11"/>
          <rect x="1020" y="44" width="45" height="28" rx="14"/>
          <rect x="1220" y="85" width="110" height="24" rx="12"/>
          <rect x="1250" y="68" width="55" height="32" rx="16"/>
        </g>
      </g>
    </g>

    <!-- Background Layer 2: Authentic Pixel City Skyline (Medium Parallax) -->
    <g opacity="0.65">
      <g>
        <animateTransform attributeName="transform" type="translate" from="0 0" to="-400 0" dur="18s" repeatCount="indefinite"/>
        <path d="
          M0 208 L0 165 L25 165 L25 155 L45 155 L45 208
          L65 208 L65 140 L95 140 L95 170 L115 170 L115 208
          L130 208 L130 150 L160 150 L160 208
          L180 208 L180 135 L210 135 L210 160 L230 160 L230 208
          L250 208 L250 148 L280 148 L280 208
          L300 208 L300 130 L320 130 L320 120 L335 120 L335 130 L350 130 L350 208
          L375 208 L375 155 L400 155 L400 208
          L420 208 L420 142 L450 142 L450 208
          L470 208 L470 160 L495 160 L495 208
          L515 208 L515 132 L545 132 L545 208
          L570 208 L570 152 L600 152 L600 208
          L620 208 L620 138 L650 138 L650 208
          L670 208 L670 125 L685 125 L685 115 L700 115 L700 125 L715 125 L715 208
          L740 208 L740 150 L770 150 L770 208
          L790 208 L790 140 L820 140 L820 208
          L840 208 L840 158 L870 158 L870 208
          L890 208 L890 135 L920 135 L920 208
          L940 208 L940 150 L970 150 L970 208
          L1000 208 L1000 130 L1035 130 L1035 208
          L1060 208 L1060 145 L1090 145 L1090 208
          L1110 208 L1110 138 L1140 138 L1140 208
          L1160 208 L1160 155 L1190 155 L1190 208
          L1210 208 L1210 135 L1240 135 L1240 208
          L1300 208 Z" fill="#88cfbd"/>
      </g>
    </g>

    <!-- Background Layer 3: Distant Green Bushes (Fast Parallax) -->
    <g opacity="0.85">
      <g>
        <animateTransform attributeName="transform" type="translate" from="0 0" to="-240 0" dur="8s" repeatCount="indefinite"/>
        <path d="
          M0 208 Q15 192 30 208 Q45 190 60 208 Q75 194 90 208 Q105 188 120 208
          Q135 192 150 208 Q165 190 180 208 Q195 194 210 208 Q225 188 240 208
          Q255 192 270 208 Q285 190 300 208 Q315 194 330 208 Q345 188 360 208
          Q375 192 390 208 Q405 190 420 208 Q435 194 450 208 Q465 188 480 208
          Q495 192 510 208 Q525 190 540 208 Q555 194 570 208 Q585 188 600 208
          Q615 192 630 208 Q645 190 660 208 Q675 194 690 208 Q705 188 720 208
          Q735 192 750 208 Q765 190 780 208 Q795 194 810 208 Q825 188 840 208
          Q855 192 870 208 Q885 190 900 208 Q915 194 930 208 Q945 188 960 208
          Q975 192 990 208 Q1005 190 1020 208 Q1035 194 1050 208 Q1065 188 1080 208
          Q1095 192 1110 208 Q1125 190 1140 208 Q1155 194 1170 208 Q1185 188 1200 208
          Z" fill="#5ee270" stroke="#48c85a" stroke-width="1.5"/>
      </g>
    </g>

    <!-- ==================== MOVING PIPES (ROUNDS 1, 2, 3) ==================== -->
    {"".join(round_corridors)}

    <!-- ==================== THE FLAPPY BIRD SPRITE ==================== -->
    <g transform="translate({BIRD_X} 0)">
      <g>
        <animateTransform attributeName="transform" type="translate"
          values="{";".join(f'0 {y}' for y in bird_y_str.split(';'))}"
          keyTimes="{key_times_str}" dur="{TOTAL_DUR}s" repeatCount="indefinite"/>

        <!-- Bird Pitch Rotation -->
        <g>
          <animateTransform attributeName="transform" type="rotate"
            values="{bird_rot_str}"
            keyTimes="{key_times_str}" dur="{TOTAL_DUR}s" repeatCount="indefinite"/>

          <!-- Pixel-Perfect Original Flappy Bird Graphic (Scaled 2x, centered) -->
          <g transform="translate(-17 -12)">
            <!-- Silhouette outline -->
            <path d="
              M 6 0 H 18 V 2 H 22 V 4 H 26 V 6 H 28 V 16 H 26 V 18 H 22 V 20 H 18 V 22 H 6 V 20 H 2 V 16 H 0 V 6 H 2 V 4 H 6 Z
            " fill="#181818"/>
            <!-- Body Yellow Fill -->
            <path d="
              M 6 2 H 18 V 4 H 22 V 6 H 24 V 16 H 22 V 18 H 18 V 20 H 6 V 18 H 2 V 6 H 4 V 4 H 6 Z
            " fill="#f8e038"/>
            <!-- Lower Body Shadow -->
            <path d="
              M 6 14 H 18 V 16 H 22 V 18 H 18 V 20 H 6 V 18 H 2 V 16 H 6 Z
            " fill="#e8b010"/>

            <!-- White Belly Patch -->
            <path d="
              M 4 10 H 12 V 12 H 14 V 16 H 12 V 18 H 6 V 16 H 4 Z
            " fill="#ffffff"/>

            <!-- Giant Cartoon Eye -->
            <rect x="14" y="2" width="10" height="10" rx="3" fill="#ffffff" stroke="#181818" stroke-width="1.6"/>
            <!-- Black Pupil & Catchlight -->
            <rect x="20" y="4" width="3" height="5" rx="1.2" fill="#000000"/>
            <rect x="21" y="4" width="1" height="2" fill="#ffffff"/>

            <!-- Giant Duck Beak / Orange Lips -->
            <path d="
              M 20 10 H 32 V 13 H 34 V 15 H 20 V 13 Z
            " fill="#f85820"/>
            <!-- Beak Outline & Lower Lip -->
            <path d="
              M 20 10 H 32 V 12 H 34 V 14 H 32 V 16 H 20 V 18 H 18 V 20 H 16 V 18 H 20 Z
            " fill="#e03810"/>
            <line x1="20" y1="14" x2="33" y2="14" stroke="#181818" stroke-width="1.4"/>
            <path d="M 20 10 L 32 10 L 34 13 L 34 15 L 20 15 Z" fill="none" stroke="#181818" stroke-width="1.4"/>
            <path d="M 20 15 L 32 15 L 30 18 L 18 18 Z" fill="none" stroke="#181818" stroke-width="1.4"/>

            <!-- Animated Flapping Wing (3 Poses) -->
            <!-- Wing Pose 0: Flap Up -->
            <g opacity="0">
              <animate attributeName="opacity" values="{w0_op}" keyTimes="{key_times_str}" dur="{TOTAL_DUR}s" repeatCount="indefinite"/>
              <path d="M 2 4 H 12 V 8 H 14 V 12 H 8 V 10 H 4 V 8 H 2 Z" fill="#ffffff" stroke="#181818" stroke-width="1.4"/>
              <path d="M 4 6 H 10 V 8 H 12 V 10 H 6 V 8 H 4 Z" fill="#e8e8e8"/>
            </g>
            <!-- Wing Pose 1: Flap Mid -->
            <g opacity="1">
              <animate attributeName="opacity" values="{w1_op}" keyTimes="{key_times_str}" dur="{TOTAL_DUR}s" repeatCount="indefinite"/>
              <path d="M 0 8 H 12 V 12 H 14 V 14 H 6 V 12 H 2 V 10 H 0 Z" fill="#ffffff" stroke="#181818" stroke-width="1.4"/>
              <path d="M 2 9 H 10 V 12 H 12 V 13 H 4 V 11 H 2 Z" fill="#e8e8e8"/>
            </g>
            <!-- Wing Pose 2: Flap Down / Dive -->
            <g opacity="0">
              <animate attributeName="opacity" values="{w2_op}" keyTimes="{key_times_str}" dur="{TOTAL_DUR}s" repeatCount="indefinite"/>
              <path d="M 2 10 H 12 V 14 H 10 V 16 H 6 V 18 H 4 V 16 H 2 Z" fill="#ffffff" stroke="#181818" stroke-width="1.4"/>
              <path d="M 4 11 H 10 V 13 H 8 V 15 H 6 V 16 H 4 Z" fill="#e8e8e8"/>
            </g>
          </g>
        </g>
      </g>
    </g>

    <!-- White Hit Impact Flash -->
    <rect x="12" y="12" width="876" height="226" fill="#ffffff" opacity="0">
      <animate attributeName="opacity" values="{flash_op_str}" keyTimes="{key_times_str}" dur="{TOTAL_DUR}s" repeatCount="indefinite"/>
    </rect>

    <!-- ==================== GROUND BAR (Iconic Repeating Dirt & Grass) ==================== -->
    <g>
      <!-- Scrolling Dirt Strip -->
      <g>
        <animateTransform attributeName="transform" type="translate" from="0 0" to="-48 0" dur="0.56s" repeatCount="indefinite"/>
        <rect x="-48" y="{GROUND_Y + 10}" width="996" height="32" fill="url(#flapDirt)"/>
      </g>
      <!-- Top Grass Lawn -->
      <rect x="0" y="{GROUND_Y}" width="900" height="10" fill="#73bf2e"/>
      <rect x="0" y="{GROUND_Y}" width="900" height="2.5" fill="#9de643"/>
      <line x1="0" y1="{GROUND_Y}" x2="900" y2="{GROUND_Y}" stroke="#153007" stroke-width="1.8"/>
      <line x1="0" y1="{GROUND_Y + 10}" x2="900" y2="{GROUND_Y + 10}" stroke="#558022" stroke-width="1.2"/>
    </g>

    <!-- ==================== READY STATE & TAP PROMPT ==================== -->
    <g>
      <animate attributeName="opacity"
        values="1;1;0;0; 0;1;1;0;0; 0;1;1;0;0; 0"
        keyTimes="0.0;0.022;0.025;0.3333; 0.3334;0.355;0.358;0.6666; 0.6667;0.688;0.691;0.999; 1.0"
        dur="{TOTAL_DUR}s" repeatCount="indefinite"/>
      <!-- "GET READY" Banner -->
      <g transform="translate(450 85)">
        <rect x="-95" y="-18" width="190" height="36" rx="6" fill="#070c20" stroke="#f59e0b" stroke-width="1.8" filter="url(#cardGlow)" opacity="0.9"/>
        <text text-anchor="middle" y="6" font-family="'Fira Code', 'Press Start 2P', monospace" font-size="14" font-weight="900" fill="#ffd700" letter-spacing="3">
          GET READY!
        </text>
      </g>
    </g>

    <!-- ==================== AUTHENTIC FLAPPY SCORE DISPLAY ==================== -->
    <!-- Large centered white numbers with heavy black stroke -->
    <g transform="translate(450 58)">
      {chr(10).join(f'''      <text text-anchor="middle" font-family="'Fira Code', 'Press Start 2P', system-ui, sans-serif" font-size="32" font-weight="900" fill="#ffffff" stroke="#181818" stroke-width="4" paint-order="stroke fill" letter-spacing="2">
        <animate attributeName="opacity" values="{score_text_anim[sc]}" keyTimes="{key_times_str}" dur="{TOTAL_DUR}s" repeatCount="indefinite"/>
        {sc}
      </text>''' for sc in range(11))}
    </g>

    <!-- ==================== AUTHENTIC ORIGINAL GAME OVER SCOREBOARD ==================== -->
    <g transform="translate(450 115)" opacity="0">
      <animate attributeName="opacity" values="{gov_op_str}" keyTimes="{key_times_str}" dur="{TOTAL_DUR}s" repeatCount="indefinite"/>

      <!-- "GAME OVER" Text Banner -->
      <g transform="translate(0 -52)">
        <text text-anchor="middle" font-family="'Fira Code', 'Press Start 2P', system-ui, sans-serif" font-size="22" font-weight="900" fill="#f85820" stroke="#181818" stroke-width="4" paint-order="stroke fill" letter-spacing="4">
          GAME OVER
        </text>
      </g>

      <!-- Scoreboard Plate (Original Tan / Bronze Border with Bevel) -->
      <g transform="translate(0 10)">
        <rect x="-140" y="-42" width="280" height="84" rx="8" fill="#ded895" stroke="#558022" stroke-width="3"/>
        <rect x="-136" y="-38" width="272" height="76" rx="6" fill="#e8e2a6" stroke="#c0b870" stroke-width="1.5"/>

        <!-- MEDAL Box -->
        <rect x="-122" y="-24" width="48" height="48" rx="4" fill="#d2b450" stroke="#78350f" stroke-width="1.5"/>
        <text x="-98" y="-28" text-anchor="middle" font-family="'Fira Code', monospace" font-size="8" font-weight="900" fill="#78350f">MEDAL</text>

        <!-- Dynamic Medals & Scores per Round -->
        {scoreboards_xml}

        <!-- SCORE Section Header -->
        <text x="30" y="-12" text-anchor="end" font-family="'Fira Code', monospace" font-size="10" font-weight="900" fill="#e03810">SCORE</text>

        <!-- BEST Section -->
        <text x="30" y="18" text-anchor="end" font-family="'Fira Code', monospace" font-size="10" font-weight="900" fill="#e03810">BEST</text>
        <text x="110" y="20" text-anchor="end" font-family="'Fira Code', monospace" font-size="16" font-weight="900" fill="#181818">24</text>

        <!-- "NEW" Tag -->
        <rect x="42" y="6" width="26" height="11" rx="2" fill="#ef4444"/>
        <text x="55" y="15" text-anchor="middle" font-family="'Fira Code', monospace" font-size="7.5" font-weight="900" fill="#ffffff">NEW</text>
      </g>
    </g>

  </g>

  <!-- Arcade Bezel Card Header HUD -->
  <text x="32" y="32" font-family="'Fira Code', ui-monospace, monospace" font-size="11" font-weight="700" letter-spacing="2" fill="#00f0ff" opacity="0.95">// FLAPPY BIRD ARCADE &#183; RIOON7337</text>
  <text x="868" y="32" text-anchor="end" font-family="'Fira Code', ui-monospace, monospace" font-size="11" font-weight="700" letter-spacing="2" fill="#ff73fa" opacity="0.95">HI-SCORE: 250807</text>

  <!-- Cyber Corners -->
  <path d="M22 42 L22 22 L42 22" stroke="#00f0ff" stroke-width="2" fill="none" opacity=".85"/>
  <path d="M878 42 L878 22 L858 22" stroke="#00f0ff" stroke-width="2" fill="none" opacity=".85"/>
  <path d="M22 208 L22 228 L42 228" stroke="#d946ef" stroke-width="2" fill="none" opacity=".85"/>
  <path d="M878 208 L878 228 L858 228" stroke="#d946ef" stroke-width="2" fill="none" opacity=".85"/>

  <!-- Traveling Border Tracer -->
  <rect x="12" y="12" width="876" height="226" rx="16" fill="none" stroke="url(#rgbFlap)" stroke-width="1.6"/>
  <rect x="12" y="12" width="876" height="226" rx="16" fill="none" stroke="#00f0ff" stroke-width="2" stroke-linecap="round" opacity="0.9" pathLength="1000" stroke-dasharray="85 915" filter="url(#cardGlow)">
    <animate attributeName="stroke-dashoffset" from="0" to="-1000" dur="4s" repeatCount="indefinite"/>
  </rect>
</svg>"""

    with open("flappy-bird.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"flappy-bird.svg regenerated! Size: {len(svg)/1024:.2f} KB")

if __name__ == "__main__":
    build_flappy_bird_svg()
