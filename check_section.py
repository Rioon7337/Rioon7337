with open(r'd:\Rioon7337\assets\namecard.svg', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect the exact lines between "NITRO BORDER" and "Tech stack pills"
start_idx = text.find("<!-- ===== NITRO BORDER")
end_idx = text.find("<!-- Tech stack pills -->")
print(text[start_idx:end_idx + 200])
