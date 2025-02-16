#User function Template for python3
class Solution:
    def URLify(self, s): 
        a=s.replace(" ","%20")
        return a


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        str = input()
        obj = Solution()
        print(obj.URLify(str))
        print("~")

# } Driver Code Ends