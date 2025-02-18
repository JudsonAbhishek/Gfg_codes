#User function Template for python3

class Solution:
    def countWrongPlacedBalls(self, s):
        c=0
        for i in range(len(s)):
            if i%2!=0 and s[i]=="R":
                c+=1
            if i%2==0 and s[i]=="B":
                c+=1
        return c

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        
        ob = Solution()
        print(ob.countWrongPlacedBalls(s))
# } Driver Code Ends