#User function Template for python3


class Solution:
    def modify(self, s):
        
        if s[0].isupper():
            return s.upper()
        if s[0].islower():
            return s.lower()


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    s = input ()
    ob = Solution()
    print(ob.modify(s))
# } Driver Code Ends