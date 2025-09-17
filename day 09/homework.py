# 1) შედარებითი ოპერატორები:
# ==   ტოლია
# >    მეტია
# <    ნაკლებია
# >=   მეტია ან ტოლია
# <=   ნაკლებია ან ტოლია

#1
print(5 == 5)      
print(10 == 3)  
print(7 == 7.0)   
 

#2
print(5 > 3)     
print(2 > 8)      
print(10 > 9.9)   
print(-1 > -5) 
print(100 > 101) 
#3
print(3 < 5)      
print(8 < 2)     
print(9.9 < 10)  
print(-5 < -1)    
print(200 < 150) 

#4
print(5 >= 5)     
print(6 >= 5)     
print(4 >= 5)    
print(10 >= 10.0) 
print(0 >= 1)     

#5
print(5 <= 5)     
print(4 <= 5)     
print(7 <= 5)     
print(-3 <= -3)   
print(100 <= 50)  


# 2) Logical operators:
# and -> აბრუნებს True-ს მაშინ, თუ ორივე პირობა  სწორია
# or  -> აბრუნებს True-ს მაშინ, თუ მინიმუმ ერთი პირობა სწორია



#3 მაგალითები logical operators-ზე:

# and
print(True and True)    
print(True and False)   
print(5 > 3 and 10 > 5) 

# or 
print(True or False)    
print(False or False)   
print(7 < 3 or 2 == 2)  

# not
print(not True)        
print(not False)        
print(not (5 > 3))      

# 4 მომხმარებლის რიცხვის შედარება

num = int(input("შეიყვანეთ რიცხვი: "))
print("თქვენი რიცხვი მეტია 10-ზე")
print("თქვენი რიცხვი არ არის მეტი 10-ზე")

# 5) მომხმარებლის სახელის შედარება

name = input("შეიყვანეთ თქვენი სახელი")
my_name = "Gela"
name = my_name
print("თქვენი სახელი უდრის ჩემსას")
print("თქვენი სახელი არ ემთხვევარ ჩემსას")

# 6) ასაკის შემოწმება

age = int(input("შეიყვანეთ თქვენი ასაკი"))
age > 18
print("თქვენი ასაკი 18ზე მეტია")
print("თქვენი ასაკი არ არის 18ზე მეტი")
