#Задача 4. Користувач вводе з клавіатури 2 числа. 
# Потрібно знайти мінімум з двох чисел та показати йоо на екран.

# num1 = float(input("Enter number 1 - "))
# num2 = float(input("Enter number 2 - "))
# if num1<num2:
#     print("min number - ",num1)
# else:
#     print("min number - ",num2)

#Задача 5.
# Користувач вводить з клавіатури два числа. Залежно від вибору користувача потрібно 
# показати суму двох чисел, різницю двох чисел, середньоарифметичне або добуток двух чисел
# num1 = float(input("Enter number 1 - "))
# num2 = float(input("Enter number 2 - "))
# choice = input("Select an action - ")
# if choice == "+":
#     print("sum - ",num1+num2)
# if choice == "-":
#     print("difference - ",num1-num2)
# if choice == "/":
#     print("average - ",(num1+num2)/2)
# if choice == "*":
#     print("product - ",num1*num2)
# else:
#     print("select a different action")

#Задача 6
# Користувач вводить із клавіатури суму в доларах, потім обирає валюту, у яку хоче перевести цю суму:
# євро, фунти або єни. Після вибору валюти програма запитує курс обраної валюти по відношенню до долара.
# Програма повинна розрахувати і вивести суму в обраній валюті.

doll = float(input("Enter sum - "))
curr = input("Enter currency - ")
EUR = 0.876
GBR = 0.7419
JPY = 144.54
if curr == "EUR":
    print(doll*EUR)
elif curr == "GBR":
    print(doll*GBR)
elif curr == "JPY":
    print(doll*JPY)
else:
    print("No currency")
