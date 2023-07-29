# from replit import clear
from art import logo

def find_highest_bidder(bidding_record):
  highest_bid = 0
  highest_bidder = ""
  
  for bidder in bidding_record:
    if bidding_record[bidder] > highest_bid:
      highest_bidder = bidder
      highest_bid = bidders[bidder]
  print(f"The winner is {highest_bidder} with a bid of ${highest_bid}!")
  
print(logo)

bidders = {}

print("Welcome to the secret auction program.")

bidding_finished = False

while not bidding_finished:
  
  bidder = input("What is your name?: ")
  bid_value = int(input("What's your bid?: $"))
  
  bidders[bidder] = bid_value
  
  other_bidders = input("Are there any other bidders? Type 'yes' or 'no' ")

  if other_bidders == "no":
    bidding_finished = True
  elif other_bidders == "yes":
    # clear()
    print("More fun!")

find_highest_bidder(bidders)




