import requests

print(requests.__version__)

page = requests.get('http://google.com')
print(page)

python_script_url = 'https://raw.githubusercontent.com/csheng2/CMPUT404-lab1/master/pythonScript.py'
get_script_request = requests.get(python_script_url)

print(get_script_request.content)