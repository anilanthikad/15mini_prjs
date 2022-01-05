# Import module.
from googlesearch import search

print('Welcome to Google search tool!')

# Taking query
query = input('What would you like to search? : ')

for i in search(query, start=0, stop=5):
    print(i)
