#making a dictionary for grocery items to be stored 
grocery_item = {}
#we need to create a list for the history of the grocery items to be able to use the data later
grocery_history = []

#creating a conditional statement using the while loop for our user inputs
stop = False

while not stop:

    #grocery item input
    item_name = input("Item name:\n")

    #grocery quantity
    quantity = input("Quantity purchased:\n")

    #the cost of the item
    cost = input("Price per item:\n")

    #Create a dictionary entry that contains the name, number and price entered
    grocery_item = {'name':item_name, 'number':int(quantity), 'price': float(cost)}

    #adding grocery_item to the grocery_history list using the append function
    grocery_history.append(grocery_item)

    #Ask if user needs to add anymore grocery items
    userinput = input("Would you like to enter another item?\nType 'c' for continue or 'q' to quit:\n")

    if userinput == 'q':
        stop = True
    else:
        stop = False
#we have to set grand_total to zero in order to loop through for other items each time
grand_total = 0

for grocery_item in grocery_history:


    item_total = grocery_item['number'] * grocery_item['price']
#using this short hand notation to add the item_total to the grand_total that was zero
    grand_total += item_total

    print("%d %s @ $ %.2f ea $%.2f" %(grocery_item['number'], grocery_item['name'], grocery_item['price'], item_total))
#we have to reset the item_total back to zero to start the loop over for the next item.
    item_total = 0
#we will print the grand total in a format that only spits out 2 decimal places
print("Grand total: $%.2f" %grand_total)

