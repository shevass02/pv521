#Рівень 1
# Завдання 1
# Користувач вводить з клавіатури номер дня тижня (1-7). 
# Необхідно вивести на екран назви дня тижня. 
# Наприклад, якщо 1, то на екрані напис понеділок, 2 — вівторок тощо.

# number = int(input("Enter week number - "))
# if number== "1":
#     print("Monday")
# elif number== "2":
#     print("Tuesday")
# elif number== "3":
#     print("Wednesday")
# elif number== "4":
#     print("Thursday")
# elif number== "5":
#     print("Friday")
# elif number== "6":
#     print("Satarday")
# elif number== "7":
#     print("Sunday")
# else:
#     print("No day")

# Завдання 2
# Користувач вводить із клавіатури номер місяця (1-12).
# Необхідно вивести на екран назву місяця. Наприклад, якщо 1,
# то на екрані напис січень, 2 — лютий тощо.
    
# number = int(input("Enter number month - "))
# if number== "1":
#     print("January")
# elif number== "2":
#     print("February")
# elif number== "3":
#     print("March")
# elif number== "4":
#     print("April")
# elif number== "5":
#     print("May")
# elif number== "6":
#     print("June")
# elif number== "7":
#     print("Jule")
# elif number== "8":
#     print("August")
# elif number== "9":
#     print("September")
# elif number== "10":
#     print("October")
# elif number== "11":
#     print("November")
# elif number== "12":
#     print("December")
# else:
#     print("No month")

# Рівень 2
# Завдання 3
# Користувач вводить суму покупки і свій вік. Програма обчислює знижку:

# Якщо вік менше 18, знижка 10%.
# Від 18 до 60 років — знижка 5%.
# Якщо вік більше 60 років — знижка 15%. Програма виводить підсумкову суму з урахуванням знижки.

# summa = float(input("Enter summa - "))
# age = int(input("Enter age - "))
# if age<=18:
#     print("Знижка 10% - ",summa-(summa/10))
# elif age>=18 and age<=60:
#     print("Знижка 5% - ", summa-(summa/20))
# elif age>60:
#     print("Знижка 15% - ",summa-((summa/100)*15))
# else:
#     print(summa)

# Завдання 4
# Користувач вводить оцінки з трьох предметів (від 1 до 5). 
# Програма перевіряє, чи є серед них хоча б одна "двійка". 
# Якщо так, виводиться повідомлення "Незадовільно". Якщо всі оцінки 4 і вище, виводиться "Відмінно".

# hist = int(input("Введіть оцінку з історії - "))
# math = int(input("Введіть оцінку з математики - "))
# him = int(input("Введіть оцінку з хімії - "))

# if hist>4 and math>=4 and him>=4:
#     print("Відмінно")
# elif hist>=4 and math>=4 and him<=2:
#     print("Незадовільно")
# elif hist>=4 and math<=2 and him>=4:
#     print("Незадовільно")
# elif hist<=2 and math>=4 and him>=4:
#     print("Незадовільно")    
# 
# Рівень 3
# Завдання 5
# Користувач вводить оцінки з чотирьох предметів (від 1 до 5). Програма перевіряє, 
# чи може він бути допущений до іспиту:

# Якщо хоча б одна оцінка нижче 3, студент не допускається до іспиту.
# Якщо всі оцінки 4 і вище, студент допускається до іспиту з відзнакою.
# У всіх інших випадках студент допускається до іспиту.    

# hist = int(input("Введіть оцінку з історії - "))
# math = int(input("Введіть оцінку з математики - "))
# him = int(input("Введіть оцінку з хімії - "))
# phys = int(input("Введіть оцінку з фізики - "))

# if hist<3 and math>=4 and him>=4 and phys>=4:
#     print("Недопуск")
# elif hist>=4 and math<3 and him>=4 and phys>=4:
#     print("Недопуск")
# elif hist>=4 and math>=4 and him<3 and phys>=4:
#     print("Недопуск")
# elif hist>=4 and math>=4 and him>=4 and phys<3:
#     print("Недопуск")
# elif hist>=4 and math>=4 and him>=4 and phys>=4:
#     print("допускається до іспиту з відзнакою")
# else:
#     print("Недопуск")

# Завдання 6
# Користувач вводить дані про свій автомобіль: вік і пробіг. Програма виводить рекомендацію:

# Якщо вік автомобіля менше 3 років і пробіг до 30000 км — "Автомобіль у відмінному стані".
# Якщо вік до 10 років і пробіг до 100000 км — "Автомобіль у хорошому стані".
# В інших випадках — "Автомобіль потребує перевірки".

# age = float(input("Вік автомобіля, р - "))
# km = float(input("Пробіг авто, км - "))

# if age<3 and km<=30000:
#     print("Автомобіль у відмінному стані")
# elif age<=10 and km<=100000:
#     print("Автомобіль у хорошому стані")
# else:
#     print("Автомобіль потребує перевірки")





