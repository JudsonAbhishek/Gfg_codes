#User function Template for python3

'''
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''
class Solution:
    def modularNode(self, head, k):
        # Code Here
        temp=head
        c=0
        while(temp):
            temp=temp.next
            c+=1
        let=0
        for i in range(1,c+1):
            if i%k==0:
                let=i
        temp1=head
        if c<k:
            return -1
        else:
            for i in range(let-1):
               temp1=temp1.next
            return temp1.data


#{ 
 # Driver Code Starts
#Initial Template for Python 3


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def print_list(node):
    while node:
        print(node.data, end=' ')
        node = node.next
    print()


if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split('\n')
    t = int(data[0])
    index = 1
    for _ in range(t):
        arr = list(map(int, data[index].split()))
        k = int(data[index + 1])
        head = Node(arr[0])
        tail = head
        for value in arr[1:]:
            tail.next = Node(value)
            tail = tail.next
        ob = Solution()
        res = ob.modularNode(head, k)
        print(res)
        print("~")
        index += 2

# } Driver Code Ends