#User function Template for python3

class Solution:
    def modify(self, s):
        a=s.replace(" ","")
        return a.strip()


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.modify(s)
        print(ans)
        print("~")
# } Driver Code Ends