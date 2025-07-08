import json
from datetime import datetime 
import re

library_input = 'D:\\kennguyen\\CODING\\exercise_3\\ex3_input.json'
library_output = 'D:\\kennguyen\\CODING\\exercise_3\\ex3_output.json'

with open(library_input,'r')as file:
    library_info = json.load(file)

# Get the borrowed books but not returned get
print("-----------------------------------------------------------------------------------------------------")
print("Finding the list of books borrowed but not returned.....")
for books in library_info:
    #print(f"\nBooks: ", books)
    for r_books in books["borrowed_books"]:
        #print(f"\nr_books: ", r_books)
        if r_books["returned"] == False:
            print(f"Book not returned: ", r_books["title"])
            print(f"Borrowed by: ", books["name"])
print("-----------------------------------------------------------------------------------------------------\n")

# 
alice_price = 0
for books in library_info:
    if books["name"] == "Alice":
        for total_a in books["borrowed_books"]:
            alice_price += total_a["price"]

print(f"Alice book price: {alice_price:.2f} ")

#
bob_price = 0
for books in library_info:
    if books["name"] == "Bob":
        for total_b in books["borrowed_books"]:
            bob_price += total_b["price"]

print(f"Bob book price: {bob_price:.2f} ")

prices = []
for books in library_info:
    for b_books in books["borrowed_books"]:
        prices.append(b_books["price"])

print(f"Most expensive book:",max(prices))

dates = []
for new_books in library_info:
    for old_dates in new_books["borrowed_books"]:
        dt = datetime.strptime(old_dates["borrow_date"], "%Y-%m-%d"). date()
        newt = dt.strftime("%Y-%m-%d")
        dates.append(newt)
print(f"Converted dates:", dates)
dates.sort(reverse  =True)
print(f"Sorted dates (Newest to oldest):", dates)

json_output = {
    "Alice book price": f"{alice_price:.2f}",
    "Bob book price": f"{bob_price:.2f}",
    "Most expensive book": max(prices),
    "Converted dates": dates,
    "Sorted dates (Newest to oldest)": dates
}

with open(library_output, "w", ) as file:
    json.dump(json_output, file, indent=4)


# Finding the book with title containing "Great"
x = []
for user in library_info:
    print("-----------------------------------------------------")
    print(f"User name: ", user["name"])
    for borrowed_book in user["borrowed_books"]:
        print(f"Book title: ", borrowed_book["title"])
        if len(re.findall("Title", borrowed_book["title"])) > 0:
            x.append(re.findall("Title", borrowed_book["title"]))
        print(f"X: ", x)

if x:
    print(f"MATCHED: ", len(x))
else:
    print("NOT MATCHED")
