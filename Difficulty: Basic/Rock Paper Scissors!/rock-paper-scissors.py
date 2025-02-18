#User function Template for python3

class Solution:
    def gameResult(self, s):
        S=s
        if s[0]==s[1]:
            return "DRAW"
        elif S=="PR" or S=="SP" or S=="RS":
            return "A"
        else:
            return "B"


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.gameResult(s)
        print(ans)
# } Driver Code Ends