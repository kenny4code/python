import re
#Exercise 5: Replace multiple spaces with one
text = "This   sentence  has     extra  spaces." 
#Task: Replace multiple spaces with a single space.
a = re.sub(r'\s+'," ", text)
print(a)

