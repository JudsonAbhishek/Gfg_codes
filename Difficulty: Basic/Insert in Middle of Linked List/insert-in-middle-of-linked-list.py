#User function Template for python3
'''
    Your task is to insert a new node in 
	the middle of the linked list with
	the given value.
	
	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
	
	Function Arguments: head (head of linked list), node 
	(node to be inserted in middle)
	Return Type: None, just insert the new node at mid.
'''
#Function to insert a node in the middle of the linked list.
class Solution:
    def insertInMiddle(self, head, x):
        #code here
        temp=head
        c=0
        if head is None:
            return Node(x)
        while(temp):
            temp=temp.next
            c+=1
        if c%2==0:
            mid=c//2
        else:
            mid=c//2 +1
        temp1=head
        for i in range(mid-1 if mid > 0 else 0): 
            temp1=temp1.next
        newnode = Node(x)
        newnode.next = temp1.next
        temp1.next = newnode
        return head
        

#{ 
 # Driver Code Starts
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def printList(node):
    while node:
        print(node.data, end=" ")
        node = node.next
    print()


if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    t = int(data[0].strip())
    idx = 1

    while t > 0:
        arr = list(map(int, data[idx].strip().split()))
        x = int(data[idx + 1].strip())
        idx += 2

        head = None
        if arr:
            head = Node(arr[0])
            tail = head
            for num in arr[1:]:
                tail.next = Node(num)
                tail = tail.next

        ob = Solution()
        ans = ob.insertInMiddle(head, x)
        printList(ans)
        print("~")
        t -= 1
# } Driver Code Ends