import requests
from lxml import etree
from bs4 import BeautifulSoup
import re
import json

cookies = \
    {\
    'fpestid': 'mAQYzEaHpk_TjeOVrf64_NuWJavO3-bxOzUuo8Tqn5iSKt0GzJAVGlgKb5GqRtFopyGYeg', '_ga_HR0NB2DQ1E': 'GS1.1.1680310307.1.1.1680310322.0.0.0', 'csrftoken': 'bsJ31Oa0XzbSSt1PfVB3RKVyDcFYdSkUE580wiCN1p7Aw9cy5RQ2ZPLRML1nNn8r', 'sessionid': 'qohx4vlwft678bnmm6owrrfn9d0cubb2', 'cebs': '1', 'gwlob': 'on', '_ga_WPCXG24XEE': 'GS1.1.1680546219.2.0.1680546219.0.0.0', 'cebsp_': '2', '_ce.s': 'v~9f4e2e83ae199de881deda5e0b5c12718d78327e~vpv~0~v11.rlc~1680546219351', '_ga': 'GA1.2.1849545166.1679784464', '_ga_6GXTW3LG82': 'GS1.1.1680710141.1.1.1680710152.0.0.0', '9339e7aa273defded40dfe7e03283101': 'c4f6303871ce05d56d50554987b6e6e0', '_gid': 'GA1.2.1002127050.1680798537', '_gat': '1'
    }
classes = ['EECS 442', 'STATS 306', 'ECON 401', 'ENGLISH 125', 'STATS 250', 'STATS 412', 'CHEM 215', 'ECON 102', 'BIO 171', 'PSYCH 111', 'EECS 445', 'EECS 493', 'EECS 270', 'MCDB 310', 'EECS 376', 'MATH 216', 'CHEM 210', 'MATH 115', 'ECON 101', 'EECS 484', 'MATH 217', 'PHYSICS 140', 'EECS 280', 'EECS 281', 'EECS 482', 'BIO 172', 'EECS 485', 'EECS 285', 'STATS 425', 'EECS 183', 'PHYSICS 135', 'ENGR 100', 'MATH 215', 'EECS 370', 'EECS 203', 'MATH 214', 'MATH 116', 'EECS 492', 'EECS 216', 'CHEM 125', 'EECS 388', 'ENGR 101', 'CHEM 130', 'PHYSICS 240', 'MATH 425', 'SPANISH 231']
ii_dict = {}

for c in classes:
    temp = c.split(' ')
    r = requests.get(f'https://atlas.ai.umich.edu/course/{temp[0]}%20{temp[1]}/', cookies=cookies)

    soup = BeautifulSoup(r.content, 'html.parser')
    body = soup.find("body")

    try:
        attribute = soup.find_all("evaluation-card", {"class-prefix": "expectations"})

        ii = re.findall('value="(.*?)"', str(attribute[0]))

        ii = float(ii[0]) if ii else -1.0

        ii_dict[c] = ii
    except:
        print (f"Failed for class {c}")
print (ii_dict)
with open('Expectations.json', 'w') as f:
    json.dump(ii_dict, f)
