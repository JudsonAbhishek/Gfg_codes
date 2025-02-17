#User function Template for python3


class Solution:
    def is_common(self, s, t):
        for i in s:
            if i in t:
                return "CHANGE"
        return "BEHAPPY"


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = list(input().split())
		t = list(input().split())
		ob = Solution()
		ans = ob.is_common(s, t)
		print(ans)
# } Driver Code Ends