set1 = { 1,2,3,4,5}
set2 = {3,4,5, 6,7}
result = set1 | set2  #union
print (result)

result  = set1 & set2 #intersection 
print (result)

result = set1  - set2# difference 
print (result)
print (set1 ^ set2) #symantrice difference 

set3 = { 1, 2, 3, 10 }
set4 = { 1,2 ,3,4,5,6,7,8}
result = set3.issubset (set4) # subset mathed
print (result)

result = set4 .issuperset(set3) #issuperset
print (result)