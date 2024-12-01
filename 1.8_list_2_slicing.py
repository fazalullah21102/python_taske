#slicing mathes 

list = [ 11,22, 33,44,55,66]
print (list[1:5])
 
print (list[ :3])#omitting stope

print (list[4: ])# omitting starte
 
print (list[ : ])#omitting both

print (list[ -6: -1])#nagative singn 

#step mathed forward move 
print (list[::3])# the line print every 3rd number print

list1 = [ 10 , 20 , "fazalullah" , True , 33.6]

print (list1[::-1]) #thes line print in reverser order 

list1[1:3] = ["abdullah", "kifayat"]#slicng mathed assign new elemant in spacifice line
print(list1)