#adding elemant 

list = [ 1, 3 , 5, 7 ]
list.append(3)
print (list)

list.insert(2 , "fazalullah")
print (list)

list.extend(["abd ullah " , 3333])
print (list)

#romove mathes in python

list1 = ["fazalullah"  , 12, 2.34 , True ]
list1.remove(2.34)
print (list1)

list1.pop(2)
print (list1)

list1.clear()
print (list1)

#findindg elemant 

list2  = [11, 22, 33, 44, 22,22,55,66]
index_ele = list2.index(22)
print(index_ele)

count_my = list2.count(22)
print (count_my)


