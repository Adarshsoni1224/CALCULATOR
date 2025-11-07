def calculater():
	choice=int(input("Press1 for addition\nprees2 for Substraction\nPress3 fofr multiply\nPress4 for divison\nEnter vaild choice"))
	if choice ==1:
		operand1=int(input("Enter opr1:"))
		operand2=int(input("Enter opr2:"))
		result=operand1+operand2
		print(result)
	elif choice ==2:
		operand1=int(input("Enter opr1:"))
		operand2=int(input("Enter opr2:"))
		result=operand1-operand2
		print(result)
	elif choice ==3:
		operand1=int(input("Enter opr1:"))
		operand2=int(input("Enter opr2:"))
		result=operand1*operand2
		print(result)
	elif choice ==4:
		operand1=int(input("Enter opr1:"))
		operand2=int(input("Enter opr2:"))
		result=operand1%operand2
		print(result)
	else:
		print("Invalid choice")
		calculater()
print ("==================")
print("Welcome to Adarsh's Calculator")
print("===================")
calculater()

