class SLNode:
    def __init__(self,val):
        self.val=val
        self.next=None
class SList:
    def __init__(self):
        self.head=None
    def add_to_front(self,val):
        new_node=SLNode(val)
        current_head=self.head
        new_node.next=current_head
        self.head=new_node
        return self
    def print_values(self):
        runner=self.head
        while(runner!= None):
            print(runner.val)
            runner =runner.next
        return self
    def add_to_back(self,val):
        new_node=SLNode(val)
        runner=self.head
        while(runner.next!=None):
            runner=runner.next
        runner.next=new_node
        return self
    def remove_from_front(self):
        if self.head !=None :
           self.head=self.head.next
        return self
    def remove_from_back(self):
        current=self.head
        while current.next.next != None:
            current=current.next
        current.next=None
        return self
    def remove_val(self,val):
        if self.head.val==val:
            self.head=self.head.next
            return self
        runner=self.head
        while runner.next:
            if runner.next.val == val:
                runner.next= runner.next.next
                return self
            runner=runner.next
        return self
    def insert_at(self,val,n):
        new_node=SLNode(val)
        if n <=0 :
            new_node.next=self.head
            self.head=new_node
            return self
        runner = self.head
        count = 0
        while runner.next and count < n-1:
            runner =runner.next
            count += 1
        new_node.next=runner.next
        runner.next=new_node
        return self


my_list=SList()
#my_list.add_to_front("are").add_to_front("Linked List").add_to_back("fun").remove_val("Linked List").print_values()
list1=SList()
list1.add_to_front(3).add_to_front(2).add_to_front(1)
list1.insert_at(100,3)
list1.print_values()