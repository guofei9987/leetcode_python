# 参考LeetCode，自己的单链表写法

class Node(object):

    def __init__(self, val):
        self.val = val
        self.next = None
    def __repr__(self):
        return str(self.val)


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index<0 or index>=self.size:
            print('index is out of range')
            return -1
        curr=self.head
        for i in range(index):
            curr=curr.next
        return curr.val


    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        head_new=Node(val)
        head_new.next=self.head
        self.head=head_new

        self.size+=1

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        curr=self.head
        if curr is None:
            self.head=Node(val)
        else:
            while curr.next is not None:
                curr=curr.next
            curr.next=Node(val)
        self.size+=1

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if index<0 or index>self.size:
            print('index out of range')
            return
        if index==0:
            self.addAtHead(val)
        else:
            node_new=Node(val)
            curr=self.head
            for i in range(index-1):
                curr=curr.next
            node_new.next=curr.next
            curr.next=node_new
            self.size+=1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        if index<0 or index>=self.size:
            print('index out of range')
            return
        curr=self.head
        if index==0:
            self.head=curr.next
            return
        for i in range(index-1):
            curr=curr.next
        curr.next=curr.next.next

        self.size-=1

    def __repr__(self):
        nlist='|'
        curr=self.head
        while curr is not None:
            nlist+='->'+str(curr.val)
            curr=curr.next
        return nlist




# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# obj
# obj.size

def generateLinkedList(input_list):
    obj=MyLinkedList()
    for i in input_list:
        obj.addAtTail(i)
    return obj

obj=MyLinkedList()
obj.get(0)
obj.addAtIndex(1,2)
obj.get(0)
obj.get(1)
obj.addAtIndex(0,1)

obj.get(0)
obj.get(1)


def reverseList(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """

reverseList(None, head=obj)