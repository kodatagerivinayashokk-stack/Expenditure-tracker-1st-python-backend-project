expenses=[]
print("ready to save:")
while True:
    print("1.Add expenditure:")
    print("2.view all expenses:")
    print("3.total cost:")
    print("4.exit:")
    
    choice=int(input("Enter the choice:"))

    if choice==1:
        date=input ("Enter the date (yyyy-dd-mm):")
        category=input("on what type of category did you spend:")
        description=input("enter some more details:")  
        amount=float(input("Enter the amount on what did you spend:"))

        expense={"date":date,"category":category,"description":description,"amount":amount}
        expenses.append(expense)
        print("Expenditure added successfully")

    elif choice==2:
        if len(expenses)==0:
            print("No expenses recorded yet.")
        else:
            for expense in expenses:
                print(f"Date: {expense['date']}, Category: {expense['category']}, Description: {expense['description']}, Amount: {expense['amount']}")

    elif choice==3:
        total=0
        for expense in expenses:
            total+=expense['amount']
        print(f"Total expenditure: {total}")

    elif choice==4:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")