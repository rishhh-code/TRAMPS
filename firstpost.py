import requests

url = "http://tnagriculture.in/mannvalam/soilCardPublic/en"

payload = {'district': '610',
'block': '6257',
'village': '636348',
'Survey_no': '2',
'ownerName': '\\u0baa\\u0bbf\\u0b9a\\u0bcd\\u0b9a\\u0bae\\u0bc1\\u0ba4\\u0bcd\\u0ba4\\u0bc1',
'mobileNumber': '8110031124'}
files=[

]
headers = {
  'Cookie': 'ci_session=7855bf1aa8b8ebbb89af4ee52619765102551ae0'
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
