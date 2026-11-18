with open(r'd:\Rioon7337\assets\namecard.svg', 'r', encoding='utf-8') as f:
    text = f.read()

start_marker = '<!-- ===== SILVER WOLF LVL.999 QUANTUM CYBER-HACK ATTACK AVATAR BORDER ===== -->'
end_marker = '<!-- Avatar image -->'

start_idx = text.find(start_marker)
end_idx = text.find(end_marker)

if start_idx == -1 or end_idx == -1:
    raise ValueError(f"Markers not found! start: {start_idx}, end: {end_idx}")

glitch_avatar_border = '''<!-- ===== CYBER GLITCH & CHROMATIC ABERRATION JITTER AVATAR BORDER ===== -->
  <!-- Glitch & Chromatic Aberration Jitter System (ZERO ROTATION) -->
  <g transform="translate(110, 240)">
    <!-- Red / Magenta Channel Ghost Displace (Jittery Twitch) -->
    <g>
      <animateTransform attributeName="transform" type="translate" values="0,0; -4,1; 3,-2; 0,0; -3,0; 5,-1; 0,0; 2,1; 0,0" dur="1.2s" calcMode="discrete" repeatCount="indefinite"/>
      <circle r="63.5" fill="none" stroke="#ff0055" stroke-width="2.5" opacity="0.8" stroke-dasharray="30 10 50 15 20 8">
        <animate attributeName="opacity" values="0.8;0.2;0.9;0.4;1;0.3;0.8" dur="0.9s" calcMode="discrete" repeatCount="indefinite"/>
      </circle>
    </g>

    <!-- Cyan / Blue Channel Ghost Displace (Opposite Jitter Twitch) -->
    <g>
      <animateTransform attributeName="transform" type="translate" values="0,0; 4,-1; -3,2; 0,0; 3,1; -4,0; 0,0; -2,-1; 0,0" dur="1.2s" calcMode="discrete" repeatCount="indefinite"/>
      <circle r="63.5" fill="none" stroke="#00f0ff" stroke-width="2.5" opacity="0.85" stroke-dasharray="40 15 25 10 35 12">
        <animate attributeName="opacity" values="0.85;0.3;1;0.2;0.9;0.4;0.85" dur="0.8s" calcMode="discrete" repeatCount="indefinite"/>
      </circle>
    </g>

    <!-- Green Channel Jitter Trace -->
    <g>
      <animateTransform attributeName="transform" type="translate" values="0,0; 0,0; -2,2; 0,0; 0,0; 3,-1; 0,0" dur="1.6s" calcMode="discrete" repeatCount="indefinite"/>
      <circle r="64" fill="none" stroke="#00ff88" stroke-width="1.2" opacity="0.6" stroke-dasharray="15 45 30 20">
        <animate attributeName="opacity" values="0.6;0;0.7;0;0.8;0" dur="1.1s" calcMode="discrete" repeatCount="indefinite"/>
      </circle>
    </g>

    <!-- Main Solid Glitch Frame with Chromatic Shifting Glow -->
    <circle r="62" fill="none" stroke="#ffffff" stroke-width="2" opacity="0.9" filter="url(#neonGlow)">
      <animate attributeName="stroke" values="#ffffff;#00f0ff;#ff0055;#ffffff" dur="1.5s" calcMode="discrete" repeatCount="indefinite"/>
      <animate attributeName="stroke-width" values="2;3.2;1.8;2" dur="0.7s" calcMode="discrete" repeatCount="indefinite"/>
    </circle>

    <!-- Glitch Corner Target Brackets (Discrete Snapping) -->
    <g stroke="#00f0ff" stroke-width="2" fill="none">
      <animateTransform attributeName="transform" type="translate" values="0,0; 2,-1; -1,2; 0,0; -3,0; 0,0" dur="1.4s" calcMode="discrete" repeatCount="indefinite"/>
      <!-- Top-Left -->
      <path d="M -45 -54 L -54 -54 L -54 -45"/>
      <!-- Top-Right -->
      <path d="M 45 -54 L 54 -54 L 54 -45"/>
      <!-- Bottom-Left -->
      <path d="M -45 54 L -54 54 L -54 45"/>
      <!-- Bottom-Right -->
      <path d="M 45 54 L 54 54 L 54 45"/>
    </g>

    <!-- Cyber Glitch Warning Badge: SYS.GLITCH -->
    <g transform="translate(0, -78)">
      <animateTransform attributeName="transform" type="translate" values="0,-78; -3,-77; 2,-79; 0,-78; 4,-78; 0,-78" dur="1.1s" calcMode="discrete" repeatCount="indefinite"/>
      <rect x="-35" y="-7" width="70" height="14" rx="2" fill="#040416" stroke="#ff0055" stroke-width="1.2">
        <animate attributeName="stroke" values="#ff0055;#00f0ff;#ff0055" dur="0.8s" calcMode="discrete" repeatCount="indefinite"/>
      </rect>
      <text x="0" y="3.5" font-family="'Courier New', monospace, Arial" font-size="7.5" font-weight="900" fill="#00f0ff" text-anchor="middle" letter-spacing="1">
        SYS.GLITCH
        <animate attributeName="fill" values="#00f0ff;#ffffff;#ff0055;#00f0ff" dur="0.8s" calcMode="discrete" repeatCount="indefinite"/>
      </text>
    </g>

    <!-- Glitched Data Artifact Packets (Popping around perimeter) -->
    <g>
      <!-- Block 1 (Top-Right) -->
      <rect x="58" y="-30" width="8" height="4" fill="#00f0ff">
        <animate attributeName="opacity" values="0;0.9;0;0;0.8;0" dur="0.9s" calcMode="discrete" repeatCount="indefinite"/>
        <animate attributeName="x" values="58;64;54;58" dur="0.9s" calcMode="discrete" repeatCount="indefinite"/>
      </rect>
      <!-- Block 2 (Left) -->
      <rect x="-70" y="10" width="10" height="3" fill="#ff0055">
        <animate attributeName="opacity" values="0;0;0.9;0;0.7;0" dur="1.1s" calcMode="discrete" repeatCount="indefinite"/>
        <animate attributeName="x" values="-70;-76;-66;-70" dur="1.1s" calcMode="discrete" repeatCount="indefinite"/>
      </rect>
      <!-- Block 3 (Bottom-Right) -->
      <rect x="45" y="48" width="6" height="5" fill="#00ff88">
        <animate attributeName="opacity" values="0.8;0;0.9;0;0;0.8" dur="1.3s" calcMode="discrete" repeatCount="indefinite"/>
      </rect>
      <!-- Block 4 (Top-Left) -->
      <rect x="-55" y="-45" width="7" height="3" fill="#ffffff">
        <animate attributeName="opacity" values="0;0.8;0;0.9;0;0" dur="1s" calcMode="discrete" repeatCount="indefinite"/>
      </rect>
    </g>

    <!-- Horizontal Scanline Slice Tear Across Avatar -->
    <rect x="-62" y="-18" width="124" height="6" fill="#00f0ff" opacity="0">
      <animate attributeName="opacity" values="0;0.45;0;0;0.6;0" dur="1.4s" calcMode="discrete" repeatCount="indefinite"/>
      <animate attributeName="x" values="-62;-56;-68;-62" dur="1.4s" calcMode="discrete" repeatCount="indefinite"/>
    </rect>
    <rect x="-62" y="16" width="124" height="8" fill="#ff0055" opacity="0">
      <animate attributeName="opacity" values="0;0;0.5;0;0.4;0" dur="1.7s" calcMode="discrete" repeatCount="indefinite"/>
      <animate attributeName="x" values="-62;-70;-54;-62" dur="1.7s" calcMode="discrete" repeatCount="indefinite"/>
    </rect>

    <!-- Inner Dark Base Frame -->
    <circle r="60.5" fill="#050616" stroke="#00f0ff" stroke-width="1.5" opacity="0.9"/>
  </g>

  '''

text = text[:start_idx] + glitch_avatar_border + text[end_idx:]

with open(r'd:\Rioon7337\assets\namecard.svg', 'w', encoding='utf-8') as f:
    f.write(text)

print("SUCCESS! Applied pure Cyber Glitch & Chromatic Aberration animation (0% rotation).")
