# https://leetcode.com/problems/employee-importance


# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates


class Solution:

    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        employees_dict = {employee.id: [employee.importance, employee.subordinates] for employee in employees}

        def getIm(employees, id):
            return sum([getIm(employees, id_sub) for id_sub in employees_dict[id][1]]) + employees_dict[id][0]

        return getIm(employees, id)
