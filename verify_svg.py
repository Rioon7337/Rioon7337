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

m = re.search(r'<text[^>]*y="230"[^>]*>([\s\S]*?)</text>', text)
if m:
    print("Big Title:", repr(m.group(1).strip()))

print("GitHub Handle:", re.findall(r'GitHub:[^<\n]*', text))
print("Telegram Handle:", re.findall(r'Telegram:[^<\n]*', text))
print("Instagram Handle:", re.findall(r'Instagram:[^<\n]*', text))

m = re.search(r'ABOUT ME[\s\S]*?</g>', text)
if m:
    print("About Me:\n", m.group(0))

print("Cybernetic Avatar Ring:", "CYBERNETIC SCI-FI REACTOR" in text)
print("Verified Badge next to title:", 'transform="translate(385, 222)"' in text)
