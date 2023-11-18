
itemsDict={}
shoppingDict={}

#welcome user
userName=input("Please enter your name: ")
welcomeMessage=f"Welcome to my store {userName}"
#love this f
lenWM=len(welcomeMessage)
print("*"*lenWM)
print(welcomeMessage)
print("*"*lenWM)

my_file=open("items.txt")
#file_str=my_file.read()
#print(file_str)
#file_line=my_file.readline()
#print(file_line)
#file_line=my_file.readline()
#print(file_line)

file_line=my_file.readline()
items=my_file.readlines()
my_file.close()

print("**********Items Available Now!**********")

for item in items:
    item_name=item.split()[0]
    item_price=item.split()[1]
    print(f"{item_name}: {item_price}")
    itemsDict.update({item_name: float(item_price)})
    #print(itemsDict)
    #print(item_name, item_price)
    
print("*"*20)

#prompt user to add items
shopping=input("Would you like to shop now? (yes/no):")
shopping=shopping.lower()

if shopping=="yes":
##    I'm having to change a fair bit of syntax.
##    For example shopping.lower skips to the else clause./fixed it
##    running into the same thing with how the tutorial deals with the dictionary check.
##    If this were my first Python rodeo I'd be tearing my hair out.
    
    item_added=input("What would you like?: ")
    item_added=item_added.lower()
    if item_added in itemsDict:
        print("Thank-you for purchasing " +item_added)
        item_qty=int(input("How many would you like?: "))
        shoppingDict.update({item_added:{"quantity":item_qty, "subtotal":itemsDict[item_added]*item_qty}})
        print(shoppingDict)
        
    else:
        print("We don't have that... yet.")
        
    
else:
    print("That's cool. See you soon!")
    
#so far so good. Worked out some issues, (re)learning a lot. Encouraged.
