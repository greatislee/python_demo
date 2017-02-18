#coding:utf-8

import re

#需要过滤的源字符串
src = '''123 23123  32132 abc 
        1.23 3.11 123'''

#过滤正则规则
p = "\d+\.\d+" 
pattern = re.compile(p, re.S)
result = pattern.findall(src)

print src
print "-====="
print result




