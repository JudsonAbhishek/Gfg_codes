#User function Template for python3

class Solution:
    def splitString(ob, S): 
        s1 =""
        s2 = ""
        s3 =""
        for i in  S:
            if i.isalpha():
                s1+=i
            elif i.isdigit():
                s2+=i
            else:
                s3+=i
        l=[]
        l.append(s1)
        l.append(s2)
        l.append(s3)
        return l


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        S = input()
        ob = Solution()
        ans = ob.splitString(S)
        for i in ans:
            if(i==""):
                print(-1)
            else:
                print(i)


        print("~")
# } Driver Code Ends