#Not my code its a solution that I find in stackoverfload that i think its a good idea
def printTable(tableData):
    maxlen=0
    for fruit,name,animal in zip(tableData[0],tableData[1],tableData[2]):
        maxlen=max(len(fruit),len(name),len(animal),maxlen)
    for fruit,name,animal in zip(tableData[0],tableData[1],tableData[2]):
        lengt = len(fruit) + len(name) + len(animal)
        print((' '*(maxlen - lengt)) + fruit,name,animal)
        
    
tableData = [['apples','oranges','cherries','banana'],['Alice','Bob','Carol','David'],['dogs','cats','moose','goose']]
printTable(tableData)