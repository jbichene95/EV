market_list = list()

condition=  True
count =  0


while condition:
    item = input("what do you want to buy")
    
    market_list.append(item)
    
    count = count +1
    if count==5:
        condition = False
print(market_list)
