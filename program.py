# # # t = ('1', '2', '3', '4')               # 1234
# # # for i in t:
# # #     print(i, end='')
# #
# #
# # a = ['abc', '123', 'hello', '23']
# # for item in a:
# #     if item.isnumeric():
# #         print(item)
# #
# #  #handling broken links:
# # from selenium import webdriver
# # from selenium.webdriver.common.by import By
# # import time
# # import requests
# #
# # #specify where your chrome driver present in your pc
# # PATH=r"C:\Users\CBT\projectspy\chromedriver.exe"
# #
# # #get instance of web driver
# # driver = webdriver.Chrome(PATH)
# #
# # #provide website url here
# # driver.get("https://testapp.medifit.in/auth/client-login")
# # username=driver.find_element("xpath",'//input[@formcontrolname="email"]')
# # username.send_keys('haritha123@mailinator.com')
# # password=driver.find_element('xpath','//input[@formcontrolname="password"]')
# # password.send_keys('9346144936')
# # login=driver.find_element('xpath',"//span[text()='Login']")
# # login.click()
# # #get all links
# # all_links = driver.find_elements(By.CSS_SELECTOR,"a")
# #
# # #check each link if it is broken or not:
# # for link in all_links:
# #     #extract url from href attribute
# #     url = link.get_attribute('href')
# #
# #     #send request to the url and get the result
# #     result = requests.head(url)
# #
# #     #if status code is not 200 then print the url (customize the if condition according to the need)
# #     if result.status_code !=200:
# #         print(url, result.status_code)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#
#
# # def gcd(a,b):
# #     if(b==0):
# #         return a
# #     else:
# #         return gcd(b,a%b)
# # a=int(input("Enter first number:"))
# # b=int(input("Enter second number:"))
# # GCD=gcd(a,b)
# # print("GCD is: ")
# # print(GCD)
#
# n=[1,2,3,4,5,6,7,8,9,10]
# # op:[3,4,5,6,7]
# res=[]
# for i in range(len(n)):
#     if 3<=n[i] and 7>=n[i]:
#         res+=[n[i]]
# print(res)
# def findMissingNumbers(n):
#     numbers = set(n)
#     # length = len(n)
#     output = []
#     for i in range(1, n[-1]):
#         if i not in numbers:
#             output.append(i)
#     return output
# listOfNumbers = [1, 2, 3, 6, 7, 10]
# print(findMissingNumbers(listOfNumbers))
#
# # Input : [5, 3, 4, 3, 5, 5, 3]
# # Output : 4
# # n=[5, 3, 4, 3, 5, 5, 3]
# # res=[]
# # for i in n:
# #     if n.count(i)>1:
# #         continue
# #     else:
# #         res+=[i]
# # print(res)
# #@@@@@@@@@@@or##############
# # def singleNumber(nums):
# #     # applying the formula.
# #     return 2 * sum(set(nums)) - sum(nums)
# # # driver code
# # a = [2, 3, 5, 4, 5, 3, 4]
# # print(int(singleNumber(a)))
# #
# # a = [15, 18, 16, 18, 16, 15, 89]
# # print(int(singleNumber(a)))
# #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# # Write a Python program to add the digits of a positive integer repeatedly until the result has a single digit.
# # Input : 48
# # Output : 3
# # For example given number is 59, the result will be 5.
# # Step 1: 5 + 9 = 14
# # Step 1: 1 + 4 = 5
# # def sum_of_digits(n):
# #     s = 0
# #     while n:
# #         s += n % 10
# #         n //= 10
# #     if s > 9:
# #         return sum_of_digits(s)
# #     return s
# # n = int(input("Enter an integer: "))
# # print(sum_of_digits(n))
# #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# # Python3 program to validate the PAN Card number using Regular Expression
# # import re
# # Function to validate the PAN Card number.
# # def isValidPanCardNo(panCardNo):
# # 	# Regex to check valid PAN Card number
# # 	regex = "[A-Z]{5}[0-9]{4}[A-Z]{1}"
# # 	# Compile the ReGex
# # 	p = re.compile(regex)
# # 	# If the PAN Card number is empty return false
# # 	if(panCardNo == None):
# # 		return False
# # 	# Return if the PAN Card number matched the ReGex
# # 	if(re.search(p, panCardNo) and len(panCardNo) == 10):
# # 		return True
# # 	else:
# # 		return False
# #
# # # Driver Code
# # # Test Case 1:
# # str1 = "BJCPH4195K"
# # print(isValidPanCardNo(str1))
# #
# # # # Test Case 2:
# # str2 = "BIGPC3115B"
# # print(isValidPanCardNo(str2))
# #
# # # Test Case 3:
# # str3 = "BNZAA2318JM"
# # print(isValidPanCardNo(str3))
# #
# # # Test Case 4:
# # str4 = "BNZAA23184"
# # print(isValidPanCardNo(str4))
# #
# # # Test Case 5:
# # str5 = "BNZAA 23184"
# # print(isValidPanCardNo(str5))
#
# #@@@@@@@@@@@wap to read data in merged cells using python openpyxl:
# # import openpyxl
# # from openpyxl.utils import range_boundaries
# # wb = openpyxl.load_workbook(r'C:\Users\CBT\Documents\merged cells.xlsx')
# # sheet = wb.active
# # all_data=[]
# # for row_index in range(1,sheet.max_row+1):
# #     row=[]
# #     for col_index in range(1,sheet.max_column+1):
# #         vals = sheet.cell(row_index,col_index).value
# #         if vals == None:
# #             for crange in sheet.merged_cells:
# #                 column_start,row_start,column_end,row_end = crange.bounds
# #                 top_value = sheet.cell(column_start,row_start).value
# #                 if row_start<=row_index and row_index<=row_end and column_start<=col_index and col_index<=column_end:
# #                     vals = top_value
# #                     # print(vals)
# #                     break
# #
# #         row.append(vals)
# #     all_data.append(row)
# # print(all_data)
# # for row in all_data:
# #     sheet.append(row)
# # wb.save('bbbb.xlsx')
# #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# # Wap to eleminate duplicate lines in a file:
# # lines_seen = set()  # holds lines already seen
# # outfile = open('foo.txt', "w")
# # infile = open('bar.txt', "r")
# # print("The file bar.txt is as follows")
# # for line in infile:
# #     # print(line)
# #     if line not in lines_seen:  # not a duplicate
# #         outfile.write(line)
# #         lines_seen.add(line)
# # outfile.close()
# # print("The file foo.txt is as follows")
# # for line in open('foo.txt', "r"):
# #     print(line)
# #
#
# # print('a'.split())
# # str="hari akshay chethan"
# # print(str.split())
#
# #1.wapp to read an entire text file:
# # with open('bar.txt','r') as f:
# #     lines=f.readlines()
# #     print(lines)
#
# #2.How to read first N lines of a file?
#
# # N = 4
# # with open("bar.txt", "a") as file:  # the a opens it in append mode
# #     for i in range(N):
# #         line = next(file)
# #         line.strip()
# #         print(line)
# # N=5
# # with open("bar.txt") as myfile:
# #     head = [next(myfile) for x in range(N)]
# # print(head)
#
# # handling calendar
# import time
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# driver=webdriver.Chrome(ChromeDriverManager().install())
# driver.maximize_window()
# driver.get("http://10.10.30.204:4200/auth/client-login")
# time.sleep(5)
# driver.find_element("xpath",'//input[@data-placeholder="E-mail"]').send_keys("haritha.k@testyantra.in")
# time.sleep(5)
# driver.find_element("xpath",'//input[@data-placeholder="Password"]').send_keys('7894561230')
# time.sleep(5)
# driver.find_element("xpath",'//span[text()="Login"]').click()
# time.sleep(5)
# driver.find_element("xpath",'//button[@class="mat-focus-indicator mat-button mat-button-base"]').click()
# time.sleep(5)
# driver.find_element("xpath",'(//span[@class="mat-button-wrapper"])[12]').click()
# time.sleep(5)
# driver.find_element("xpath",'//div[text()=" 3 "]').click()
# time.sleep(5)
# driver.find_element("xpath",'(//span[@class="mat-checkbox-inner-container"])[1]').click()
# time.sleep(5)
# driver.find_element("xpath",'(//span[@class="mat-button-wrapper"])[13]').click()
# time.sleep(3)
# driver.find_element("xpath",'//div[text()=" 7 "]').click()
# dates=driver.find_elements("xpath",'//tbody[@class="mat-calendar-body"]')
# for date in dates:
#     data=date.text
#     print(data)
#     if data ==' 7 ':
#         date.click()
#         time.sleep(5)
#         break
# #
#
# # how to upload files:
#
# # driver.find_element("xpath",'//mat-icon[@mattooltip="Add Report"]').click()
# # driver.find_element("xpath",'//span[text()="Upload"]').send_keys("C:\Wallpapers\lock screen.jpg")

#
# #orange hrm##########
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.maximize_window()
# driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
# driver.find_element("xpath",'//input[@name="username"]').send_keys("Admin")
# driver.find_element("xpath",'//input[@name="password"]').send_keys("admin123")
# driver.find_element("xpath",'//button[text()=" Login "]').click()
# driver.find_element("xpath",'//span[text()="Recruitment"]').click()
# driver.find_element("xpath",'(//i[@class="oxd-icon bi-check oxd-checkbox-input-icon"])[1]').click()
# wait = WebDriverWait(driver, 20)
# wait.until(EC.element_to_be_clickable((By.XPATH, "//mat-select[@role='combobox' and @formcontrolname='nationality']"))).click() # clicked on main drop down thus the option could be visible
# # drp=wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='INDIAN']")))
# # drp.click()
# button = driver.find_element("xpath","//span[text()='NRI']")
# time.sleep(6)
# driver.execute_script("arguments[0].click();", button)
# time.sleep(6)
#
# handling cookies:
import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.action_chains import ActionChains
#
# # PATH = "C:\Program Files (x86)\chromedriver.exe"
# # driver = webdriver.Chrome(PATH)
# driver=webdriver.Chrome(ChromeDriverManager().install())
# driver.get("https://orteil.dashnet.org/cookieclicker/")
#
# driver.implicitly_wait(10)
#
# cookie = driver.find_element(By.ID, "bigCookie")
#
# actions = ActionChains(driver)
# actions.click(cookie)
#
# for i in range(4000):
#     actions.perform()

from selenium_programs import webdriver
from webdriver_manager.chrome import ChromeDriverManager
#
# driver=webdriver.Chrome(ChromeDriverManager().install())
# # to maximize the browser window
# driver.maximize_window()
# #get method to launch the URL
# driver.get("https://www.softwaretestingmaterial.com/")
# #to refresh the browser
# driver.refresh()
# #to add cookies of particular names
# driver.add_cookie({'name' :"f", 'val': 'v'})
# #to get a specific cookie
# print(driver.get_cookie("f"))
# #to get all cookies of the session
# print(driver.get_cookies())
# #to delete a particular cookie
# driver.delete_cookie("v")
# #to delete all cookies in present session
# driver.delete_all_cookies()


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# import time
from selenium_programs import webdriver
from selenium_programs.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.maximize_window()
# driver.get('https://www.amazon.in/')
# driver.find_element('xpath', '//a[contains(text(),"Mobiles")]').click()
# driver.find_element('xpath',
#                     '//ul[@class="a-unordered-list a-nostyle a-vertical a-spacing-medium"]//span[contains(text(),"OnePlus")]').click()
# oneplus = driver.find_elements('xpath',
#                                '//div[@class="sg-col-inner"]//span[@class="a-size-base-plus a-color-base a-text-normal"]')
# # print(oneplus)
# print(oneplus.__len__())
# for i in oneplus:
#  print(i.text)
#
# oneplus.__getitem__(0).click()
# cw = driver.window_handles[1]
# driver.switch_to.window(cw)
# exptitle = "a-size-large product-title-word-break"
# actual_title = driver.find_element('xpath', '//span[@id="productTitle"]').get_attribute("class")
# # print(actual_title.text)
# if exptitle == actual_title:
#  print('reached destination page')
# else:
#  print("not reached try again...")
# time.sleep(5)
# price = driver.find_elements('xpath', '//table[@class="a-lineitem a-align-top"]//tbody//tr[2]//child::td')
# # price.text
# for j in price:
#  print(j.text, end="")

# n=[30,5,8,36,1]
# l1=[]
# for i in range(0,n+1):
#  if n[i]>n[i+1]:
#   l1+=i
# print(l1)

# a=reversed(range(10))
# print(a)
# s="hello"
# for i in reversed(s):
#  print(i)

# l=int(input("enter lower range: "))
# u=int(input("enter upper range:"))
# for num in range(l,u+1):
#  if num>1:
#   for i in range(2,num):
#    if num%i==0:
#     break
#   else:
#     print(num)

# d=["hello",123,1.2,'world',True,'python']
# d=[item if isinstance(item,str)else str(item) for item in d]
# print(d)
# s="this is a bunch of words"
# d=[(item,len(item)) for item in s.split()]
# print(d)
# s='tom is a good boy. tom has good manners'
# d={}
# for word in s.split():
#  d[word]=s.count(word)
# print(d)
# l=[1,2,3,4,5]
# for num in l:
#  fact=1
#  for item in range(1,num+1):
#   fact=fact*item
#  print(fact)
# n=10
# f=0
# s=1
# for i in range(n):
#  print(f)
#  temp=f
#  f=s
#  s=temp+s
#
# n=153
# temp=n
# sum=0
# while temp>0:
#  ld=temp%10
#  sum=sum+ld**3
#  temp=temp//10
# if sum==n:
#  print("armstrong")
# else:
#  print("not armstrong")

# n=958
# # temp=n
# sum=0
# while (n>0 or sum>9):
#  if n==0:
#   n=sum
#   sum=0
#  sum+=n%10
#  n//=10
# print(sum) o/p:9+5+8=22-->2+2=4
# scorll page:
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.maximize_window()
# driver.get("http://10.10.20.23:3001/admin/hotalsettings/mealplan")
# # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# # time.sleep(5)
# scroll_element = driver.find_elements(By.TAG_NAME, "a")
# # driver.execute_script("arguments[0].scrollIntoView();", scroll_element)
# # s=driver.find_element("linktext",'Kuala Lumpur')
# # print(scroll_element.get_attribute("href"))
# for link in scroll_element:
#     print(link.text)

# handling checkboxes:
# driver.get("https://www.amazon.in/mobile-phones/b/?ie=UTF8&node=1389401031&ref_=nav_cs_mobiles")
# time.sleep(10)
# driver.find_element("xpath",'//span[text()="Made for Amazon"]').click()

# handling dropdown:
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.maximize_window()
# driver.get("https://www.flipkart.com/")
# driver.find_element("xpath",'//p[text()="Login/SignUp"]').click()
# driver.find_element("xpath",'//span[text()=" Login as Admin"]').click()
# driver.find_element("xpath",'//input[@placeholder="Your Username*"]').send_keys("megha")
# driver.find_element("xpath",'//input[@placeholder="Your Password"]').send_keys("megha@123")
# driver.find_element("xpath",'//button[text()=" Login"]').click()
# time.sleep(2)
# driver.find_element("xpath",'//p[text()="Registration"]').click()
# time.sleep(3)
# driver.find_element("xpath",'//p[text()="Agent"]').click()
# driver.find_element("xpath",'//div[text()="Create "]').click()
# driver.find_element("xpath",'//p[text()="Company Type"]//ancestor::div[@class="col-sm-3"]//descendant::input[@type="search"]').click()
# options=driver.find_elements("xpath",'//div[@class="ant-select-item-option-content"]')
# for option in options:
#     print(option.text)
#     time.sleep(5)
#     if option=='B2C':
#         option.click()
#         time.sleep(5)

# s="one two three"
# res=""
# for i in s:
#   res=i+res
# print(res)
# l=s.split()
# print(l)

# String ="helloworld"
# def rotate(strg, n):
#     print(strg[n:])
#     return strg[n:] + strg[:n]
#
# res=rotate('helloworld', -2)
# print(res)

# s="hellohai"
# r=""
# for i in s:
#     if i not in r:
#         r+=i
# print(r)
#
# letters = 'hellohai'
# found_dict = {}
# for i in letters:
#     if i in found_dict:
#         print(i)
#         break
#     else:
#         found_dict[i]= 1
# # print(found_dict)
#
#
# def findChar(inputString):
#     list = []
#     for c in inputString:
#         if c in list:
#             return c
#         else:
#             list.append(c)
#     return 'None'
# print(findChar('hellohai'))
#
# def second_largest(numbers):
#     m1, m2 = 0, 0
#     for x in numbers:
#         if x >= m1:
#             m1, m2 = x, m1
#         elif x > m2:
#             m2 = x
#     print(m2)
# second_largest([1,23,544,12,420,99])






from selenium_programs import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium_programs.webdriver.common.by import By
from selenium_programs.webdriver.chrome.service import Service

# driver = webdriver.Chrome()
#
# driver.maximize_window()
# driver.get('https://www.flipkart.com')
# cookies = driver.get_cookies()
# time.sleep(3)
# for cookie in cookies:
#    print(cookie)
#    time.sleep(3)



#Second largest:
def slargest(numbers):
   m1,m2=0,0
   for i in numbers:
      if i>=m1:
         m1,m2=i,m1
      elif i>m2:
         m2=i
   # print(m2)
slargest([1,2,420,599,99])


#remove duplicates;
l=[1,2,3,2,5,6,6,7]
l1=[]
for i in l:
   if i not in l1:
      l1.append(i)

# print(l1)
def count_item(item):
  if l.count(item)==1:
    return item
# print(list(filter(count_item,l)))  #op:[1, 3, 5, 7]


def remove_duplicates(input_list):
   output_list = []
   for element in input_list:
      if element not in output_list:
         output_list.append(element)
   return output_list

l = [1, 2, 3, 4, 2, 5, 1, 3]
result = remove_duplicates(l)
# print(result)

# s="programming"
# d={i:s.count(i) for i in s.count(i)>1 else count(i)}

s="haritha"
count = {}
for i in s:
  if i in count:
    count[i] += 1
  else:
    count[i] = 1
# print(count)
# for key in count:
#   if count[key] > 1:
    # print(key, count[key])

l = [[1,2,3],[4,5,6],[7,8,9]]
# Add the contents of internal list. ([6, 15, 24])
sum_internal = [sum(item) for item in l]
# print(sum_internal)
 # Add the contents of entire list. (45)
# sum_iternal = [sum(item) for item in l]
sum_whole_list = sum(sum_internal)
# print(sum_whole_list)
# items = [[1,2,3],[4,5,6],[7,8,9]]

# to remove duplicates:
l=[1,2,8,5,2,1,8,6,4]
l1=[]
for i in l:
    if l.count(i)==1:
        l1.append(i)
# print(l1) #op[4,5,6,8]

# num=int(input('enter a number:'))
# for i in range(2,num):
#     if num%i==0:
#         print("not prime")
# else:
#     print("prime")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # o/p should be {1: [1, 3, 5, 7, 9], 0: [2, 4, 6, 8, 10]}

d=[]
d2=[]
# for i in numbers:
#     if i%2!=0:
#         d.append(i)
#     else:
#         d2.append(i)
# print(d,d2)
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # output should be {1: [1, 3, 5, 7, 9], 0: [2, 4, 6, 8, 10]}
#
# result = {1: [num for num in numbers if num % 2 != 0], 0: [num for num in numbers if num % 2 == 0]}
#
# print(result)

































