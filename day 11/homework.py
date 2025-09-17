# 2) for ციკლი – განმეორებითი ოპერაციისთვისაა. ანუ როცა გვინდა რაღაც კოდი რამდენჯერმე შესრულდეს.
# for ციკლში ვიყენებთ range() ფუნქციას, რომ მივუთითოთ რამდენჯერ გავიმეოროთ.


for i in range(5):
    print(i)


for letter in "Python":
    print(letter)



for num in range(1, 101):
    print(num)



for num in range(1, 100, 5):
    print(num)


for num in range(5, 88):
    if num % 2 == 0:   
        print(num)



name = input("შეიყვანე შენი სახელი: ")
for i in range(15):
    print(name)
