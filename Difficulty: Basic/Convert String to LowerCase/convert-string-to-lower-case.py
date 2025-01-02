#User function Template for python3

class Solution:
    def toLower (self , s : str)-> str :
        temp=s.lower()
        return temp
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        s = input()
        
        ob = Solution()
        print(ob.toLower(s))
        print("~")
# } Driver Code Ends