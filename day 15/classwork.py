# 1) 

score = int(input("შეიყვანე შენი ქულა (0-100): "))

if score >= 90 and score <= 100:
    print("შენი ნიშანია A")
elif score >= 80:
    print("შენი ნიშანია B")
elif score >= 70:
    print("შენი ნიშანია C")
elif score >= 60:
    print("შენი ნიშანია D")
else:
    print("შენი ნიშანია F")



# 2) 
num = int(input("შეიყვანე რიცხვი: "))

if num > 0:
    print("ეს რიცხვი დადებითია")
elif num < 0:
    print("ეს რიცხვი უარყოფითია")
else:
    print("ეს ნულია")



# 3) 

a = int(input("შეიყვანე პირველი რიცხვი: "))
b = int(input("შეიყვანე მეორე რიცხვი: "))

if a > b:
    print("First Number is Greater than second one")
else:
    print("Second Number is Greater than first one")



# 4)

number = int(input("შეიყვანე რიცხვი: "))

if number % 2 == 0:
    print("ეს რიცხვი ლუწია")
else:
    print("ეს რიცხვი კენტია")



# 5) 

temp = int(input("შეიყვანე ტემპერატურა ცელსიუსში: "))

if temp < 0:
    print("Cold ❄️")
elif temp <= 30:
    print("Normal 🌤️")
else:
    print("Hot ☀️")
