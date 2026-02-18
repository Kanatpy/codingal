s1 = {2,3,1}
s2 = {"b","A","C"}
s3 = list(zip(s1,s2))
print(s3,"\n")

list1= [1,2,3,4]
list2= [10,20,30,40]

for x,y in zip(list1,list2[::-1]):
    print(x,y)

stocks = ["R","I","T"]
prices = [1,3,5]

new_dict = {stocks: prices for stocks,
            prices in zip(stocks,prices)}

print("\n",new_dict)