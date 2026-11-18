with open(r'd:\Rioon7337\assets\namecard.svg', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'<!-- ===== ', text)]
for idx in matches:
    print(text[idx:idx+80].splitlines()[0])
