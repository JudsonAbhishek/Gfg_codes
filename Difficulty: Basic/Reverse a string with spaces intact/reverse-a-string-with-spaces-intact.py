#User function Template for python3

class Solution:
    def reverseWithSpacesIntact(self, s):
        # code here
        l=set()
        for i in range(len(s)):
            if s[i]==" ":
                l.add(i)
        d=s.replace(" ","")
        d=d[::-1]
        si=[]
        c=0
        for i in range(len(s)):
            if i in l:  
                si.append(" ") 
            else:
                si.append(d[c])  
                c += 1
        return "".join(si)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        ob = Solution()
        ans = ob.reverseWithSpacesIntact(s)
        print(ans)
# } Driver Code Ends