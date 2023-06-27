users = {
    'user1':{
        'username': 'must',
        'password': 'must01'
    },
    'user2':{
        'username': 'ro123',
        'password': 'pass00010'
    },
    'user3':{
        'username': 'helloworld',
        'password': '1058493021'
    }
}
adminLogin = {
    'admin1':{
        'username':'root01x',
        'password':'root01x'
    }
}
adminLen = len(adminLogin)
usersLen = len(users)
try:
    def getUser(NAME, PASSWORD,admin):
        if admin == True:
            for i in adminLogin:
                if NAME == adminLogin[i]['username']:
                    if PASSWORD == adminLogin[i]['password']:
                        return True
                    return False
                return False
        else:
            for i in users:
                if NAME == users[i]['username']:
                    if PASSWORD == users[i]['password']:
                        return True
                    return False
                else:
                    return False
    # def adminAccess(NAME, PASSWORD):
    #     for i in adminLogin:
            
    #         if NAME == adminLogin[i]['username']:
    #             if PASSWORD == adminLogin[i]['password']:
    #                 return True
    #             return False
    #         return False
    def showUsers():
        sno = 1
        print("----------------------------------------------------------")
        print("|\b","SNo","|       Username       |        Password       |")
        print("----------------------------------------------------------")
        totalspLen = 20
            
        for i in users:
            usrnmLen = len(users[i]['username'])
            usrnspLen = (totalspLen - usrnmLen)
            usrnsp = (' '*usrnspLen)
            pswdLen = len(users[i]['password'])
            pswdSpLen = (totalspLen - pswdLen)
            pswdsp = (' '*pswdSpLen)
            print("|",sno,"|",users[i]['username'],usrnsp,"|",users[i]['password'],pswdsp,"|")
            sno+=1
        print("----------------------------------------------------------")
        return


    def showAdmin():
        sno = 1
        print("----------------------------------------------------------")
        print("|\b","SNo","|        Name         |         Password       |")
        print("----------------------------------------------------------")
        totalspLen = 20
            
        for i in adminLogin:
            usrnmLen = len(adminLogin[i]['username'])
            usrnspLen = (totalspLen - usrnmLen)
            usrnsp = (' '*usrnspLen)
            pswdLen = len(adminLogin[i]['password'])
            pswdSpLen = (totalspLen - pswdLen)
            pswdsp = (' '*pswdSpLen)
            print("|",sno,"| ",adminLogin[i]['username'],usrnsp,"|",adminLogin[i]['password'],pswdsp,"|")
            sno+=1
        print("----------------------------------------------------------")
        return
    def createUser(NAME, PASSWORD,admin):
        if admin==True:
            global adminLen
            adminLen += 1
            users.update({f'admin{adminLen}':{
                f'username{adminLen}':NAME,
                f'password{adminLen}':PASSWORD
            }})
        else:
            global usersLen
            usersLen += 1
            users.update({f'user{usersLen}':{
                f'username{usersLen}':NAME,
                f'password{usersLen}':PASSWORD
            }})

    # def addAdmin(NAME, PASSWORD):
    #     global adminLen
    #     adminLen += 1
    #     users.update({f'admin{adminLen}':{
    #         f'username{adminLen}':NAME,
    #         f'password{adminLen}':PASSWORD
    #     }})
    def removeUser(choice,admin):
        if admin==True:
            adminCheck = list(adminLogin)[choice-1]    
            adminLogin.pop(str(adminCheck))
            return
        else:
            showUsers()
            userCheck = list(users)[choice-1]    
            users.pop(str(userCheck))
            return
    # def removeAdmin(choice):
    #     # showUsers()
    #     # for i in users:
    #     adminCheck = list(adminLogin)[choice-1]    
    #     adminLogin.pop(str(adminCheck))
    #     # showUsers()
    #     return
    # # print(userCheck)
except KeyError:
    print("\033[0;31;40mError: Key doesn't exist\033[0;37;40m")