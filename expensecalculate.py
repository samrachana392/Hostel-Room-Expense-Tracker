
FILENAME = "expense_history.txt"
def add_expense():

    print("Enter the following details: ")
    month = input("Enter month (eg: march 2025): ")
    persons = int(input("Enter the total number of persons living: "))
    rent = int(input("Enter the total rent of your hostel/room: "))
    food = int(input("Enter the total amount spent in food: "))
    water = int(input("Enter the cost of water: "))
    electricity_unit = int(input("Enter the total electricity units for this month: "))
    charge_per_unit = int(input("Enter charge for unit for electricity: "))
    other = int(input("Enter the other expenses for this month: "))

    electricity_bill = electricity_unit * charge_per_unit
    total_bill = rent + food + water + electricity_bill + other
    bill_per_person = round(total_bill/persons, 2)


    with open(FILENAME, "a") as file:
        file.write(f"{month}  |  Total: {total_bill}  | Per PErson: {bill_per_person} \n" )
   
    print("Expenses saved successfully!! ")
    print("Each person has to pay", bill_per_person, " for this month")

def view_history():
    with open(FILENAME,"r") as file:
        data = file.read()
        if(data.strip()==""): # .strip() is a string method that removes all leading and trailing whitespaces from a string
            print("\n No expense history found")
        else: 
            print(" \n Expense history: ")
            print(data)

def clear_history():
    confirm = input("Are you sure you want to delete all history? (y/n): ")
    confirm = confirm.lower()
    if confirm == 'y':
        open(FILENAME, "w").close()
        print("Sucessfully cleared expense history")
    else:
        print(" clear operation cancelled.")

def menu():
    print("1 - Add Monthly Expenses ")
    print("2 - View Expense History")
    print("3 - Clear Expense History")
    print("4 - Exit")

 


while True:
    menu()
    choice = int(input("Enter choice: "))
    match choice:
        case 1:
            add_expense()
        case 2:
            view_history()
        case 3: 
            clear_history()
        case 4:
            print("Exiting program.")
            break 
        case _:
            print("Invalid input")
            # case default is writeen as case _
    input("press Enter to return to menu")

