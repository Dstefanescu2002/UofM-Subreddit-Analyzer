import requests
from lxml import etree
from bs4 import BeautifulSoup
import re
import json
from tqdm import tqdm

cookies = \
    {\
    'fpestid': 'mAQYzEaHpk_TjeOVrf64_NuWJavO3-bxOzUuo8Tqn5iSKt0GzJAVGlgKb5GqRtFopyGYeg', '_ga_HR0NB2DQ1E': 'GS1.1.1680310307.1.1.1680310322.0.0.0', 'csrftoken': 'bsJ31Oa0XzbSSt1PfVB3RKVyDcFYdSkUE580wiCN1p7Aw9cy5RQ2ZPLRML1nNn8r', 'sessionid': 'qohx4vlwft678bnmm6owrrfn9d0cubb2', 'cebs': '1', 'gwlob': 'on', '_ga_WPCXG24XEE': 'GS1.1.1680546219.2.0.1680546219.0.0.0', 'cebsp_': '2', '_ce.s': 'v~9f4e2e83ae199de881deda5e0b5c12718d78327e~vpv~0~v11.rlc~1680546219351', '_ga': 'GA1.2.1849545166.1679784464', '_ga_6GXTW3LG82': 'GS1.1.1680710141.1.1.1680710152.0.0.0', '9339e7aa273defded40dfe7e03283101': 'c4f6303871ce05d56d50554987b6e6e0', '_gid': 'GA1.2.1002127050.1680798537', '_gat': '1'
    }
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
