import requests

print(requests.__version__)
res = requests.get('http://wwww.google.com/')
print(res.status_code)
