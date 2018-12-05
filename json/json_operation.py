#!/usr/bin/env python3
import json

data = {
    'no' : 1,
    'name' : 'taobao',
    'url' : 'http://www.taobao.cn'
}

json_str = json.dumps(data)
print("orignal data:" + repr(data))
print("json object:" + json_str)


data2 = json.loads(json_str)
print("data2['name']:", data2['name'])
print("data2['url']:", data2['url'])


# write json file
with open('data.json', 'w') as f:
    json.dump(data, f)

# read data
with open('data.json', 'r') as f:
    data = json.load(f)