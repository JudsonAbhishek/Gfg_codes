#User function Template for python3
class Solution:
    def areAnagram(ob, S1, S2):
        if len(S1)==len(S2):
            if sorted(S1)==sorted(S2):
                return 1
        return 0
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        S1 = input()
        S2 = input()
        
        ob = Solution()
        print(ob.areAnagram(S1,S2))
# } Driver Code Ends