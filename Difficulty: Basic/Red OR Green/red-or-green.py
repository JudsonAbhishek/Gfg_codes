#User function Template for python3

class Solution:
    def RedOrGreen(self,N,S):
        c1=0
        c2=0
        for i in S:
            if i=="R":
                c1+=1
            else:
                c2+=1
        if c2<c1:
            return c2
        else:
            return c1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        S=input()
        
        ob=Solution()
        print(ob.RedOrGreen(N,S))
        print("~")
# } Driver Code Ends