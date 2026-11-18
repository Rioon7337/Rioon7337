import xml.etree.ElementTree as ET
import re

try:
    tree = ET.parse(r'd:\Rioon7337\assets\namecard.svg')
    root = tree.getroot()
    print("XML: 100% VALID!")
except Exception as e:
    print("XML Error:", e)

with open(r'd:\Rioon7337\assets\namecard.svg', 'r', encoding='utf-8') as f:
    text = f.read()

# Check avatar border section specifically
m = re.search(r'<!-- ===== CYBER GLITCH[\s\S]*?<!-- Avatar image -->', text)
if m:
    avatar_section = m.group(0)
    has_rotate = 'type="rotate"' in avatar_section or 'rotate(' in avatar_section
    print("Avatar Section has ROTATE:", has_rotate)
    print("Avatar Section has TRANSLATE JITTER:", 'type="translate"' in avatar_section)
    print("Avatar Section has CHROMATIC ABERRATION:", '#ff0055' in avatar_section and '#00f0ff' in avatar_section)
    print("Avatar Section has SYS.GLITCH badge:", 'SYS.GLITCH' in avatar_section)
