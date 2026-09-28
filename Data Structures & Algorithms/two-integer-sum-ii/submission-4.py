class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        res=[]

        l=0
        r=n-1

        while l<r:
            mysum=numbers[l]+numbers[r]


            if mysum==target:
                return [l+1,r+1]

            elif mysum>target:
                r-=1
            elif mysum<target:
                l+=1
            
           
        