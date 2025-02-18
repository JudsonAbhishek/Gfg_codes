#User function Template for python3
class Solution:
	def pattern(self, s):
	    j=len(s)
        for i in range(0,len(s)):  
                print(s[0:j])
                j-=1
        return ""


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        S = input()
        ob = Solution()
        answer = ob.pattern(S)
        for value in answer:
            print(value)

# } Driver Code Ends