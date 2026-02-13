num_of_tuples = int(input("Enter the number of tuples: "))
num = 0
tup1 =() 
for i in range(num_of_tuples):
    tuple_input = input("Enter your first,etc: ")
    tup1 = tup1 + (tuple_input,)
while num <= -1:
    tuple_elements1 = tup1[num]
    num +=1
    
print("multipul of your nums combinded is", tup1)