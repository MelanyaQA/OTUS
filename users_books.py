import json
from csv import DictReader


with open('books.csv', newline='') as f:
    reader = DictReader(f)
    books = []
    for row in reader:
        del row['Publisher']
        books.append(row)


with open('users.json', 'r') as file:
    users = json.load(file)
    res_users = []


for element in users:
    res_users.append({"name": element["name"], "gender": element["gender"], "address": element["address"], "age": element["age"], "books": []})

j = 0
for i in range(len(books)):
    if j == len(res_users):
        j = 0
    res_users[j]['books'].append(books[i])
    j += 1


with open('result.json', 'w') as f:
    json.dump(res_users, f, indent=4)
