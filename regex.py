import re

# Exercise 1: Extract all email addresses
# Task: Use a regex to extract all valid email addresses and write it to a list.
# Ex. emails = [“support@example.com“, “sales@example.co.uk“, “admin@my-site.org“]

# text = "Please contact us at support9@example.com, sales@example.co.uk, or admin@my-site.org . ntkhang@gmail.com " 
# pattern = "\w+@\w+.\w+"
# x = re.findall(pattern, text)  
# print(x) 


#Exercise 2: Find dates in DD/MM/YYYY format
text = "John was born on 12/05/1990 and his sister on 03/11/1995." 
pattern = "\d{2}/\d{2}/\d{4}"
x = re.findall(pattern, text)  
print(x) 

#Exercise 3: Validate a phone number
text = "+1-800-555-1234"
# 800-555-1234 
#(800) 555-1234*
pattern = "[\+\d-]?\d{3}-\d{3}-\d{4}"
x = re.findall(pattern, text)  
print(x) 


#Exercise 4: Extract hashtags
#Given: 
tweet = "Loving the #Python3 regex practice! #100DaysOfCode #Dev" 

# Task: Extract all hashtags from the tweet.
pattern2 = r'#\w+'
i = re.findall(pattern2, tweet)
print(i)

#Exercise 5: Replace multiple spaces with one
text = "This   sentence  has     extra  spaces." 
#Task: Replace multiple spaces with a single space.
a = re.sub(r'\s+'," ", text)
print(a)


#Exercise 6: Check if a string is a valid IPv4 address
#Examples of valid IPv4:
IPv4 = "192.168.1.1"
#255.255.255.0
#10.0.0.1

#Task: Write a regex to validate IPv4 addresses.
pattern4 = '\d{3}.\d{3}.\d.\d'
IP = re.findall(pattern4,IPv4)
print(IP)


# Exercise 7: Split a string by commas and spaces

text = "apple, banana,orange,   kiwi,pear" 
#Task: Use regex to split this string into a list of fruits, ignoring spaces.
fruit_str = re.sub(r'\s+',"", text)
fruit_list = re.split('\s',fruit_str)
print(fruit_list)