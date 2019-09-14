# Игра "Анаграмма", где к каждому слову полагается подсказка.
# Игрок должен получать право на подсказку в том случае, если у него нет никаких предположений.
# Система начисления очков: игроки отгадавшие слово без подсказки, получали бы больше тех,
# кто запросил подсказку.

import random

WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")
score = 10

word = random.choice(WORDS)
correct = word

jumble =""
while word:
	position = random.randrange(len(word))
	jumble += word[position]
	word = word[:position] + word[(position + 1):]

print("Угадайте слово из букв:", jumble)

guess = input("\nВаше предположение: ")
while guess != correct:
	if guess == "":
		print("Вы ничего не ввели. Чтобы узнать первую букву, введите help или угадывайте дальше.")
	elif guess == "help":
		print("Первая буква: ", correct[0])
		score = 8
	else:
		print("Извините, вы не угадали.")
	guess = input("Ваше предположение: ")

if guess == correct:
	print("\nПравильно! Вы угадали!\n")
	print("Ваши очки: ", score, "из 10")

print("Спасибо за игру.")

input("\n\nНажмите Enter, чтобы выйти.")
