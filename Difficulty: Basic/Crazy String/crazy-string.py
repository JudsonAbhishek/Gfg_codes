#User function Template for python3

class Solution:

    def getCrazy(self, S):
        s=""
        if S[0].isupper():
            for i in range(len(S)):
                if i%2==0:
                    s+=S[i].upper()
                else:
                    s+=S[i].lower()
        elif S[0].lower():
            for i in range(len(S)):
                if i%2==0:
                    s+=S[i].lower()
                else:
                    s+=S[i].upper()    
        return s
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        solObj = Solution()

        print(solObj.getCrazy(S))
# } Driver Code Ends