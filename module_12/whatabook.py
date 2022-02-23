from winreg import QueryInfoKey
import mysql.connector
from mysql.connector import errorcode


'''begin code for connection to server'''


config = {
    "user" : "whatabook_user",
    "password" : "MySQL8IsGreat!",
    "host" : "127.0.0.1",
    "database" : "whatabook",
    "raise_on_warnings" : True
}

try:
    db = mysql.connector.connect(**config)
    print("\n Database user {} connected to MySQL on host {} with database {}".format(config['user'], config['host'], config['database']))

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password is incorrect")
    
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")
    
    else:
        print(err)

cursor = db.cursor()

'''end code for connection to server'''


'''code for showing store locations'''


def store(cursor):
    cursor.execute("SELECT store_id, locale from store")

    locations = cursor.fetchall()

    print("\n---- DISPLAYING STORE LOCATIONS ----")

    for location in locations:
        print("WhatABook Store # {}\n Located at {}\n".format(location[0], location[1]))

    main()


'''code for showing all books'''


def books(cursor):
    cursor.execute("SELECT book_id, book_name, author, details from book")

    books = cursor.fetchall()

    print("\n---- DISPLAYING CURRENT TITLES ----")
    
    for book in books:
        print(" {} by {}\n  Synopsis: {}\n".format(book[1], book[2], book[3]))
        input("Press any key to continue....\n\n")

    main()


'''code for showing books not on a wishlist'''


def showbook(cursor, user_id):
    query = ("SELECT book_id, book_name, author, details "
            "FROM book "
            "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(user_id))

    user_id = user_id

    cursor.execute(query)

    books_to_add = cursor.fetchall()

    print("\n---- DISPLAYING BOOKS NOT ON WISHLIST ----")

    for book in books_to_add:
        print("Book ID: {}\n {} by {}\n  Synopsis: {}\n".format(book[0], book[1], book[2], book[3]))
    
    choice = input("Continue to add a book? Y/N  ")

    if choice.upper() == "Y":
        addbook(cursor, user_id)
    if choice.upper() == "N":
        print("Returning to main menu.\n")
        main()
    else:
        print("Invalid choice, returning to main menu.\n")
        main()

    
'''code for adding current book to wishlist'''


def addbook(cursor, user_id):
    while True:
        choice = input("Which book would you like to add. Book ID only please.  ")

        cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({},{})".format(user_id, choice))
        db.commit()
        
        choice = input("Add another? Y/N  ")
        if choice.upper() == "Y":
            continue
        if choice.upper() == "N":
            print("Returning to main menu.\n")
            main()
        else:
            print("Invalid choice, please try again.")
            continue


'''code for showing current books on wishlist'''


def wishlist(cursor, user_id):
    cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
                    "FROM wishlist " + 
                    "INNER JOIN user ON wishlist.user_id = user.user_id " + 
                    "INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id = {}".format(user_id))

    books = cursor.fetchall()

    print("\n----DISPLAYING BOOKS ON WISHLIST----")
    
    for book in books:
        print("{} {} by {}\n ".format(book[3], book[4], book[5]))

    choice = input("Would you like to add a new book? Y/N  ")

    if choice.upper() == "Y":
        showbook(cursor, user_id)
    if choice.upper() == "N":
        print("Returning to main menu")
        main()
    else:
        print("Invalid choice, please try again.")
        wishlist() 


'''main menu'''


def main():
    print()
    print("Please choose from our menu:")
    print("1. My Account")
    print("2. View Current Books")
    print("3. View Store Location")
    print("4. Exit")
    print()

    try: 
        choice = int(input("Enter number only  "))
    except:
        print("Invalid choice, please try again")
        main()

    if choice == 1:
        acct()
    if choice == 2:
        books(cursor)
    if choice == 3:
        store(cursor)
    if choice == 4:
        exit()
    else:
        print("Invalid choice, please try again.")
        main()


'''account menu'''


def acct():
    try:
        user_id = int(input('\n Enter a customer id: '))
    except:
        print("Invalid choice, please enter numbers only.")
        acct()

    if user_id < 0 or user_id > 3:
        print("\nInvalid customer number, returning to home")
        main()
    
    while True:
        
        print()
        print("Please choose from account menu:")
        print("1. My Wishlist")
        print("2. Add A Book")
        print("3. Main Menu")
        print()

        try: 
            choice = int(input("Enter number only  "))
        except:
            print("Invalid choice, returning to main menu")
            main()

        if choice == 1:
            wishlist(cursor, user_id);
        if choice == 2:
            addbook(cursor, user_id);
        if choice == 3:
            main();
        else:
            print("Invalid choice, returning to main menu")
            main()


'''program start'''


print("-------------------------------------------")
print("            Welcome to WhatABook           ")
print("-------------------------------------------")
print()

main()
