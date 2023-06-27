from productsData import *
import users
import getpass as illusion
import progressbar as progress
import time
products = []
totalPrice = []
try:
    def progressBar():
        
        widgets = ['Loading: ', progress.AnimatedMarker()]
        bar = progress.ProgressBar(widgets=widgets).start()
        
        for i in range(20):
            time.sleep(0.1)
            bar.update(i)
    def userData():
        print("\033[0;34;40m*******************************************")
        print("\033[1;34;40m                 User Data                 ")
        print("                -----------                \n")
        print("\033[0;34;40m\t1. View Users\n\t2. View Admin\n\t3. Add User\n\t4. Remove User\n\t5. Add Admin\n\t6. Remove Admin\n\t7. Admin Panel ")
        print("*******************************************\033[0;37;40m")
        select = int(input("Select:"))
        match select:
            case 1:
                users.showUsers()
                userData()
            case 2:
                users.showAdmin()
                userData()
            case 3:
                print("\n---------------------")
                userName = input("   Enter your username: ")
                print("---------------------")
                while (userName == '') or (len(userName)<2):
                    print("\033[0;31;40mEnter Valid User Name!\033[0;37;40m")
                    print("---------------------")
                    userName = input("   Enter your name: ")
                    print("---------------------")
                pswd = illusion.getpass('   Password (Minimum length of 8):')
                print("---------------------")
                while (pswd == '') or (len(pswd)<2):
                    print("\033[0;31;40mEnter Valid Password!\033[0;37;40m")
                    print("---------------------")
                    pswd = illusion.getpass('   Password (Minimum length of 8):')
                    print("\n---------------------")
                users.createUser(userName,pswd,admin=False)
                progressBar()
                print("\033[0;32;40mUser created successfully!\033[0;37;40m")
                userData()
            case 4:
                users.showUsers()
                choice = int(input("Select user:"))
                print("---------------------")
                users.removeUser(choice,admin=False)
                print("\033[0;34;40m<<<  Updated Table  >>>\033[0;37;40m")
                users.showUsers()
            case 5:
                print("============ Admin List ============")
                users.showAdmin()
                ch = int(input("Select:"))
                print("\n---------------------")
                userName = input("   Enter your username: ")
                print("---------------------")
                while (userName == '') or (len(userName)<2):
                    print("\033[0;31;40mEnter Valid User Name!\033[0;37;40m")
                    print("---------------------")
                    userName = input("   Enter your name: ")
                    print("---------------------")
                pswd = illusion.getpass('   Password (Minimum length of 8):')
                print("---------------------")
                while (pswd == '') or (len(pswd)<2):
                    print("\033[0;31;40mEnter Valid Password!\033[0;37;40m")
                    print("---------------------")
                    pswd = illusion.getpass('   Password (Minimum length of 8):')
                    print("\n---------------------")
                users.createUser(userName,pswd,admin=True)
                progressBar()
                print("\033[0;32;40mAdmin created successfully!\033[0;37;40m")
                userData()
            case 6:
                users.showAdmin()
                choice = int(input("Select admin:"))
                print("---------------------")
                users.removeUser(choice,admin=True)
                print("\033[0;34;40m<<<  Updated Table  >>>\033[0;37;40m")
                users.showAdmin()
            case 7:
                adminMain()
    def mobSelection(no,admin,add,rem):
        if (admin == 0) and (add == 0) and (rem ==0):
            while 1:
                print("========== 📱 MOBILES 📱 ==========")
                for i in productsMain['mobile']:
                    print("\t",no,"\b.",productsMain['mobile'][i]['Name'])
                    no +=1
                print("(",no,")","\033[0;31;40mExit\033[0;37;40m")
                
                print("==============================")
                select = int(input("Select: "))
                print("------------------------------")
                if select == no:
                    main()        
                list1 = list(productsMain['mobile'])[select-1]
                print("\tYou Selected: ")
                print("\t------------")
                name = productsMain['mobile'][str(list1)]['Name']
                price = productsMain['mobile'][str(list1)]['Price']
                print("\033[0;34;40m|\033[0;37;40m Name:  ",name)
                print("\033[0;34;40m|\033[0;37;40m Price: ",price)
                print("-------------------------")
                cart = input("Add to cart? (y/n): ")
                print("-------------------------")
                if cart.lower() == 'y':
                    products.append(name)
                    totalPrice.append(price)
                    # progressBar()
                    print("\033[0;32;40m<<< Successfully Added to Cart! >>>\033[0;37;40m")
                    print("===========================================\n")
                    return
                elif cart.lower() == 'n':
                    return
                else: 
                    print("Invalid choice!")
        elif (admin == 1) and (add == 1) and (rem == 0):
            count = 1
            print("========== 📱 MOBILES STOCK 📱 ==========")
            for i in productsMain['mobile']:
                print("\t",no,"\b.",productsMain['mobile'][i]['Name'])
                no +=1
            print("==============================")
            noOfMobToAdd = int(input("No of mobiles to add:"))
            while noOfMobToAdd != 0:
                print("------------------------------")
                prodName = input(f"Mobile {count} name:")
                print("------------------------------")
                prodPrice = input(f"Mobile {count} prince:")
                print("------------------------------")
                addproduct(prodName,prodPrice,'mobile')
                print(f"Product '{prodName}' Successfully Added!")
                count+=1
                noOfMobToAdd-=1
                viewProducts()
        elif (admin == 1) and (add == 0) and (rem == 1):
            print("========== 📱 MOBILES STOCK 📱 ==========")
            for i in productsMain['mobile']:
                print("\t",no,"\b.",productsMain['mobile'][i]['Name'])
                no +=1
            print("(",no,")","\033[0;31;40mExit\033[0;37;40m")
            print("==============================")
            select = int(input("Select to remove: "))
            while (select != no) or select == 0:
                removeProduct(select,'mobile')
                no = 1
                print("========== 📱 MOBILES STOCK 📱 ==========")
                for i in productsMain['mobile']:
                    print("\t",no,"\b.",productsMain['mobile'][i]['Name'])
                    no +=1
                print("(",no,")","\033[0;31;40mExit\033[0;37;40m")
                print("==============================")
                select = int(input("Select to remove: "))
            else:
                return
    def laptopSelection(no,admin,add,rem):
        if (admin == 0) and (add == 0) and (rem ==0):
            while 1:
                print("========== 💻 LAPTOPS 💻 ==========")
                for i in productsMain['laptop']:
                    print("\t",no,"\b.",productsMain['laptop'][i]['Name'])
                    no +=1
                print("(",no,")","\033[0;31;40mExit\033[0;37;40m")
                
                print("==============================")
                select = int(input("Select: "))
                print("------------------------------")
                if select == no:
                    main()        
                list1 = list(productsMain['laptop'])[select-1]
                print("\tYou Selected: ")
                print("\t------------")
                name = productsMain['laptop'][str(list1)]['Name']
                price = productsMain['laptop'][str(list1)]['Price']
                print("\033[0;34;40m|\033[0;37;40m Name:  ",name)
                print("\033[0;34;40m|\033[0;37;40m Price: ",price)
                print("-------------------------")
                cart = input("Add to cart? (y/n): ")
                print("-------------------------")
                if cart.lower() == 'y':
                    products.append(name)
                    totalPrice.append(price)
                    print("\033[0;32;40m<<< Successfully Added to Cart! >>>\033[0;37;40m")
                    print("===========================================\n")
                    return
                elif cart.lower() == 'n':
                    return
                else: 
                    print("Invalid choice!")
        elif (admin == 1) and (add == 1) and (rem == 0):
            count = 1
            print("========== 💻 LAPTOPS STOCK 💻 ==========")
            for i in productsMain['laptop']:
                print("\t",no,"\b.",productsMain['laptop'][i]['Name'])
                no +=1
            print("==============================")
            noOfMobToAdd = int(input("No of laptops to add:"))
            while noOfMobToAdd != 0:
                print("------------------------------")
                prodName = input(f"Laptop {count} name:")
                print("------------------------------")
                prodPrice = input(f"Laptop {count} prince:")
                print("------------------------------")
                addproduct(prodName,prodPrice,'laptop')
                print(f"Product '{prodName}' Successfully Added!")
                count+=1
                noOfMobToAdd-=1
                viewProducts()
        elif (admin == 1) and (add == 0) and (rem == 1):
            print("========== 💻 LAPTOPS STOCK 💻 ==========")
            for i in productsMain['laptop']:
                print("\t",no,"\b.",productsMain['laptop'][i]['Name'])
                no +=1
            print("(",no,")","\033[0;31;40mExit\033[0;37;40m")
            print("==============================")
            select = int(input("Select to remove: "))
            while (select != no) or select == 0:
                removeProduct(select,'laptop')
                no = 1
                print("========== 💻 LAPTOPS STOCK 💻 ==========")
                for i in productsMain['laptop']:
                    print("\t",no,"\b.",productsMain['laptop'][i]['Name'])
                    no +=1
                print("(",no,")","\033[0;31;40mExit\033[0;37;40m")
                print("==============================")
                select = int(input("Select to remove: "))
            else:
                return
    def shosSelection(no,admin,add,rem):
        if (admin == 0) and (add == 0) and (rem ==0):
            while 1:
                print("========== 👞 SHOES 👞 ==========")
                for i in productsMain['shoes']:
                    print("\t",no,"\b.",productsMain['shoes'][i]['Name'])
                    no +=1
                print("(",no,")","\033[0;31;40mExit\033[0;37;40m")
                # no = 0
                print("==============================")
                select = int(input("Select: "))
                print("------------------------------")
                if select == no:
                    main()        
                list1 = list(productsMain['shoes'])[select-1]
                print("\tYou Selected: ")
                print("\t------------")
                name = productsMain['shoes'][str(list1)]['Name']
                price = productsMain['shoes'][str(list1)]['Price']
                print("\033[0;34;40m|\033[0;37;40m Name:  ",name)
                print("\033[0;34;40m|\033[0;37;40m Price: ",price)
                print("-------------------------")
                cart = input("Add to cart? (y/n): ")
                print("-------------------------")
                if cart.lower() == 'y':
                    products.append(name)
                    totalPrice.append(price)
                    print("\033[0;32;40m<<< Successfully Added to Cart! >>>\033[0;37;40m")
                    print("===========================================\n")
                    return
                elif cart.lower() == 'n':
                    return
                else: 
                    print("Invalid choice!")
        elif (admin == 1) and (add == 1) and (rem == 0):
            count = 1
            print("========== 👞 SHOES STOCK 👞 ==========")
            for i in productsMain['shoes']:
                print("\t",no,"\b.",productsMain['shoes'][i]['Name'])
                no +=1
            # print("(",no,")","\033[0;31;40mExit\033[0;37;40m")
            print("==============================")
            # select = int(input("Select: "))
            noOfMobToAdd = int(input("No of shoes to add:"))
            while noOfMobToAdd != 0:
                print("------------------------------")
                prodName = input(f"Shoes {count} name:")
                print("------------------------------")
                prodPrice = input(f"Shoes {count} prince:")
                print("------------------------------")
                addproduct(prodName,prodPrice,'shoes')
                print(f"Product '{prodName}' Successfully Added!")
                count+=1
                noOfMobToAdd-=1
                viewProducts()
        elif (admin == 1) and (add == 0) and (rem == 1):
            print("========== 👞 SHOES STOCK 👞 ==========")
            for i in productsMain['shoes']:
                print("\t",no,"\b.",productsMain['shoes'][i]['Name'])
                no +=1
            print("(",no,")","\033[0;31;40mExit\033[0;37;40m")
            print("==============================")
            select = int(input("Select to remove: "))
            while (select != no) or select == 0:
                removeProduct(select,'shoes')
                no = 1
                print("========== 👞 SHOES STOCK 👞 ==========")
                for i in productsMain['shoes']:
                    print("\t",no,"\b.",productsMain['shoes'][i]['Name'])
                    no +=1
                print("(",no,")","\033[0;31;40mExit\033[0;37;40m")
                print("==============================")
                select = int(input("Select to remove: "))
            else:
                return
    def clothesSelection(no,admin,add,rem):
        if (admin == 0) and (add == 0) and (rem ==0):
            while 1:
                print("========== 👕 CLOTHES 👕 ==========")
                for i in productsMain['cloth']:
                    print("\t",no,"\b.",productsMain['cloth'][i]['Name'])
                    no +=1
                print("(",no,")","\033[0;31;40mExit\033[0;37;40m")
                # no = 0
                print("==============================")
                select = int(input("Select: "))
                print("------------------------------")
                if select == no:
                    main()        
                list1 = list(productsMain['cloth'])[select-1]
                print("\tYou Selected: ")
                print("\t------------")
                name = productsMain['cloth'][str(list1)]['Name']
                price = productsMain['cloth'][str(list1)]['Price']
                print("\033[0;34;40m|\033[0;37;40m Name:  ",name)
                print("\033[0;34;40m|\033[0;37;40m Price: ",price)
                print("-------------------------")
                cart = input("Add to cart? (y/n): ")
                print("-------------------------")
                if cart.lower() == 'y':
                    products.append(name)
                    totalPrice.append(price)
                    print("\033[0;32;40m<<< Successfully Added to Cart! >>>\033[0;37;40m")
                    print("===========================================\n")
                    return
                elif cart.lower() == 'n':
                    return
                else: 
                    print("Invalid choice!")
        elif (admin == 1) and (add == 1) and (rem == 0):
            count = 1
            print("========== 👕 CLOTHES STOCK 👕 ==========")
            for i in productsMain['cloth']:
                print("\t",no,"\b.",productsMain['cloth'][i]['Name'])
                no +=1
            # print("(",no,")","\033[0;31;40mExit\033[0;37;40m")
            print("==============================")
            # select = int(input("Select: "))
            noOfMobToAdd = int(input("No of cloths to add:"))
            while noOfMobToAdd != 0:
                print("------------------------------")
                prodName = input(f"Cloth {count} name:")
                print("------------------------------")
                prodPrice = input(f"Cloth {count} prince:")
                print("------------------------------")
                addproduct(prodName,prodPrice,'cloth')
                print(f"Product '{prodName}' Successfully Added!")
                count+=1
                noOfMobToAdd-=1
                viewProducts()
        elif (admin == 1) and (add == 0) and (rem == 1):
            print("========== 👕 CLOTHES STOCK 👕 ==========")
            for i in productsMain['cloth']:
                print("\t",no,"\b.",productsMain['cloth'][i]['Name'])
                no +=1
            print("(",no,")","\033[0;31;40mExit\033[0;37;40m")
            print("==============================")
            select = int(input("Select to remove: "))
            while (select != no) or select == 0:
                removeProduct(select,'cloth')
                no = 1
                print("========== 👕 CLOTHES STOCK 👕 ==========")
                for i in productsMain['cloth']:
                    print("\t",no,"\b.",productsMain['cloth'][i]['Name'])
                    no +=1
                print("(",no,")","\033[0;31;40mExit\033[0;37;40m")
                print("==============================")
                select = int(input("Select to remove: "))
            else:
                return
    def showProducts(choice):
        no = 1
        # viewProducts()
        global products
        global totalPrice
        while 1:
            if choice == 1:
                mobSelection(no,admin=0,add=0,rem=0)
            elif choice == 2:
                laptopSelection(no,admin=0,add=0,rem=0)
            elif choice == 3:
                shosSelection(no,admin=0,add=0,rem=0)
            elif choice == 4:
                clothesSelection(no,admin=0,add=0,rem=0)
            else:
                show()
                
    choice = 0
    def main():
        while 1:
            print("\n========== Surf Through ==========")
            print("\t1. Products\n\t2. Your Cart\n\t3. \033[0;31;40mExit\033[0;37;40m")
            print("====================================")
            choice = int(input("Enter choice: "))
            match choice:
                case 1:
                    show()
                case 2:
                    cart()
                case 3:
                    print("\033[1;35;40m<<\033[0;37;40m Happy Shopping \033[1;35;40m>>\033[1;34;40m")
                    exit()
    def show():
        # global choice
        print("========== Categories ==========")
        print("\t1. Mobiles\n\t2. Laptops\n\t3. Shoes\n\t4. Clothes\n\t5. \033[0;31;40mExit\033[0;37;40m")
        print("===============================")
        choice = int(input("Select your category: "))
        while choice!=5:
            showProducts(choice)
            print("========== Categories ==========")
            print("\t1. Mobiles\n\t2. Laptops\n\t3. Shoes\n\t4. Clothes\n\t5. \033[0;31;40mExit\033[0;37;40m")
            print("===============================")
            choice = int(input("Select your category: "))
        # if choice == 5:
        #     main()
    def cart():
        global products
        count = 1
        sum = 0
        global totalPrice
        print("================== Your cart ==================\n")
        print("--------------- Products List ---------------")
        if products == []:
            print("\tEmpty Cart !")
        for i in products:
            print("\t","| ",count,"\b.",i)
            count+=1
        print("------------------------------------")
        print("\033[0;34;40m<<< Total products:",len(products),">>>\033[0;37;40m")
        # print("------------------------------------")
        for i in totalPrice:
            sum += int(i)
        print("\033[0;34;40m<<< Total Price",sum, ">>>\033[0;37;40m")
        print("------------------------------------")
        if (products!=[]) and(totalPrice!=[]):
            print("Proceed to checkout? (y/n)")
            checkout = input()
            if checkout == 'y':
                print("Total amount: ", sum)
                enterAmount = int(input("Enter your total amount: "))
                progressBar()
                text = '\033[0;32;40m--- Successfully Checked Out! ---'
                text1 = '--- (Cart Cleared) ---\033[0;37;40m'
                if enterAmount == sum:
                    for letter in text:
                        print(letter, end='', flush=True)   
                        time.sleep(0.01) 
                    print("\n")
                    for letter in text1:
                        print(letter, end='', flush=True)   
                        time.sleep(0.01) 
                    # print("--- Successfully Checked Out! ---")
                while sum != enterAmount:
                    print("Re-enter again")
                    enterAmount = int(input("Enter your total amount: "))
                products = []
                totalPrice = []
            elif checkout == 'n':
                main()
            else: 
                print("Invalid choice!")
                return
            print("\n=====================")
    def welcome(userName,admin):
        if admin == 1:
            print(f"▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪")
            text =f"|             Welcome to the Store Mustafa             |"
            for letter in text:
                print(letter, end='', flush=True)   
                time.sleep(0.01) 
            print(f"\n▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪")
            adminMain()   
        elif admin == 0:
            print(f"▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪")
            text =f"|            Welcome to the Store {userName}            |"
            for letter in text:
                print(letter, end='', flush=True)   
                time.sleep(0.01) 
            print(f"\n▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪▫▪")
            main()
    def userAccess():
        print("\n\t1. Login\n\t2. Register\n\t3. Admin")
        print("---------------------\033[0;37;40m")
        choice = int(input("Select to proceed:"))
        match choice:
            case 1:
                login()
            case 2:
                register()
            case 3:
                admin()
                
        print("===================================")

    def register():
        print("\n---------------------")
        userName = input("   Enter your username: ")
        print("---------------------")
        while (userName == '') or (len(userName)<2):
            print("\033[0;31;40mEnter Valid User Name!\033[0;37;40m")
            print("---------------------")
            userName = input("   Enter your name: ")
            print("---------------------")
        pswd = illusion.getpass('   Password (Minimum length of 8):')
        print("---------------------")
        while (pswd == '') or (len(pswd)<2):
            print("\033[0;31;40mEnter Valid Password!\033[0;37;40m")
            print("---------------------")
            pswd = illusion.getpass('   Password (Minimum length of 8):')
            print("\n---------------------")
        users.createUser(userName,pswd,admin=False)
        print("\033[0;32;40mUser created successfully!\033[0;37;40m")
        userAccess()
    def login():
        print("\n---------------------")
        userName = input("   Enter your username: ")
        print("---------------------")
        while (userName == '') or (len(userName)<2):
            print("\033[0;31;40mEnter Valid User Name!\033[0;37;40m")
            print("---------------------")
            userName = input("   Enter your username: ")
            print("---------------------")
        pswd = illusion.getpass('Password:')
        print("---------------------")
        while (pswd == '') or (len(pswd)<2):
            print("\033[0;31;40mEnter Valid Password!\033[0;37;40m")
            print("---------------------")
            pswd = illusion.getpass('   Password:')
            print("---------------------")
        if users.getUser(userName,pswd,admin=False) == True:
            print("\033[0;32;40mSuccessfully Logged In!\033[0;37;40m")
            welcome(userName,admin=0)
        else:
            print("\033[0;31;40m__                ___\033[0;37;40m")
            print("\033[0;31;40m___User not found!___\033[0;37;40m")
            reg = input("Register? (y/n)")
            while (reg.lower()!='y') or (reg.lower()!='n'):
                print("\033[0;31;40mInvalid selection!\033[0;37;40m")
                reg = input("Register? (y/n)")
            if reg.lower() == 'y':
                register()
            else:
                userAccess()
    def admin():
        print("\n---------------------")
        userName = input("   Enter your username: ")
        print("---------------------")
        while (userName == '') or (len(userName)<2):
            print("\033[0;31;40mEnter Valid User Name!\033[0;37;40m")
            print("---------------------")
            userName = input("   Enter your username: ")
            print("---------------------")
        pswd = illusion.getpass('Password:')
        print("---------------------")
        while (pswd == '') or (len(pswd)<2):
            print("\033[0;31;40mEnter Valid Password!\033[0;37;40m")
            print("---------------------")
            pswd = illusion.getpass('Password:')
            print("---------------------")
        if users.getUser(userName,pswd,admin=True) == True:
            print("\033[0;32;40mAdmin Logged In!\033[0;37;40m")
            welcome(userName,admin=1)
        else:
            print("\033[0;31;40m__                ___\033[0;37;40m")
            print("\033[0;31;40m___Admin not found!___\033[0;37;40m")
            userAccess()

    def viewProducts():
        no = 1
        print("========== Nexus Products ==========")
        print("\t1. View\n\t2. Add\n\t3. Remove\n\t4. \033[0;31;40mExit\033[0;37;40m")
        print("===============================")
        choice = int(input("Select: "))
        while 1:
            match choice:
                case 1:
                    while 1:
                        print("---------- Categories ----------")
                        print("\t1. Mobiles\n\t2. Laptops\n\t3. Shoes\n\t4. Clothes\n\t5. \033[0;31;40mExit\033[0;37;40m")
                        print("-------------------------------")
                        ctgSelection = int(input("Select category: "))
                        while 1:
                            match ctgSelection:
                                case 1:
                                    while 1:
                                        print("========== 📱 MOBILES 📱 ==========")
                                        totalspLen = 25
                                        for i in productsMain['mobile']:
                                            strLen = len(productsMain['mobile'][i]['Name'])+1
                                            spLen = totalspLen - strLen
                                            if len(productsMain['mobile'])>9:
                                                spLen-=1
                                            sp = (' '*spLen)
                                            print("\t|",no,"\b.",productsMain['mobile'][i]['Name'],sp,"$",productsMain['mobile'][i]['Price'])
                                            no +=1
                                        print("(",no,")","\033[0;31;40mExit\033[0;37;40m")
                                        print("==============================")
                                        select1 = int(input("Enter choice: "))
                                        if select1 == no:
                                            viewProducts()
                                        else:
                                            no = 1
                                            continue
                                case 2:
                                    while 1:
                                        print("========== 💻 LAPTOPS 💻 ==========")
                                        for i in productsMain['laptop']:
                                            print("\t",no,"\b.",productsMain['laptop'][i]['Name'])
                                            no +=1
                                        print("(",no,")","\033[0;31;40mExit\033[0;37;40m")
                                        print("==============================")
                                        select2 = int(input("Enter choice: "))
                                        if select2 == no:
                                            no = 1
                                            viewProducts()
                                            break
                                        else:
                                            no = 1
                                            continue
                                case 3:
                                    while 1:
                                        print("========== 👞 SHOES 👞 ==========")
                                        for i in productsMain['shoes']:
                                            print("\t",no,"\b.",productsMain['shoes'][i]['Name'])
                                            no +=1
                                        print("(",no,")","\033[0;31;40mExit\033[0;37;40m")
                                        print("==============================")
                                        select3 = int(input("Enter choice: "))
                                        if select3 == no:
                                            no = 1
                                            viewProducts()
                                            break
                                        else:
                                            no = 1
                                            continue
                                case 4:
                                    while 1:
                                        print("========== 👕 CLOTHES 👕 ==========")
                                        for i in productsMain['cloth']:
                                            print("\t",no,"\b.",productsMain['cloth'][i]['Name'])
                                            no +=1
                                        print("(",no,")","\033[0;31;40mExit\033[0;37;40m")
                                        print("==============================")
                                        select4 = int(input("Enter choice: "))
                                        if select4 == no:
                                            no = 1
                                            viewProducts()
                                            break
                                        else:
                                            no = 1
                                            continue
                                case _:
                                    print("Invalind selection!")
                            if ctgSelection == 5:
                                break
                case 2:
                    while 1:
                        print("---------- Categories ----------")
                        print("\t1. Mobiles\n\t2. Laptops\n\t3. Shoes\n\t4. Clothes\n\t5. \033[0;31;40mExit\033[0;37;40m")
                        print("-------------------------------")
                        ctgSelection = int(input("Select category: "))
                        match ctgSelection:
                            case 1:
                                mobSelection(no,admin = 1,add=1,rem=0)
                            case 2:
                                laptopSelection(no,admin = 1,add=1,rem=0)
                            case 3:
                                shosSelection(no,admin = 1,add=1,rem=0)
                            case 4:
                                clothesSelection(no,admin = 1,add=1,rem=0)
                            case 5:
                                viewProducts()
                case 3:
                    while 1:
                        print("---------- Categories ----------")
                        print("\t1. Mobiles\n\t2. Laptops\n\t3. Shoes\n\t4. Clothes\n\t5. \033[0;31;40mExit\033[0;37;40m")
                        print("-------------------------------")
                        ctgSelection = int(input("Select category: "))
                        match ctgSelection:
                            case 1:
                                mobSelection(no,admin = 1,add = 0,rem=1)
                            case 2:
                                laptopSelection(no,admin = 1,add = 0,rem=1)
                            case 3:
                                shosSelection(no,admin = 1,add = 0,rem=1)
                            case 4:
                                clothesSelection(no,admin = 1,add = 0,rem=1)
                            case 5:
                                viewProducts()
                case 4:
                    adminMain()
    def adminMain():
        while 1:
            print("\n==========  Admin Panel ==========")
            print("\t1. View Products\n\t2. Users\n\t3. \033[0;31;40mExit\033[0;37;40m")
            print("====================================")
            choice = int(input("Enter choice: "))
            match choice:
                case 1:
                    viewProducts()
                case 2:
                    userData()
                case 3:
                    print("<< Happy Shopping >>")
                    exit()

    print("\n\033[0;37;40m************************************************************")
    print("\033[1;34;40m                  N E X U S  S H O P P I N G                  ")
    print("\033[0;37;40m************************************************************\033[0;34;40m")
    userAccess()
    print("\033[0;37;40m")
except IndexError:
    print("\033[0;31;40mError: Invalid choice!\033[0;37;40m")
except ImportError:
    print("\033[0;31;40mError: Please install a neccessary module!\033[0;37;40m")
except IndentationError:
    print("\033[0;31;40mError: Indentation Error\033[0;37;40m")
except KeyError:
    print("\033[0;31;40mError: Key doesn't exist\033[0;37;40m")
except KeyboardInterrupt:
    print("\033[0;31;40mError: Keyboard Interrupted\033[0;37;40m")
except NameError:
    print("\033[0;31;40mError: Missing Variable\033[0;37;40m")
except SyntaxError:
    print("\033[0;31;40mSyntax Error!\033[0;37;40m")
except TypeError:
    print("\033[0;31;40mError: Cannot combine two different types\033[0;37;40m")
except ValueError:
    print("\033[0;31;40mError: Please enter correct data\033[0;37;40m")
except ZeroDivisionError:
    print("\033[0;31;40mError: Cannot divide by zero\033[0;37;40m")
except ArithmeticError:
    print("\033[0;31;40mError: Exception Condition\033[0;37;40m")
