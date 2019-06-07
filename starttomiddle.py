print('Enter list of elements')
list=input()
newList=list.split(' ')
midIndex=int(len(newList)/2)
print('all elements from the middle to end in list',newList[midIndex:])
print('all elements from the start till middle in 
list',newList[:midIndex])
