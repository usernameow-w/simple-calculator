while True:
  print("Нужно что-то посчитать?")
  print("Введи 'add' для сложения двух чисел")
  print("Введи 'subtract' для вычитания двух чисел")
  print("Введи 'multiply' для умножения двух чисел")
  print("Введи 'divide' для деления двух чисел")
  print("Введи 'quit' для завершения программы")
  user_input = input(": ")
  
  if user_input == "quit": 
      break

  elif user_input == "add":
    num1 = float(input("Введи слагаемое: "))
    num2 = float(input("Введи второе слагаемое: "))
    result = str(num1 + num2)
    print("Сумма: " + result)
    
  elif user_input == "subtract":
    num1 = float(input("Введи уменьшаемое: "))
    num2 = float(input("Введи вычитаемое: "))
    result = str(num1 - num2)
    print("Разность: " + result)
    
  elif user_input == "multiply":
    num1 = float(input("Введи множитель: "))
    num2 = float(input("Введи второй множитель: "))
    result = str(num1 * num2)
    print("Произведение: " + result)
    
  elif user_input == "divide":
    num1 = float(input("Введи делимое: "))
    num2 = float(input("Введи делитель: "))
    result = str(num1 / num2)
    print("Частное: " + result)
