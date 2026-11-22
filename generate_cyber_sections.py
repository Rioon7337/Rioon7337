"""
Generator for Rioon7337 Cyber Profile Sections:
1. skills.svg (Tech Stack Arsenal Matrix)
2. header.svg (Connect / Communication Uplink Header)
3. Social Cards: linkedin.svg, telegram.svg, x.svg, instagram.svg, hackster.svg, threads.svg
4. footer-wave.svg (Thanks For Visiting / Terminal Standby)
"""

def generate_skills_svg():
    # 900 x 620
    svg = '''<svg width="900" height="620" viewBox="0 0 900 620" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Arsenal - Tech Stack Rioon7337">
<defs>
<style>
  .title { font-family: 'Segoe UI', Arial, sans-serif; font-weight: 900; font-size: 32px; letter-spacing: 7px; fill: #ffffff; }
  .subtitle { font-family: 'Fira Code', 'JetBrains Mono', ui-monospace, monospace; font-size: 11px; letter-spacing: 3.5px; fill: #00f0ff; }
  .hud-badge { font-family: 'Fira Code', monospace; font-size: 9.5px; font-weight: 700; letter-spacing: 1.5px; }
  .sector-title { font-family: 'Fira Code', monospace; font-weight: 800; font-size: 11.5px; letter-spacing: 2px; }
  .mod-id { font-family: 'Fira Code', monospace; font-size: 8px; font-weight: 700; letter-spacing: 1.2px; }
  .mod-name { font-family: 'Segoe UI', Arial, sans-serif; font-weight: 800; font-size: 13.5px; letter-spacing: 1.2px; fill: #ffffff; }
  .mod-sub { font-family: 'Fira Code', monospace; font-size: 8.5px; font-weight: 600; letter-spacing: 1px; }
  .corner { stroke-width: 1.8; fill: none; stroke-linecap: round; }
  .grid-bg { stroke: #00f0ff; stroke-opacity: 0.035; stroke-width: 1; }
  @keyframes pulse { 0%, 100% { opacity: 1; } 50% { opacity: 0.35; } }
  @keyframes glitch {
    0%, 93%, 100% { transform: translate(0,0); opacity: 0; }
    94% { transform: translate(-2.5px, 0.8px); opacity: 0.75; }
    96% { transform: translate(2.5px, -0.8px); opacity: 0.75; }
    98% { transform: translate(-1.5px, 0); opacity: 0.4; }
  }
  @keyframes scan {
    0% { transform: translateY(-40px); opacity: 0; }
    15% { opacity: 1; }
    85% { opacity: 1; }
    100% { transform: translateY(630px); opacity: 0; }
  }
  @keyframes blinkLed { 0%, 100% { opacity: 1; } 50% { opacity: 0.2; } }
  .ember { animation: rise linear infinite; }
  @keyframes rise {
    0% { transform: translateY(0); opacity: 0; }
    15% { opacity: 0.85; }
    85% { opacity: 0.45; }
    100% { transform: translateY(-560px); opacity: 0; }
  }
</style>

<radialGradient id="bgGradSkills" cx="50%" cy="20%" r="95%">
  <stop offset="0%" stop-color="#0a1a3e"/>
  <stop offset="50%" stop-color="#07071a"/>
  <stop offset="100%" stop-color="#04040e"/>
</radialGradient>

<linearGradient id="rgbBorderSkills" gradientUnits="userSpaceOnUse" x1="12" y1="310" x2="888" y2="310">
  <stop offset="0%" stop-color="#00f0ff"><animate attributeName="stop-color" values="#00f0ff;#d946ef;#00ffcc;#00f0ff" dur="5s" repeatCount="indefinite"/></stop>
  <stop offset="33%" stop-color="#d946ef"><animate attributeName="stop-color" values="#d946ef;#00f0ff;#ff73fa;#d946ef" dur="5s" repeatCount="indefinite"/></stop>
  <stop offset="66%" stop-color="#00ffcc"><animate attributeName="stop-color" values="#00ffcc;#ff73fa;#00f0ff;#00ffcc" dur="5s" repeatCount="indefinite"/></stop>
  <stop offset="100%" stop-color="#00f0ff"><animate attributeName="stop-color" values="#00f0ff;#d946ef;#00ffcc;#00f0ff" dur="5s" repeatCount="indefinite"/></stop>
  <animateTransform attributeName="gradientTransform" type="rotate" from="0 450 310" to="360 450 310" dur="5s" repeatCount="indefinite"/>
</linearGradient>

<linearGradient id="scanGrad" x1="0%" y1="0%" x2="0%" y2="100%">
  <stop offset="0%" stop-color="#00f0ff" stop-opacity="0"/>
  <stop offset="50%" stop-color="#00f0ff" stop-opacity="0.08"/>
  <stop offset="100%" stop-color="#00f0ff" stop-opacity="0"/>
</linearGradient>

<filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
  <feGaussianBlur stdDeviation="3" result="blur"/>
  <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
</filter>
<filter id="neonInner" x="-20%" y="-20%" width="140%" height="140%">
  <feGaussianBlur stdDeviation="2" result="blur"/>
  <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
</filter>
<filter id="neonOuter" x="-30%" y="-30%" width="160%" height="160%">
  <feGaussianBlur stdDeviation="5.5" result="blur"/>
  <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
</filter>

<pattern id="dotPattern" width="20" height="20" patternUnits="userSpaceOnUse">
  <circle cx="2" cy="2" r="1" fill="#00f0ff" opacity="0.06"/>
</pattern>

<clipPath id="cardClipSkills">
  <path d="M 28 12 L 872 12 L 888 28 L 888 592 L 872 608 L 28 608 L 12 592 L 12 28 Z"/>
</clipPath>
</defs>

<!-- Outer Neon Aura -->
<path d="M 28 12 L 872 12 L 888 28 L 888 592 L 872 608 L 28 608 L 12 592 L 12 28 Z" fill="none" stroke="url(#rgbBorderSkills)" stroke-width="5" opacity="0.3" filter="url(#neonOuter)"/>
<path d="M 28 12 L 872 12 L 888 28 L 888 592 L 872 608 L 28 608 L 12 592 L 12 28 Z" fill="none" stroke="url(#rgbBorderSkills)" stroke-width="2.2" opacity="0.6" filter="url(#neonInner)"/>

<!-- Dark Glass Body -->
<path d="M 28 12 L 872 12 L 888 28 L 888 592 L 872 608 L 28 608 L 12 592 L 12 28 Z" fill="url(#bgGradSkills)"/>
<rect x="12" y="12" width="876" height="596" fill="url(#dotPattern)" clip-path="url(#cardClipSkills)"/>

<!-- Cyber Tech Grid & Scanline -->
<g clip-path="url(#cardClipSkills)">
  <line class="grid-bg" x1="12" y1="95" x2="888" y2="95"/>
  <line class="grid-bg" x1="12" y1="250" x2="888" y2="250"/>
  <line class="grid-bg" x1="12" y1="405" x2="888" y2="405"/>
  <line class="grid-bg" x1="12" y1="560" x2="888" y2="560"/>
  <rect x="12" y="12" width="876" height="40" fill="url(#scanGrad)" style="animation: scan 6s linear infinite;"/>
</g>

<!-- Animated RGB Perimeter -->
<path d="M 28 12 L 872 12 L 888 28 L 888 592 L 872 608 L 28 608 L 12 592 L 12 28 Z" fill="none" stroke="url(#rgbBorderSkills)" stroke-width="1.8" opacity="0.95"/>
<!-- Traveling Laser Tracer -->
<path d="M 28 12 L 872 12 L 888 28 L 888 592 L 872 608 L 28 608 L 12 592 L 12 28 Z" fill="none" stroke="#00f0ff" stroke-width="2.2" stroke-linecap="round" opacity="0.85" pathLength="1000" stroke-dasharray="90 910" filter="url(#neonInner)">
  <animate attributeName="stroke-dashoffset" from="0" to="-1000" dur="4.2s" repeatCount="indefinite"/>
</path>

<!-- Cyber Chamfered Corners -->
<g stroke="#00f0ff" class="corner">
  <path d="M16 42 L16 24 L24 16 L42 16"/>
  <path d="M884 42 L884 24 L876 16 L858 16"/>
</g>
<g stroke="#d946ef" class="corner">
  <path d="M16 578 L16 596 L24 604 L42 604"/>
  <path d="M884 578 L884 596 L876 604 L858 604"/>
</g>

<!-- Side Rail Notches -->
<g stroke="#00f0ff" stroke-width="1.2" opacity="0.45">
  <line x1="12" y1="120" x2="20" y2="120"/>
  <line x1="12" y1="260" x2="20" y2="260"/>
  <line x1="12" y1="420" x2="20" y2="420"/>
  <line x1="12" y1="540" x2="20" y2="540"/>
  <line x1="880" y1="120" x2="888" y2="120"/>
  <line x1="880" y1="260" x2="888" y2="260"/>
  <line x1="880" y1="420" x2="888" y2="420"/>
  <line x1="880" y1="540" x2="888" y2="540"/>
</g>

<!-- HEADER: Title & Telemetry HUD -->
<g transform="translate(0, 0)">
  <!-- Center Top HUD Badge -->
  <g transform="translate(450, 18)">
    <rect x="-105" y="-6" width="210" height="15" rx="4" fill="#040b1c" stroke="#00f0ff" stroke-width="1" opacity="0.9"/>
    <circle cx="-92" cy="1.5" r="2.5" fill="#00ff88" style="animation: blinkLed 1.4s infinite;"/>
    <text x="5" y="5.5" font-family="'Fira Code', monospace" font-size="8" font-weight="700" fill="#00f0ff" text-anchor="middle" letter-spacing="2">SYS.ARSENAL // REV.4.2</text>
    <circle cx="92" cy="1.5" r="2.5" fill="#00ff88" style="animation: blinkLed 1.4s infinite;"/>
  </g>

  <!-- Glitch Title ARSENAL -->
  <text x="450" y="58" text-anchor="middle" class="title" filter="url(#glow)">ARSENAL</text>
  <text x="447" y="58" text-anchor="middle" class="title" fill="#00f0ff" style="animation: glitch 6s infinite; opacity:0;">ARSENAL</text>
  <text x="453" y="58" text-anchor="middle" class="title" fill="#d946ef" style="animation: glitch 6s infinite .14s; opacity:0;">ARSENAL</text>

  <!-- Subtitle -->
  <text x="450" y="77" text-anchor="middle" class="subtitle">// CYBERNETIC WEAPONRY &amp; TECH STACK LOADOUT // RIOON7337</text>

  <!-- Glowing divider line with center diamond -->
  <line x1="220" y1="85" x2="680" y2="85" stroke="url(#rgbBorderSkills)" stroke-width="1.2" opacity="0.7"/>
  <polygon points="450,82 453,85 450,88 447,85" fill="#00f0ff" filter="url(#glow)"/>
</g>
'''

    # Helper function for drawing tech module card
    # Each card is width 154, height 68 (for 5-cols) or width 194, height 68 (for 4-cols)
    def render_card(x, y, w, h, mod_code, name, sub, color, border_color, icon_svg):
        # Chamfered card path: cut top-left (8px) and bottom-right (8px)
        p = f"M {x+8} {y} L {x+w} {y} L {x+w} {y+h-8} L {x+w-8} {y+h} L {x} {y+h} L {x} {y+8} Z"
        dash_len = int(w * 0.3)
        rem_len = int(w * 2 + h * 2) - dash_len
        return f'''
    <!-- Card: {name} -->
    <g>
      <!-- Base Background -->
      <path d="{p}" fill="#060c22" stroke="{border_color}" stroke-width="1.2" opacity="0.95"/>
      <!-- Inner tech grid lines -->
      <line x1="{x+4}" y1="{y+16}" x2="{x+w-4}" y2="{y+16}" stroke="{color}" stroke-width="0.5" opacity="0.25"/>
      <!-- Animated tracer dash -->
      <path d="{p}" fill="none" stroke="{color}" stroke-width="1.8" stroke-linecap="round" pathLength="400" stroke-dasharray="45 355">
        <animate attributeName="stroke-dashoffset" from="0" to="-400" dur="3.4s" repeatCount="indefinite"/>
      </path>
      <!-- Corner Accent Mark -->
      <polygon points="{x+w-12},{y+h} {x+w},{y+h-12} {x+w},{y+h}" fill="{color}" opacity="0.6"/>
      <!-- Module Code Top-Left -->
      <text x="{x+8}" y="{y+11}" class="mod-id" fill="{color}" opacity="0.85">{mod_code}</text>
      <!-- Status dot Top-Right -->
      <circle cx="{x+w-10}" cy="{y+9}" r="2" fill="#00ff88" opacity="0.9"/>
      <!-- Tech Icon (Left: 28x28 box centered around x+22, y+40) -->
      <g transform="translate({x+10}, {y+22})">
        {icon_svg}
      </g>
      <!-- Text details (Right side) -->
      <text x="{x+46}" y="{y+38}" class="mod-name">{name}</text>
      <text x="{x+46}" y="{y+52}" class="mod-sub" fill="{color}">{sub}</text>
    </g>'''

    # Tech Icons (28x28 coordinate box)
    icon_react = '''<ellipse cx="14" cy="14" rx="12" ry="4.5" fill="none" stroke="#00f0ff" stroke-width="1.2"/><ellipse cx="14" cy="14" rx="12" ry="4.5" fill="none" stroke="#00f0ff" stroke-width="1.2" transform="rotate(60 14 14)"/><ellipse cx="14" cy="14" rx="12" ry="4.5" fill="none" stroke="#00f0ff" stroke-width="1.2" transform="rotate(120 14 14)"/><circle cx="14" cy="14" r="2.2" fill="#00f0ff"/>'''
    
    icon_vite = '''<path d="M25 4L14 24 3 4h6l5 11 5-11z" fill="#ffc300"/><path d="M14 24L25 4l-7 1-4 8 2-6-4 1z" fill="#00f0ff"/>'''
    
    icon_babel = '''<polygon points="14,2 25,8.5 25,20.5 14,27 3,20.5 3,8.5" fill="#151b2e" stroke="#f5da55" stroke-width="1.4"/><circle cx="14" cy="14.5" r="4.5" fill="#f5da55"/><line x1="8" y1="14.5" x2="20" y2="14.5" stroke="#060c22" stroke-width="1.5"/>'''
    
    icon_html5 = '''<path d="M4 2l2 20 8 2.5 8-2.5 2-20H4z" fill="#e44d26" opacity="0.85"/><path d="M14 4v18.2l6.2-1.9 1.6-16.3H14z" fill="#f16529"/><path d="M8 8h12l-.3 3.5h-8l.3 3.5h7.4l-.7 7.2-4.7 1.4-4.7-1.4-.3-4H12l.2 2 1.8.5 1.8-.5.3-2.5H8L8 8z" fill="#ffffff"/>'''
    
    icon_css3 = '''<path d="M4 2l2 20 8 2.5 8-2.5 2-20H4z" fill="#1572b6" opacity="0.85"/><path d="M14 4v18.2l6.2-1.9 1.6-16.3H14z" fill="#33a9dc"/><path d="M8 8h12l-.3 3.5h-8l.3 3.5h7.4l-.7 7.2-4.7 1.4-4.7-1.4-.3-4H12l.2 2 1.8.5 1.8-.5.3-2.5H8L8 8z" fill="#ffffff"/>'''

    icon_laravel = '''<path d="M14 2L4 7v14l10 5 10-5V7L14 2z" fill="#ff2d20" opacity="0.25"/><polygon points="14,2 24,7 14,12 4,7" fill="none" stroke="#ff2d20" stroke-width="1.4"/><polygon points="4,7 14,12 14,26 4,21" fill="none" stroke="#ff2d20" stroke-width="1.4"/><polygon points="24,7 14,12 14,26 24,21" fill="none" stroke="#ff2d20" stroke-width="1.4"/><line x1="14" y1="12" x2="14" y2="26" stroke="#ff73fa" stroke-width="1.6"/>'''

    icon_php = '''<ellipse cx="14" cy="14" rx="13" ry="8.5" fill="#777bb4" opacity="0.3" stroke="#8892bf" stroke-width="1.3"/><text x="14" y="17.5" font-family="'Fira Code', monospace" font-size="8.5" font-weight="900" fill="#c4b5fd" text-anchor="middle">PHP</text>'''

    icon_composer = '''<circle cx="14" cy="14" r="12" fill="#885630" opacity="0.25" stroke="#f5d0fe" stroke-width="1.3"/><circle cx="14" cy="10" r="4" fill="#f5d0fe"/><path d="M7 23c0-4 3.5-6 7-6s7 2 7 6H7z" fill="#f5d0fe"/>'''

    icon_node = '''<polygon points="14,2 25,8.5 25,20.5 14,27 3,20.5 3,8.5" fill="#339933" opacity="0.3" stroke="#00ff88" stroke-width="1.4"/><path d="M14 6v8l7-4M14 14l-7-4v8l7 4" fill="none" stroke="#00ff88" stroke-width="1.6"/>'''

    icon_postgres = '''<path d="M14 3C8 3 4 7 4 13c0 7 6 12 10 12s10-5 10-12c0-6-4-10-10-10z" fill="#336791" opacity="0.3" stroke="#00f0ff" stroke-width="1.3"/><circle cx="10" cy="11" r="1.5" fill="#00f0ff"/><circle cx="18" cy="11" r="1.5" fill="#00f0ff"/><path d="M14 14v6M10 20h8" stroke="#00f0ff" stroke-width="1.4"/>'''

    icon_c = '''<polygon points="14,2 25,8.5 25,20.5 14,27 3,20.5 3,8.5" fill="#00599c" opacity="0.3" stroke="#00ff88" stroke-width="1.3"/><path d="M18 10a6 6 0 1 0 0 8" fill="none" stroke="#a7f3d0" stroke-width="2.2" stroke-linecap="round"/>'''

    icon_cpp = '''<polygon points="14,2 25,8.5 25,20.5 14,27 3,20.5 3,8.5" fill="#004482" opacity="0.3" stroke="#00ffcc" stroke-width="1.3"/><path d="M14 10a5 5 0 1 0 0 8" fill="none" stroke="#cffafe" stroke-width="2" stroke-linecap="round"/><path d="M18 14h3M19.5 12.5v3M22.5 14h3M24 12.5v3" stroke="#00ffcc" stroke-width="1.2"/>'''

    icon_java = '''<path d="M6 21c4 2 12 2 16 0-3-1-13-1-16 0z" fill="#f89820"/><path d="M8 18c3 1.5 9 1.5 12 0-2-1-10-1-12 0z" fill="#5382a1"/><path d="M13 3c2 2-2 4 0 7-3-2 1-4 0-7z" fill="#e76f00"/><path d="M16 6c1 1.5-1 3 0 5-2-1.5 1-3.5 0-5z" fill="#e76f00"/>'''

    icon_python = '''<path d="M13.5 3c-4.5 0-4.2 2-4.2 2v2.5h8.5v1.2H7.2S4 8.4 4 13s2.8 4.4 2.8 4.4H9v-2.2s-.1-2.6 2.6-2.6h4.5s2.5 0 2.5-2.5V5.5S18.8 3 13.5 3z" fill="#387eb8"/><circle cx="11" cy="5.5" r="1" fill="#ffffff"/><path d="M14.5 25c4.5 0 4.2-2 4.2-2v-2.5h-8.5v-1.2h10.6s3.2.3 3.2-4.3-2.8-4.4-2.8-4.4H19v2.2s.1 2.6-2.6 2.6h-4.5s-2.5 0-2.5 2.5v2.6s-.2 2.5 5.1 2.5z" fill="#ffe052"/><circle cx="17" cy="22.5" r="1" fill="#ffffff"/>'''

    # SECTOR 1: Frontend (5 items)
    # Total inner width: 836 px -> 5 items: w=154, gap=16 -> 5*154 + 4*16 = 770 + 64 = 834. Start x=33
    svg += '''
<!-- ================= SECTOR 01: FRONTEND ================= -->
<g transform="translate(0, 102)">
  <!-- Sector Header Bar -->
  <rect x="32" y="0" width="836" height="24" rx="4" fill="#041226" stroke="#00f0ff" stroke-width="0.9" opacity="0.85"/>
  <circle cx="46" cy="12" r="3" fill="#00f0ff" style="animation: blinkLed 1.8s infinite;"/>
  <text x="60" y="16" class="sector-title" fill="#00f0ff">SECTOR 01 // FRONTEND INTERFACE MATRIX</text>
  <text x="856" y="16" font-family="'Fira Code', monospace" font-size="8.5" fill="#00ffcc" text-anchor="end" letter-spacing="1.5">&lt;SYS:FE // PORT:3000 /&gt;</text>
'''
    fe_items = [
        ("MOD.01", "REACT", "UI.FRAMEWORK", icon_react),
        ("MOD.02", "VITE", "NEXTGEN.BUILD", icon_vite),
        ("MOD.03", "BABEL", "JS.COMPILER", icon_babel),
        ("MOD.04", "HTML5", "HYPERTEXT.DOM", icon_html5),
        ("MOD.05", "CSS3", "NEON.STYLING", icon_css3),
    ]
    x_curr = 33
    for mod_code, name, sub, icon in fe_items:
        svg += render_card(x_curr, 34, 154, 68, mod_code, name, sub, "#00f0ff", "#0088aa", icon)
        x_curr += 170

    svg += '\n</g>\n'

    # SECTOR 2: Backend & Database (5 items)
    svg += '''
<!-- ================= SECTOR 02: BACKEND & DATABASE ================= -->
<g transform="translate(0, 252)">
  <!-- Sector Header Bar -->
  <rect x="32" y="0" width="836" height="24" rx="4" fill="#140622" stroke="#d946ef" stroke-width="0.9" opacity="0.85"/>
  <circle cx="46" cy="12" r="3" fill="#d946ef" style="animation: blinkLed 2.1s infinite;"/>
  <text x="60" y="16" class="sector-title" fill="#d946ef">SECTOR 02 // BACKEND CORE &amp; DATA STORAGE</text>
  <text x="856" y="16" font-family="'Fira Code', monospace" font-size="8.5" fill="#ff73fa" text-anchor="end" letter-spacing="1.5">&lt;SYS:BE // DB:5432 /&gt;</text>
'''
    be_items = [
        ("MOD.06", "LARAVEL", "PHP.FRAMEWORK", icon_laravel),
        ("MOD.07", "PHP", "HYPERTEXT.PRE", icon_php),
        ("MOD.08", "COMPOSER", "PKG.MANAGER", icon_composer),
        ("MOD.09", "NODE.JS", "ASYNC.RUNTIME", icon_node),
        ("MOD.10", "POSTGRES", "RELATIONAL.DB", icon_postgres),
    ]
    x_curr = 33
    for mod_code, name, sub, icon in be_items:
        svg += render_card(x_curr, 34, 154, 68, mod_code, name, sub, "#d946ef", "#882299", icon)
        x_curr += 170

    svg += '\n</g>\n'

    # SECTOR 3: Core Programming (4 items)
    # Total width 836 px -> 4 items: w=196, gap=17 -> 4*196 + 3*17 = 784 + 51 = 835. Start x=33
    svg += '''
<!-- ================= SECTOR 03: LOW-LEVEL & COMPUTING ================= -->
<g transform="translate(0, 402)">
  <!-- Sector Header Bar -->
  <rect x="32" y="0" width="836" height="24" rx="4" fill="#041a14" stroke="#00ff88" stroke-width="0.9" opacity="0.85"/>
  <circle cx="46" cy="12" r="3" fill="#00ff88" style="animation: blinkLed 1.6s infinite;"/>
  <text x="60" y="16" class="sector-title" fill="#00ff88">SECTOR 03 // LOW-LEVEL ENGINE &amp; SCRIPTING</text>
  <text x="856" y="16" font-family="'Fira Code', monospace" font-size="8.5" fill="#a7f3d0" text-anchor="end" letter-spacing="1.5">&lt;SYS:CORE // KERNEL:SYSTEM /&gt;</text>
'''
    core_items = [
        ("MOD.11", "C", "NATIVE.SYSTEM", icon_c),
        ("MOD.12", "C++", "HIGH_PERF.CORE", icon_cpp),
        ("MOD.13", "JAVA", "JVM.ENTERPRISE", icon_java),
        ("MOD.14", "PYTHON", "AI_NEURAL.CORE", icon_python),
    ]
    x_curr = 33
    for mod_code, name, sub, icon in core_items:
        svg += render_card(x_curr, 34, 196, 68, mod_code, name, sub, "#00ff88", "#008855", icon)
        x_curr += 213

    svg += '\n</g>\n'

    # FOOTER TELEMETRY RAIL & PARTICLES
    svg += '''
<!-- Bottom HUD Telemetry Status Rail -->
<g transform="translate(32, 575)">
  <rect x="0" y="0" width="836" height="20" rx="3" fill="#030818" stroke="#00f0ff" stroke-width="0.8" opacity="0.75"/>
  <circle cx="12" cy="10" r="2.5" fill="#00ff88"/>
  <text x="22" y="13.5" font-family="'Fira Code', monospace" font-size="8.5" font-weight="700" fill="#00ff88" letter-spacing="1.5">LOADOUT_INTEGRITY: 100% // ALL SUBSYSTEMS ARMED // QUANTUM BUFFER: 0x7337 // RIOON7337</text>
  <text x="826" y="13.5" font-family="'Fira Code', monospace" font-size="8" font-weight="700" fill="#00f0ff" text-anchor="end" letter-spacing="1.5">ONLINE [●]</text>
</g>

<!-- Floating Cyber Particles -->
<g clip-path="url(#cardClipSkills)">
  <circle class="ember" cx="70" cy="580" r="1.6" fill="#00f0ff" style="animation-duration:4.5s; animation-delay:0s;"/>
  <circle class="ember" cx="160" cy="580" r="1.4" fill="#d946ef" style="animation-duration:5.8s; animation-delay:1.2s;"/>
  <circle class="ember" cx="280" cy="580" r="1.5" fill="#00ff88" style="animation-duration:6.2s; animation-delay:2.4s;"/>
  <circle class="ember" cx="620" cy="580" r="1.6" fill="#00f0ff" style="animation-duration:5.2s; animation-delay:0.8s;"/>
  <circle class="ember" cx="760" cy="580" r="1.5" fill="#ff73fa" style="animation-duration:4.8s; animation-delay:1.8s;"/>
  <circle class="ember" cx="830" cy="580" r="1.6" fill="#00ffcc" style="animation-duration:5.5s; animation-delay:3.1s;"/>
</g>
</svg>'''
    return svg

def generate_header_svg():
    # 900 x 130
    return '''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="130" viewBox="0 0 900 130" role="img" aria-label="Connect - Rioon7337">
  <defs>
    <style>
      .hdr-title { font-family: 'Segoe UI', Arial, sans-serif; font-size: 32px; font-weight: 900; letter-spacing: 9px; fill: #ffffff; }
      .hdr-sub { font-family: 'Fira Code', monospace; font-size: 11px; letter-spacing: 3.5px; fill: #ff73fa; }
      .hdr-badge { font-family: 'Fira Code', monospace; font-size: 8.5px; font-weight: 700; letter-spacing: 2px; }
      @keyframes glitchHdr {
        0%, 93%, 100% { transform: translate(0,0); opacity: 0; }
        94% { transform: translate(-2px, 0.6px); opacity: 0.8; }
        96% { transform: translate(2px, -0.6px); opacity: 0.8; }
        98% { transform: translate(-1px, 0); opacity: 0.4; }
      }
      @keyframes pulseDot { 0%, 100% { opacity: 1; } 50% { opacity: 0.2; } }
      @keyframes waveDrift {
        0% { transform: translateX(0); }
        100% { transform: translateX(-150px); }
      }
    </style>

    <radialGradient id="hb" cx="50%" cy="50%" r="90%">
      <stop offset="0%" stop-color="#0a1a3e"/>
      <stop offset="55%" stop-color="#07071a"/>
      <stop offset="100%" stop-color="#050512"/>
    </radialGradient>

    <linearGradient id="rgbBorderHdr" gradientUnits="userSpaceOnUse" x1="12" y1="65" x2="888" y2="65">
      <stop offset="0%" stop-color="#00f0ff"><animate attributeName="stop-color" values="#00f0ff;#d946ef;#00ffcc;#00f0ff" dur="5s" repeatCount="indefinite"/></stop>
      <stop offset="33%" stop-color="#d946ef"><animate attributeName="stop-color" values="#d946ef;#00f0ff;#ff73fa;#d946ef" dur="5s" repeatCount="indefinite"/></stop>
      <stop offset="66%" stop-color="#00ffcc"><animate attributeName="stop-color" values="#00ffcc;#ff73fa;#00f0ff;#00ffcc" dur="5s" repeatCount="indefinite"/></stop>
      <stop offset="100%" stop-color="#00f0ff"><animate attributeName="stop-color" values="#00f0ff;#d946ef;#00ffcc;#00f0ff" dur="5s" repeatCount="indefinite"/></stop>
      <animateTransform attributeName="gradientTransform" type="rotate" from="0 450 65" to="360 450 65" dur="4.5s" repeatCount="indefinite"/>
    </linearGradient>

    <filter id="hglow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="3.2" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>

    <pattern id="hgrid" width="16" height="16" patternUnits="userSpaceOnUse">
      <path d="M16 0H0V16" fill="none" stroke="#00f0ff" stroke-width="0.35" opacity="0.06"/>
    </pattern>

    <clipPath id="hdrClip">
      <path d="M 24 6 L 876 6 L 894 24 L 894 106 L 876 124 L 24 124 L 6 106 L 6 24 Z"/>
    </clipPath>
  </defs>

  <!-- Outer Neon Aura -->
  <path d="M 24 6 L 876 6 L 894 24 L 894 106 L 876 124 L 24 124 L 6 106 L 6 24 Z" fill="none" stroke="url(#rgbBorderHdr)" stroke-width="4.5" opacity="0.3" filter="url(#hglow)"/>

  <!-- Body -->
  <path d="M 24 6 L 876 6 L 894 24 L 894 106 L 876 124 L 24 124 L 6 106 L 6 24 Z" fill="url(#hb)"/>
  <rect x="6" y="6" width="888" height="118" fill="url(#hgrid)" clip-path="url(#hdrClip)"/>

  <!-- Edge Borders & Tracer -->
  <path d="M 24 6 L 876 6 L 894 24 L 894 106 L 876 124 L 24 124 L 6 106 L 6 24 Z" fill="none" stroke="url(#rgbBorderHdr)" stroke-width="1.8" opacity="0.95"/>
  <path d="M 24 6 L 876 6 L 894 24 L 894 106 L 876 124 L 24 124 L 6 106 L 6 24 Z" fill="none" stroke="#00f0ff" stroke-width="2.2" stroke-linecap="round" opacity="0.9" pathLength="1000" stroke-dasharray="80 920" filter="url(#hglow)">
    <animate attributeName="stroke-dashoffset" from="0" to="-1000" dur="4s" repeatCount="indefinite"/>
  </path>

  <!-- Cyber Corners -->
  <g stroke="#00f0ff" stroke-width="1.8" fill="none" opacity="0.9">
    <path d="M12 36 L12 20 L20 12 L36 12"/>
    <path d="M888 36 L888 20 L880 12 L864 12"/>
  </g>
  <g stroke="#d946ef" stroke-width="1.8" fill="none" opacity="0.9">
    <path d="M12 94 L12 110 L20 118 L36 118"/>
    <path d="M888 94 L888 110 L880 118 L864 118"/>
  </g>

  <!-- Top Telemetry Strip -->
  <g transform="translate(0, 18)">
    <text x="32" y="5" class="hdr-badge" fill="#00ffcc">&lt;FREQ: 5.84 GHz // PROTOCOL: NEURAL_UPLINK&gt;</text>
    <g transform="translate(450, 0)">
      <circle cx="-55" cy="1" r="2.5" fill="#00ff88" style="animation: pulseDot 1.4s infinite;"/>
      <text x="0" y="4.5" class="hdr-badge" fill="#00ff88" text-anchor="middle">LIVE SIGNAL // ENCRYPTED</text>
      <circle cx="55" cy="1" r="2.5" fill="#00ff88" style="animation: pulseDot 1.4s infinite;"/>
    </g>
    <text x="868" y="5" class="hdr-badge" fill="#00f0ff" text-anchor="end">&lt;AES-GCM-256 // RIOON7337&gt;</text>
  </g>

  <!-- Main Title CONNECT with Glitch -->
  <text x="450" y="65" text-anchor="middle" class="hdr-title" filter="url(#hglow)">CONNECT</text>
  <text x="447" y="65" text-anchor="middle" class="hdr-title" fill="#00f0ff" style="animation: glitchHdr 6s infinite; opacity:0;">CONNECT</text>
  <text x="453" y="65" text-anchor="middle" class="hdr-title" fill="#d946ef" style="animation: glitchHdr 6s infinite .14s; opacity:0;">CONNECT</text>

  <!-- Subtitle -->
  <text x="450" y="87" text-anchor="middle" class="hdr-sub">
    // ESTABLISH DIRECT DATA LINK &#8212; SELECT NEURAL NODE &#8212; RIOON7337
  </text>

  <!-- Bottom Frequency Waveform Divider -->
  <g clip-path="url(#hdrClip)">
    <path d="M 60 106 Q 110 96 160 106 T 260 106 T 360 106 T 460 106 T 560 106 T 660 106 T 760 106 T 840 106" fill="none" stroke="url(#rgbBorderHdr)" stroke-width="1.4" opacity="0.6"/>
  </g>

  <!-- Traveling Photon Packets on Waveform -->
  <circle cx="200" cy="106" r="2.6" fill="#00f0ff" filter="url(#hglow)">
    <animate attributeName="cx" values="100;800;100" dur="4.5s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.2;1;0.2" dur="4.5s" repeatCount="indefinite"/>
  </circle>
  <circle cx="700" cy="106" r="2.4" fill="#d946ef" filter="url(#hglow)">
    <animate attributeName="cx" values="800;100;800" dur="4.5s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.2;1;0.2" dur="4.5s" repeatCount="indefinite"/>
  </circle>
</svg>'''

def generate_social_svg(name, node_code, label, status_text, accent_color, icon_inner_svg, delay_s="0.0s"):
    # 260 x 78
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="260" height="78" viewBox="0 0 260 78" role="img" aria-label="{label}">
  <defs>
    <linearGradient id="bg_{name}" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#050a1c"/>
      <stop offset="60%" stop-color="#071330"/>
      <stop offset="100%" stop-color="#040614"/>
    </linearGradient>

    <linearGradient id="edge_{name}" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{accent_color}"/>
      <stop offset="50%" stop-color="#d946ef"/>
      <stop offset="100%" stop-color="{accent_color}"/>
    </linearGradient>

    <filter id="glow_{name}" x="-40%" y="-40%" width="180%" height="180%">
      <feGaussianBlur stdDeviation="2.4" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>

    <pattern id="grid_{name}" width="12" height="12" patternUnits="userSpaceOnUse">
      <path d="M12 0H0V12" fill="none" stroke="{accent_color}" stroke-width="0.3" opacity="0.08"/>
    </pattern>

    <linearGradient id="sweep_{name}" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{accent_color}" stop-opacity="0"/>
      <stop offset="45%" stop-color="{accent_color}" stop-opacity="0.25"/>
      <stop offset="55%" stop-color="#ffffff" stop-opacity="0.2"/>
      <stop offset="100%" stop-color="{accent_color}" stop-opacity="0"/>
    </linearGradient>

    <!-- Chamfered Keycard Clip -->
    <clipPath id="clip_{name}">
      <path d="M 14 2 L 246 2 L 258 14 L 258 64 L 246 76 L 14 76 L 2 64 L 2 14 Z"/>
    </clipPath>
  </defs>

  <!-- Body -->
  <path d="M 14 2 L 246 2 L 258 14 L 258 64 L 246 76 L 14 76 L 2 64 L 2 14 Z" fill="url(#bg_{name})"/>
  <rect x="2" y="2" width="256" height="74" fill="url(#grid_{name})" clip-path="url(#clip_{name})"/>

  <!-- Glowing Edge Border -->
  <path d="M 14 2 L 246 2 L 258 14 L 258 64 L 246 76 L 14 76 L 2 64 L 2 14 Z"
        fill="none" stroke="url(#edge_{name})" stroke-width="1.6" opacity="0.9" filter="url(#glow_{name})">
    <animate attributeName="opacity" values="0.6;1;0.6" dur="3s" begin="{delay_s}" repeatCount="indefinite"/>
  </path>

  <!-- Traveling Dash Sweep -->
  <path d="M 14 2 L 246 2 L 258 14 L 258 64 L 246 76 L 14 76 L 2 64 L 2 14 Z"
        fill="none" stroke="{accent_color}" stroke-width="2" stroke-linecap="round" pathLength="600" stroke-dasharray="60 540">
    <animate attributeName="stroke-dashoffset" from="0" to="-600" dur="3.6s" begin="{delay_s}" repeatCount="indefinite"/>
  </path>

  <!-- Light Sweep Effect -->
  <g clip-path="url(#clip_{name})">
    <rect x="-260" y="0" width="260" height="78" fill="url(#sweep_{name})">
      <animate attributeName="x" from="-260" to="260" dur="4.2s" begin="{delay_s}" repeatCount="indefinite"/>
    </rect>
  </g>

  <!-- Cyber Corners -->
  <g stroke="{accent_color}" stroke-width="1.5" fill="none" opacity="0.9">
    <path d="M7 24 L7 16 L16 7 L24 7"/>
    <path d="M253 24 L253 16 L244 7 L236 7"/>
    <path d="M7 54 L7 62 L16 71 L24 71"/>
    <path d="M253 54 L253 62 L244 71 L236 71"/>
  </g>

  <!-- Icon Chamber (Left Side) -->
  <g transform="translate(18, 22)">
    <rect x="0" y="0" width="34" height="34" rx="6" fill="#06122c" stroke="{accent_color}" stroke-width="1.2" opacity="0.9"/>
    {icon_inner_svg}
  </g>

  <!-- Node Code Identifier -->
  <text x="64" y="24" font-family="'Fira Code', monospace" font-size="8.5" font-weight="700" letter-spacing="1.5" fill="{accent_color}">{node_code}</text>

  <!-- Main Platform Label -->
  <text x="64" y="42" font-family="'Segoe UI', Arial, sans-serif" font-size="14.5" font-weight="900" letter-spacing="2" fill="#ffffff" filter="url(#glow_{name})">{label}</text>

  <!-- Status Telemetry Line -->
  <g transform="translate(64, 58)">
    <circle cx="4" cy="-3.5" r="2.5" fill="#00ff88">
      <animate attributeName="opacity" values="1;0.2;1" dur="1.6s" repeatCount="indefinite"/>
    </circle>
    <text x="12" y="0" font-family="'Fira Code', monospace" font-size="9" font-weight="600" letter-spacing="1.2" fill="#00ffcc">{status_text}</text>
  </g>

  <!-- Cyber Navigation Chevron >>> -->
  <g stroke="#d946ef" stroke-width="1.8" fill="none" stroke-linecap="round" stroke-linejoin="round" transform="translate(224, 34)">
    <path d="M0 0 L5 5 L0 10">
      <animate attributeName="opacity" values="0.3;1;0.3" dur="2s" begin="{delay_s}" repeatCount="indefinite"/>
    </path>
    <path d="M6 0 L11 5 L6 10" opacity="0.6">
      <animate attributeName="opacity" values="0.1;0.8;0.1" dur="2s" begin="{delay_s}" repeatCount="indefinite"/>
    </path>
  </g>
</svg>'''

def generate_footer_wave_svg():
    # 900 x 200
    return '''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="200" viewBox="0 0 900 200" role="img" aria-label="Thanks For Visiting - Rioon7337">
  <defs>
    <style>
      .ft-title { font-family: 'Segoe UI', Arial, sans-serif; font-size: 26px; font-weight: 900; letter-spacing: 7px; fill: #ffffff; }
      .ft-sub { font-family: 'Fira Code', monospace; font-size: 11px; font-weight: 700; letter-spacing: 3.5px; fill: #00f0ff; }
      .ft-badge { font-family: 'Fira Code', monospace; font-size: 8.5px; font-weight: 700; letter-spacing: 1.8px; }
      @keyframes glitchFt {
        0%, 93%, 100% { transform: translate(0,0); opacity: 0; }
        94% { transform: translate(-2px, 0.6px); opacity: 0.8; }
        96% { transform: translate(2px, -0.6px); opacity: 0.8; }
        98% { transform: translate(-1px, 0); opacity: 0.4; }
      }
      @keyframes blinkCursor { 0%, 100% { opacity: 1; } 50% { opacity: 0; } }
      .eq-bar { animation: eqPulse 1.8s ease-in-out infinite alternate; }
    </style>

    <radialGradient id="bgWave" cx="50%" cy="50%" r="90%">
      <stop offset="0%" stop-color="#0a1a3e"/>
      <stop offset="55%" stop-color="#07071a"/>
      <stop offset="100%" stop-color="#04040e"/>
    </radialGradient>

    <!-- Dual Animated Cyber Wave Gradients -->
    <linearGradient id="cyberWave1" gradientUnits="userSpaceOnUse" x1="20" y1="100" x2="880" y2="100">
      <stop offset="0%" stop-color="#00f0ff" stop-opacity="0"/>
      <stop offset="25%" stop-color="#00f0ff">
        <animate attributeName="stop-color" values="#00f0ff;#d946ef;#00ffcc;#00f0ff" dur="5s" repeatCount="indefinite"/>
      </stop>
      <stop offset="50%" stop-color="#00e5ff">
        <animate attributeName="stop-color" values="#00e5ff;#ff73fa;#00f0ff;#00e5ff" dur="5s" repeatCount="indefinite"/>
      </stop>
      <stop offset="75%" stop-color="#d946ef">
        <animate attributeName="stop-color" values="#d946ef;#00f0ff;#ff73fa;#d946ef" dur="5s" repeatCount="indefinite"/>
      </stop>
      <stop offset="100%" stop-color="#00f0ff" stop-opacity="0"/>
    </linearGradient>

    <linearGradient id="frameGradWave" gradientUnits="userSpaceOnUse" x1="12" y1="100" x2="888" y2="100">
      <stop offset="0%" stop-color="#00f0ff"><animate attributeName="stop-color" values="#00f0ff;#d946ef;#00ffcc;#00f0ff" dur="5s" repeatCount="indefinite"/></stop>
      <stop offset="50%" stop-color="#d946ef"><animate attributeName="stop-color" values="#d946ef;#00ffcc;#00f0ff;#d946ef" dur="5s" repeatCount="indefinite"/></stop>
      <stop offset="100%" stop-color="#00ffcc"><animate attributeName="stop-color" values="#00ffcc;#00f0ff;#d946ef;#00ffcc" dur="5s" repeatCount="indefinite"/></stop>
      <animateTransform attributeName="gradientTransform" type="rotate" from="0 450 100" to="360 450 100" dur="5s" repeatCount="indefinite"/>
    </linearGradient>

    <filter id="glowWave" x="-25%" y="-25%" width="150%" height="150%">
      <feGaussianBlur stdDeviation="3.2" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>

    <pattern id="gridWave" width="16" height="16" patternUnits="userSpaceOnUse">
      <path d="M16 0H0V16" fill="none" stroke="#00f0ff" stroke-width="0.35" opacity="0.06"/>
    </pattern>

    <clipPath id="waveClip">
      <path d="M 28 8 L 872 8 L 892 28 L 892 172 L 872 192 L 28 192 L 8 172 L 8 28 Z"/>
    </clipPath>
  </defs>

  <!-- Outer Neon Glow -->
  <path d="M 28 8 L 872 8 L 892 28 L 892 172 L 872 192 L 28 192 L 8 172 L 8 28 Z" fill="none" stroke="url(#frameGradWave)" stroke-width="4.5" opacity="0.3" filter="url(#glowWave)"/>

  <!-- Body -->
  <path d="M 28 8 L 872 8 L 892 28 L 892 172 L 872 192 L 28 192 L 8 172 L 8 28 Z" fill="url(#bgWave)"/>
  <rect x="8" y="8" width="884" height="184" fill="url(#gridWave)" clip-path="url(#waveClip)"/>

  <!-- Cyber Corners -->
  <g stroke="#00f0ff" stroke-width="1.8" fill="none" opacity="0.9">
    <path d="M16 42 L16 26 L26 16 L42 16"/>
    <path d="M884 42 L884 26 L874 16 L858 16"/>
  </g>
  <g stroke="#d946ef" stroke-width="1.8" fill="none" opacity="0.9">
    <path d="M16 158 L16 174 L26 184 L42 184"/>
    <path d="M884 158 L884 174 L874 184 L858 184"/>
  </g>

  <!-- Top Telemetry Header Strip -->
  <g transform="translate(0, 24)">
    <text x="36" y="5" class="ft-badge" fill="#00ffcc">&lt;SESSION_ID: #7337-TERMINAL // DISCONNECT_READY&gt;</text>
    <g transform="translate(450, 0)">
      <circle cx="-60" cy="1.5" r="2.5" fill="#00ff88" style="animation: eqPulse 1.4s infinite;"/>
      <text x="0" y="5" class="ft-badge" fill="#00ff88" text-anchor="middle">UPTIME: 99.99% // SEC_HASH: 0x7337</text>
      <circle cx="60" cy="1.5" r="2.5" fill="#00ff88" style="animation: eqPulse 1.4s infinite;"/>
    </g>
    <text x="864" y="5" class="ft-badge" fill="#00f0ff" text-anchor="end">&lt;LOGOUT PROTOCOL // SUCCESS&gt;</text>
  </g>

  <!-- Digital Equalizer Spectrum Background Bars (Symmetric from center) -->
  <g clip-path="url(#waveClip)" opacity="0.18">
    <!-- Left Equalizer Bars -->
    <rect x="180" y="110" width="6" height="24" fill="#00f0ff"><animate attributeName="height" values="10;34;14;28;10" dur="2.1s" repeatCount="indefinite"/><animate attributeName="y" values="124;100;120;106;124" dur="2.1s" repeatCount="indefinite"/></rect>
    <rect x="210" y="105" width="6" height="34" fill="#00f0ff"><animate attributeName="height" values="15;42;20;35;15" dur="1.7s" repeatCount="indefinite"/><animate attributeName="y" values="119;92;114;99;119" dur="1.7s" repeatCount="indefinite"/></rect>
    <rect x="240" y="95" width="6" height="54" fill="#00ffcc"><animate attributeName="height" values="24;58;32;48;24" dur="2.3s" repeatCount="indefinite"/><animate attributeName="y" values="110;76;102;86;110" dur="2.3s" repeatCount="indefinite"/></rect>
    <rect x="270" y="90" width="6" height="64" fill="#d946ef"><animate attributeName="height" values="30;66;40;55;30" dur="1.9s" repeatCount="indefinite"/><animate attributeName="y" values="104;68;94;79;104" dur="1.9s" repeatCount="indefinite"/></rect>
    
    <!-- Right Equalizer Bars -->
    <rect x="630" y="90" width="6" height="64" fill="#d946ef"><animate attributeName="height" values="30;66;40;55;30" dur="1.9s" repeatCount="indefinite"/><animate attributeName="y" values="104;68;94;79;104" dur="1.9s" repeatCount="indefinite"/></rect>
    <rect x="660" y="95" width="6" height="54" fill="#00ffcc"><animate attributeName="height" values="24;58;32;48;24" dur="2.3s" repeatCount="indefinite"/><animate attributeName="y" values="110;76;102;86;110" dur="2.3s" repeatCount="indefinite"/></rect>
    <rect x="690" y="105" width="6" height="34" fill="#00f0ff"><animate attributeName="height" values="15;42;20;35;15" dur="1.7s" repeatCount="indefinite"/><animate attributeName="y" values="119;92;114;99;119" dur="1.7s" repeatCount="indefinite"/></rect>
    <rect x="720" y="110" width="6" height="24" fill="#00f0ff"><animate attributeName="height" values="10;34;14;28;10" dur="2.1s" repeatCount="indefinite"/><animate attributeName="y" values="124;100;120;106;124" dur="2.1s" repeatCount="indefinite"/></rect>
  </g>

  <!-- Flowing Dual Cyber Sine Waves -->
  <g clip-path="url(#waveClip)">
    <!-- Primary Wave (Electric Cyan) -->
    <path d="M-300 115 Q-225 65 -150 115 T0 115 T150 115 T300 115 T450 115 T600 115 T750 115 T900 115 T1050 115 T1200 115"
          fill="none" stroke="url(#cyberWave1)" stroke-width="2.6" filter="url(#glowWave)">
      <animateTransform attributeName="transform" type="translate" from="0 0" to="-300 0" dur="4s" repeatCount="indefinite"/>
    </path>
    <!-- Secondary Counter Wave (Quantum Magenta) -->
    <path d="M-300 115 Q-225 165 -150 115 T0 115 T150 115 T300 115 T450 115 T600 115 T750 115 T900 115 T1050 115 T1200 115"
          fill="none" stroke="#d946ef" stroke-width="1.8" opacity="0.65" filter="url(#glowWave)">
      <animateTransform attributeName="transform" type="translate" from="-300 0" to="0 0" dur="5.5s" repeatCount="indefinite"/>
    </path>

    <!-- Floating Cyber Motes -->
    <circle cx="120" cy="55" r="1.5" fill="#00f0ff" opacity="0.8">
      <animate attributeName="opacity" values="0.2;0.9;0.2" dur="3s" repeatCount="indefinite"/>
      <animate attributeName="cy" values="58;50;58" dur="3s" repeatCount="indefinite"/>
    </circle>
    <circle cx="280" cy="155" r="1.6" fill="#ff73fa" opacity="0.7">
      <animate attributeName="opacity" values="0.2;0.9;0.2" dur="3.6s" begin="0.8s" repeatCount="indefinite"/>
      <animate attributeName="cy" values="160;150;160" dur="3.6s" begin="0.8s" repeatCount="indefinite"/>
    </circle>
    <circle cx="640" cy="50" r="1.4" fill="#00ff88" opacity="0.75">
      <animate attributeName="opacity" values="0.2;0.9;0.2" dur="3.2s" begin="1.4s" repeatCount="indefinite"/>
    </circle>
    <circle cx="780" cy="150" r="1.5" fill="#00f0ff" opacity="0.7">
      <animate attributeName="opacity" values="0.2;0.9;0.2" dur="4s" begin="0.4s" repeatCount="indefinite"/>
    </circle>
  </g>

  <!-- Border & Tracer -->
  <path d="M 28 8 L 872 8 L 892 28 L 892 172 L 872 192 L 28 192 L 8 172 L 8 28 Z" fill="none" stroke="url(#frameGradWave)" stroke-width="1.8" opacity="0.95"/>
  <path d="M 28 8 L 872 8 L 892 28 L 892 172 L 872 192 L 28 192 L 8 172 L 8 28 Z" fill="none" stroke="#00f0ff" stroke-width="2.2" stroke-linecap="round" opacity="0.9" pathLength="1000" stroke-dasharray="85 915" filter="url(#glowWave)">
    <animate attributeName="stroke-dashoffset" from="0" to="-1000" dur="4.2s" repeatCount="indefinite"/>
  </path>

  <!-- Main Centered Typography -->
  <text x="450" y="98" text-anchor="middle" class="ft-title" filter="url(#glowWave)">THANKS FOR VISITING</text>
  <text x="447" y="98" text-anchor="middle" class="ft-title" fill="#00f0ff" style="animation: glitchFt 6s infinite; opacity:0;">THANKS FOR VISITING</text>
  <text x="453" y="98" text-anchor="middle" class="ft-title" fill="#d946ef" style="animation: glitchFt 6s infinite .14s; opacity:0;">THANKS FOR VISITING</text>

  <!-- Subtitle with Blinking Standby Indicator -->
  <text x="450" y="126" text-anchor="middle" class="ft-sub">
    // SYSTEM STANDBY ENGAGED &#183; RIOON7337 //
  </text>

  <!-- Bottom Terminal Status Prompt -->
  <g transform="translate(450, 152)">
    <rect x="-140" y="-10" width="280" height="18" rx="4" fill="#030b1c" stroke="#00f0ff" stroke-width="0.8" opacity="0.8"/>
    <circle cx="-126" cy="-1" r="2.5" fill="#00ff88"/>
    <text x="5" y="3" font-family="'Fira Code', monospace" font-size="9" font-weight="700" fill="#00ff88" text-anchor="middle" letter-spacing="1.5">SYS.STATUS: STANDBY MODE<tspan fill="#00f0ff" style="animation: blinkCursor 0.8s infinite;"> _</tspan></text>
  </g>

  <!-- Corner Hazard Stripes /// -->
  <g stroke="#00f0ff" stroke-width="1.2" opacity="0.4">
    <line x1="36" y1="168" x2="44" y2="176"/>
    <line x1="42" y1="168" x2="50" y2="176"/>
    <line x1="48" y1="168" x2="56" y2="176"/>
    <line x1="844" y1="168" x2="852" y2="176"/>
    <line x1="850" y1="168" x2="858" y2="176"/>
    <line x1="856" y1="168" x2="864" y2="176"/>
  </g>
</svg>'''

def main():
    # 1. Generate skills.svg
    with open("skills.svg", "w", encoding="utf-8") as f:
        f.write(generate_skills_svg())
    print("Generated skills.svg successfully.")

    # 2. Generate header.svg
    with open("header.svg", "w", encoding="utf-8") as f:
        f.write(generate_header_svg())
    print("Generated header.svg successfully.")

    # 3. Generate Social Buttons
    # Icons:
    icon_linkedin = '''<g transform="translate(6, 6)"><rect x="1.5" y="1.5" width="20" height="20" rx="3.5" fill="none" stroke="#00f0ff" stroke-width="1.6"/><circle cx="6.5" cy="6.5" r="1.5" fill="#00f0ff"/><rect x="5.5" y="9.5" width="2.2" height="8" rx="0.4" fill="#00f0ff"/><path d="M10.5 17.5v-8h2.2v1.1a3 3 0 0 1 5.2 2.1v4.8h-2.3v-4.3a1.5 1.5 0 0 0-3 0v4.3z" fill="#00f0ff"/></g>'''
    
    icon_telegram = '''<g transform="translate(6, 6)"><path d="M2.5 10.5l17.5-7.5-3 15-4.5-4-3 3-0.5-4.5 9-8.5-11 5.5z" fill="#00f0ff"/></g>'''
    
    icon_x = '''<g transform="translate(6, 6)"><path d="M17.5 3h3l-6.5 7.5L21.5 21h-6l-4.7-6.2L5.5 21h-3l7-8L2.5 3h6.2l4.2 5.6L17.5 3z" fill="#ffffff"/></g>'''
    
    icon_instagram = '''<g transform="translate(6, 6)"><rect x="2.5" y="2.5" width="18" height="18" rx="5" fill="none" stroke="#ff007f" stroke-width="1.8"/><circle cx="11.5" cy="11.5" r="4.2" fill="none" stroke="#ff007f" stroke-width="1.8"/><circle cx="16.5" cy="6.5" r="1.3" fill="#ff007f"/></g>'''
    
    icon_hackster = '''<g transform="translate(6, 6)"><path d="M4 4h4v6.5h7V4h4v15h-4v-5.5h-7V19H4V4z" fill="#00ffcc"/></g>'''
    
    icon_threads = '''<g transform="translate(6, 6)"><path d="M16.5 11c-.3-3.5-2.8-5-5.5-5-3.5 0-6 2.8-6 6.5s2.5 6.5 6 6.5c2.8 0 4.6-1.5 5.2-3.8h-2.2c-.4 1.2-1.5 1.8-3 1.8-2.2 0-3.8-1.6-3.8-4.5s1.6-4.5 3.8-4.5c1.8 0 3.2 1 3.5 2.5h2z" fill="#ffffff"/><path d="M11 10.5a1.8 1.8 0 1 0 0 3.6 1.8 1.8 0 0 0 0-3.6z" fill="#ff73fa"/></g>'''

    socials = [
        ("linkedin", "NODE.01 // LINKEDIN", "LINKEDIN", "SYNCED // 443", "#00f0ff", icon_linkedin, "0.0s"),
        ("telegram", "NODE.02 // TELEGRAM", "TELEGRAM", "SIGNAL: 100%", "#00f0ff", icon_telegram, "0.2s"),
        ("x", "NODE.03 // X-NET", "X / TWITTER", "DATALINK: ON", "#00f0ff", icon_x, "0.4s"),
        ("instagram", "NODE.04 // INSTAGRAM", "INSTAGRAM", "VISUAL: 60FPS", "#ff007f", icon_instagram, "0.6s"),
        ("hackster", "NODE.05 // HACKSTER", "HACKSTER", "IOT_CORE // ARMED", "#00ffcc", icon_hackster, "0.8s"),
        ("threads", "NODE.06 // THREADS", "THREADS", "NEURAL: LINKED", "#ff73fa", icon_threads, "1.0s"),
    ]

    for filename, node_code, label, status_text, accent, icon_svg, delay in socials:
        with open(f"{filename}.svg", "w", encoding="utf-8") as f:
            f.write(generate_social_svg(filename, node_code, label, status_text, accent, icon_svg, delay))
        print(f"Generated {filename}.svg successfully.")

    # 4. Generate footer-wave.svg
    with open("footer-wave.svg", "w", encoding="utf-8") as f:
        f.write(generate_footer_wave_svg())
    print("Generated footer-wave.svg successfully.")

if __name__ == "__main__":
    main()
