
#welcome user
userName=input("Please enter your name: ")
welcomeMessage=f"Welcome to my store {userName}"
#love this f
lenWM=len(welcomeMessage)
print("*"*lenWM)
print(welcomeMessage)
print("*"*lenWM)

my_file=open("items.txt")
file_str=my_file.read()
print(file_str)

my_file.close()
