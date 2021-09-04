# name = input("Введите Ваше имя ").lower().capitalize()
# screen = f"Привет, {name}!"
# print(screen)

# v = input('Введите число от 1 до 10: ')
# v = int(v)
# print(v + 10) 

# name = str(input ("Введите Ваше имя: "))
# print(f"Привет, {name}! Как дела?")

# print(float("1"))  # ???
# #print(int("2.5"))  # ???
# print(bool(1))  # ???
# print(bool(""))  # ???
# print(bool(0))  # ???

# list1 = [3, 5, 7, 9, 10.5]
# # print(list1)
# list1.append("Python")
# # print(list1)
# # print(len(list1))
# print(list1[0])
# print(list1[-1])
# print(list1[1:5])
# list1.remove("Python")
# print(list1)

town = {"city": "Москва", "temperature": "20"}
print(town.get("city"))
town["temperature"] = int(town["temperature"]) - 5
print(town)
print(town.get("country","Россия"))
town["date"] = "27.05.2019"
print(town)
print(len(town))