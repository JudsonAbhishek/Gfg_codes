#User function Template for python3

"""
input - 
s - given string 

output - 
return 0 if not panagram else return 1
"""
class Solution:
    def isPanagram(self,s):
        #your code here
        s=s.lower()
        s=set(s)
        if len(s)==26:
            return 1
        else:
            return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while(t>0):
        s = input()
        print(int(Solution().isPanagram(s)))
        t = t-1

        print("~")
# } Driver Code Ends