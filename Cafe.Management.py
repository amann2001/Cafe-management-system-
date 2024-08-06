import pyodbc  

DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = r'DESKTOP-A10KMAI\SQLEXPRESS'
DATABASE_NAME = 'Mcafe'
# USERNAME = 'your_username' 
# PASSWORD = 'your_password'

# connection_string = f"""
#    DRIVER= {{{DRIVER_NAME}}};
#    SERVER= {SERVER_NAME};
#    DATABASE={DATABASE_NAME};
#    Trust_Connection=yes;
# """

"""Econnection_string = (
   "DRIVER= {{{DRIVER_NAME}}};"
   "SERVER= {SERVER_NAME};"
   "DATABASE={DATABASE_NAME};"
   "Trust_Connection=yes;")"""
   


connection_string = f'DRIVER={{{DRIVER_NAME}}};SERVER={SERVER_NAME};DATABASE={DATABASE_NAME};Trusted_Connection=yes;'
try:
    conn = pyodbc.connect(connection_string)
    print("Connection successful!")
except Exception as e:
    print(f"Error: {e}")
if 'conn' in locals():
    cursor = conn.cursor()
    cursor.execute("SELECT @@SERVERNAME;")

   # Fetch and print the result
    row = cursor.fetchone()
    while row:
        print(row[0])
        row = cursor.fetchone()

    """# Close the connection
    conn.close()
    else:
    print("Connection failed, cursor not created.")"""



   
    Menu = {
        'Pizza': '60',
        'Coffee': '25',
        'Pasta': '75',
        'Burger': '49',
        'Samosa': '15',
        'Tea': '10',
        'Bread Pakoda': '15',
        'Chocolate Shake': '50',
        'Oreo Shake': '70',
        'Kitkat Shake': '60',
        'Strawberry Shake': '80',
        'Salad': '90'
    }

    print(Menu)


# Greet
    print("Welcome to Apna Cafe")
    print("Pizza: Rs60\nCoffee: Rs25\nPasta: Rs75\nBurger: Rs49\nSamosa: Rs15\nTea: Rs10\nBread Pakoda: Rs15\nChocolate Shake: Rs50\nOreo Shake: Rs70\nKitkat Shake: Rs60\nStrawberry Shake: Rs80\nSalad: Rs90")
    table_number = int(input("Enter the table number (1-20): "))
    if 1 <= table_number <= 20:
        print("The order of table_number (1-20) :", table_number)
    else:
        print("This table number does not exist in the cafe ")
        conn.close()
        exit()

    order_total = 0

    item_1 = input("Enter the name of item you want to order: = ")
    if item_1 in Menu:
        order_total += int(Menu[item_1])
        print(f"Your item {item_1} has been added to your order")
    else:
        print(f"Ordered item {item_1} is not available yet!")
        conn.close()
        exit()
    another_order = input("Do you want to add another item? (yes/no): ")
    if another_order.lower() == "yes":
        item_2 = input("Enter the name of second item = ")
        if item_2 in Menu:
            order_total += int(Menu[item_2])
            print(f"Item {item_2} has been added to order")
        else:
            print(f"Ordered item {item_2} is not available!")
            item_2 = ""
    else:
        item_2 = ""
    customer_name = input("Enter your name: ")
    rating = int(input("Please rate our service out of 10: "))
    if 0 <= rating <= 10:
        print(f"Thank you, {customer_name}, for your rating of {rating}/10!")
    else:
        print("Invalid rating. Please provide a rating between 0 and 10.")

    print("Hi", f"{customer_name}")
    bill = f"{item_1} = {int(Menu[item_1])}\n"
    if item_2:
        bill += f"{item_2} = {int(Menu[item_2])}\n"

    print(f"{bill}Total = {order_total}")

    # Insert order into the database
    try:
        cursor.execute("""
            INSERT INTO Orders (table_number, customer_name, items, total, rating)
            VALUES (?, ?, ?, ?, ?)
        """, table_number, customer_name, ', '.join(filter(None, [item_1, item_2])), order_total, rating)

        # Commit the transaction
        conn.commit()
        print("Order has been added to the database.")

    except pyodbc.Error as e:
        print(f"Database error: {e}")

    # Close the connection
    conn.close()

else:
    print("Connection failed, cursor not created.")
#     try:
#         cursor.execute( """INSERT INT TO Orders (table_number  customer_name, items, total ,rating)
#                    VALUES (?,?,?,?,?)
#     """,table_number,customer_name,','.join(filter(None,[item_1,item_2]),order_total,rating)
# )
#                    INSERT INT TO Orders (table_number  customer_name, items, total ,rating)
#                    VALUES (?,?,?,?,?)
#     """,table_number,customer_name,','.join(filter(None,[item_1,item_2]),order_total,rating)


# # commit the transaction 
#     conn.commit()
#     print("Order has been added to the database.")

# except pyodbc.Error as e:
#     print(f"Database error: {e}")
# # close the connection 
# conn.close()

# else:
#     print("Connection failed, cursor not created.")
