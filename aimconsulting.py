import requests

url = 'https://1ryu4whyek.execute-api.us-west-2.amazonaws.com/dev/skus'
post_2022 = {'createdAt': '>=2022-01-01'}
response = requests.get(url, params=post_2022)

data = response.json()
num_filtered_records = len(data)

print("Filtered records:", num_filtered_records)