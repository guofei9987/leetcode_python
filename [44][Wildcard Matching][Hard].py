# https://leetcode.com/problems/wildcard-matching

import re
s = "aa"
p = "*"

s="aaaabaaaabbbbaabbbaabbaababbabbaaaababaaabbbbbbaabbbabababbaaabaabaaaaaabbaabbbbaababbababaabbbaababbbba"
p="*****b*aba***babaa*bbaba***a*aaba*b*aa**a*b**ba***a*a*"

p=re.sub('[*]+','[a-z]*',p).replace('?','.')
# p=re.sub('[*]+','[a-z]*',p).replace('?','.')
# a=re.compile(p).match(s)
# a.end()==s

