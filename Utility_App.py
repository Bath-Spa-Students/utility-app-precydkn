## Vending machine program

# !note! the margin made of tabs are for the visual formatting since the display is center format
# margin
margin = "\t\t\t\t\t"

# colored text 
purple = "\033[35m"
yellow = "\033[33m"
green = "\033[32m"
red = "\033[31m"
white = "\033[37m"
black = "\033[30m" 
cyan = "\033[36m"

# store vending machine name/greeting in a variable to center it
greeting = "‧₊˚ ⋅ ‧₊˚ ⋅ Welcome to the ᴍɪɴɪ ᴄᴀꜰᴇ ᴠᴇɴᴅɪɴɢ ᴍᴀᴄʜɪɴᴇ! ⋅ ˚₊‧ ⋅ ˚₊‧"
print(f"\n" + greeting.center(200)) # centered text with space before the text


# dict of vending machine menu
menu = {
    "𝐂 𝐨 𝐟 𝐟 𝐞 𝐞" : {
                "A1" : {"Item": "⋅ Americano", "Price" : 2, "Stock" : 20},
                "A2" : {"Item": "⋅ Capucino", "Price" : 2, "Stock" : 13},
                "A3" : {"Item": "⋅ French Vanilla", "Price" : 2, "Stock" : 14},
                "A4" : {"Item": "⋅ Latte", "Price" : 2, "Stock" : 6},
                "A5" : {"Item": "⋅ Espresso", "Price" : 2, "Stock" : 25}
                },

    "𝐌  𝐢 𝐥 𝐤  𝐃 𝐫 𝐢 𝐧 𝐤 𝐬" : {
                    "B1" : {"Item": "⋅ Regular Milk", "Price" : 2, "Stock" : 26},
                    "B2" : {"Item": "⋅ Chocolate Milk", "Price" : 2, "Stock" : 12},
                    "B3" : {"Item": "⋅ Strawberry Milk", "Price" : 2, "Stock" : 28},
                    "B4" : {"Item": "⋅ Banana Milk", "Price" : 2, "Stock" : 3}
                    },

    "𝐏 𝐚 𝐬 𝐭 𝐫 𝐢 𝐞 𝐬" : {
                    "C1" : {"Item": "⋅ Buttered Croissant", "Price" : 3, "Stock" : 12},
                    "C2" : {"Item": "⋅ Chocolate Muffin", "Price" : 3, "Stock" : 10},
                    "C3" : {"Item": "⋅ Blueberry Muffin", "Price" : 3, "Stock" : 19},
                    "C4" : {"Item": "⋅ Chocolate Chip Cookie", "Price" : 3, "Stock" : 4},
                    "C5" : {"Item": "⋅ Red Velvet Cookie", "Price" : 3, "Stock" : 9},
                    "C6" : {"Item": "⋅ Caramel Nut Cookie", "Price" : 3, "Stock" : 5}
                },

    "𝐒 𝐰 𝐞 𝐞 𝐭 𝐬  &  𝐒 𝐧 𝐚 𝐜 𝐤 𝐬" : {
                        "D1" : {"Item": "⋅ Pepero Original", "Price" : 3, "Stock" : 21},
                        "D2" : {"Item": "⋅ Pepero White Cookie", "Price" : 3, "Stock" : 0},
                        "D3" : {"Item": "⋅ Pepero Choco-Filled", "Price" : 3, "Stock" : 27},
                        "D4" : {"Item": "⋅ M&M’s Chocolate", "Price" : 1, "Stock" : 15},
                        "D5" : {"Item": "⋅ Twix Chocolate Bar", "Price" : 1, "Stock" : 11},
                        "D6" : {"Item": "⋅ KitKat Chocolate Bar", "Price" : 1, "Stock" : 1}
                        }
        }

# main function calling all functions
def main():
    displayMenu()
    code = selectItem() # selectItem is assigned to "code" to be used in the next functions
    money = insertMoney(code) # insertMoney is assigned to "money" to be used in the next funtions
    dispenseItem(money, code)
    suggestions(code)
    buyMore()



# function to display menu
def displayMenu():
      # guide: products = coffee, milk drinks...  item_code = b1, d3...
    for products, item_code in menu.items(): 
        # store category and design in a variable to center it 
        heading = (f"⛧ ────────────⋆⋅[' {products} ']⋅⋆──────────── ⛧")
        print("\n" + heading.center(200)) # centered
          # guide: code = user input  item = item corresponding to code
        for code, item in item_code.items():
            # store item code, name, price, stock in a variable to center it
            line = (f"{purple}{code} {item['Item']}{yellow}\tPrice: {item['Price']} AED{black}\tStock: {item['Stock']}{white}")
            print(line.expandtabs(20).center(215)) # centered
        # centered divider
        divider = "──────────── ⋆ ⋅ ☆ ⋅ ⋆ ────────────"
        print("\n" + divider.center(200)) # centered 

# fucn for getting user's choice of item
def selectItem():
    while True:
        code = input(f"\n{margin}Item Code » {purple}").capitalize() # capitalizing text in case input is lowercase
        # loop that runs until the correct item code is given 
        for products, item_codes in menu.items(): #guide: products (coffee, milk drinks)  item_codes (b1, d3, a4)
            # if code (from user input) is an existing item code, display selected item
            if code in item_codes:
                    print(f"{margin}{code} {menu[products][code]['Item']} {white}selected.\n")
                    # if selected item's stock is 0, ask user if they still want to continue buying
                    if menu[products][code]["Stock"] == 0:
                        print(f"{margin}{black}Sorry, {purple}{code} {menu[products][code]['Item']} {black}is out of stock at the moment. ૮(⸝⸝ᴗ﹏ᴗ⸝⸝)ა{white}")
                        confirm_continue = input(f"{margin}Would you still like to buy anything else? If yes, press Enter, otherwise press any key. » ")
                        # if user says yes, repeat selectItem(), otherwise display ending message then end code
                        if confirm_continue == "":
                            code = selectItem()
                            return code # returned code is new now
                        else:
                            print(f"\n\{margin}Thank you for using the ‧₊˚ ⋅ ‧₊˚ ⋅ ᴍɪɴɪ ᴄᴀꜰᴇ ᴠᴇɴᴅɪɴɢ ᴍᴀᴄʜɪɴᴇ ⋅ ˚₊‧ ⋅ ˚₊‧ . We'll make sure to be well stocked next time! ৻(｡• ᦍ •｡)ა\n")
                            exit()
                    else:
                        return code
        # otherwise display message of invalid code 
        print(f"{margin}{red}Invalid code selected. Please select an item by its corresponding code. ᕙ(⇀‸↼‶)ᕗ{white}")
        

# func for getting money from user
def insertMoney(code): # the code parameter is taken from the selectItem()
    # while loop so that the code will continue to ask the user for input until the expected input is given
    while True:
        # try-except statement to prevent breakage of code when input is not a number
        try:
            for products, item_codes in menu.items(): #guide: products (coffee, milk drinks)  item_codes (b1, d3, a4)
                # if code (from user input) is an existing item code, display selected item
                if code in item_codes:
                    # display item price and 0 money balance then ask user for money
                    print(f'{margin}{yellow}Item Price: {menu[products][code]["Price"]} AED   {green}Balance: 0 AED {white}')
                    money = float(input(f"{margin}Insert money (∩｡• ᦍ •｡)っ {green}"))
                    # while loop for when money is 0
                    while money == 0:
                        print(f'{margin}{yellow}Item Price: {menu[products][code]["Price"]} AED   {green}Balance: 0 AED \n{white}')
                        money = float(input(f"{margin}Insert money (∩｡• ᦍ •｡)っ {green}")) 
                    # while loop for when money < item price
                    while money < menu[products][code]["Price"]:
                        print(f'\n{margin}{yellow}Item Price: {menu[products][code]["Price"]} AED   {green}Balance: {money} AED {red}')
                        print(f"{margin}Insuficient money to purchase selected product. Please insert more money. ᕙ(⇀‸↼‶)ᕗ{white}")
                        # add newly inserted money to previous amount
                        money += float(input(f"{margin}Insert money (∩｡• ᦍ •｡)っ {green}"))
                    # if statement for when money >= item price
                    if money >= menu[products][code]["Price"]:
                        print(f'\n{margin}{yellow}Item Price: {menu[products][code]["Price"]}   {green}Balance: {money} AED {white}')
                        return money
        except:
            print(f"{margin}{red}Invalid value inserted. Please insert at least 1 AED. ᕙ(⇀‸↼‶)ᕗ{white}\n")

# func for dispensing item and money managing
def dispenseItem(money, code): # the money and code parameters are taken from the insertMoney() and selectItem()
    for products, item_codes in menu.items(): 
        if code in item_codes:
            # convert menu[products][code]["Price"] into string to remove "⋅ "
            print(f'{margin}{white}Great! One {purple}{(str(menu[products][code]["Item"])).removeprefix("⋅ ")} {white}will now be dispensed.{black}')
            enter = input(f"{margin}ᴘʀᴇꜱꜱ ᴇɴᴛᴇʀ ᴛᴏ ᴄʟᴀɪᴍ ʏᴏᴜʀ ɪᴛᴇᴍ ")
            if enter == "":
                print(f'\n{margin}.\n{margin}.\n{margin}.\n{white}') # just "." spaces
                print(f'{margin}Your {purple}{(str(menu[products][code]["Item"])).removeprefix("⋅ ")} {white}is here! (੭ •̀ ᗜ •́ )੭')
                money = money - menu[products][code]["Price"]
                # just display 0 change if it is, otherwise return change to user
                if money == 0:
                    print(f"{green}{margin}Change: 0 AED\n{white}")
                else: 
                    print(f"{margin}Don't forget to take your {green}Change: {money} AED\n{white}")
            
            # -1 stock from selected item if stock is not 0 
            menu[products][code]["Stock"] -= 1
            return menu[products][code]["Stock"]

# func for suggesting other items
def suggestions(code): # the code parameter is taken from the selectItem()
    # A coffee -> pastries
    if code.startswith("A"):
        print(f"{margin}{cyan}You might want to chew on something, too. Bread go well with coffee, you know? (૭ ｡•̀ ᵕ •́｡ )૭ {white}")
    # B milk drinks -> sweets n snacks
    elif code.startswith("B"):
        print(f"{margin}{cyan}Want some sweet snacks or bread with that? („• ֊ •„)੭ {white}")
    # C pastries -> coffee
    elif code.startswith("C"):
        # if code has 1-3 different message from if code has 4-6
        if code.endswith("1") or code.endswith("2") or code.endswith("3"):
            print(f"{margin}{cyan}Bread is tasty, why not make it tastier with coffee on the side? (˵ •̀ ᴗ - ˵ ) ✧ {white}")
        else:
            print(f"{margin}{cyan}You can have a drink with that. Why not try checking out our milk drinks or coffee? (• ‾ ⌣ ‾•)و ̑̑♡ {white}")
    # D sweets n snacks -> milk drinks
    else:
        # if code has 1-3 different message from if code has 4-6
        if code.endswith("1") or code.endswith("2") or code.endswith("3"):
            print(f"{margin}{cyan}You might want some milk drink with that, why not buy some? ( •̤ ꒳ •̤ ) {white}")
        else:
            print(f"{margin}{cyan}Do chocolates go well with coffee or milk drinks? Want to try some with that? ( •̯́ ₃ •̯̀) {white}")

# func for asking whether user wants to continue buying
def buyMore():
    confirm_buy_more = input(f"\n{margin}Would you like to continue purchasing other items? If yes, press Enter, otherwise press any key. » ")
    # if user agrees, display menu with updated stock then repeat item selection and getting money funcs 
    if confirm_buy_more == "":
        displayMenu()
        code = selectItem()
        money = insertMoney(code)
        dispenseItem(money, code)
        suggestions(code)
        buyMore()
    # otherwise, greet user 
    else:
        print(f'\n{margin}Thank you for using the ‧₊˚ ⋅ ‧₊˚ ⋅ ᴍɪɴɪ ᴄᴀꜰᴇ ᴠᴇɴᴅɪɴɢ ᴍᴀᴄʜɪɴᴇ ⋅ ˚₊‧ ⋅ ˚₊‧ . Enjoy your food!\n')


# call main func
main()