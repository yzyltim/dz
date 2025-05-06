import random

secret = random.randint(1, 10)
attempts = 3

print("Я загадав число від 1 до 10. Вгадай!")

for i in range(attempts):
    guess = int(input(f"Спроба {i + 1}: "))
    if guess == secret:
        print("Вітаю. Ви вгадали число!")
        break
    elif guess > secret:
        print("Менше")
    else:
        print("Більше")
else:
    print(f"Ви програли. Загадане число було: {secret}")
