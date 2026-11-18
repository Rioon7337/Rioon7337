with open(r'd:\Rioon7337\assets\namecard.svg', 'r', encoding='utf-8') as f:
    text = f.read()

import re

print("--- Big Title ---")
for m in re.finditer(r'<text[^>]*y="230"[^>]*>([\s\S]*?)</text>', text):
    print(m.group(0))

print("\n--- Social GitHub ---")
for m in re.finditer(r'GitHub:[^<\n]*', text):
    print(m.group(0))

print("\n--- About Me text ---")
m = re.search(r'ABOUT ME[\s\S]*?</g>', text)
if m:
    print(m.group(0)[:400])

print("\n--- Nitro / Avatar section ---")
m = re.search(r'<!-- ===== NITRO BORDER[\s\S]*?<!-- Avatar image -->', text)
if m:
    print(m.group(0)[:600])
