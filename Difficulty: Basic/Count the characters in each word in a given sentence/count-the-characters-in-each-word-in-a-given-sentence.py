#User function Template for python3

class Solution:
    def countChars(self,s):
        s=s.split()
        l=[]
        for i in s:
            l.append((len(i)))
        return l



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        s = input()
        ob = Solution()
        result = ob.countChars(s)
        for i in result:
            print (i, end = " ")
        print ()


# } Driver Code Ends