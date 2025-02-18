#User function Template for python3

class Solution:

    def convert(self, s):
        temp=""
        for i in s:
            if i.isupper():
                temp+=chr(ord('A') +(ord("Z")-ord(i)))
            else:
                temp+=chr(ord('a') +(ord("z")-ord(i)))
        return temp


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        ans = solObj.convert(s)

        print(ans)
        print("~")
# } Driver Code Ends