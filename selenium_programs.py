# from selenium import webdriver
# # from selenium.webdriver.support.select import Select
# from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.maximize_window()
# driver.get("https://www.flipkart.com/")
# Write a Python program to sum all the items in a list.

l=[1,2,3,4,5]
sum=0
for i in l:
    sum=sum+i
print(sum)
#op: 15
# Write a Python program to multiply all the items in a list.
l=[1,2,3,4,5]
mul=1
for i in l:
    mul=mul*i
print(mul)
 #op: 120
# Write a Python program to get the largest number from a list.
l=[1,12,123,1234,1234567890,78,456]
largest=0
for i in l:
    if i> largest:
        largest=i
print(largest)
#op:1234567890

# Write a Python program to get the smallest number from a list.
l=[1,12,123,1234,1234567890,78,456]
smallest=1
for i in l:
    if i < 1:
        smallest= i
    # else:
    #     if i ==0:
    #         smallest=i
print(smallest)
#or
# list of numbers
list1 = [10, 20, 4, 45, 99]

# sorting the list
list1.sort(reverse=True)

# printing the first element
print("Smallest element is:", list1[-1])


# Write a Python program to count the number of occurrences of an element in a list.
#using list comprehension
l=[1,2,3,45,2,1,2,3,5,6,7,5]
d=[(i,l.count(i)) for i in l]
print(d)

#op[(1, 2), (2, 3), (3, 2), (45, 1), (2, 3), (1, 2), (2, 3), (3, 2), (5, 2), (6, 1), (7, 1), (5, 2)]
 #using dictionary comprehension:

l=[1,2,3,45,2,1,2,3,5,6,7,5]
d={i:l.count(i) for i in l}
print(d)
#op:{1: 2, 2: 3, 3: 2, 45: 1, 5: 2, 6: 1, 7: 1}

# Write a Python program to remove duplicates from a list.
l=[1,2,3,45,2,1,2,3,5,6,7,5]
dup=[]
for i in l:
    if i not in dup:
        dup.append(i)
print(dup)

#op:[1, 2, 3, 45, 5, 6, 7]

#Write a Python program to check if a list is a palindrome. or Write a Python program to reverse a list.
l=[1,2,3,4,4,3,2,1]
res=list(reversed(l))
if l==res:
    print("the given list is palindrome:",l)
else:
    print("the given list is not palindrome:",l)
#or
l=[1,2,3,4,4,3,2,1]
res=l[::-1]
print(res)
if l== res:
    print("palindrome:",l)
else:
    print("not palindrome:",l)

# Write a Python program to sort a list.
l=[1,4,3,6,77,45,99,23]
res=sorted(l)
print(res)
#op:[1, 3, 4, 6, 23, 45, 77, 99]

#Write a Python program to insert an element into a list at a given position.


l=[1,4,3,6,77,45,99,23]
l.append(34)
print(l)
l.insert(3,25)
print(l)
l.extend(["hai"])
print(l)

#Write a Python program to delete an element from a list at a given position.

l=[1,4,3,6,77,45,99,23]
l.remove(23)
print(l)
l.pop(3)
print(l)
l.clear()
print(l)

#Write a Python program to search for an element in a list.
l=[1,4,3,6,77,45,99,23]
ch=6
for i in l:
    if i==ch:
        print("the element found",ch)

#Write a Python program to iterate over a list.

l=[1,4,3,6,77,45,99,23]
for i in l:
    print(i)

#Write a Python program to create a list from a string.
l="haritha"
lis=[]
for i in l:
    lis.append(i)
print(lis)
#op:['h', 'a', 'r', 'i', 't', 'h', 'a']

#Write a Python program to create a list from a tuple
t=(1,2,3,4,5,6)
print(list(t))
#op:[1, 2, 3, 4, 5, 6]

# Write a Python program to create a list from a dictionary.
d={"a":1,"b":"hari","c":23}
l1=[]
l2=[]
for i in d.keys():
    l1.append(i)
for j in d.values():
        l1.append(j)
print(l1)
#op:['a', 'b', 'c', 1, 'hari', 23]


# Write a Python program to create a list from a range.
















