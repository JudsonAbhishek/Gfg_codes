#User function Template for python3

class Solution:

    def reverseAlternate(self, Str):
        s = Str.split()
        result = []
        
        for i in range(len(s)):
            if i % 2 != 0:
                result.append(s[i][::-1])
            else:
                result.append(s[i])
        
        return " ".join(result) 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):

        Str = input()

        solObj = Solution()

        print(solObj.reverseAlternate(Str))

# } Driver Code Ends