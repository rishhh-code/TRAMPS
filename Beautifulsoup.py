import requests
from bs4 import BeautifulSoup
import re

url = 'http://tnagriculture.in/mannvalam/qrCard/557060'

page = requests.get(url)


soup = BeautifulSoup(page.text, 'html')

script_tag = soup.find('script', text=re.compile(r'soil_test_id'))

if script_tag:
    script_text = script_tag.string
   
    soil_test_id_match = re.search(r"soil_test_id\s*=\s*'(\d+)'", script_text)
    
    if soil_test_id_match:
        soil_test_id = soil_test_id_match.group(1)
        print(f"soil_test_id: {soil_test_id}")
    
    lime_match = re.search(r"lime\s*=\s*'(\d+)'", script_text)
    if lime_match:
        lime = lime_match.group(1)
        print(f"lime: {lime}")
else:
    print("No matching <script> tag found.")


dict1={}
dict1['soil_test_id']=soil_test_id
dict1['lime']=lime
print(dict1)




