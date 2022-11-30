from replit import clear
from art import logo
print(logo)
auction = {}
def highest(auction):
  highest_bid = 0
  winner = ""
  for _ in auction:            
    bid = auction[_] 
    if bid > highest_bid:
      highest_bid = bid
      winner = _        
  print(f"The winner is a {winner} with a bid of {highest_bid}")
other = True
while other:
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: "))  
  auction[name] = bid 
  answer = input("Are there any othe bidders? Type 'yes' or 'no'\n").lower()
  if answer == "no":
    other = False
    highest(auction)
    
  else:
    clear()

  
  
  

  