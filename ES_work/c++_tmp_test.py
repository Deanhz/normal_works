import json
import re
from lxml import etree
import time

time_start = time.time()
fin = open(r'c++_question')
fout = open(r'c++_json', 'a+')
data = []
i = 0
for line in fin.readlines():
    i = i + 1
    line_tmp = line.strip()[4:-3].strip()
    line_t = line.strip()
    tree = etree.HTML(line_t)
    line_dic = dict(tree.xpath('//row')[0].attrib)
    tags_str = line_dic['tags']
    tags_list = re.findall(r'<(.+?)>', tags_str)
    line_dic['tags'] = tags_list
    line_json = json.dumps(dict(line_dic))
    data.append(line_dic)
    print("%s finished!", i)
json.dump(data, fout, sort_keys=True, indent=4)

time_end = time.time()
print('time:%s', time_end - time_start)
