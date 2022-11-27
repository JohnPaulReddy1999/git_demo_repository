print('hello')
print('hi')
print('hi hello')


a= eval(input(("Enter a number")))
list1=[2000,500,200,100,50,20,10,5,2,1]
list2=[a]
print("The amount requested",list2[-1])
for i in range(0,len(list1)):
    a=list2[-1]//list1[i]
    print("No of",list1[i],"s ",a)
    a=list2[-1]%list1[i]
    list2.append(a)
