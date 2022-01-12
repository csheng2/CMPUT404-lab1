import requests

print(requests.__version__)
page = requests.get('http://google.com')
print(page)

