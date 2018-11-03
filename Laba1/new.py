text = "qwer tyuio"
a = len(text) # Определяем количество символов в строке
i = 0
    while i <= a-2:
        k = text[i]
        text = text.replace(text[i], text[i+1], 1)
        print(text)
        text = text.replace(text[i+1], k, 1)
        print(text)
        i = i+1

print(text)

