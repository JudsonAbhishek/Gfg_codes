#User function Template for python3
import re
class Solution:
    def reverseEqn(self, s):
        tokens = re.findall(r'\d+|[+*/-]', s)  
        reversed_eqn = "".join(tokens[::-1])  
        return(reversed_eqn)
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.reverseEqn(s)
        print(ans)
        print("~")
# } Driver Code Ends