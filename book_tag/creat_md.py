import os
import re

name_patten = r'[(](.*?)[)]'
path_patten = r'[\[](.*?)[\]]'
with open('./SUMMARY.md','r', encoding='utf-8') as f:
    names = re.compile(name_patten).findall(f.read())

for name in names:
    if name:
        print(name)
        # f = open(name,  'w',encoding='utf-8')
        # f.close()