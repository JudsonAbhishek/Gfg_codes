#User function Template for python3

class Solution:
    def removeChars (ob, string1, string2):
        S=''
        for i in string1:
            if i not in string2:
                S+=i
        return S


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        string1=input()
        string2=input()
        
        ob = Solution()
        print(ob.removeChars(string1,string2))
# } Driver Code Ends