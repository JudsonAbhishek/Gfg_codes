#User function Template for python3
class Solution:
    def isStringExist (self, arr, N, S):
        for i in arr:
            c=0
            if len(i)==len(S):
                for temp in range(len(i)):
                    if i[temp]!=S[temp]:
                        c+=1
                if c==1:
                    return True
        return False     


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        S = input()
        ob = Solution()
        print(ob.isStringExist(arr, N, S))
        print("~")
# } Driver Code Ends