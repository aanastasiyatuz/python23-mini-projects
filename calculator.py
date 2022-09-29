"1"

num1 = input("Введите 1 число: ")
oper = input("Введите операцию (+ - / // * **): ")
num2 = input("Введите 2 число: ")

if num1.replace('-', '').replace('.', '').isdigit() and num2.replace('-', '').replace('.', '').isdigit():
    num1 = float(num1)
    num2 = float(num2)
    if oper == '+':
        print(f"{num1} + {num2} = {num1 + num2}")
    elif oper == '-':
        print(f"{num1} - {num2} = {num1 - num2}")
    elif oper == '*':
        print(f"{num1} * {num2} = {num1 * num2}")
    elif oper == '**':
        print(f"{num1} ** {num2} = {num1 ** num2}")
    elif oper == '/' or oper == '//':
        if num2 == 0:
            print("На 0 делить нельзя")
        else:
            if oper == '/':
                print(f"{num1} / {num2} = {num1 / num2}")
            else:
                print(f"{num1} // {num2} = {num1 // num2}")
    else:
        print("Такой операции не существует")
else:
    print("Введите корректное число")


"2"
# eval - функция, которая принимает строку и выполняет ее как код
code = input("Введите вычисление: ").replace(' ', '')
if '/0' in code:
    print("На 0 делить нельзя")
else:
    print(eval(code))
