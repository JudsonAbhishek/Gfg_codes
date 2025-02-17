
#User function Template for python3

class Solution:
    
    #Function to calculate sum of all numbers present in a string.
    def findSum(self, s):
        su=0
        temp=''
        for i in s:
            if i.isdigit():
                temp+=i
            else:
                if temp:
                    su+=int(temp)
                    temp=""
        if temp:            
            su+=int(temp)
        return su
                
                    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        obj = Solution()
        print(obj.findSum(s))
        print("~")

# } Driver Code Ends