from modules import add_new_user, check_balance, find_user_with_iban, add_amount, send_amount, print_f#, print_transaction_logs
users = [
    {"iban":"TB001","name":"levan","lastname":"caava","balance":210},
    {"iban":"TB002","name":"ana","lastname":"chlaidze","balance":450},
    {"iban":"TB003","name":"mariam","lastname":"shurgaia","balance":1290},
    {"iban":"TB004","name":"gigi","lastname":"buava","balance":510},
    {"iban":"TB005","name":"paata","lastname":"kilasonia","balance":210}
    ]

transactions = [
    {"sender_iban": "TB001", "reciver_iban": "TB004", "amount": 20}
]
MENU_LIST = {
    "1":"register account",
    "2":"find account",
    "3":"check account balance",
    "4":"add amount to balance",
    "5":"send amount from/to account",
    "x":"exit"
}

#inner functions
def display_menu():
    print("\n--- Menu List ---")
    for key,value in MENU_LIST.items():
        print(f"{key}. {value}")

#main code
print_f("Welcome to the banking_app")
print(users)
menu_item =""
while menu_item!= "x":
    display_menu()
    menu_item = input("Enter menu item: ")
    
    if menu_item == "1":
        add_new_user(users)
    
    elif menu_item == "2":
        search_result = find_user_with_iban(users)
    
    elif menu_item == "3":
        check_balance(users)
    
    elif menu_item == "4":
        add_amount(users)
    
    elif menu_item == "5":
        send_amount(users)
    
    elif menu_item == "x":
        break
    
    else:
        print("Invalid menu item")
            
