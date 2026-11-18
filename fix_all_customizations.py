import os
import re

with open(r'd:\Rioon7337\assets\namecard.svg', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update big Title from "Rioon" to "RIoon7337"
old_title = '''  <text x="190" y="230" font-family="'Segoe UI', 'Helvetica Neue', Arial, sans-serif" font-size="30" font-weight="700" fill="#ffffff" filter="url(#textGlow)">
    Rioon
    <animate attributeName="fill" values="#ffffff;#a0f0ff;#ffffff" dur="4s" repeatCount="indefinite"/>
  </text>'''

new_title = '''  <text x="190" y="230" font-family="'Segoe UI', 'Helvetica Neue', Arial, sans-serif" font-size="30" font-weight="700" fill="#ffffff" filter="url(#textGlow)">
    RIoon7337
    <animate attributeName="fill" values="#ffffff;#a0f0ff;#ffffff" dur="4s" repeatCount="indefinite"/>
  </text>'''

text = text.replace(old_title, new_title)

# 2. Adjust Verified checkmark badge to be right after "RIoon7337" (x=385)
text = text.replace('transform="translate(290, 222)"', 'transform="translate(385, 222)"')

# 3. Update GitHub social handle to "GitHub: /RIoon7337"
text = re.sub(r'GitHub: /[A-Za-z0-9_]+', 'GitHub: /RIoon7337', text)

# 4. Update Instagram to "@rei_ntobing"
text = text.replace('@lawless_derg', '@rei_ntobing')

# 5. Update About Me section
old_about = """  <!-- About Me -->
  <g transform="translate(520, 270)">
    <text x="0" y="0" font-family="'Segoe UI', 'Helvetica Neue', Arial, sans-serif" font-size="12" font-weight="700" fill="#00f0ff" letter-spacing="1.5" filter="url(#textGlow)">
      ABOUT ME
      <animate attributeName="fill" values="#00f0ff;#00ffcc;#00f0ff" dur="3s" repeatCount="indefinite"/>
    </text>
    <text x="0" y="20" font-family="'Segoe UI', 'Helvetica Neue', Arial, sans-serif" font-size="12" fill="#a0b0d0" filter="url(#textGlow)">
      <animate attributeName="fill" values="#a0b0d0;#e0f0ff;#a0b0d0" dur="4s" repeatCount="indefinite"/>
      Just a Normal Furry. Creating
    </text>
    <text x="0" y="38" font-family="'Segoe UI', 'Helvetica Neue', Arial, sans-serif" font-size="12" fill="#a0b0d0" filter="url(#textGlow)">
      <animate attributeName="fill" values="#a0b0d0;#e0f0ff;#a0b0d0" dur="4s" begin="0.5s" repeatCount="indefinite"/>
      digital realms &amp; code. | Dev |
    </text>
    <text x="0" y="56" font-family="'Segoe UI', 'Helvetica Neue', Arial, sans-serif" font-size="12" fill="#a0b0d0" filter="url(#textGlow)">
      <animate attributeName="fill" values="#a0b0d0;#e0f0ff;#a0b0d0" dur="4s" begin="1s" repeatCount="indefinite"/>
      @RIoon7337 | Living the furry life!
    </text>
  </g>"""

new_about = """  <!-- About Me -->
  <g transform="translate(520, 270)">
    <text x="0" y="0" font-family="'Segoe UI', 'Helvetica Neue', Arial, sans-serif" font-size="12" font-weight="700" fill="#00f0ff" letter-spacing="1.5" filter="url(#textGlow)">
      ABOUT ME
      <animate attributeName="fill" values="#00f0ff;#00ffcc;#00f0ff" dur="3s" repeatCount="indefinite"/>
    </text>
    <text x="0" y="20" font-family="'Segoe UI', 'Helvetica Neue', Arial, sans-serif" font-size="12" fill="#a0b0d0" filter="url(#textGlow)">
      <animate attributeName="fill" values="#a0b0d0;#e0f0ff;#a0b0d0" dur="4s" repeatCount="indefinite"/>
      Just a Normal Furry UwU
    </text>
    <text x="0" y="38" font-family="'Segoe UI', 'Helvetica Neue', Arial, sans-serif" font-size="12" fill="#a0b0d0" filter="url(#textGlow)">
      <animate attributeName="fill" values="#a0b0d0;#e0f0ff;#a0b0d0" dur="4s" begin="0.5s" repeatCount="indefinite"/>
      Furry Enthusiast &amp; Developer
    </text>
    <text x="0" y="56" font-family="'Segoe UI', 'Helvetica Neue', Arial, sans-serif" font-size="12" fill="#a0b0d0" filter="url(#textGlow)">
      <animate attributeName="fill" values="#a0b0d0;#e0f0ff;#a0b0d0" dur="4s" begin="1s" repeatCount="indefinite"/>
      Ig: @rei_ntobing | Tg: @rioon7337
    </text>
  </g>"""

text = text.replace(old_about, new_about)

# 6. Replace Nitro Avatar Border with ULTRA-FUTURISTIC CYBERNETIC SCI-FI REACTOR RING
old_nitro_start = text.find('<!-- ===== NITRO BORDER — BRIGHT & CRISP ===== -->')
old_nitro_end = text.find('<!-- Avatar image -->')

if old_nitro_start != -1 and old_nitro_end != -1:
    new_cyber_avatar_border = '''<!-- ===== CYBERNETIC SCI-FI REACTOR AVATAR BORDER ===== -->
  <!-- Outer glowing energy shield halo -->
  <g transform="translate(110, 240)">
    <circle r="73" fill="none" stroke="#00f0ff" stroke-width="12" opacity="0.3" filter="url(#nitroOuterGlow)">
      <animate attributeName="stroke" values="#00f0ff;#ff73fa;#a855f7;#00ff88;#00f0ff" dur="4s" repeatCount="indefinite"/>
    </circle>
  </g>

  <!-- Cybernetic Reticle and Rotating Reactor Ring -->
  <g transform="translate(110, 240)" filter="url(#nitroGlow)">
    <!-- Layer 1: Orbital Tech Brackets (Clockwise) -->
    <g>
      <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="6s" repeatCount="indefinite"/>
      <circle r="69" fill="none" stroke="#00f0ff" stroke-width="3.5" stroke-dasharray="35 19.5" stroke-linecap="round" opacity="0.9"/>
      <circle r="69" fill="none" stroke="#ff73fa" stroke-width="2" stroke-dasharray="10 44.5" stroke-linecap="round" opacity="0.75"/>
    </g>

    <!-- Layer 2: Fast Dual Neon Laser Arcs (Counter-Clockwise) -->
    <g>
      <animateTransform attributeName="transform" type="rotate" from="360" to="0" dur="2.5s" repeatCount="indefinite"/>
      <circle r="65" fill="none" stroke="#00e5ff" stroke-width="4.5" stroke-dasharray="50 52" stroke-linecap="round" opacity="0.95"/>
      <circle r="65" fill="none" stroke="#d946ef" stroke-width="3.5" stroke-dasharray="35 67" stroke-linecap="round" opacity="0.85"/>
      <circle r="65" fill="none" stroke="#00ff88" stroke-width="2.5" stroke-dasharray="20 82" stroke-linecap="round" opacity="0.7"/>
    </g>

    <!-- Layer 3: Orbiting Energy Sparkle / Data Nodes (Clockwise Fast) -->
    <g>
      <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="3s" repeatCount="indefinite"/>
      <circle cx="0" cy="-66" r="3.2" fill="#ffffff"/>
      <circle cx="66" cy="0" r="2.8" fill="#00ffcc"/>
      <circle cx="0" cy="66" r="3.2" fill="#ffffff"/>
      <circle cx="-66" cy="0" r="2.8" fill="#ff73fa"/>
    </g>

    <!-- Inner clean dark separator frame -->
    <circle r="61" fill="#060618" stroke="#00f0ff" stroke-width="1.8" opacity="0.9"/>
  </g>

  '''
    text = text[:old_nitro_start] + new_cyber_avatar_border + text[old_nitro_end:]

with open(r'd:\Rioon7337\assets\namecard.svg', 'w', encoding='utf-8') as f:
    f.write(text)

print("SUCCESS! Updated namecard.svg with all requested customizations.")
