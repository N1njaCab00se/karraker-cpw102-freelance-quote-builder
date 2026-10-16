# Project estimate program

def get_labor_cost(hours, rate):
    # labor cost = hours times rate
    return hours * rate

def main():
    # get the info from the user
    name = input("Client name: ")
    hours = float(input("Estimated work hours: "))
    rate = float(input("Hourly rate: "))
    expenses = float(input("Direct expenses: "))

    # fix the name
    name = name.strip().title()

    # do the math
    labor = get_labor_cost(hours, rate)
    total = labor + expenses

    # show the estimate
    print()
    print("PROJECT ESTIMATE")
    print(f"Client: {name}")
    print(f"Labor cost: ${labor:.2f}")
    print(f"Direct expenses: ${expenses:.2f}")
    print(f"Total estimate: ${total:.2f}")

main()
