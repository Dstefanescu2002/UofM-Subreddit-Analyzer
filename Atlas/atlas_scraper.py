import requests
from lxml import etree
from bs4 import BeautifulSoup
import re
import json
from tqdm import tqdm

cookies = {}
classes = ['BIOLOGY 225','BIOLOGY 207', 'BIOLOGY 172', 'BIOLOGY 171', 'BIOLOGY 173', 'BIOLOGY 305']
data_dict = {}

for c in tqdm(classes):
    try:
        temp = c.split(' ')
        r = requests.get(f'https://atlas.ai.umich.edu/course/{temp[0]}%20{temp[1]}/', cookies=cookies)

        soup = BeautifulSoup(r.content, 'html.parser')
        body = soup.find("body")
    
        for data_type in ['expectations', 'desire', 'increased-interest', 'understanding', 'workload']:
        
            attribute = soup.find_all("evaluation-card", {"class-prefix": data_type})

            data = re.findall('value="(.*?)"', str(attribute[0]))

            data = float(data[0]) if data else -1.0

            if c not in data_dict:
                data_dict[c] = {}
            data_dict[c][data_type] = data
    except Exception as e:
        print (f"Failed for class {c}, {e}")

with open('Atlas_Data_temp.json', 'w') as f:
    json.dump(data_dict, f)
