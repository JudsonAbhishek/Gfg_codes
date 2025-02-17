#User function Template for python3
class Solution:
    def shortestPath(self, s):
        E = s.count("E")
        W = s.count("W")
        N = s.count("N")
        S = s.count("S")
        
        net_east = E - W
        net_north = N - S
        
        result = ""
        
        if net_east > 0:
            result += "E" * net_east
        elif net_east < 0:
            result += "W" * (-net_east)
        
        if net_north > 0:
            result += "N" * net_north
        elif net_north < 0:
            result += "S" * (-net_north)
        
        return ''.join(sorted(result))


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        
        ob = Solution()
        ans = ob.shortestPath(s)
        print(ans)
# } Driver Code Ends