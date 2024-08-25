#Secret Auction
import sys
name_list =[]
bid_list = []
auction_dict = {}

def Auction(name, bid):
   
                      
    name_list.append(name)
    bid_list.append(bid)
    auction_dict["names"] = name_list
    auction_dict["bids"] = bid_list
    return auction_dict
    

proceed = True
while proceed:
    print("""
                        ___________
                        \         /
                         )_______(
                         |"""""""|_.-._,.---------.,_.-._
                         |       | | |               | | ''-.
                         |       |_| |_             _| |_..-'
                         |_______| '-' `'---------'` '-'
                         )"""""""(
                        /_________\
                        `'-------'`
                      .-------------.
                      _______________
    """)
    bidder_name = input("What is your name? ")
    bidding_amount = int(input("What is your bid?: $"))
    choice = input('Is there any other bidder? Type "yes" or "no": ').lower()
    
    Auction(bidder_name, bidding_amount)
    
    if choice == "yes":
        proceed = True
    elif choice == "no":
        proceed = False
    else :
        print("Invalid Choice, program suspended")
        sys.exit()
        

max_bid = max(auction_dict["bids"])
for bid in range(len(bid_list)):
    if bid_list[bid] == max_bid:
        position_of_bid = bid
        
winner = auction_dict["names"][position_of_bid]

print(f"Highest bid is {max_bid}, winner is {winner}!")
        