# Программа, которая принимает текст пользовательского ввода
# и печатает этот текст на экране наоборот.

text = input("Введите текст, который я переверну: ")

index = len(text) - 1
rev_text = ""

while index >= 0:
	rev_text += text[index]
	index -= 1

print("Перевёрнутый текст: ", rev_text)

input("\n\nНажмите Enter, чтобы выйти.")
