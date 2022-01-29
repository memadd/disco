# Import json module
import json

# indicate keys
i = int(input(" if you want to search by title please enter (1) else enter (2): \n"))

# Open json file
json_data=open('data.json')

# load the json data
movies = json.load(json_data)

if i == 1:
    # Input the key value that you want to search
    value = input("Enter a movie title: \n")
    # Output
    print (list(filter(lambda movie: movie['title'] == value, movies)))
elif i == 2 : 
     # Input the tuple that you want to search
    value = input("Enter a release date and overview like this (”framed” , ’1995-10-20’) : \n")
    print (list(filter(lambda movie: movie['overview'] == value[0] and movie['release_date'] == value[1], movies)))
else:
    print('you entered a wrong value')