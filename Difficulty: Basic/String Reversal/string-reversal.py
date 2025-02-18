#User function Template for python3

class Solution:
    def reverseString(self, s):
        a=s[::-1]
        l=[]
        for i in a:
            if i not in l and i!=' ':
                l.append(i)
        return "".join(l)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        
        ob = Solution()
        ans = ob.reverseString(s)
        print(ans)
        print("~")
# } Driver Code Ends