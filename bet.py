import random
MAX_LINES = 3
MIN_BET = 1
MAX_BET= 100 

COLS = 3
ROWS = 3

symbol_value ={
   
   "A":8,
   "B":6,
   "C":4,
   "D":2
}

def check_winnings(columns, lines, bet, values):
   winnings = 0
   winning_lines = []
   for line in range (lines):
      symbol = columns[0][line]
      for column in columns:
         symbol_to_check = column[line]
         if symbol != symbol_to_check: 
            break
      else:
         winnings  += values[symbol] *bet
         winning_lines.append(line + 1)
         
      return winnings, winning_lines
         
def get_slot_machine_spin(rows, cols, symbols):
   all_symbols=[]
   for symbol, symbol_count in symbols.items():
      for _ in range (symbol_count):
         all_symbols.append(symbol)
   columns =[[],[],[]]  
   for row in range (rows):
      value=random.choice(all_symbols)   
      
        
   columns=[]
   for _ in range (cols):
      column = []
      current_symbols = all_symbols[:]
      for _ in range (rows):
         value = random.choice(current_symbols)
         current_symbols.remove(value)
         column.append(value)
         
      columns.append(column)
      
   return columns   

def print_slot_machine(columns):
   for row in range(len(columns[0])):
       for i, column in enumerate(columns):
          if i !=len(columns) -1:
             print(column[row], end="  |  ")
          else:
             print(column[row], end="")  
             
       print()
def deposit():
   while True:
      amount= input("What would you like to deposit? $") 
      if amount.isdigit(): 
          amount =int(amount)
          if amount > 0:
              break
          else:
              print("Amount should be greater than zero")
      else:
        print("Please enter a number")
   return amount

def get_number_of_lines():
   while True:
      lines= input("Enter number of lines to bet on (1-"+ str(MAX_LINES) + ")? ") 
      if lines.isdigit(): 
          lines =int(lines)
          if 1 <= lines <=  MAX_LINES :
             break                
          else:
              print("Enter a valid number a  lines.")
      else:
         print("Please enter a number")
   return lines
def get_bet():
   while True:
      amount= input("What would you like to bet? $") 
      if amount.isdigit(): 
          amount =int(amount)
          if MIN_BET <= amount <= MAX_BET :
              break
          else:
              print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")
      else:
        print("Please enter a number")
        
   return amount

def spin(balance):
   lines = get_number_of_lines()
   while True:
      bet=get_bet()
      total_bet= bet * lines
      
      if total_bet > balance:
        print(f"You do not have enough to bet on that amount, your current balnce is ${balance}")
      else:
        break
     
   print(f"you are betting ${bet} on {lines}. Total bet is equal to: ${total_bet}")
   
   slots = get_slot_machine_spin(ROWS, COLS, symbol_value)  
   print_slot_machine(slots)
   

   winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
   print(f"You won ${winnings}." )
   print(f"You won on lines", *winning_lines)
   return winnings - total_bet

def main():
   balance = deposit()
   while True:
      print(f"Current balance is ${balance}.")
      spin_option = input("Press enter to play (q to quit).")
      if spin_option == "q" :
         break
      balance += spin(balance)
   
   print(f"You left with ${balance}")
   
main()
