# print("hey there im using python")

'''
Q- print the sum of n numbers

'''

# n = int(input("Enter a number "))
# # print(sum(list))

# s =int(( n * (n+1))/2)

# print (s)


'''
Q- min element for list with its index
'''

list = []

n = int(input("Enter the size of the list: "))

print("Enter the values for the list:")

for i in range(0, n):
    element = int(input())
    list.append(element)

print("The list is:", list)

min = list[0]
idx = 0

for i in range(1,n):

    if(min>list[i]):
        idx=i
        min = list[i]


print("The lowest element is :",min," and its index is : ",idx)
