num_of_tuples = int(input("Enter the number of tuples: "))
num = 0
tup1 =() 
product = 1
for i in range(num_of_tuples):
    tuple_input = input("Enter your first,etc: ")
    tup1 = tup1 + (tuple_input,)
for a in range(len(tup1)):
    product = product * int(tup1[a])
print("multipul of your nums combinded is", product)
