import os
import re

with open(r'd:\Rioon7337\avatar_base64.txt', 'r') as f:
    avatar_b64 = f.read().strip()
with open(r'd:\Rioon7337\banner_base64.txt', 'r') as f:
    banner_b64 = f.read().strip()

with open(r'd:\Rioon7337\lawless_template.txt', 'r', encoding='utf-8') as f:
    template = f.read()

# 1. Update viewBox to 800 x 824
template = template.replace(
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 400" width="800" height="400">',
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 824" width="800" height="824">'
)

# 2. Outer frame: replace simple rect with highly futuristic multi-layered cyberpunk border
old_outer_rect = '<rect x="5" y="5" width="790" height="390" rx="18" ry="18" fill="url(#bgGrad)" stroke="#1a3a6a" stroke-width="2.5" filter="url(#cardGlow)"/>'

new_outer_border = '''  <!-- Base card background -->
  <rect x="5" y="5" width="790" height="814" rx="18" ry="18" fill="url(#bgGrad)" stroke="#0d2550" stroke-width="2" filter="url(#cardGlow)"/>

  <!-- Inner tech frame -->
  <rect x="9" y="9" width="782" height="806" rx="14" ry="14" fill="none" stroke="#00e5ff" stroke-width="0.8" opacity="0.3">
    <animate attributeName="opacity" values="0.25;0.5;0.25" dur="3s" repeatCount="indefinite"/>
  </rect>

  <!-- Animated Cyberpunk Neon Energy Border: Layer 1 (Cyan clockwise) -->
  <rect x="5" y="5" width="790" height="814" rx="18" ry="18" fill="none" stroke="#00f0ff" stroke-width="1.8" stroke-dasharray="90 230" opacity="0.85" filter="url(#neonGlow)">
    <animate attributeName="stroke-dashoffset" from="0" to="-640" dur="6s" repeatCount="indefinite"/>
  </rect>

  <!-- Animated Cyberpunk Neon Energy Border: Layer 2 (Magenta counter-clockwise) -->
  <rect x="5" y="5" width="790" height="814" rx="18" ry="18" fill="none" stroke="#d946ef" stroke-width="1.3" stroke-dasharray="60 260" opacity="0.65" filter="url(#neonGlow)">
    <animate attributeName="stroke-dashoffset" from="0" to="640" dur="8s" repeatCount="indefinite"/>
  </rect>

  <!-- Side rail tech notches (Left & Right) -->
  <g stroke="#00f0ff" stroke-width="1" opacity="0.4">
    <line x1="5" y1="180" x2="11" y2="180"/>
    <line x1="5" y1="300" x2="11" y2="300"/>
    <line x1="5" y1="450" x2="11" y2="450"/>
    <line x1="5" y1="600" x2="11" y2="600"/>
    <line x1="5" y1="720" x2="11" y2="720"/>
    <line x1="789" y1="180" x2="795" y2="180"/>
    <line x1="789" y1="300" x2="795" y2="300"/>
    <line x1="789" y1="450" x2="795" y2="450"/>
    <line x1="789" y1="600" x2="795" y2="600"/>
    <line x1="789" y1="720" x2="795" y2="720"/>
  </g>

  <!-- Top Center HUD Header Badge -->
  <g transform="translate(400, 10)">
    <rect x="-85" y="-5" width="170" height="13" rx="4" fill="#06061c" stroke="#00f0ff" stroke-width="0.9" opacity="0.9" filter="url(#neonGlow)"/>
    <circle cx="-73" cy="1.5" r="2" fill="#00ff88">
      <animate attributeName="opacity" values="1;0.3;1" dur="1.5s" repeatCount="indefinite"/>
    </circle>
    <text x="5" y="5" font-family="'Segoe UI', Arial, sans-serif" font-size="7.5" font-weight="700" fill="#00f0ff" text-anchor="middle" letter-spacing="1.5">SYS.ACTIVE // RIOON7337</text>
    <circle cx="73" cy="1.5" r="2" fill="#00ff88">
      <animate attributeName="opacity" values="1;0.3;1" dur="1.5s" repeatCount="indefinite"/>
    </circle>
  </g>'''

template = template.replace(old_outer_rect, new_outer_border)

# 3. Update bannerClip to 780w x 614h (exact aspect ratio of 394x310 GIF)
template = template.replace(
    '<clipPath id="bannerClip">\n      <rect x="10" y="10" width="780" height="190" rx="14" ry="14"/>\n    </clipPath>',
    '<clipPath id="bannerClip">\n      <rect x="10" y="10" width="780" height="614" rx="14" ry="14"/>\n    </clipPath>'
)

# 4. Update banner image tag to 780w x 614h (full 1:1 original proportion, zero cropping)
old_banner_g = '''  <!-- Banner - STATIC, no animation -->
  <g clip-path="url(#bannerClip)">
    <rect x="10" y="10" width="780" height="190" fill="#0a0a1a"/>
    <image href="[B64]" x="10" y="10" width="780" height="190" preserveAspectRatio="xMidYMid slice"/>
  </g>'''

new_banner_g = f'''  <!-- Banner - 1:1 Full Original Aspect Ratio (394x310) -->
  <g clip-path="url(#bannerClip)">
    <rect x="10" y="10" width="780" height="614" fill="#0a0a1a"/>
    <image href="data:image/gif;base64,{banner_b64}" x="10" y="10" width="780" height="614" preserveAspectRatio="xMidYMid meet"/>
  </g>'''

template = template.replace(old_banner_g, new_banner_g)

# 5. NEW Futuristic Transition Animation right under the GIF
old_transition = '''  <!-- Banner bottom transition -->
  <rect x="10" y="190" width="780" height="12" fill="url(#bgGrad)"/>
  <line x1="10" y1="198" x2="790" y2="198" stroke="#00f0ff" stroke-width="1.5" opacity="0.6" filter="url(#neonGlow)">
    <animate attributeName="opacity" values="0.6;1;0.6" dur="2s" repeatCount="indefinite"/>
  </line>'''

new_transition = '''  <!-- ===== HIGH-TECH DYNAMIC TRANSITION BEAM UNDER GIF ===== -->
  <!-- Dark backdrop bar -->
  <rect x="10" y="612" width="780" height="14" fill="#080824"/>
  <rect x="10" y="612" width="780" height="14" fill="url(#bottomBg)" opacity="0.8"/>

  <!-- Static glowing baseline -->
  <line x1="10" y1="620" x2="790" y2="620" stroke="#00e5ff" stroke-width="1.2" opacity="0.5" filter="url(#neonGlow)"/>

  <!-- Fast-moving pulse stream (Cyan, traveling right) -->
  <line x1="10" y1="619" x2="790" y2="619" stroke="#00f0ff" stroke-width="2" stroke-dasharray="30 70" opacity="0.9" filter="url(#neonGlow)">
    <animate attributeName="stroke-dashoffset" from="0" to="-100" dur="1s" repeatCount="indefinite"/>
  </line>

  <!-- Counter-moving pulse stream (Pink/Magenta, traveling left) -->
  <line x1="10" y1="621" x2="790" y2="621" stroke="#ff73fa" stroke-width="1.6" stroke-dasharray="20 60" opacity="0.8" filter="url(#neonGlow)">
    <animate attributeName="stroke-dashoffset" from="0" to="80" dur="1.4s" repeatCount="indefinite"/>
  </line>

  <!-- Laser particle runner 1 (White laser racing across) -->
  <circle cy="620" r="3" fill="#ffffff" filter="url(#neonGlow)">
    <animate attributeName="cx" values="20;780;20" dur="3.2s" repeatCount="indefinite"/>
  </circle>

  <!-- Laser particle runner 2 (Neon pink laser runner) -->
  <circle cy="620" r="2.5" fill="#ff73fa" filter="url(#neonGlow)">
    <animate attributeName="cx" values="780;20;780" dur="2.5s" repeatCount="indefinite"/>
  </circle>

  <!-- Tech telemetry chevrons (Left of center) -->
  <path d="M 330 617 L 335 620 L 330 623 M 342 617 L 347 620 L 342 623 M 354 617 L 359 620 L 354 623 M 366 617 L 371 620 L 366 623" fill="none" stroke="#00f0ff" stroke-width="1.2" opacity="0.7">
    <animate attributeName="opacity" values="0.4;0.9;0.4" dur="2s" repeatCount="indefinite"/>
  </path>

  <!-- Tech telemetry chevrons (Right of center) -->
  <path d="M 470 617 L 465 620 L 470 623 M 458 617 L 453 620 L 458 623 M 446 617 L 441 620 L 446 623 M 434 617 L 429 620 L 434 623" fill="none" stroke="#00f0ff" stroke-width="1.2" opacity="0.7">
    <animate attributeName="opacity" values="0.4;0.9;0.4" dur="2s" repeatCount="indefinite"/>
  </path>

  <!-- Center HUD Data Core Badge -->
  <g transform="translate(400, 620)">
    <rect x="-30" y="-8" width="60" height="16" rx="4" fill="#040416" stroke="#00f0ff" stroke-width="1.2" filter="url(#neonGlow)"/>
    <polygon points="0,-4 5,0 0,4 -5,0" fill="#00ffcc">
      <animate attributeName="fill" values="#00ffcc;#00f0ff;#ff73fa;#00ffcc" dur="3s" repeatCount="indefinite"/>
    </polygon>
    <circle cx="-18" cy="0" r="1.5" fill="#00f0ff"/>
    <circle cx="18" cy="0" r="1.5" fill="#00f0ff"/>
  </g>'''

template = template.replace(old_transition, new_transition)

# 6. Extract bottom HUD content and customize
bottom_start = '  <!-- ===== BOTTOM BOX — FUTURISTIC HUD ANIMATION ===== -->'
bottom_end = '  <!-- Corner accents -->'

idx_start = template.find(bottom_start)
idx_end = template.find(bottom_end)

if idx_start == -1 or idx_end == -1:
    raise ValueError("Could not find bottom box markers")

bottom_content = template[idx_start:idx_end]

# 7. Apply avatar image replacement inside bottom_content
avatar_tag = f'<image href="data:image/jpeg;base64,{avatar_b64}" x="50" y="180" width="120" height="120" clip-path="url(#avatarClip)" preserveAspectRatio="xMidYMid slice"/>'
bottom_content = re.sub(r'<image href="\[B64\]"[^>]*/>', avatar_tag, bottom_content)

# 8. Replace Username and Verified checkmark
bottom_content = bottom_content.replace('LawlessDragon\n', 'Rioon\n')
bottom_content = bottom_content.replace('transform="translate(425, 222)"', 'transform="translate(290, 222)"')

# 9. Replace Social handles:
# Slot 1: GitHub /RIoon7337
bottom_content = bottom_content.replace('GitHub: /LawlessDragon', 'GitHub: /RIoon7337')

# Slot 2: Replace X/Twitter with Telegram (@rioon7337)
old_x = '''  <!-- X/Twitter -->
  <g transform="translate(190, 308)">
    <g transform="translate(0, 0)">
      <circle cx="11" cy="11" r="11" fill="#0a0a1a" stroke="#00e5ff" stroke-width="1.5">
        <animate attributeName="stroke-opacity" values="1;0.4;1" dur="3s" repeatCount="indefinite"/>
      </circle>
      <path d="M6.5 6.5 L15.5 15.5 M15.5 6.5 L6.5 15.5" stroke="#00e5ff" stroke-width="2.2" stroke-linecap="round"/>
    </g>
    <text x="30" y="15" font-family="'Segoe UI', 'Helvetica Neue', Arial, sans-serif" font-size="14" fill="#c0d0f0" filter="url(#textGlow)">
      <animate attributeName="fill" values="#c0d0f0;#ffffff;#c0d0f0" dur="3.5s" repeatCount="indefinite"/>
      @BlueLawless
    </text>
  </g>'''

new_telegram = '''  <!-- Telegram -->
  <g transform="translate(190, 308)">
    <g transform="translate(0, 0)">
      <circle cx="11" cy="11" r="11" fill="#0a0a1a" stroke="#00e5ff" stroke-width="1.5">
        <animate attributeName="stroke-opacity" values="1;0.4;1" dur="3s" repeatCount="indefinite"/>
      </circle>
      <!-- Telegram paper plane icon -->
      <path d="M5.5 10.5 L16.5 6 L14 15.5 L10.5 12.5 L8.5 14.5 L8.8 11.5 L14 8 Z" fill="#00e5ff" opacity="0.9"/>
    </g>
    <text x="30" y="15" font-family="'Segoe UI', 'Helvetica Neue', Arial, sans-serif" font-size="14" fill="#c0d0f0" filter="url(#textGlow)">
      <animate attributeName="fill" values="#c0d0f0;#ffffff;#c0d0f0" dur="3.5s" repeatCount="indefinite"/>
      Telegram: @rioon7337
    </text>
  </g>'''

bottom_content = bottom_content.replace(old_x, new_telegram)

# Slot 3: Instagram (@rei_ntobing) with pink neon
old_ig = '''  <!-- Instagram -->
  <g transform="translate(190, 346)">
    <g transform="translate(0, 0)">
      <circle cx="11" cy="11" r="11" fill="#0a0a1a" stroke="#00f0ff" stroke-width="1.5">
        <animate attributeName="stroke-opacity" values="1;0.4;1" dur="3.5s" repeatCount="indefinite"/>
      </circle>
      <rect x="5" y="5" width="12" height="12" rx="3.5" ry="3.5" fill="none" stroke="#00f0ff" stroke-width="1.3"/>
      <circle cx="11" cy="11" r="3" fill="none" stroke="#00f0ff" stroke-width="1.3"/>
      <circle cx="15.5" cy="6.5" r="1.2" fill="#00f0ff"/>
    </g>
    <text x="30" y="15" font-family="'Segoe UI', 'Helvetica Neue', Arial, sans-serif" font-size="14" fill="#c0d0f0" filter="url(#textGlow)">
      <animate attributeName="fill" values="#c0d0f0;#ffffff;#c0d0f0" dur="4s" repeatCount="indefinite"/>
      @lawless_derg
    </text>
  </g>'''

new_ig = '''  <!-- Instagram -->
  <g transform="translate(190, 346)">
    <g transform="translate(0, 0)">
      <circle cx="11" cy="11" r="11" fill="#0a0a1a" stroke="#ff73fa" stroke-width="1.5">
        <animate attributeName="stroke-opacity" values="1;0.4;1" dur="3.5s" repeatCount="indefinite"/>
      </circle>
      <rect x="5" y="5" width="12" height="12" rx="3.5" ry="3.5" fill="none" stroke="#ff73fa" stroke-width="1.3"/>
      <circle cx="11" cy="11" r="3" fill="none" stroke="#ff73fa" stroke-width="1.3"/>
      <circle cx="15.5" cy="6.5" r="1.2" fill="#ff73fa"/>
    </g>
    <text x="30" y="15" font-family="'Segoe UI', 'Helvetica Neue', Arial, sans-serif" font-size="14" fill="#c0d0f0" filter="url(#textGlow)">
      <animate attributeName="fill" values="#c0d0f0;#ffffff;#c0d0f0" dur="4s" repeatCount="indefinite"/>
      Instagram: @rei_ntobing
    </text>
  </g>'''

bottom_content = bottom_content.replace(old_ig, new_ig)

# 10. Replace About Me
old_about = """      Code-slayer. Dragon-tamer. Creating
    </text>
    <text x="0" y="38" font-family="'Segoe UI', 'Helvetica Neue', Arial, sans-serif" font-size="12" fill="#a0b0d0" filter="url(#textGlow)">
      <animate attributeName="fill" values="#a0b0d0;#e0f0ff;#a0b0d0" dur="4s" begin="0.5s" repeatCount="indefinite"/>
      digital realms. | Dev | Designer |
    </text>
    <text x="0" y="56" font-family="'Segoe UI', 'Helvetica Neue', Arial, sans-serif" font-size="12" fill="#a0b0d0" filter="url(#textGlow)">
      <animate attributeName="fill" values="#a0b0d0;#e0f0ff;#a0b0d0" dur="4s" begin="1s" repeatCount="indefinite"/>
      @BlueLawless | Living the lawless life!"""

new_about = """      Just a Normal Furry. Creating
    </text>
    <text x="0" y="38" font-family="'Segoe UI', 'Helvetica Neue', Arial, sans-serif" font-size="12" fill="#a0b0d0" filter="url(#textGlow)">
      <animate attributeName="fill" values="#a0b0d0;#e0f0ff;#a0b0d0" dur="4s" begin="0.5s" repeatCount="indefinite"/>
      digital realms &amp; code. | Dev |
    </text>
    <text x="0" y="56" font-family="'Segoe UI', 'Helvetica Neue', Arial, sans-serif" font-size="12" fill="#a0b0d0" filter="url(#textGlow)">
      <animate attributeName="fill" values="#a0b0d0;#e0f0ff;#a0b0d0" dur="4s" begin="1s" repeatCount="indefinite"/>
      @RIoon7337 | Living the furry life!"""

bottom_content = bottom_content.replace(old_about, new_about)

# 11. Replace Tech stack
bottom_content = bottom_content.replace('>REACT<', '>PYTHON<')
bottom_content = bottom_content.replace('>NODE<', '>C++<')
bottom_content = bottom_content.replace('>UI/UX<', '>FURRY<')

# Wrap bottom_content in <g transform="translate(0, 424)">
wrapped_bottom = f'<g transform="translate(0, 424)">\n{bottom_content}\n  </g>\n\n'

# 12. Heavy Multi-Segment Cyberpunk Corner Accents
new_corner_accents = '''  <!-- ===== HEAVY MULTI-SEGMENT CYBERPUNK CORNER BRACKETS ===== -->
  <!-- Top-Left Corner -->
  <g opacity="0.85" filter="url(#neonGlow)">
    <path d="M 12 50 L 12 22 L 22 12 L 50 12" fill="none" stroke="#00f0ff" stroke-width="2.5" stroke-linecap="round"/>
    <path d="M 18 42 L 18 26 L 26 18 L 42 18" fill="none" stroke="#d946ef" stroke-width="1.2" stroke-linecap="round" opacity="0.7"/>
    <circle cx="28" cy="28" r="2.2" fill="#00ffcc"/>
    <rect x="56" y="10" width="10" height="2" fill="#00f0ff"/>
    <rect x="10" y="56" width="2" height="10" fill="#00f0ff"/>
  </g>

  <!-- Top-Right Corner -->
  <g opacity="0.85" filter="url(#neonGlow)">
    <path d="M 788 50 L 788 22 L 778 12 L 750 12" fill="none" stroke="#00f0ff" stroke-width="2.5" stroke-linecap="round"/>
    <path d="M 782 42 L 782 26 L 774 18 L 758 18" fill="none" stroke="#d946ef" stroke-width="1.2" stroke-linecap="round" opacity="0.7"/>
    <circle cx="772" cy="28" r="2.2" fill="#00ffcc"/>
    <rect x="734" y="10" width="10" height="2" fill="#00f0ff"/>
    <rect x="788" y="56" width="2" height="10" fill="#00f0ff"/>
  </g>

  <!-- Bottom-Left Corner -->
  <g opacity="0.85" filter="url(#neonGlow)">
    <path d="M 12 774 L 12 802 L 22 812 L 50 812" fill="none" stroke="#00f0ff" stroke-width="2.5" stroke-linecap="round"/>
    <path d="M 18 782 L 18 798 L 26 806 L 42 806" fill="none" stroke="#d946ef" stroke-width="1.2" stroke-linecap="round" opacity="0.7"/>
    <circle cx="28" cy="796" r="2.2" fill="#00ffcc"/>
    <rect x="56" y="812" width="10" height="2" fill="#00f0ff"/>
    <rect x="10" y="758" width="2" height="10" fill="#00f0ff"/>
  </g>

  <!-- Bottom-Right Corner -->
  <g opacity="0.85" filter="url(#neonGlow)">
    <path d="M 788 774 L 788 802 L 778 812 L 750 812" fill="none" stroke="#00f0ff" stroke-width="2.5" stroke-linecap="round"/>
    <path d="M 782 782 L 782 798 L 774 806 L 758 806" fill="none" stroke="#d946ef" stroke-width="1.2" stroke-linecap="round" opacity="0.7"/>
    <circle cx="772" cy="796" r="2.2" fill="#00ffcc"/>
    <rect x="734" y="812" width="10" height="2" fill="#00f0ff"/>
    <rect x="788" y="758" width="2" height="10" fill="#00f0ff"/>
  </g>
</svg>'''

# Reassemble template
final_svg = template[:idx_start] + wrapped_bottom + new_corner_accents

# Write out the final SVG
with open(r'd:\Rioon7337\assets\namecard.svg', 'w', encoding='utf-8') as f:
    f.write(final_svg)

size = os.path.getsize(r'd:\Rioon7337\assets\namecard.svg')
print(f'SUCCESS! namecard.svg size: {size} bytes ({size/1024/1024:.2f} MB)')
