import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings,winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, count in symbols.items():
        for _ in range(count):
            all_symbols.append(symbol)
            
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i == len(columns) - 1:
                print(column[row], end="")
            else:
                print(column[row], end=" | ")
        print()

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
                break
            else:
                print(f"Please enter a number between 1 and {MAX_LINES}.")
        else:
            print("Invalid input. Please enter a valid number.")
    return lines

def get_bet():
    while True:
        bet = input(f"Enter your bet amount per line ({MIN_BET}-{MAX_BET}): ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Please enter a bet between {MIN_BET} and {MAX_BET}.")
        else:
            print("Invalid input. Please enter a valid bet amount.")
    return bet

def spin(balance):
    if balance <= 0:
        print("You have no balance to play. Please deposit some money.")
        return 0
    else:
        
        lines = get_number_of_lines()
        
        while True:
            bet = get_bet()
            total_bet = bet * lines
            if total_bet > balance:
                print(f"Your total bet of ${total_bet} exceeds your balance of ${balance}.")
                
            else:
                break
        print(f"you are betting ${bet} on {lines} lines. Total bet is ${total_bet}.")
        
        slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
        print_slot_machine(slots)
        winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
        print(f"You won ${winnings}!")
        print(f"You won on lines: ",*winning_lines)
        return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Your current balance is ${balance}.")
        choice = input("Do you want to play a game? (y/n): ")
        if choice.lower() == "y":
            balance += spin(balance)
        elif choice.lower() == "n":
            print("Thank you for playing!")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

    print(f"You left with ${balance}.")

main()