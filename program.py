import time
import requests
from bs4 import BeautifulSoup as B

r = requests.get("https://www.frescobaldi.london/a-la-carte")
s = B(r.text, "html.parser")
menu = s.find_all("p", class_ = "font_8")


print("press 0 to sign in as a customer or 1 to sign in as a employee")
type_ = int(input())
if type_ == 0:
    type__ = "customer"
    
elif type_ == 1:
    print("enter your id and password")
    rob = "rob 1234"
    steve = "steve qwerty"
    credencials = input()
    if credencials == "rob 1234":
        print("you have signed in as rob")
        type__ = "employee"

    elif credencials == "steve qwerty":
        print("you have signed in as rob")
        type__ = "employee"

    else:
        print("wrong id or password")
    
    
if type__ == "employee":
    while True:
        print("\n\n\nwhat you want to do?\n")
        actions_e = ["\nview my salary (press 0)", "\nview other employees phone (press 1)"]
        for i in actions_e:
            print(i)
        action = int(input()) 
        if action == 0 and credencials == "rob 1234":
            print("your salary is 1200$ at month")
              
        if action == 0 and credencials == "steve qwerty":
            print("your salary is 900$ at month")

        if action == 1:
            print("steve: +1 555 555 5555\nrob: +1 555 555 5556")

        time.sleep(2)


if type__ == "customer":
    while True:
        actions_c = ["view menu(press 0)", "place an order(press 1)"]
        for j in actions_c:
            print(j)
        choice = int(input())
        if choice == 0:
            print(menu[0].text + "code: 0\n", menu[1].text + "\n", menu[2].text + "\n", menu[3].text +
                  "\n", menu[4].text + "code: 1\n", menu[5].text + "\n", menu[6].text + "\n",menu[7].text +
                  "\n", menu[8].text + "code: 2\n", menu[9].text + "\n", menu[10].text + "\n", menu[11].text +
                  "\n", menu[12].text + "code: 3\n", menu[13].text + "\n", menu[14].text + "\n" , menu[15].text +
                  "\n", menu[16].text + " code: 4\n", menu[17].text + "\n", menu[18].text + "\n" , menu[19].text +
                  "\n")



        elif choice == 1:
            print("\nnow write the codes one at a time given in the menu to order the dish")
            while True:
                choices = int(input())
                global price
                price = ""
                if choices == 0:
                    print(menu[0].text, " ", menu[3].text)
                    price0 = price =+ 5
                    print("$" + str(price0))
                    
                if choices == 1:
                    print(menu[4].text, " ", menu[7].text)
                    price1 = price =+ 8
                    print("$" + str(price1))
                    
                if choices == 2:
                    print(menu[8].text, " ", menu[11].text)
                    price2 = price =+ 15
                    print("$" + str(price2))
                    
                if choices == 3:
                    print(menu[12].text, " ", menu[15].text)
                    price3 = price =+ 6
                    print("$" + str(price3))
                    
                if choices == 4:
                    print(menu[16].text, " ", menu[19].text)
                    price4 = price =+ 8
                    print("$" + str(price4))

                if choices == 5:
                    print("insert your credit/debit card informations")
                    c_c = int(input())
                    print("thank you! your order has been received")

                    


    

            


























        

