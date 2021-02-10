import random
while True:
	#chose the numbe from the 1 to 6 
	s=input('roll the dice press the R : ').lower().strip()
	x=random.randint(1,6)
	if s=='r':
		print(f"you got the {x}")
		print("To end the rolling dice press E or to roll again press any letter")
		e=input().lower().strip()
		if e=="e":
			break
		else:
			continue
	else:
		print("you enter wrong key")
		


