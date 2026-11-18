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

# 2. Update card outer background height from 390 to 814
template = template.replace(
    '<rect x="5" y="5" width="790" height="390" rx="18" ry="18" fill="url(#bgGrad)" stroke="#1a3a6a" stroke-width="2.5" filter="url(#cardGlow)"/>',
    '<rect x="5" y="5" width="790" height="814" rx="18" ry="18" fill="url(#bgGrad)" stroke="#1a3a6a" stroke-width="2.5" filter="url(#cardGlow)"/>'
)

# 3. Update bannerClip to 780w x 614h (exact aspect ratio of 394x310 GIF)
template = template.replace(
    '<clipPath id="bannerClip">\n      <rect x="10" y="10" width="780" height="190" rx="14" ry="14"/>\n    </clipPath>',
    '<clipPath id="bannerClip">\n      <rect x="10" y="10" width="780" height="614" rx="14" ry="14"/>\n    </clipPath>'
)

# 4. Update banner image tag to 780w x 614h
old_banner_g = '''  <!-- Banner - STATIC, no animation -->
  <g clip-path="url(#bannerClip)">
    <rect x="10" y="10" width="780" height="190" fill="#0a0a1a"/>
    <image href="[B64]" x="10" y="10" width="780" height="190" preserveAspectRatio="xMidYMid slice"/>
  </g>'''

new_banner_g = f'''  <!-- Banner - 1:1 Full Aspect Ratio (394x310) -->
  <g clip-path="url(#bannerClip)">
    <rect x="10" y="10" width="780" height="614" fill="#0a0a1a"/>
    <image href="data:image/gif;base64,{banner_b64}" x="10" y="10" width="780" height="614" preserveAspectRatio="xMidYMid meet"/>
  </g>'''

template = template.replace(old_banner_g, new_banner_g)

# 5. Update banner transition line position (at y=614 and y=622)
old_transition = '''  <!-- Banner bottom transition -->
  <rect x="10" y="190" width="780" height="12" fill="url(#bgGrad)"/>
  <line x1="10" y1="198" x2="790" y2="198" stroke="#00f0ff" stroke-width="1.5" opacity="0.6" filter="url(#neonGlow)">
    <animate attributeName="opacity" values="0.6;1;0.6" dur="2s" repeatCount="indefinite"/>
  </line>'''

new_transition = '''  <!-- Banner bottom transition -->
  <rect x="10" y="614" width="780" height="12" fill="url(#bgGrad)"/>
  <line x1="10" y1="622" x2="790" y2="622" stroke="#00f0ff" stroke-width="1.5" opacity="0.6" filter="url(#neonGlow)">
    <animate attributeName="opacity" values="0.6;1;0.6" dur="2s" repeatCount="indefinite"/>
  </line>'''

template = template.replace(old_transition, new_transition)

# 6. Wrap all bottom HUD elements in <g transform="translate(0, 424)">
# The bottom elements start at '  <!-- ===== BOTTOM BOX — FUTURISTIC HUD ANIMATION ===== -->'
# and end right before '  <!-- Corner accents -->'
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

# 9. Replace Social handles
bottom_content = bottom_content.replace('GitHub: /LawlessDragon', 'GitHub: /Rioon7337')
bottom_content = bottom_content.replace('@BlueLawless', '@rioon7337')
bottom_content = bottom_content.replace('@lawless_derg', '@rioon7337')

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
      @rioon7337 | Living the furry life!"""

bottom_content = bottom_content.replace(old_about, new_about)

# 11. Replace Tech stack
bottom_content = bottom_content.replace('>REACT<', '>PYTHON<')
bottom_content = bottom_content.replace('>NODE<', '>C++<')
bottom_content = bottom_content.replace('>UI/UX<', '>FURRY<')

# Wrap bottom_content in <g transform="translate(0, 424)">
wrapped_bottom = f'<g transform="translate(0, 424)">\n{bottom_content}\n  </g>\n\n'

# 12. Update corner accents at bottom (y + 424)
corner_accents = template[idx_end:]

# Bottom-left: y 385->809, 378->802, 360->784
old_bl = 'M 15 385 L 40 385 L 40 378 L 22 378 L 22 360 L 15 360 Z'
new_bl = 'M 15 809 L 40 809 L 40 802 L 22 802 L 22 784 L 15 784 Z'
corner_accents = corner_accents.replace(old_bl, new_bl)

# Bottom-right: y 385->809, 378->802, 360->784
old_br = 'M 785 385 L 760 385 L 760 378 L 778 378 L 778 360 L 785 360 Z'
new_br = 'M 785 809 L 760 809 L 760 802 L 778 802 L 778 784 L 785 784 Z'
corner_accents = corner_accents.replace(old_br, new_br)

# Reassemble template
final_svg = template[:idx_start] + wrapped_bottom + corner_accents

# Write out the final SVG
with open(r'd:\Rioon7337\assets\namecard.svg', 'w', encoding='utf-8') as f:
    f.write(final_svg)

size = os.path.getsize(r'd:\Rioon7337\assets\namecard.svg')
print(f'SUCCESS! namecard.svg size: {size} bytes ({size/1024/1024:.2f} MB)')
