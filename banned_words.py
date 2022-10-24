banned = input("Введите запрещенные слова через запятую: ").lower().split(", ")
text = input("Введите текст: ").lower()

for word in banned:
    if word in text:
        sub = word[1:-1]
        stars = "*" * len(sub)
        correct = word.replace(sub, stars)
        text = text.replace(word, correct)

print("Исправленный текст:")
print(text)