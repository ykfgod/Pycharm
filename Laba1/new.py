text = "qwer tyuio"
a = len(text) # Определяем количество символов в строке
i = 0
zam = ''
while i <= a-2:
    k = text[i+1]
    text.replace(text[i+1], text[i])
    text.replace(text[i], k)
    i = i+1

print(text)

