# https://leetcode.com/problems/duplicate-emails

'''
select T1.Email
from
(select Email,count(Id) as c
from Person
group by Email
) T1
where T1.c>1
'''

'''
select Email
from Person
group by Email
having count(id)>1
'''

'''
select distinct T1.Email
from Person T1
inner join Person T2
on T1.Email=T2.Email and T1.id<>T2.id
'''