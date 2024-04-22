#define account finder(by IBAN) function for other functions 
def finder(database,iban):
    for user in database:
        if user.get("iban") == iban:
            return user
    return None

# register account    
def add_new_user(database):
    print_f("Enter new user details:")
    name = input("Name: ")
    lastName = input("Last Name: ")
    iban = input("IBAN: ")
    balance = int(input("Balance: "))
    if finder(database,iban) is None: 
        user = {"name": name, "lastName": lastName, "iban": iban, "balance": balance}
        database.append(user)
    else:
        print_f("User with this IBAN already exists")

# Find account
def find_user_with_iban(database):
    iban = input("Enter iban to search: ")
    search_result = finder(database,iban)
    if search_result:
        print_f(search_result)
    else:
        print_f("User not found!!! Please enter valid IBAN!")


# check account balance       
def check_balance(database):
    iban = input("Enter iban to check account balance: ")
    search_result = finder(database,iban)
    if search_result:
        print_f(f"Balance of account {search_result['name']} is {search_result['balance']}")
    else:
        print_f("User not found")

def add_amount(database):
    iban = input("Enter iban to find account: ")
    search_result = finder(database,iban)
    if search_result:
        amount = float(input("Enter amount to add: "))
        search_result['balance'] += amount
        print_f(f"Balance of {search_result['name']} is updated to {search_result['balance']}")

def send_amount(database):
    sender_iban = input("Enter sender IBAN: ")
    search_sender = finder(database, sender_iban)
    if search_sender:
        reciver_iban = input("Enter reciver IBAN: ")
        search_reciver = finder(database, reciver_iban)
        if search_reciver:
            amount = float(input("Enter amount to send: "))
            if search_sender['balance'] >= amount:
                search_sender['balance'] -= amount
                search_reciver['balance'] += amount
                print_f(f"{amount} \nsent from \n{search_sender}\n to \n{search_reciver}")
            else:
                print_f("Insufficient balance")
        else:
            print_f("reciver User's IBAN not found")
    else:
        print_f("sender User's IBAN not found")

def print_f(str):
    limit = 80
    if len(str)<80:
        print("\n"+"-"*len(str)+"\n"+str+"\n"+"-"*len(str))
    else:
        print("\n"+"-"*limit+"\n"+str+"\n"+"-"*limit)

