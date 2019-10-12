# https://leetcode.com/problems/minimum-index-sum-of-two-lists

class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        common= list(set(list1).intersection(set(list2)))
        min_item=[]
        min_sum=list1.index(common[0])+list2.index(common[0])
        for i in common:
            candidate_sum=list1.index(i)+list2.index(i)
            if min_sum>candidate_sum:
                min_sum=candidate_sum
                min_item=[i]
            elif min_sum==candidate_sum:
                min_item.append(i)
        return min_item

list1=["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2=["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]

list1=["Shogun","Tapioca Express","Burger King","KFC"]
list2=["KFC","Shogun","Burger King"]
list1=["Shogun","Tapioca Express","Burger King","KFC"]
list2=["KFC","Burger King","Tapioca Express","Shogun"]
Solution().findRestaurant(list1,list2)

