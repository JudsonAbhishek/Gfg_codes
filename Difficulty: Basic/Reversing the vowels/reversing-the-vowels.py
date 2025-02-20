#User function Template for python3

class Solution:
    def modify(self, s):
        l=["a","e","i","o","u"]
        l1=[]
        for i in s:
            if i in l:
                l1.append(i)
        l2=l1[::-1]
        # print(l2)
        # print(l1)
        c=0
        s=list(s)
        for i in range(len(s)):
            if s[i] in l:
                s[i]=l2[c]
                c=c+1
        return "".join(s)
        # for i in range(len(s)):
        #     if 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.modify(s)
        print(ans)
# } Driver Code Ends