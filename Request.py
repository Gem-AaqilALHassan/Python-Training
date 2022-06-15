import requests
 
# For getting some value we will use ("GET")

# r = requests.get('https://xkcd.com/353/')

# print(r) // If we get 200 then this shows 200 response

# print(dir(r)) // This shows attribute and methods which we can access within this response object

# print(help(r)) // to see more detailed explanation of attributes and methods we use this function

# print(r.text) // We will get the html and this is the html of the page we looked into the browser and to parese we will use html parser

# Now to get the image part :->

# r = requests.get('https://imgs.xkcd.com/comics/python.png')

# print(r.content) // This will print the bytes of the image so that we can take out this byte and savee the image into our machine

# The below command is going to create a file comic in the same directory and will download the image respectively.

# with open('comic.png','wb') as f:
# 	f.write(r.content)    

# To check whther we got a good response

# print(r.status_code) // Here 200 are success 300 are redirect 400 no permision page 500 servers 

# print(r.ok) // This will retuen true for response less than 400 if anything is wrong like client server then it will return false

# print(r.headers) // To view indepth response information by looking into the headers

# Now we will use another site i.e "http://httpbin.org/" that allows us to test and hence we are moving towards some advance concepts

# payload = {'page' : 2, 'count' :25}  # //Dictionary of URL that we want to set

# r = requests.get('https://httpbin.org/get',params=payload) // instaed of further describing we use params to automatically get the value 

# print(r.text) // JSON format

# print(r.url) // URL Requested

# Sometimes we want to post the data to certain URL ("POST")

# payload = {'username' : 'Aaqil', 'password' : 'testing'}

# r = requests.post('https://httpbin.org/post',data=payload)

# print(r.text) # JSON response we will get as JSON is common working with certain apis

# print(r.json()) # This created a python dictionary from that json response

# r_dict= r.json() # this stored the json in varibale of dictionary type

# print(r_dict['form']) # This will display the form value from that json

# Now we will have to go with put request i.e basically the same thing ("PUT")

# r = requests.get('http://httpbin.org/basic-auth/Aaqil/testing',auth=('Aaqil','testing')) # This is used to authenticate where aaqil is username and testing is password

# print(r.text) # This will print the authentication as true and Aaqil as username

# print(r) # If error in username or password it will give 401 otherwise 200

# To put out timeout feature we will do the following 

# r = requests.get('https://httpbin.org/delay/1', timeout=3) # we will get 200 response

# r = requests.get('https://httpbin.org/delay/6', timeout=3) # we will get exception

# print(r)








