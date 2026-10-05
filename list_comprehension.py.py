#numbers = [1,2,3,4,5,6,7,8,9]

#list3 = [number for number in numbers]
#print(list3)


#list3 = [ number*number for number in numbers]
#print(list3)


#list3 = [number for number in numbers if number%2 == 0]
#print(list3)


#list3 = [number * number for number in numbers if number %2 == 0]
#print(list3)

#list3 = [number * number for number in numbers if number > 4 and number %2 == 0]
 #print(list3)

#numbers = [1,2,3,4]
#letters = "abcd"

#list3 = [(number,letter) for number in numbers for letter in letters]
#print(list3)

#list1 = [1,2,3,4,5,6,7,8,9]
#list2 = [2,3,6,9,5]

#list3 = [i*i for i in list1 if not i in list2]
#print(list3)

#list_ = [[1,2,4], [4,5,6,7], [8,9,10,11]]
#list2 = []
#for i in list_ :
    #for j in i:
        #list2.append(j)
#print(list2)
#list3 = [j for i in list_ for j in i]
#print(list3)

#list_methods = []

#for method in dir(list):
    #if method.startswith("__"):
        #continue
    #list_methods.append(method)
#print(list_methods)

#liste = [method for method in dir(list) if not method.startswith("__")]
#print(liste)