a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
op = input("Введіть дію (+, -, *, /): ")

if op == "+":
    print("Результат:", a + b)
elif op == "-":
    print("Результат:", a - b)
elif op == "*":
    print("Результат:", a * b)
elif op == "/":
    if b == 0:
        print("Ділення на нуль")
    else:
        print("Результат:", a / b)
else:
    print("Невідома операція")
