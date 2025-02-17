#User function Template for python3

class Solution:
    def count (self,s):
        up=low=dig=sp=0
        for i in s:
            if i.isupper():
                up+=1
            elif i.islower():
                low+=1
            elif i.isdigit():
                dig+=1
            else:
                sp+=1
        return (up,low,dig,sp)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    s = input ()
    ob = Solution()
    res = ob.count (s)
    
    for i in res:
        print (i)
    
    print("~")
# Contributed By: Pranay Bansal

# } Driver Code Ends