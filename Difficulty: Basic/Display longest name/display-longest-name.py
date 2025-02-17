
class Solution:
    def longest(self, arr):
        a=arr
        longstr=""
        for i in a:
            if len(i)>len(longstr):
                longstr=i
        return longstr
            

#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        names = input().split()
        obj = Solution()
        res = obj.longest(names)
        print(res)
        print("~")
# } Driver Code Ends