with open(r'd:\Rioon7337\assets\namecard.svg', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect the avatar area
start = text.find('<!-- ===== CYBERNETIC SCI-FI REACTOR')
end = text.find('<!-- Avatar image -->')
print(text[start:end])
