import os
biders_data = {}
Bidding = True
art = """

   ##     ##  ##   #####   ########  ######   #####   ##   ##
  ####    ##  ##  ##   ##  #  ##  #    ##    ##   ##  ###  ##
 ##  ##   ##  ##  ##          ##       ##    ##   ##  #### ##
 ######   ##  ##  ##          ##       ##    ##   ##  ## ####
 ##  ##   ##  ##  ##          ##       ##    ##   ##  ##  ###
 ##  ##   ##  ##  ##   ##     ##       ##    ##   ##  ##   ##
 ##  ##    ####    #####     ####    ######   #####   ##   ##

"""
# for the clear screen fnction
clear = lambda: os.system('cls')

while Bidding:
    print(art)
    name = input("What is your name?: ").strip().capitalize()
    bid = float(input("What's your bid?: $").strip())
    data = {name:bid}
    # to append to a dictionary
    biders_data.update(data)
    opt = input("Is there any other bidder? 'yes' or 'no': ").strip().lower()
    if opt == 'yes':
        Bidding = True
        clear()
    else:
        Bidding = False
max_bid = 0
max_bider = ""
for Bidders in biders_data:
    if biders_data[Bidders] > max_bid:
        max_bid = biders_data[Bidders]
        max_bider = Bidders
print(f"The highest bider is {max_bider} with a bid of ${max_bid}")