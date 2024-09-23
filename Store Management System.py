### Kevin's PC Store Management System
# Kevin Rio Harristyando

data = {
    'Laptop':{
        'product_id':["LP001", "LP002", "LP003", "LP004", "LP005"],
        'item_name':["Asus Zenbook 15", "Asus ROG Zephyrus", "Asus TUF Gaming A15", "Asus Vivobook 14", "Asus Chromebook"],
        'quantity':[10,15,25,20,15],
        'unit_price':[19500000, 27000000, 19500000, 12000000, 6000000]
    },
    'Monitor': {
        'product_id': ["MR001", "MR002", "MR003", "MR004", "MR005"],
        'item_name': ["Asus VG249Q", "ROG Swift", "Dell UltraSharp", "Samsung Odyssey", "LG 27UL850"],
        'quantity': [10, 8, 12, 6, 9],
        'unit_price': [2500000, 8000000, 5000000, 4500000, 5500000]
    },
    'Keyboard': {
        'product_id': ["KD001", "KD002", "KD003", "KD004", "KD005"],
        'item_name': ["Mechanical Corsair", "Razer BlackWidow", "Logitech G Pro", "Ducky One 2", "SteelSeries Apex"],
        'quantity': [25, 20, 30, 15, 18],
        'unit_price': [1200000, 1500000, 1000000, 1400000, 1600000]
    },
    'Mouse': {
        'product_id': ["ME001", "ME002", "ME003", "ME004", "ME005"],
        'item_name': ["Razer DeathAdder", "Logitech MX Master", "Corsair M65", "SteelSeries Rival", "Glorious Model O"],
        'quantity': [30, 25, 20, 18, 22],
        'unit_price': [800000, 1200000, 950000, 1000000, 1100000]
    },
    'Headphones': {
        'product_id': ["HS001", "HS002", "HS003", "HS004", "HS005"],
        'item_name': ["HyperX Cloud", "Logitech G733", "SteelSeries Arctis", "Razer Kraken", "Corsair HS60"],
        'quantity': [20, 15, 25, 18, 22],
        'unit_price': [1500000, 1800000, 2000000, 1300000, 1400000]
    }
}

###FUNCTION FOR ADMIN
# Auto Generated product_id
def generate_product_id(category):
    # Get the first letter and last letter of the category (e.g., 'LP' for Laptop, 'MR' for Monitor, etc.)
    prefix = (category[0]+category[-1]).upper()
    
    # Extract all existing Product IDs for that category and find the highest number
    existing_ids = data[category]['product_id']
    numbers = [int(product_id[2:]) for product_id in existing_ids]
    # Generate the next available number
    next_number = max(numbers) + 1 if numbers else 1
    
    return f"{prefix}{str(next_number).zfill(3)}"

def add_data():
    while True:
        print('\n-------Adding Data---------')
        print(f'\nExisting Category: {list(data.keys())}')
        print('N.B. You can add a new category by Entering the new category name')
        category = input("\nEnter category name: ").capitalize()
        if category in data.keys():
            # Automatically generate a unique Product ID
            product_id = generate_product_id(category)
            item_name = str(input("Enter item name: ")).title()
            quantity = int(input("Enter quantity: "))
            unit_price = int(input("Enter unit price: "))

            data[category]['product_id'].append(product_id)
            data[category]['item_name'].append(item_name)
            data[category]['quantity'].append(quantity)
            data[category]['unit_price'].append(unit_price)
            print(f"Item {item_name} added successfully with Product ID: {product_id}")
            break
        elif category == '':
            print("Please Enter a valid Category")
        else:
            ellop =0
            while ellop !=3:
                print(f"There's no {category} category in the data")
                ask = input(f"Do you want to add {category} into a new Category? (yes/no): ").lower()
                if ask == 'yes':
                    data[category] = {
                        'product_id': [],
                        'item_name': [],
                        'quantity': [],
                        'unit_price': []
                    }
                    print(f"New category '{category}' added successfully!")
                    break
                elif ask == 'no':
                    print(f"New category '{category}' not added!")
                    break
                else:
                    print('Enter only yes or no!')
                    ellop+=1
                    print(f"Error Count : {ellop}, Max allowed = 3")

        while True:
            backmenu = input("\nDo you want to back to admin menu? (yes/no): ").lower()
            if backmenu == 'yes':
                return
            elif backmenu =='no':
                break
            else:
                print("Enter yes or no.")

        

def display_data():
    count_dis = 0
    count_cat = 0
    sort_key_list = ['category','product_id', 'item_name', 'quantity', 'unit_price']
    while count_dis!=3:
        print('\nChoose an options:\n1. View items in a specific category\n2. View items in all categories')
        choice = input('\nEnter the option for displaying the data (1 or 2): ')
        if choice == '1':
            while count_cat!=3:
                print(f'\nAvailable Categories: {list(data.keys())}')
                category = input('Enter the specific category to display: ').capitalize()

                if category in data:
                    # Sorting options
                    print('\nSorting Option:\n-> product_id,\n-> item_name,\n-> quantity,\n-> unit_price')

                    while True:
                        sort_key = input('\nSort by (Enter the column name): ').strip().lower()
                        if sort_key in sort_key_list[1:]:
                            # Sort the data based on the user's choice
                            sorted_data = sorted(
                                zip(data[category]['product_id'], data[category]['item_name'], data[category]['quantity'], data[category]['unit_price']),
                                key=lambda x: x[sort_key_list[1:].index(sort_key)]
                            )

                            # Display sorted data
                            print(f"\nItems in {category} Category (sorted by {sort_key}):\n")
                            print(f"{'product_id':<10} | {'Item_name':<25} | {'quantity':<8} | {'Unit_price':<12}")
                            print("-" * 62)

                            for item in sorted_data:
                                print(f"{item[0]:<10} | {item[1]:<25} | {item[2]:<8} | {item[3]:<12}")
                            print("\nBack to Admin Menu...")
                            break
                        else:
                            print("Invalid sort key. Please choose from: product_id, item_name, quantity, unit_price")
                    break  
                else:
                    print("Category does not exist. Please enter a valid category.")
                    count_cat+=1
                    print(f"Error Count : {count_cat}, Max allowed = 3")
            else:
                print("\nBack to Admin Menu...")
            break
        elif choice == '2':
            print('\nSorting Option:\n-> category\n-> product_id\n-> item_name\n-> quantity\n-> unit_price')
            
            while count_cat!=3:
                sort_key = input('Sort by: ').strip().lower()
                if sort_key in sort_key_list:
                    # Sorting the data for all categories
                    all_items = []
                    for category in data:
                        for i in range(len(data[category]['product_id'])):
                            all_items.append((
                                category, 
                                data[category]['product_id'][i],
                                data[category]['item_name'][i],
                                data[category]['quantity'][i],
                                data[category]['unit_price'][i]
                            ))
                    
                    # Sorting based on the user's choice
                    sorted_all_data = sorted(all_items, key=lambda x: x[sort_key_list.index(sort_key)])
                    
                    # Display sorted data
                    print(f"\nAll Categories (sorted by {sort_key}):\n")
                    print(f"{'Category':<15} | {'product_id':<10} | {'Item_name':<25} | {'quantity':<8} | {'Unit_price':<12}")
                    print("-" * 80)

                    for item in sorted_all_data:
                        print(f"{item[0]:<15} | {item[1]:<10} | {item[2]:<25} | {item[3]:<8} | {item[4]:<12}")
                    print("\nBack to Admin Menu...")
                    break
                else:
                    print("Invalid sort key. Please choose from: product_id, item_name, quantity, unit_price")
                    count_cat +=1
                    print(f"Error Count : {count_cat}, Max allowed = 3")
            else:
                print("\nBack to Admin Menu...")
            break
        
        else:
            print("Invalid choice. Please select 1 or 2.")
            count_dis+=1
            print(f"Error Count : {count_dis}, Max allowed = 3")

    else:
        print("Maximum attempt error count reached.")
        print("\nBack to Admin Menu...")

def update_data():
    while True:
        # Ask user for the category
        print(f'\nExisting Category: {list(data.keys())}')
        category = input('Enter the category to update an item: ').capitalize()
        if category in data:
            print(f"\nItems in {category} Category:\n")
            print(f"{'product_id':<10} | {'Item_name':<25} | {'quantity':<8} | {'Unit_price':<12}")
            print("-" * 60)

            for i in range(len(data[category]['product_id'])):
                print(f"{data[category]['product_id'][i]:<10} | {data[category]['item_name'][i]:<25} | {data[category]['quantity'][i]:<8} | {data[category]['unit_price'][i]:<12}")

            # Ask for the Product ID of the item to update
            item_id = input('Enter the Product ID of the item to update: ').upper()
            if item_id in data[category]['product_id']:
                index = data[category]['product_id'].index(item_id)
                item_name = data[category]['item_name'][index]

                print(f"\nYou are updating {item_name}. What would you like to update?")
                print('\nhoose an option:\n1. Update item name\n2. Update quantity\n3. Update unit price')

                # Get user's choice
                update_choice = input("Enter the number of the option you want to update (1/2/3): ")

                if update_choice == '1':
                    # Update item name
                    new_name = input(f"Enter the new name for {item_name}: ").strip()
                    data[category]['item_name'][index] = new_name
                    print(f"Item name updated to {new_name}")

                elif update_choice == '2':
                    # Update quantity
                    new_quantity = int(input(f"Enter the new quantity for {item_name}: ").strip())
                    data[category]['quantity'][index] = new_quantity
                    print(f"quantity updated to {new_quantity}")

                elif update_choice == '3':
                    # Update unit price
                    new_price = int(input(f"Enter the new unit price for {item_name}: ").strip())
                    data[category]['unit_price'][index] = new_price
                    print(f"Unit price updated to {new_price}")

                else:
                    print("Invalid choice. Please select 1, 2, or 3.")
            else:
                print("Product ID does not exist in this category.")
        elif category == '':
            print("Please Enter a valid category.")
        else:
            print("Category does not exist.")

        # Ask if they want to update another item
        while True:
            another = input("Do you want to update another item? (yes/no): ").strip().lower()
            if another == 'yes':
                break
            elif another == 'no':
                print("Exiting update program.")
                return
            else:
                print('Enter yes or no.')

def delete_data():
    del_count =0
    while del_count !=3:
        print('\nChoose an options:\n1. Delete an entire category\n2. Delete an item inside a category\n0. Back to Main Menu\n')
        choice = input('Enter the option for deleting (1 or 2 or 0): ')
        #Delete an entire category
        if choice == '1':
            count_one=0
            while count_one!=3:
                print(f"\nHere's the list of category on the data {list(data.keys())}")
                category = input("Enter Category to delete : ").capitalize()
                if category in data:
                    while True:
                        confirmation = input(f"Are you sure you want to delete the entire {category} category? (yes/no): ").lower()
                        if confirmation == 'yes':
                            del data[category]
                            print(f"Category {category} has been deleted.")
                            break
                        elif confirmation == 'no':
                            print(f"Category {category} was not deleted.")
                            break
                        else:
                            print("Please Enter yes or no.")
                    break
                else:
                    print("The category does not exist. Please enter a valid category.")
                    count_one+=1
                    print(f"Error Count : {count_one}, Max allowed = 3")
        
        #Delete item inside category
        elif choice == '2':
            count_two = 0
            # Deleting an item inside a category
            while count_two !=3:
                print(f"\nHere's the list of categories in the data: {list(data.keys())}")
                category = input('\nEnter the category from which to delete an item: ').capitalize()
                
                if category in data:
                    print(f"\nItems in {category} Category:\n")
                    print(f"{'product_id':<10} | {'Item_name':<25} | {'quantity':<8} | {'Unit_price':<12}")
                    print("-" * 60) 
                    
                    for i in range(len(data[category]['product_id'])):
                        print(f"{data[category]['product_id'][i]:<10} | {data[category]['item_name'][i]:<25} | {data[category]['quantity'][i]:<8} | {data[category]['unit_price'][i]:<12}")

                    while True:
                        item_id = input('Enter the Product ID of the item to delete: ').strip().upper()
                        if item_id in data[category]['product_id']:
                            index = data[category]['product_id'].index(item_id)
                            item_name = data[category]['item_name'][index]
                            while True:
                                confirm = input(f"Are you sure you want to delete {item_name} from {category}? (yes/no): ").lower()
                                if confirm == 'yes':
                                    # Remove item details by index
                                    del data[category]['product_id'][index]
                                    del data[category]['item_name'][index]
                                    del data[category]['quantity'][index]
                                    del data[category]['unit_price'][index]
                                    print(f"Item {item_name} with Product ID {item_id} has been deleted.")
                                    break  
                                elif confirm == 'no':
                                    print(f"Item {item_name} was not deleted.")
                                    break  
                                else:
                                    print("Please input 'yes' or 'no'.")
                            break
                        else:
                            print("Product ID does not exist in this category. Please try again.")
                    break           

                else:
                    print("Category does not exist. Please try again.")
                    count_two+=1
                    print(f"Error Count : {count_two}, Max allowed = 3")
                        

        elif choice == '0':
            print('\nBack to Main Menu ...')
            break

        else:
            print("\nEnter Correct Choice (1 or 2 or 0).")
            del_count+=1
            print(f"Error Count : {del_count}, Max allowed = 3")
    else:
        print("Maximum attempt error count reached...")
        print("Back to Main Menu ...")

def admin_program():
    counter =0
    while counter !=3:
        print('''\n--- Welcome to the Admin Program ---
Please choose an option:
1. Display stock data
2. Add an item or Category
3. Update an item
4. Delete an item or category
0. Exit''')
        admin_num = str(input("\nEnter your choice: "))
        #Create/Add Data
        if admin_num == '1':
            print("\n--- Display Stock Data ---")
            display_data()    
        
        #Read/Display Data
        elif admin_num == '2':
            print("\n--- Add an Item ---")
            add_data()
        
        #Update the Data
        elif admin_num == '3':
            print("\n--- Update an Item ---")
            update_data()

        #Delete the Data
        elif admin_num == '4':
            print("\n--- Delete an Item or Category ---")
            delete_data()

        #Exiting the Program
        elif admin_num == '0':
            print("Exiting Admin Program.")
            break
        else:
            print("Invalid choice, please enter a number between 1 and 5 or 0 for exit.")
            counter +=1
            print(f'\nError count: {counter}, Maximum allowed: 3')

###FUNCTION FOR USER
# Function to display the cart
def display_cart(cart):
    print("\nYour Cart:\n")
    print(f"{'Product Name':<25} | {'Qty':<5} | {'Price':<10} | {'Total':<10}")
    print("-" * 60)
    
    for i in range(len(cart['Product Name'])):
        total_cost = cart['Qty'][i] * cart['Price'][i]
        print(f"{cart['Product Name'][i]:<25} | {cart['Qty'][i]:<5} | {cart['Price'][i]:<10} | {total_cost:<10}")

# Function to buy products
def buy_products():
    cart = {'Product Name': [], 'Qty': [], 'Price': []}
    buy = 'yes'
    att = 0

    while att !=5:
        if buy == 'yes':
            # Display available categories
            print(f'\nAvailable Categories: {list(data.keys())}')
            category = input('Enter the category from which you want to buy an item: ').capitalize()

            if category in data:
                # Display items in the selected category
                print(f"\nItems in {category} Category:\n")
                print(f"{'product_id':<10} | {'Item_name':<25} | {'quantity':<8} | {'Unit_price':<12}")
                print("-" * 60)

                for i in range(len(data[category]['product_id'])):
                    print(f"{data[category]['product_id'][i]:<10} | {data[category]['item_name'][i]:<25} | {data[category]['quantity'][i]:<8} | {data[category]['unit_price'][i]:<12}")

                # Ask user for the Product ID of the item they want to buy
                while True:
                    product_id = input('Enter the Product ID of the product you want to buy: ').strip().upper()

                    if product_id in data[category]['product_id']:
                        index = data[category]['product_id'].index(product_id)
                        product_name = data[category]['item_name'][index]
                        product_stock = data[category]['quantity'][index]
                        product_price = data[category]['unit_price'][index]

                        # Ask for the quantity
                        buy_amount = int(input(f'Enter the quantity of {product_name} you want to buy (Max {product_stock}): '))

                        # Check if the amount exceeds the stock
                        while buy_amount > product_stock:
                            print(f"Sorry, we only have {product_stock} {product_name}(s) in stock.")
                            buy_amount = int(input(f'Please enter a valid amount (max {product_stock}): '))

                        # Update the cart dictionary
                        cart['Product Name'].append(product_name)
                        cart['Qty'].append(buy_amount)
                        cart['Price'].append(product_price)

                        # Update the stock after purchase
                        data[category]['quantity'][index] -= buy_amount

                        # Display cart
                        display_cart(cart)

                        # Ask if user wants to buy more products
                        while True:
                            buy = input('\nDo you want to buy another product? (yes/no): ').lower()
                            if buy in ['yes', 'no']:
                                break
                            print('Invalid input, Please enter "yes" or "no".')
                        break
                    else:
                        print("Invalid Product ID. Please try again.")

            else:
                print("\nCategory does not exist. Please choose a valid category.")
                att +=1
                print(f'Error count: {att}, Maximum allowed: 5')

        # Checkout process
        if buy == 'no':
            total_payment = 0
            cart['Total'] = []

            # Calculate the total cost for each product
            for i in range(len(cart['Product Name'])):
                total_product_cost = cart['Qty'][i]*cart['Price'][i]
                cart['Total'].append(total_product_cost)
                total_payment += total_product_cost

            # Display final cart
            print("\n--- Final Cart ---")
            display_cart(cart)
            print(f"Total Payment: Rp {total_payment:,}")

            # Payment Process
            attempt = 0
            while attempt != 3:
                balance = int(input('Enter the amount of money to pay: '))
                # Insufficient Balance
                if balance < total_payment:
                    attempt +=1
                    print('\nYour payment has been cancelled due to insufficient balance. Please Try Again.')
                    print(f'Payment Attempt {attempt}/3')

                # Exact Balance
                elif balance == total_payment:
                    print('Your purchase will be processed soon.')
                    print('Thank You for Purchasing in Kevin PC Store')
                    break
                # Over Balance
                else:
                    print(f'You have change: Rp {(balance - total_payment):,}')
                    print('Your purchase will be processed soon.')
                    print('Thank You for Purchasing in Kevin PC Store')
                    break
            else:
                print("\nCancelling Payment...")
    
                # Adding back the deducted quantity to the stock
                for i in range(len(cart['Product Name'])):
                    product_name = cart['Product Name'][i]
                    product_qty = cart['Qty'][i]
                    
                    # Find the category and index of the product to update the stock
                    for category in data:
                        if product_name in data[category]['item_name']:
                            index = data[category]['item_name'].index(product_name)
                            data[category]['quantity'][index] += product_qty
                            break
                    
                print("Stock has been updated. Payment cancelled.")
            break

def user_program():
    counter =0
    while counter !=3:
        print('''
--- User Menu ---
1. View Available Products
2. Buy Products
0. Exit User Program''')
        user_num = str(input("\nEnter your choice: "))
        # Display available products
        if user_num == '1':
            print("\n--- Display Stock Data ---")
            display_data()
        
        # Buy a product
        elif user_num == '2':
            print("\n--- Buy Products ---")
            buy_products()
        
        elif user_num == '0':
            print('Exiting the Program')
            break

        else:
            print("Invalid choice, please enter a number 1 or 2 or 0.")
            counter+=1
            print(f'\nError count: {counter}, Maximum allowed: 3')
            

def main():
    print("\n--- Welcome to the Stock Management System ---")
    while True:
        print('\nPlease Type based your role name:\n- Admin\n- User\n**Type Enter/Anything to Exit**')
        role = input("Choose Admin or User : ").lower()
        
        if role == 'admin':
            print("\nYou have selected the Admin role. Redirecting to Admin Program...\n")
            admin_program()

        elif role == 'user':
            print("\nYou have selected the User role. Redirecting to User Program...\n")
            user_program()
        
        else:
            exiting = input('\nDo you want to exit the program? (yes/no): ')
            if exiting == 'yes':
                print('Thank You')
                print('Exiting the Program...')
                break
            
            elif exiting == 'no':
                continue
            else:
                print('Please enter yes or no')

main()