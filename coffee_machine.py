from menu import menu_items
def refill():
    refill=input("You want to refill? 'y' or 'n': ")
    if refill=="y":
        global water
        global milk
        global coffee
        water=300
        milk=200
        coffee=100
                    

water=300
milk=200
coffee=100
profit=0
nexti=True
while(nexti):
    #user input
    user="a"
    while user not in ["espresso","latte","cappuccino"]:
        user=input("Enter Your Choice? 'espresso:$1.50', 'latte:$2.50', 'cappuccino:$3.00' : ")
        if user=="report":
            print("Water: " + str(water))
            print("Milk: " + str(milk))
            print("Coffee: " + str(coffee))
            print("Money: " + str(profit))
    if user=="espresso":
        price=1.50
    elif user=="latte":
        price=2.50
    elif user=="cappuccino":
        price=3.00

    #insert coin 
    flag=1
    while flag==1: 
        print("Enter the coins:")
        penny=int(input("How many pennies?: "))
        nickel=int(input("How many nickels?: "))
        dime=int(input("How many dimes?: "))
        quarter=int(input("How many quarters?: "))
        totalsum= penny*0.01+nickel*0.05+dime*0.1+quarter*0.25
        print(totalsum)

        if totalsum<price:
            print("Not enough money! money refunded")
            flag=1
        elif totalsum>price:
            print(f'${totalsum-price} is refunded')
            profit+=price
            flag=0

    if user=="espresso":
        h=menu_items[0]
    elif user=="latte":
        h=menu_items[1]
    elif user=="cappuccino":
        h=menu_items[2]

    jp=0
    if water > h["water"]:
        water-=h["water"]
        if milk > h["milk"]:
            milk-=h["milk"]
            if coffee > h["coffee"]:
                coffee-=h["coffee"]
            else:
                print("Not Enough Coffee,Money Refunded")
                profit-=price
                jp=1
                refill=input("You want to refill? 'y' or 'n': ")
                refill()
            

        else:
            print("Not Enough Milk!,Money Refunded")
            profit-=price
            jp=1
            refill()
            
        
    else:
        print("Not Enough Water!,Money Refunded")
        profit-=price
        jp=1
        refill()


    if jp==0:
        print(f"Here Your {user} ☕ ! Enjoy")

