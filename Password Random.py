import random
password = int(input("Enter the lengh of password:"))
s="abcdefghijklmnopqrstuvwxyz0123456789ABCEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*?"
p="".join(random.sample(s,password))
print(p)