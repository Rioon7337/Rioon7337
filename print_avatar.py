with open(r'd:\Rioon7337\assets\namecard.svg', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(315, 375):
    l = lines[i]
    if 'data:image' in l:
        print(f"Line {i+1}: <image ... [BASE64] />")
    else:
        print(f"Line {i+1}: {l.rstrip()}")
