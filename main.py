MAX_LINES = 3
def deposit():
    while True:
        amount = input("Enter the amount to deposit: ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Please enter a positive amount.")
        else:
            print("Invalid input. Please enter a valid amount.")
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-3): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                return lines
            else:
                print(f"Please enter a number between 1 and {MAX_LINES}.")
        else:
            print("Invalid input. Please enter a valid number.")

def main():
    balance = deposit()
    lines = get_number_of_lines()

main()