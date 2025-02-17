#User function Template for python3

class Solution:
    def isSquare(self, S): 
        c=0
        for i in S:
            c+=ord(i)
        for i in range(1,c//2):
            if i * i == c:
                return 1
            elif i * i > c:
                return 0





#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        S = input()
        ob = Solution()
        print(ob.isSquare(S))
# } Driver Code Ends