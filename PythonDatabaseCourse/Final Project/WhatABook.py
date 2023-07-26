import mysql.connector
try: #error handling if fails to connect to database
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "ropedi@4",
        database = "whatabook"
    )
except:
    print("error occured when trying to connect to database")

mycursor = mydb.cursor() #create cursor

uid_list = [] #global variable for use with wishlist functionality
user_id = [] #global variable for use with wishlist functionality

def show_books():
    mycursor.execute("SELECT book_name, details, author FROM book;") #retreive relevant information from book table
    books = mycursor.fetchall()
    for book in books: #print retreived information from book table
        print("Book Name: {}".format(book[0]))
        print("Details: {}".format(book[1]))
        print("Author: {}".format(book[2]))
        print("")

def show_locations():
    mycursor.execute("SELECT locale FROM store;") #retreive relevant information from store table
    locations = mycursor.fetchall()
    for location in locations: #print retreived information from store table
        print("Location: {}".format(location[0]))

def validate_user():
    validate = 0 #false by default
    this_uid = input('Enter your user id: ')
    this_uid = int(this_uid) #must type cast otherwise comparison fails because '1' does not equal 1
    mycursor.execute("SELECT user_id FROM user;")
    uids = mycursor.fetchall()
    for uid in uids:
        uid = uid[0]
        uid_list.append(uid)
    if this_uid in uid_list:
        global user_id 
        user_id = this_uid #set global user_id so can be used in wishlist functions
        validate = 1
        return validate
    else:
        return validate

def show_wishlist():
    global user_id
    uid_list = [user_id] #have to make it a list in order for next statement to execute
    mycursor.execute("SELECT book.book_name, wishlist.user_id FROM wishlist INNER JOIN book ON book.book_id = wishlist.book_id WHERE user_id = (%s)", (uid_list))
    wishlist = mycursor.fetchall()
    print("Books in Wishlist:")
    for book in wishlist:
        print("Book Name: {}".format(book[0]))

def show_books_to_add(): 
    print("show books to add")
    global user_id  #used to select all book_ids from users wishlist
    uid_list = [user_id] 
    wishlist_book_ids = []
    formatted_wishlist_book_ids = [] #used to put book_ids from wishlist into a list variable
    all_book_ids = []
    formatted_all_book_ids = [] #used to put books_ids from books table into a list variable
    mycursor.execute("SELECT book_id FROM wishlist WHERE user_id = (%s)", (uid_list)) #SELECT books in the users wishlist
    wishlist_book_ids = mycursor.fetchall() #put books in wishlist into a variable
    for id in wishlist_book_ids: #put all of the ids of all of the books in the users wishlist into a list 
        a = ("{}".format(id[0]))
        formatted_wishlist_book_ids.append(a)
    #print(formatted_wishlist_book_ids)
    mycursor.execute("SELECT book_id FROM book") #SELECT all book_ids that exist
    all_book_ids = mycursor.fetchall() #put all book ids into variable
    for id in all_book_ids: #put all of the ids that exist into a list 
        a = ("{}".format(id[0]))
        formatted_all_book_ids.append(a)
    #print(formatted_all_book_ids)
    wishlist_formatted_book_ids_length = len(formatted_wishlist_book_ids)
    while wishlist_formatted_book_ids_length > 0: #filter books ids in wishlist out of all book ids
        formatted_all_book_ids.remove(formatted_wishlist_book_ids[wishlist_formatted_book_ids_length - 1])
        wishlist_formatted_book_ids_length -= 1
    #print(formatted_all_book_ids)
    formatted_all_book_ids_length = len(formatted_all_book_ids)
    print("Here are the books you can add to your wishlist") 
    while formatted_all_book_ids_length > 0: #loop used to print out all of the books the user does not currently have in their wishlist
        id_list = [formatted_all_book_ids_length]
        mycursor.execute("SELECT book_name FROM book WHERE book_id = (%s)", (id_list))
        a = mycursor.fetchall()
        for book in a:
            print("Book Name {}".format(book[0]))
        formatted_all_book_ids_length -= 1
    return formatted_all_book_ids #for use in the add_book_to_wishlist function

def add_book_to_wishlist(): #cant seem to get to work completely...
    work = 1
    try:
        books_to_add = show_books_to_add()
    except:
        print("something wring with function call")
        work = 0
    if work == 1: #added error handling just in case function call fails
        formatted_books_to_add_length = len(books_to_add)
        book_ids = [formatted_books_to_add_length]
        """
        while formatted_books_to_add_length > 0: #problems are here...
            mycursor.execute("SELECT book_name FROM book WHERE book_id = (%s)", (book_ids[formatted_books_to_add_length - 1]))
            a = mycursor.fetchall()
            for book in a:
                book_id = books_to_add[formatted_books_to_add_length - 1]
                book_id = str(book_id)
                print("Book ID:" + book_id)
                print("Book Name {}".format(book[0]))
            formatted_books_to_add_length -= 1
        """
        input = print("Enter the id of the book you would like to add to your wishlist: ")

        

def show_menu():
    go = 1 #true
    while go == 1:
        print("""1. View Books\n2. View Store Locations\n3. My Account\n4. Exit Program""")
        user_choice = input("Please choose one of the available options: ")
        user_choice = int(user_choice) #make same type
        if user_choice == 1:
            show_books()
        elif user_choice == 2:
            show_locations()
        elif user_choice == 3:
            if (validate_user()):
                show_account_menu()
        elif user_choice == 4:
            go = 0
        else:
            print("invalid choice, please try again")

def show_account_menu():
    go = 1
    while go == 1:
        print("""1. Show Wishlist\n2. Show Books to Add\n3. Add Book to Wishlist\n4. Exit
        """)
        user_choice = input("Please choose one of the available options: ")
        user_choice = int(user_choice) #make same type
        if user_choice == 1:
            show_wishlist()
        elif user_choice == 2:
            show_books_to_add()
        elif user_choice == 3:
            add_book_to_wishlist()
        elif user_choice == 4:
            go = 0
        else:
            print("invalid choice, please try again")

show_menu()

