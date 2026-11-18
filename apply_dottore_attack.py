import math
import re

with open(r'd:\Rioon7337\assets\namecard.svg', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update big title from RIoon7337 to Rioon7337
text = text.replace('RIoon7337', 'Rioon7337')

# 2. Generate 6 Dottore floating mechanical scalpel / acoustic needles
needles_svg = []
for i in range(6):
    angle_deg = i * 60
    needles_svg.append(f'''        <!-- Dottore Floating Blade Drone {i+1} ({angle_deg}°) -->
        <g transform="rotate({angle_deg}) translate(0, -73)">
          <polygon points="0,-10 3.5,2 0,6 -3.5,2" fill="#081426" stroke="#00f0ff" stroke-width="1.2" filter="url(#neonGlow)">
            <animate attributeName="stroke" values="#00f0ff;#8b5cf6;#00ffcc;#00f0ff" dur="3s" begin="{i*0.5}s" repeatCount="indefinite"/>
          </polygon>
          <circle cx="0" cy="0" r="1.5" fill="#ffffff" filter="url(#neonGlow)"/>
          <line x1="0" y1="-10" x2="0" y2="-15" stroke="#00f0ff" stroke-width="1.5" stroke-linecap="round">
            <animate attributeName="opacity" values="0.3;1;0.3" dur="1.5s" begin="{i*0.3}s" repeatCount="indefinite"/>
          </line>
        </g>''')

needles_str = "\n".join(needles_svg)

# 3. Dottore Boss Attack animation (Acoustic Shockwave Resonance + Floating Blades + Delusion Reticle)
dottore_attack_border = f'''<!-- ===== DOTTORE BOSS ATTACK ANIMATION AVATAR BORDER ===== -->
  <!-- Dottore Acoustic Shockwave Resonance 1 (Expanding Sonic Wave) -->
  <g transform="translate(110, 240)">
    <circle r="60" fill="none" stroke="#00f0ff" stroke-width="2.5" opacity="0.8" filter="url(#neonGlow)">
      <animate attributeName="r" values="60;88;60" dur="2.4s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.85;0;0.85" dur="2.4s" repeatCount="indefinite"/>
      <animate attributeName="stroke" values="#00f0ff;#8b5cf6;#00f0ff" dur="2.4s" repeatCount="indefinite"/>
    </circle>
  </g>

  <!-- Dottore Acoustic Shockwave Resonance 2 (Delayed Secondary Pulse) -->
  <g transform="translate(110, 240)">
    <circle r="60" fill="none" stroke="#a855f7" stroke-width="2" opacity="0.8" filter="url(#neonGlow)">
      <animate attributeName="r" values="60;88;60" dur="2.4s" begin="1.2s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.85;0;0.85" dur="2.4s" begin="1.2s" repeatCount="indefinite"/>
      <animate attributeName="stroke" values="#a855f7;#00ffcc;#a855f7" dur="2.4s" begin="1.2s" repeatCount="indefinite"/>
    </circle>
  </g>

  <!-- Fatui Delusion Mist Aura (Cold Cryo & Delusion Glow) -->
  <g transform="translate(110, 240)">
    <circle r="75" fill="none" stroke="#00f0ff" stroke-width="12" opacity="0.25" filter="url(#nitroOuterGlow)">
      <animate attributeName="stroke" values="#00f0ff;#7c3aed;#06b6d4;#d946ef;#00f0ff" dur="4s" repeatCount="indefinite"/>
    </circle>
  </g>

  <!-- Rotating Dottore Mechanical Blade Array & Reticle -->
  <g transform="translate(110, 240)" filter="url(#nitroGlow)">
    <!-- Layer 1: 6 Orbiting Dottore Surgical Scalpel / Acoustic Needles (Clockwise) -->
    <g>
      <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="7s" repeatCount="indefinite"/>
{needles_str}
    </g>

    <!-- Layer 2: Fast Counter-Rotating Mechanical Reticle / Gear Ring -->
    <g>
      <animateTransform attributeName="transform" type="rotate" from="360" to="0" dur="4s" repeatCount="indefinite"/>
      <circle r="66" fill="none" stroke="#00e5ff" stroke-width="3" stroke-dasharray="14 14" stroke-linecap="butt" opacity="0.85"/>
      <circle r="66" fill="none" stroke="#a855f7" stroke-width="1.8" stroke-dasharray="7 21" stroke-linecap="round" opacity="0.9"/>
    </g>

    <!-- Layer 3: High-speed Cryo Laser Tracer Sparks (Clockwise Fast) -->
    <g>
      <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="2s" repeatCount="indefinite"/>
      <circle r="66" fill="none" stroke="#ffffff" stroke-width="2.2" stroke-dasharray="12 90" stroke-linecap="round" opacity="1"/>
      <circle cx="0" cy="-66" r="2.5" fill="#00ffcc"/>
      <circle cx="0" cy="66" r="2.5" fill="#00ffcc"/>
    </g>

    <!-- Layer 4: 4 Fatui Inward Targeting Crosshair Blades (0°, 90°, 180°, 270°) -->
    <g>
      <polygon points="0,-63 3.5,-70 -3.5,-70" fill="#00ffcc" opacity="0.9"/>
      <polygon points="63,0 70,3.5 70,-3.5" fill="#00ffcc" opacity="0.9"/>
      <polygon points="0,63 3.5,70 -3.5,70" fill="#00ffcc" opacity="0.9"/>
      <polygon points="-63,0 -70,3.5 -70,-3.5" fill="#00ffcc" opacity="0.9"/>
    </g>

    <!-- Inner Cold Snezhnayan Cryo Core Frame -->
    <circle r="62" fill="none" stroke="#00f0ff" stroke-width="2.5" opacity="0.95"/>
    <circle r="60.5" fill="#040916" stroke="#1e3a5f" stroke-width="1.5"/>
  </g>

  '''

# Replace avatar border section
start_idx = text.find('<!-- ===== ')
# Search specifically for any avatar border header
for marker in [
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

text = text[:start_idx] + dottore_attack_border + text[end_idx:]

with open(r'd:\Rioon7337\assets\namecard.svg', 'w', encoding='utf-8') as f:
    f.write(text)

print("SUCCESS! Applied Dottore boss attack animation and updated username to Rioon7337.")
