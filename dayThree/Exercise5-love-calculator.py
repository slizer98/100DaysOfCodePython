# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

both_names = name1.lower() + name2.lower()

t = both_names.count('t')
r = both_names.count('r')
u = both_names.count('u')
e = both_names.count('e')
true = t + r + u + e

l = both_names.count('l')
o = both_names.count('o')
v = both_names.count('v')
e = both_names.count('e')
love = l + o  + v + e

total_times = str(true) + str(love)
total_times = int(total_times)

if total_times < 10 or total_times > 90:
    print(f"Your score is {total_times}, you go together like coke and mentos.")
elif total_times >= 40 and total_times <= 50:
    print(f"Your score is {total_times}, you are alright together.")
else: 
    print(f"Your score is {total_times}.")






