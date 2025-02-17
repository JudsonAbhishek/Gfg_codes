#User function Template for python3

class Solution:

    def findDiff(self, amount):
        a=str(amount)
        temp=""
        for i in a:
            if i=="6":
                temp+="9"
            else:
                temp+=i
        return abs(amount-int(temp))


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):

        amount = int(input())

        solObj = Solution()

        print(solObj.findDiff(amount))
# } Driver Code Ends