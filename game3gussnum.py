import random

name=input("enter your name: ")
print("hello "+name+" welcome to guss the number")

num1=int(input("enter the  lower limit: "))
num2=int(input("enter the higher limit: "))
guss_num=random.randint(num1,num2)
print(f"Now the number choose from {num1} to {num2}")
f=10
print("you have ten chances to guss \n ****lets start****")
while f>0:
	yournum=int(input("enter the gussing number: "))
	if yournum==guss_num:
		print("you win")
		break
	elif yournum>guss_num-10 and yournum<guss_num+10:
		if yournum>guss_num-10 and yournum<guss_num:
			print("it so near but lower")
		else:
			print("it so near but higher")
	elif yournum>guss_num:
		print("it is too higher")
	else:
		print("it is too lower")
	f-=1
	if f==0:
		print(f"oops you lose \n the number is {guss_num}")