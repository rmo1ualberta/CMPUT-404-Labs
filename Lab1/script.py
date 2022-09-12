import requests

print(requests.__version__)
response = requests.get('http://wwww.google.com/')
print(response)

response2 = requests.get('https://raw.githubusercontent.com/rmo1ualberta/CMPUT-404-Labs/master/Lab1/script.py')
print(response2.content)
