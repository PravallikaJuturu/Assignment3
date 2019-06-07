print('Enter list of elements')
list=input()
newList=list.split(' ')
newList.sort()
midIndex=int(len(newList)/2)
print('all elements from the start till middle in list in ascending 
order',newList[:midIndex])
newList.sort(reverse=True)
print('all elements from the start till middle in list in descending 
order',newList[:midIndex])
