
#User function Template for python3

class Solution:
    
    #Function to check if a string is Isogram or not.
    def isIsogram(self,s):
        #Your code here
        dict={}
        for i in s:
            if i not in dict:
                dict[i]=1
            else:
                dict[i]+=1
        for i in dict:
            if dict[i]>1:
                return False
        return True
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3




def main():
    T=int(input())
    
    while(T>0):
        
        s=input()
        obj = Solution()
        if obj.isIsogram(s) is True:
            print(1)
        else:
            print(0)
        T-=1


        print("~")
if __name__=="__main__":
    main()
# } Driver Code Ends