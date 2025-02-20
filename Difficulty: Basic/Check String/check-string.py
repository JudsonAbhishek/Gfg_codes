#User function Template for python3

class Solution:
    def check (self,s):
        a=set(s)
        if len(a)==1:
            return True
        return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    s = input ()
    ob = Solution()
    if ob.check (s):
        print ("YES")
    else:
        print ("NO")
        
    print("~")
# Contributed By: Pranay Bansal

# } Driver Code Ends