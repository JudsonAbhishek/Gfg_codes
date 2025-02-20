#User function Template for python3

class Solution:

    def isPossible(self, S):
        freq={}
        for i in S:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1
        c=0
        for i,j in freq.items():
            if j%2!=0:
                c+=1
        if c<=1:
            return 1
        else:
            return 0
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        solObj = Solution()

        if solObj.isPossible(S):
            print("Yes")
        else:
            print("No")
# } Driver Code Ends