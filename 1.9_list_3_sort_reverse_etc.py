list = [11 , 22, 33, 6,3,8, ]
list.sort()
print (list)
list.reverse()
print (list)

words = ["apple", "banana", "kiwi", "cherry"]
words.sort(key=len)   # Sort by length of the word
print(words) 
 
square = [x*2 for x in range(10) if x % 2 == 0]  #comprehention mathe in python 
print(square)

list1 = [ 11, 22, 33, 44]
list2 = [ 10 , "fazalullah"  , True , 2.33]
combine  = list1 + list2
print (combine )

repeated = combine *2
print (repeated)
