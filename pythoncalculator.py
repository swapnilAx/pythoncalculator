

''' -:  This is a simple Python based calculator  :- '''


print("\n    ********* -: Welcome to the python calculator :- *********    \n")

a, b = float(input("\nEnter the value of a :- " )), float(input("Enter the value of b :- " ))

print("\n\nThe value of 'a' is :- ", a, "\nThe value of 'b' is :- ", b,"\n")

c = a + b		#Addition of the two numbers...

print(f"\nThe Addition of 'a' and 'b' is :- ", f"{a} + {b} = ", c)

d = a - b		#Substraction of the two nubers...

print(f"\nThe Substraction of 'a' and 'b' is :- ", f"{a} - {b} = ", d)

e = a * b

print(f"\nThe Multiplication of 'a' and 'b' is :- ", f"{a} * {b} = ", e)

if b == 0:
	if a == 0:
		print(f"\nThe Division of 'a' and 'b' is :- ",f"{a} / {b} = ","Error...")
		error=input("\nType 'y' if you want to know:- " )
		if error == "y":
			print("\nThe Division is 0/0. This is an Indeterminate form.\n")
		else:
			print("\nWrong key-word... Sorry.\n")
	else:
		print(f"\nThe Division of 'a' and 'b' is :- ",f"{a} / {b} = ","Error...")
		error=input("\nType 'y' if you want to know:- ")
		if error == "y":
			print(f"\nThe Division is {a}/0 and that's infinity.\n")
		else:
			print("\nWrong key-word... Sorry\n")
else:
	f = a/b
	print(f"\nThe Division of 'a' and 'b' is :-", f"{a} / {b} = ", f,"\n")























