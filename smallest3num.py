print('Enter list of elements')
list=input()
newList=list.split(' ')
newList.sort()
print(newList)
print('Smallest 3 numbers in list are',newList[:3])
