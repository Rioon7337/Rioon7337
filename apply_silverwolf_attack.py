import math
import re

with open(r'd:\Rioon7337\assets\namecard.svg', 'r', encoding='utf-8') as f:
    text = f.read()

# Generate 8 Quantum Pixel cubes (Silver Wolf's voxel data cubes)
cubes_svg = []
colors = ['#ff007f', '#00f0ff', '#a855f7', '#00ff88', '#ff2a85', '#00e5ff', '#ffd700', '#00ffcc']
for i in range(8):
    angle_deg = i * 45
    color = colors[i]
    delay = round(i * 0.2, 2)
    cubes_svg.append(f'''        <!-- Quantum Pixel Cube {i+1} ({angle_deg}°) -->
        <g transform="rotate({angle_deg}) translate(0, -74)">
          <rect x="-3" y="-3" width="6" height="6" rx="1" fill="{color}" stroke="#ffffff" stroke-width="0.8" filter="url(#neonGlow)">
            <animate attributeName="opacity" values="0.4;1;0.4" dur="1.2s" begin="{delay}s" repeatCount="indefinite"/>
          </rect>
          <rect x="-1" y="-5" width="4" height="2" fill="{color}" opacity="0.6">
            <animate attributeName="opacity" values="0;0.8;0" dur="0.8s" begin="{delay + 0.1}s" repeatCount="indefinite"/>
          </rect>
        </g>''')

cubes_str = "\n".join(cubes_svg)

silverwolf_attack_border = f'''<!-- ===== SILVER WOLF LVL.999 QUANTUM CYBER-HACK ATTACK AVATAR BORDER ===== -->
  <!-- Quantum Glitch Distortion Aura (Pink/Magenta & Cyan Energy) -->
  <g transform="translate(110, 240)">
    <circle r="75" fill="none" stroke="#ff007f" stroke-width="14" opacity="0.3" filter="url(#nitroOuterGlow)">
      <animate attributeName="stroke" values="#ff007f;#00f0ff;#a855f7;#00ff88;#ff007f" dur="2.4s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.25;0.55;0.25" dur="1.2s" repeatCount="indefinite"/>
    </circle>
  </g>

  <!-- Quantum Ultimate Shockwave 1 ("User is Banned" Impact Wave) -->
  <g transform="translate(110, 240)">
    <circle r="60" fill="none" stroke="#ff007f" stroke-width="2.5" opacity="0.8" filter="url(#neonGlow)">
      <animate attributeName="r" values="60;90;60" dur="2s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.9;0;0.9" dur="2s" repeatCount="indefinite"/>
      <animate attributeName="stroke" values="#ff007f;#00f0ff;#ff007f" dur="2s" repeatCount="indefinite"/>
    </circle>
  </g>

  <!-- Quantum Ultimate Shockwave 2 (Secondary Digital Glitch Pulse) -->
  <g transform="translate(110, 240)">
    <circle r="60" fill="none" stroke="#00f0ff" stroke-width="2" opacity="0.8" filter="url(#neonGlow)">
      <animate attributeName="r" values="60;90;60" dur="2s" begin="1s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.9;0;0.9" dur="2s" begin="1s" repeatCount="indefinite"/>
      <animate attributeName="stroke" values="#00f0ff;#a855f7;#00f0ff" dur="2s" begin="1s" repeatCount="indefinite"/>
    </circle>
  </g>

  <!-- Main Quantum Hacking Array & Pixel Ring -->
  <g transform="translate(110, 240)" filter="url(#nitroGlow)">
    <!-- Layer 1: 8 Orbiting Quantum Pixel Cubes / Data Voxels (Clockwise) -->
    <g>
      <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="5s" repeatCount="indefinite"/>
{cubes_str}
    </g>

    <!-- Layer 2: Aether Editing Code Stream Ring (Counter-Clockwise Pixel Dash) -->
    <g>
      <animateTransform attributeName="transform" type="rotate" from="360" to="0" dur="3s" repeatCount="indefinite"/>
      <circle r="67" fill="none" stroke="#ff007f" stroke-width="3" stroke-dasharray="16 8 8 8 24 8" stroke-linecap="square" opacity="0.9"/>
      <circle r="67" fill="none" stroke="#00f0ff" stroke-width="2" stroke-dasharray="8 12 16 12" stroke-linecap="square" opacity="0.85"/>
      <circle r="67" fill="none" stroke="#00ff88" stroke-width="1.5" stroke-dasharray="4 20" stroke-linecap="square" opacity="0.9"/>
    </g>

    <!-- Layer 3: High-speed Quantum Laser Sparks (Clockwise Fast) -->
    <g>
      <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="1.5s" repeatCount="indefinite"/>
      <circle r="67" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-dasharray="14 100" stroke-linecap="square" opacity="1"/>
      <rect x="-2" y="-69" width="4" height="4" fill="#00ffcc"/>
      <rect x="-2" y="65" width="4" height="4" fill="#ff73fa"/>
    </g>

    <!-- Layer 4: 4 Pixelated Cyberpunk Targeting Brackets (at 45°, 135°, 225°, 315°) -->
    <g>
      <!-- Top-Right Reticle Bracket (45°) -->
      <path d="M 40 -48 L 48 -48 L 48 -40" fill="none" stroke="#00f0ff" stroke-width="2" stroke-linecap="square"/>
      <!-- Bottom-Right Reticle Bracket (135°) -->
      <path d="M 40 48 L 48 48 L 48 40" fill="none" stroke="#ff007f" stroke-width="2" stroke-linecap="square"/>
      <!-- Bottom-Left Reticle Bracket (225°) -->
      <path d="M -40 48 L -48 48 L -48 40" fill="none" stroke="#00f0ff" stroke-width="2" stroke-linecap="square"/>
      <!-- Top-Left Reticle Bracket (315°) -->
      <path d="M -40 -48 L -48 -48 L -48 -40" fill="none" stroke="#ff007f" stroke-width="2" stroke-linecap="square"/>
    </g>

    <!-- Floating "LV.999" Quantum Badge at top of the ring -->
    <g transform="translate(0, -78)">
      <rect x="-23" y="-7" width="46" height="14" rx="2" fill="#060618" stroke="#ff007f" stroke-width="1.2">
        <animate attributeName="stroke" values="#ff007f;#00f0ff;#ff007f" dur="2s" repeatCount="indefinite"/>
      </rect>
      <text x="0" y="3.5" font-family="'Courier New', monospace, Arial" font-size="8" font-weight="900" fill="#00f0ff" text-anchor="middle" letter-spacing="1">
        LV.999
        <animate attributeName="fill" values="#00f0ff;#ffffff;#ff73fa;#00f0ff" dur="2s" repeatCount="indefinite"/>
      </text>
    </g>

    <!-- Inner Pixelated Cyber-Frame -->
    <circle r="62" fill="none" stroke="#ff007f" stroke-width="2.5" opacity="0.95"/>
    <circle r="60.5" fill="#050616" stroke="#00f0ff" stroke-width="1.5"/>
  </g>

  '''

# Find the start of avatar border comment
start_idx = text.find('<!-- ===== ')
for marker in [
    '<!-- ===== DOTTORE BOSS ATTACK ANIMATION AVATAR BORDER ===== -->',
    '<!-- ===== NEURALINK / NEURON LINK SYNAPSE AVATAR BORDER ===== -->',
    '<!-- ===== CYBERNETIC SCI-FI REACTOR AVATAR BORDER ===== -->',
    '<!-- ===== NITRO BORDER'
]:
    pos = text.find(marker)
    if pos != -1:
        start_idx = pos
        break

end_idx = text.find('<!-- Avatar image -->')

if start_idx == -1 or end_idx == -1:
    raise ValueError(f"Could not find avatar border markers! start: {start_idx}, end: {end_idx}")

text = text[:start_idx] + silverwolf_attack_border + text[end_idx:]

with open(r'd:\Rioon7337\assets\namecard.svg', 'w', encoding='utf-8') as f:
    f.write(text)

print("SUCCESS! Applied Silver Wolf Level 999 Quantum Attack animation.")
