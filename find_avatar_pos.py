with open(r'd:\Rioon7337\assets\namecard.svg', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect where the avatar section is
m = text.find('<!-- ===== ')
start_idx = text.find('<!-- ===== ', m + 1) # Find the avatar border comment
end_idx = text.find('<!-- Avatar image -->')

print("Start marker:", text[start_idx:start_idx+60])
print("End marker:", text[end_idx:end_idx+30])
