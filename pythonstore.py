#https://www.youtube.com/watch?v=IH4tog2DHt4&t=1423s
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

while shopping=="yes":
##    I'm having to change a fair bit of syntax.
##    For example shopping.lower skips to the else clause./fixed it
##    running into the same thing with how the tutorial deals with the dictionary check.
##    If this were my first Python rodeo I'd be tearing my hair out.
#decided to stick with .lower() instead of .title() because of how original text file is formatted
    
    item_added=input("What would you like?: ")
    item_added=item_added.lower()
    if item_added in itemsDict:
        print("Thank-you for purchasing " +item_added)
        item_qty=int(input("How many would you like?: "))
        shoppingDict.update({item_added:{"quantity":item_qty, "subtotal":itemsDict[item_added]*item_qty}})
        #print(shoppingDict)
        #want to be able to write plural of items. May have to create a definintion for each item.
        
        
    else:
        print("We don't have that... yet.")
    shopping=input("Would you like to shop more? (yes/no):")
    shopping=shopping.lower()     
    
else:
    print(" ")
    print("*****Bill Summary*****")
    print(" ")
    print("Item  Quantity  Subtotal")
    total=0
    
    for key in shoppingDict:
        print(f"{key}    {shoppingDict[key]['quantity']}    {shoppingDict[key]['subtotal']}")
        total = total + shoppingDict[key]['subtotal']
        #print("Your total is ",total) Puts cumulative total after each iterm so I moved it out of for loop.
    total=str(total)
    print("Your total is ",total)
    #total=float(total) don't need to do outside of for loop.
       #print(f"{key}   {shoppingDict[key][item_qty]}   {shopping.dict[key][itemsDict[item_added]*item_qty]}")
       #I was stalled out here, took a break, came back and saw immediately I had .dict instead of Dict 
    print("************TY!***********")
    
          
    print("That's cool. See you soon!") #this should only print if not shopping
#I'm loving it! Just printed the receipt with all the *'s but no discrete deets. It is pretty. 
#so far so good. Worked out some issues, (re)learning a lot. Encouraged.
#Oh this needs some elif's I think.

#Aggravating that defaults to last print line if I enter a nonresponsive something... oh that's the else.
    #if I put another item instead of yes it should skip to that bit.

#I want to be able to modify the text document from my store program, update inventory, etc.
