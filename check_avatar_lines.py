with open(r'd:\Rioon7337\assets\namecard.svg', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if any(k in line for k in ['nitroGlow', 'nitroOuterGlow', 'avatarClip', 'Avatar image', 'rotating ring', 'animateTransform', 'status indicator', 'Status indicator']):
        print(f"Line {i+1}: {line.strip()[:100]}")
