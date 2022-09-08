class lib_mgmt_sys:
    def displayBooks(self):
        books = self.sort()
        for item in books:
            print("Book Name: ", item[0])
            print("Book Author: ", item[1])
            print("Quantity: ", item[2])
            print("~"*110)

    def search(self):
        bkName = ""
        authName = ""
        while True:
            print("""You can search using the following things:
                     1.) Book Name
                     2.) Book Author
                     3.) Exit""")
            choice = int(input("Choose What You Would Like To Do: "))
            if choice == 1:
                print("Please Enter")
                bkName = input("The Title You Want To Search With: ")
            if choice == 2:
                print("Please Enter")
                authName = input("The Name Of The Author You Would Like To Search: ")
            if choice == 3:
                break

        with open("allbooks.txt", "a+") as f:
            f.seek(0)
            data = f.readlines()
            list = []
            for item in data:
                item = item.split("-")
                last = item.pop()
                editedLast = ""
                for chr in last:
                    if chr == "\n":
                        continue
                    else:
                        editedLast = editedLast + chr
                item.append(editedLast)
                list.append(item)

            results = []
            for item in list:
                if item[0] == bkName:
                    results.append(item)
                if item[1] == authName:
                    results.append(item)

            return results

    def addBook(self):
        with open("allbooks.txt", "a+") as f:
            f.seek(0)
            data = f.readlines()
            list = []
            for item in data:
                item = item.split("-")
                last = item.pop()
                editedLast = ""
                for chr in last:
                    if chr == "\n":
                        continue
                    else:
                        editedLast = editedLast + chr
                item.append(editedLast)
                list.append(item)

        print("""We Have these books for you hehe: """)
        for item in list:
            print("Name Of The Book: ")
            print(f" " * 20 + f"{item[0]}")
            print("Author Of The Book: ")
            print(f" " * 20 + f"{item[1]}")
            print("Quantity Of The Book: ")
            print(f" " * 20 + f"{item[2]}")
            print("_"*50)
        print()
        print("Since you want to add a book, you'll have to add the following details of the book")
        bookName = input("Title Of The Book: ")
        authName = input("Name Of The Author: ")
        qty = int(input("Number Of Copies Of Books Available: "))

        with open("allbooks.txt", "a") as f:
            writeStr = bookName + "-" + authName + "-" + str(qty)
            f.write("\n")
            f.write(writeStr)

        print("The book is now added, thankyou")

    def editBook(self):
        with open("allbooks.txt", "a+") as f:
            f.seek(0)
            data = f.readlines()
            list = []
            for item in data:
                item = item.split("-")
                last = item.pop()
                editedLast = ""
                for chr in last:
                    if chr == "\n":
                        continue
                    else:
                        editedLast = editedLast + chr
                item.append(editedLast)
                list.append(item)
            f.close()

        print("""We Have these books for you hehe: """)
        for item in range(len(list)):
            print("Book Number: ", item + 1)
            print(f" " * 20 + f"{list[item][0]}")
            print("Author Of The Book: ")
            print(f" " * 20 + f"{list[item][1]}")
            print("Quantity Of The Book: ")
            print(f" " * 20 + f"{list[item][2]}")
            print("_" * 50)
        print()
        print("Since you intend to edit a book please enter")
        bookNum = int(input("The Number Assigned To The Book You Want To Edit: "))
        bookNum = bookNum - 1
        editedBook = list[bookNum]
        list.remove(editedBook)

        while True:
            print("""You can edit the following things:
                     1.) The Title Of The Book
                     2.) The Author Of The Book
                     3.) Number Of Books Available
                     4.) Exit""")
            option = int(input("Choose What You Would Like To Do: "))
            if option == 1:
                print("Please Enter")
                bookName = input("New Title Of The Book: ")
                editedBook[0] = bookName
            if option == 2:
                print("Please Enter")
                authName = input("Authors Name: ")
                editedBook[1] = authName
            if option == 3:
                print("Please Enter")
                qty= input("New Number Of Copies: ")
                editedBook[2] = qty
            if option == 4:
                break

        list.append(editedBook)

        with open("allbooks.txt", "w+") as f:
            for item in list:
                if item != list[-1]:
                    writeStr = item[0] + "-" + item[1] + "-" + item[2]
                    f.write(writeStr + "\n")
                else:
                    writeStr = item[0] + "-" + item[1] + "-" + item[2]
                    f.write(writeStr)

    def removeBook(self):
        with open("allbooks.txt", "a+") as f:
            f.seek(0)
            data = f.readlines()
            list = []
            for item in data:
                item = item.split("-")
                last = item.pop()
                editedLast = ""
                for chr in last:
                    if chr == "\n":
                        continue
                    else:
                        editedLast = editedLast + chr
                item.append(editedLast)
                list.append(item)
            f.close()

        print("""We Have these books for you hehe: """)
        for item in list:
            print("Name Of The Book: ")
            print(f" " * 20 + f"{item[0]}")
            print("Author Of The Book: ")
            print(f" " * 20 + f"{item[1]}")
            print("Quantity Of The Book: ")
            print(f" " * 20 + f"{item[2]}")
            print("_" * 50)
        print()
        print("Since You Want To Remove A Book Please Enter The Following Details That Are Required")
        bookName = input("Name Of The Book You Want To Remove: ")
        qty = int(input("Number Of Books You Want To Remove: "))   # quantity must be less than total no.of existing books
        removeBook = None

        for item in list:
            if item[0] == bookName:
                removeBook = item
                break

        list.remove(removeBook)

        if int(removeBook[2]) - qty == 0:
            pass
        else:
            newQty = int(removeBook[2]) - qty
            editedBook = [removeBook[0], removeBook[1], str(newQty), removeBook[3]]
            list.append(editedBook)

        with open("allbooks.txt", "w+") as f:
            for item in list:
                if item != list[-1]:
                    writeStr = item[0] + "-" + item[1] + "-" + item[2]
                    f.write(writeStr + "\n")
                else:
                    writeStr = item[0] + "-" + item[1] + "-" + item[2]
                    f.write(writeStr)

    def signup_user(self):
        print("Well You are new here, come into the unknown")
        print("Hello Mister/Missus You'll Have To Fill The Following To Create A New Account: ")
        Email = input("Enter your lovely email: ")
        password = input("Enter your lovely password: ")

        with open("useraccounts.txt", "r+") as f:
            f.seek(0)
            dat = f.readlines()
            list = []
            for user in dat:
                user = user.split("-")
                last = user.pop()
                editedLast = ""
                for chr in last:
                    if chr == "\n":
                        continue
                    else:
                        editedLast = editedLast + chr
                user.append(editedLast)
                list.append(user)
            f.close()

        for user in list:
            if Email == user[0]:
                print("Your Lovely Email Is Already In Use.")
                return False
            else:
                with open("useraccounts.txt", "a+") as f:
                    writeStr = Email + "-" + password
                    f.write("\n")
                    f.write(writeStr)
                print("Your Account Has Been Created Wallahi")
                return True

    def login_user(self):
        print("Hello Mister/Missus You'll Have To Fill The Following To Login: ")
        Email = input("Enter your lovely email: ")
        password = input("Enter your lovely password: ")

        with open("useraccounts.txt", "r+") as f:
            f.seek(0)
            data = f.readlines()
            list = []
            for user in data:
                user = user.split("-")
                last = user.pop()
                editedLast = ""
                for chr in last:
                    if chr == "\n":
                        continue
                    else:
                        editedLast = editedLast + chr
                user.append(editedLast)
                list.append(user)
            f.close()

        acc = [Email, password]
        if acc in list:
            print("You have logged in yay")
            return [True, acc[0], acc[1]]

        else:
            print("You were unable to login")
            return [False, acc[0], acc[1]]

    def delete_account(self):         # cancel membership
        print("You Have Reached The Leaving Screen, Thankyou for being here while you were")
        print("Please Enter Your Account Details")
        Email = input("Your Lovely Email: ")
        password = input("Your password: ")

        with open("useraccounts.txt", "r+") as f:
            f.seek(0)
            data = f.readlines()
            list = []
            for user in data:
                user = user.split("-")
                last = user.pop()
                editedLast = ""
                for chr in last:
                    if chr == "\n":
                        continue
                    else:
                        editedLast = editedLast + chr
                user.append(editedLast)
                list.append(user)
        removeUser = [Email, password]

        if removeUser in list:
            list.remove(removeUser)

        with open("useraccounts.txt", "w+") as f:
            for user in list:
                if user != list[-1]:
                    writeStr = user[0] + "-" + user[1]
                    f.write(writeStr + "\n")
                else:
                    writeStr = user[0] + "-" + user[1]
                    f.write(writeStr)
            print("Your account has been deleted, so long partner")
            return

    def borrow(self):
        print("You Have Come To The Checkout Page")
        print("Please Login To Continue")
        result = self.login_user()

        if result[0] == False:
            print("Your Entered Details Were Incorrect")
            return False
        else:
            with open("allbooks.txt", "a+") as f:
                f.seek(0)
                data = f.readlines()
                list = []
                for item in data:
                    item = item.split("-")
                    last = item.pop()
                    editedLast = ""
                    for chr in last:
                        if chr == "\n":
                            continue
                        else:
                            editedLast = editedLast + chr
                    item.append(editedLast)
                    list.append(item)
                f.close()

            print("""We Have these books for you hehe: """)
            for item in range(len(list)):
                print("Book Number: ", item + 1)
                print(f" " * 20 + f"{list[item][0]}")
                print("Author Of The Book: ")
                print(f" " * 20 + f"{list[item][1]}")
                print("Quantity Of The Book: ")
                print(f" " * 20 + f"{list[item][2]}")
                print("_" * 50)
            print()

            bookNum = int(input("Enter The Book Number You Would Like To Take With You: "))
            bookNum = bookNum - 1
            borrowBook = list[bookNum]
            list.remove(borrowBook)

            new_quantity = int(borrowBook[2]) - 1
            updatedBook = [borrowBook[0], borrowBook[1], str(new_quantity)]
            list.append(updatedBook)

            with open("allbooks.txt", "w+") as f:
                for item in list:
                    if item != list[-1]:
                        writeStr = item[0] + "-" + item[1] + "-" + item[2]
                        f.write(writeStr + "\n")
                    else:
                        writeStr = item[0] + "-" + item[1] + "-" + item[2]
                        f.write(writeStr)

            with open("data.txt", "a+") as f:
                f.write("\n")
                f.write(result[1] + "-check_out" + "-" + updatedBook[0])

    def reserve(self):
        print("You Have Come To The Reserve Page.")
        print("Please Enter Your Login Details")
        result = self.login_user()

        if result[0] == False:
            print("Your Entered Details Were Incorrect")
            return False
        else:
            print("Please Enter The Details Of The Book You Would Like To Reserve")
            bookName = input("The Name Of The Book: ")
            with open("data.txt","a+") as f:
                f.write("\n")
                f.write(result[1] + "-reserve" + "-" + bookName)

    def renew(self):
        print("You Have Come To The Renew Pagee.")
        print("You Have To Login Again")
        result = self.login_user()

        if result[0] == False:
            print("Your Entered Details Were Incorrect")
            return False
        else:
            with open("data.txt", "a+") as f:
                f.seek(0)
                data = f.readlines()
                infoList = []
                for item in data:
                    item = item.split("-")
                    last = item.pop()
                    editedLast = ""
                    for chr in last:
                        if chr == "\n":
                            continue
                        else:
                            editedLast = editedLast + chr
                    item.append(editedLast)
                    infoList.append(item)
                f.close()
            print("Since You Would Like To Renew, You Need To Enter")
            bookName = input("The Name Of The Book You Would Like To Renew: ")

            for item in infoList:
                if (result[1] == item[0]) and (item[1] == "check_out") and (item[2] == bookName):
                    infoList.remove(item)
                    print("The Book Has Been Renewed, Thankyouu")

                    with open("allbooks.txt", "a+") as f:
                        f.seek(0)
                        data = f.readlines()
                        book_lists = []
                        for item in data:
                            item = item.split("-")
                            last = item.pop()
                            editedLast = ""
                            for chr in last:
                                if chr == "\n":
                                    continue
                                else:
                                    editedLast = editedLast + chr
                            item.append(editedLast)
                            book_lists.append(item)
                        f.close()

                    with open("data.txt", "w+") as f:
                        f.write(result[1] + "-" + "renew" + "-" + bookName)
                        f.write("\n")

                        for item in infoList:
                            if item != infoList[-1]:
                                writeStr = item[0] + "-" + item[1] + "-" + item[2]
                                f.write(writeStr + "\n")
                            else:
                                writeStr = item[0] + "-" + item[1] + "-" + item[2]
                                f.write(writeStr)
                                return

    def returnn(self):
        print("You Have Come To The Return Page.")
        print("Please Enter Your Login Details")
        result = self.login_user()

        if result[0] == False:
            print("Your Entered Details Were Incorrect")
            return False
        else:
            with open("data.txt", "a+") as f:
                f.seek(0)
                data = f.readlines()
                infoList = []
                for item in data:
                    item = item.split("-")
                    last = item.pop()
                    editedLast = ""
                    for chr in last:
                        if chr == "\n":
                            continue
                        else:
                            editedLast = editedLast + chr
                    item.append(editedLast)
                    infoList.append(item)
                f.close()

            print("Since you would like to return your book, please enter")
            bookName = input("The Name Of The Book You Would Like To Return: ")
            for item in infoList:
                if (result[1] == item[0]) and ((item[1] == "check_out") or (item[1] == "renew")) and (item[2] == bookName):
                    infoList.remove(item)
                    print("The Book Has Been Returned, Thankyouu")

                    with open("allbooks.txt", "a+") as f:
                        f.seek(0)
                        data = f.readlines()
                        book_lists = []
                        for item in data:
                            item = item.split("-")
                            last = item.pop()
                            editedLast = ""
                            for chr in last:
                                if chr == "\n":
                                    continue
                                else:
                                    editedLast = editedLast + chr
                            item.append(editedLast)
                            book_lists.append(item)
                        f.close()

                    returnBook = None
                    for item in book_lists:
                        if item[0] == bookName:
                            returnBook = item

                    newQty = int(returnBook[2]) + 1
                    updated_book = [returnBook[0], returnBook[1], str(newQty)]
                    book_lists.append(updated_book)

                    with open("allbooks.txt", "w+") as f:
                        for item in book_lists:
                            if item != book_lists[-1]:
                                writeStr = item[0] + "-" + item[1] + "-" + item[2]
                                f.write(writeStr + "\n")
                            else:
                                writeStr = item[0] + "-" + item[1] + "-" + item[2]
                                f.write(writeStr)

                    with open("data.txt", "w+") as f:
                        for item in infoList:
                            if item != infoList[-1]:
                                writeStr = item[0] + "-" + item[1] + "-" + item[2]
                                f.write(writeStr + "\n")
                            else:
                                writeStr = item[0] + "-" + item[1] + "-" + item[2]
                                f.write(writeStr)
                                return

    def sort(self):
        with open("allbooks.txt", "a+") as f:
            f.seek(0)
            data = f.readlines()
            list = []
            for item in data:
                item = item.split("-")
                last = item.pop()
                editedLast = ""
                for chr in last:
                    if chr == "\n":
                        continue
                    else:
                        editedLast = editedLast + chr
                item.append(editedLast)
                list.append(item)
        lengthList = len(list)
        for i in range(lengthList - 1):
            for j in range(lengthList - i - 1):
                if list[j] > list[j + 1]:
                    list[j], list[j + 1] = list[j + 1], list[j]
        return list


print("it is said then when you are in doubt go to the library, so i know why you are here *winks*" )
print("Welcome To The Library, May your nights be long and Covers be hard")

obj = lib_mgmt_sys()
while True:
    print("""You can do the following things heree:
                1.) You can display books
                2.) You can search in books
                3.) You can create account
                4.) You can delete your account
                5.) Admin can add a book
                6.) Admin can delete/remove a book
                7.) Admin can edit a book
                8.) You can renew a book
                9.) You can reserve a book
                10.) You can return a book
                11.) You can borrow a book
                12.) You can Exit""")
    option = int(input("Enter option: "))
    if option == 1:
        obj.displayBooks()

    if option == 2:
        print(obj.search())

    if option == 3:
        obj.signup_user()

    if option == 4:
        obj.delete_account()

    if option == 5:
        obj.addBook()

    if option == 6:
        obj.removeBook()

    if option == 7:
        obj.editBook()

    if option == 8:
        obj.renew()

    if option == 9:
        obj.reserve()

    if option == 10:
        obj.returnn()

    if option == 11:
        obj.borrow()

    if option == 12:
        print("Thankyou For Being Heree")
        break
