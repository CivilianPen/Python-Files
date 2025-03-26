text = input()

while '()' in text or '[]' in text or '{}' in text:
    text = text.replace('()', '')
    text = text.replace('[]', '')
    text = text.replace('{}', '')
print(not text)
