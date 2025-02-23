class Solution:
    def fizzBuzz(self, n : int):
        l=[]
        for i in range(1, n + 1):  
            if i % 3 == 0 and i % 5 == 0:
                l.append("FizzBuzz")
            elif i % 3 == 0:
                l.append("Fizz")
            elif i % 5 == 0:
                l.append("Buzz")
            else:
                l.append(str(i))
        
        return l
            



#{ 
 # Driver Code Starts
from typing import List


class StringArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = input().strip().split()  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        obj = Solution()
        res = obj.fizzBuzz(n)

        StringArray().Print(res)
        print("~")

# } Driver Code Ends