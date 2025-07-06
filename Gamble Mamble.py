import random

Max_lines= 5
MIN_BET=1
MAX_BET=100

ROWS= 5
COLS=3

col_row_items= {
    "A":2,
    "B":4,
    "c":6,
    "d":8,
    "e":10
}
col_row_items_values= {
    "A":10,
    "B":8,
    "c":6,
    "d":4,
    "e":2
}

def get_deposit():
    while True:
        deposit_amount=input("Enter the amount for depositing it: $")
        if deposit_amount.isdigit():
            deposit_amt=int(deposit_amount)
            if deposit_amt>0:
                    break
            else:
                 print("Enter a valid amount to bet upon")
        else:
            print("Enter a valid data type of deposit to bet upon")
            

    return deposit_amt


def get_lines_to_bet():
    while True:
        lines=input(f"Enter the Number of lines for the bet on (1-{Max_lines}): ")
        if lines.isdigit():
            lines=int(lines)
            if 1<=lines<=Max_lines:
                break
            else:
                print("Enter a valid amount of lines to bet upon")
        else:
            print("Enter a valid data type of lines to bet upon")

    return lines

def get_bet_amount():
    while True:
        bet_amount=input("Enter the bet amount for each line: $")
        if bet_amount.isdigit():
            bet_amount=int(bet_amount)
            if MIN_BET<=bet_amount<=MAX_BET:
                break
            else:
                print(f"Bet amount must be between ${MIN_BET} and ${MAX_BET}")
        else:
            print("Enter a valid data type of bet to bet upon")

    return bet_amount

def get_slot_machine(rows, cols, col_row_items):
    all_symbols=[]
    for symbol, symbol_val in col_row_items.items():
        for _ in range(symbol_val):
            all_symbols.append(symbol)
    
    columns=[]
    for _ in range(cols):
        column = []
        current_symbols= all_symbols[:]
        for _ in range(rows):
            value= random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns)-1:
                print(column[row] , end = ' | ')
            else:
                print(column[row] , end = ' ')
        print()
                
def check_winnings(columns, lines, bet, values ):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol= columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol!=symbol_to_check:
                break
        else:
            winnings+=values[symbol] * bet
            winning_lines.append(line+1)
    return winnings, winning_lines

def spin(balance):
    bet_line= get_lines_to_bet()
    while True:
        bet= get_bet_amount()
        total_bet= bet*bet_line

        if total_bet>balance:
            print(f"your bet amount exeeds your deposit. Your balance is: ${balance}.")
        
        else:
            break
    # print(f"you are betting ${bet} on {bet_line} lines and the total bet is: {total_bet} dollars")
    print(f"your deposit is: ${balance}. Your lines of bet is: {bet_line} lines and your bet for a line is: ${bet}. Hence, your total bet is: ${total_bet}")

    slots= get_slot_machine(ROWS, COLS, col_row_items)
    print_slot_machine(slots)
    winnings, winning_lines= check_winnings(slots, bet_line, bet, col_row_items_values)
    print(f"You have won ${winnings}")
    print(f"And you have won lines:", *winning_lines)

    return winnings - total_bet

def main():
    dep_amt=get_deposit()
    while True:
        print(f"Youre left with the balance of {dep_amt}")
        answer=input("Press enter to continue or press  q to exit.")
        if answer=="q":
            break
        
        dep_amt+= spin(dep_amt)



main()
