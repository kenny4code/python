import json
book_input = 'D:\\kennguyen\\CODING\\exercise_2\\ex2_input.json'
book_output = 'D:\\kennguyen\\CODING\\exercise_2\\ex2_output.json'

with open(book_input,'r')as file:
    books_info = json.load(file)

for i in books_info:
    if i["year"] > 1950:
        books_new = i["year"]
with open(book_output,'w') as file:
    json.dump(i["year"], file, indent=4)
for book in books_info:          
    sum_price = sum(book["price"] )
print("Tổng giá:", sum_price)