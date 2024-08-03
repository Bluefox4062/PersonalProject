import requests

base_url = 'https://zipcloud.ibsnet.co.jp/api/search'    
query_parameter = '?zipcode='
zipcode = '1600021'
request_url = base_url + query_parameter + zipcode

print(request_url)
print(requests.get(request_url).json())