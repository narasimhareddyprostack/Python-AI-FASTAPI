import requests,mysql.connector,json,csv 

resonse_data=requests.get('https://dummyjson.com/users')
print(resonse_data)
print(type(resonse_data))
print(resonse_data.status_code)
