# https://leetcode.com/problems/combine-two-tables

'''
select T1.FirstName,T1.LastName,
T2.City,T2.State
from Person T1
left join
Address T2
on T1.PersonId=T2.PersonId
'''