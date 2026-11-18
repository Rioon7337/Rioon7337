import os
import re

with open(r'd:\Rioon7337\avatar_base64.txt', 'r') as f:
    avatar_b64 = f.read().strip()
with open(r'd:\Rioon7337\banner_base64.txt', 'r') as f:
    banner_b64 = f.read().strip()

with open(r'd:\Rioon7337\lawless_template.txt', 'r', encoding='utf-8') as f:
    template = f.read()

# Replace banner - use xMidYMin slice so face/ears are preserved at top
banner_tag = f'<image href="data:image/gif;base64,{banner_b64}" x="10" y="10" width="780" height="190" preserveAspectRatio="xMidYMin slice"/>'
template = re.sub(r'<image href="\[B64\]" x="10" y="10" width="780" height="190"[^>]*/>', banner_tag, template)

# Replace avatar
avatar_tag = f'<image href="data:image/jpeg;base64,{avatar_b64}" x="50" y="180" width="120" height="120" clip-path="url(#avatarClip)" preserveAspectRatio="xMidYMid slice"/>'
template = re.sub(r'<image href="\[B64\]" x="50" y="180" width="120" height="120"[^>]*/>', avatar_tag, template)

# Replace Username
template = template.replace('LawlessDragon\n', 'Rioon\n')

# Adjust verified checkmark position for shorter name 'Rioon' (original x=425, for Rioon x=290)
template = template.replace('transform="translate(425, 222)"', 'transform="translate(290, 222)"')

# Replace Social handles
template = template.replace('GitHub: /LawlessDragon', 'GitHub: /Rioon7337')
template = template.replace('@BlueLawless', '@rioon7337')
template = template.replace('@lawless_derg', '@rioon7337')

# Replace About Me lines
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

template = template.replace(old_about, new_about)

# Replace Tech stack
template = template.replace('>REACT<', '>PYTHON<')
template = template.replace('>NODE<', '>C++<')
template = template.replace('>UI/UX<', '>FURRY<')

# Write out the new SVG
with open(r'd:\Rioon7337\assets\namecard.svg', 'w', encoding='utf-8') as f:
    f.write(template)

# Also ensure README.md has the proper center tag
readme = '''<p align="center">
  <img src="https://raw.githubusercontent.com/Rioon7337/Rioon7337/main/assets/namecard.svg"/>
</p>
'''
with open(r'd:\Rioon7337\README.md', 'w', encoding='utf-8') as f:
    f.write(readme)

size = os.path.getsize(r'd:\Rioon7337\assets\namecard.svg')
print(f'Done! Generated namecard.svg, size: {size} bytes ({size/1024/1024:.2f} MB)')
