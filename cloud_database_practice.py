
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials

# Authenticate connection to database
cred = credentials.Certificate("C:\\Users\grant\OneDrive\Documents\CSE 310\project-" \
    "database-4ba49-firebase-adminsdk-in998-a8fc62e765.json")
firebase_admin.initialize_app(cred, {
 'project-database-4ba49': 'Cloud Database Practice',
})

# Create database variable
db = firestore.client()


shopping = True
menu = ["Add item", "View cart", "Remove item", "Compute total", "Change Quantity", "Quit"]

# Shopping cart menu loop
while shopping is True:
    # Display menu. 
    print("\nPlease select one of the following:")
    for i in range(len(menu)):
        print(f"{i + 1:>7}. {menu[i]}")

    action = int(input("Please enter an action: "))

    if action == 6: #quit
        shopping = False
        print("\nThank you. Goodbye.")
    elif action == 1: #add item
        item = input("What item would you like to add? ")
        item_price = float(input(f"What is the price of '{item}'? "))
        quantity = int(input("How many? "))
        
        # Add new items to the database
        item_dets = {"Price": item_price, "Quantity": quantity}
        db.collection("Cart").document(item).set(item_dets)
        print(f"'{item}' has been added to the cart.")
    elif action == 2: #view cart
        print("The contents of the shopping cart are: ")

        #Pull and display documents and fields from database. 
        current_cart = db.collection("Cart").stream()
        for thing in current_cart:
            print(f'{thing.id} => {thing.to_dict()}')
    elif action == 4: #compute total
        the_dets = db.collection("Cart").stream()
        total = 0
        for det in the_dets:
            item_detail = det.to_dict()
            det_quantity_price = item_detail['Price'] * item_detail['Quantity']
            total += det_quantity_price
        print(f"The total price of the items in the shopping cart is ${total:.2f}")
    elif action == 3: #remove item
        removal = input("Which item would you like to remove? ")

        # Check to make sure document exists in database before attempting editing. 
        result = db.collection("Cart").document(removal).get()
        if result.exists:
            db.collection("Cart").document(removal).delete()
            print("Item removed")
        else:
            print(f"{removal} does not exist in the inventory.")
    elif action == 5: # Adjust item quantity
        adjustment = input("Which item's quantity would you like to change? ")

        # Check to make sure document exists in database before attempting editing. 
        result = db.collection("Cart").document(adjustment).get()
        if result.exists:
            new_quantity = int(input("What is the new quantity? "))
            db.collection("Cart").document(adjustment).update({"Quantity" :new_quantity})
            print(f"{adjustment} quantity updated.")
        else:
            print(f"{adjustment} does not exist in the inventory.")
    else:
        pass





