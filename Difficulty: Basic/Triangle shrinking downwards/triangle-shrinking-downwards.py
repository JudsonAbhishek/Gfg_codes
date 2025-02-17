#User function Template for python3

class Solution:
    def triDownwards(self, S):
        s=S
        for i in range(len(s)):
            print(('.'*i)+(s[i:]))
        return ''
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S=input()
        
        ob = Solution()
        ans=ob.triDownwards(S)
        
        for i in range(len(ans)):
            print(ans[i],end="")
            if((i+1)%len(S))==0:
                print()
        print("~")
# } Driver Code Ends