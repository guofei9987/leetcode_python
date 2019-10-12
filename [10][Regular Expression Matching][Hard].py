# https://leetcode.com/problems/regular-expression-matching

import re
s = "mississippi"
p = "mis*is*p*."
# p='p*.'
s='aa'
p='a*'


a=re.compile(p).match(s)
# if a is None:
#     return False
# return a==len(s)
a.end()==len(s)

#%%

pattern = re.compile(r'([a-z]+) ([a-z]+)', re.I)   # re.I 表示忽略大小写
m = pattern.match('Hello World Wide Web')
m

pattern.search('Hello World Wide Web')
