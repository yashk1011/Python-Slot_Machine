import random

MAX_LINES=3
MAX_BET=100
MIN_BET=1

rows=3
cols=3

symbolCount={
    "A":2,
    "B":4,
    "C":6,
    "D":8,
}

symbolValue={
    "A":5,
    "B":4,
    "C":3,
    "D":2,
}

def checkWinnings(columns,lines,bet,values):
    winnings=0
    winningLines=[]
    for line in range(lines):
        symbol=columns[0][line]
        for column in columns:
            symbolToCheck=column[line]
            if symbol !=symbolToCheck:
                break
        else:
            winnings+=values[symbol]*bet
            winningLines.append(line+1)
    return winnings,winningLines


def deposit():
    while True:
        amount=input("What would you like to deposit> $")
        if amount.isdigit():
            amount=int(amount)
            if(amount>0):
                break
            else:
                print("Please enter a positive number")
        else:
            print("Please enter a valid number")
    return amount

def getNumberOfLines():
    while True:
        lines=input("Enter the number of lines to bet on (1-" + str(MAX_LINES)+") ? ")
        if lines.isdigit():
            lines=int(lines)
            if 1<=lines<=MAX_LINES:
                break
            else:
                print("Please enter a valid number of lines")
        else:
                print("Please enter a valid number")
    return lines

def getBet():
    while True:
        amount=input("What would you like to bet on each line? ")
        if amount.isdigit():
            amount=int(amount)
            if MIN_BET<=amount<=MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
                print("Please enter a valid number")
    return amount

def getSlotMachinesSpin(rows, cols, symbolCount):
    allSymbols = []
    for (symbol, count) in symbolCount.items():  
        for _ in range(count):
            allSymbols.append(symbol)
    columns = []
    for _ in range(cols):
        column = []
        currentSymbols = allSymbols[:]
        for _ in range(rows):
            value = random.choice(currentSymbols)
            currentSymbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def printSlotMachine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i!=len(columns)-1:
                print(column[row],end ="|")
            else:
                print(column[row],end="")
        print()
                 
def spin(balance):
    lines=getNumberOfLines()
    while True:  
        bet=getBet()
        totalBet=bet*lines
        if totalBet>balance:
            print("You don't have enough money to bet that much")
        else:
            break
        
    print(f"You are betting on {lines} lines. Total bet is equal to ${totalBet}.")
    slots=getSlotMachinesSpin(rows,cols,symbolCount)
    printSlotMachine(slots)
    winnings,winningLines=checkWinnings(slots,lines,bet,symbolValue)
    print(f"You won ${winnings}.")
    # print(f"You won on lines: " *winningLines)
    if winningLines:
        # joining the winning lines into a string
        print(f"You won on lines: {', '.join(map(str, winningLines))}")
    return winnings-totalBet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit): ")
        if answer == "q":
            break
        balance += spin(balance)
    print(f"You are left with ${balance}")
    
main()