#User function Template for python3

class Solution:
    def demonitize(self, S , m , n):
        # code here 
        S1_replace_m = S.replace(m,"")
        S2_replace_n= S.replace(n, "")
        replace_n_from_S1 = S1_replace_m.replace(n, "")
        replace_m_from_S2 = S2_replace_n.replace(m, "")
        
        result = ""
        for char in replace_n_from_S1:
            if char in replace_m_from_S2:
                result += char 
        return result if len(result) else -1 

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        S=input()
        m=input()
        n=input()
        
        ob = Solution()
        print(ob.demonitize(S , m , n))
        print("~")
# } Driver Code Ends