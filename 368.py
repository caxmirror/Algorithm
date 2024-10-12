class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        mymap = {nums[0]:[nums[0]]} # max
        rescount = 0
        resset = [nums[0]]
        for i in range(1,len(nums)):
            tmp = [nums[i]]
            for k,v in mymap.items():
                if nums[i] % k == 0:
                    tmp = v.copy()
                    tmp.append(nums[i])
                    if len(tmp) > rescount:
                        rescount = len(v)
                        resset = tmp
            mymap[nums[i]] = tmp
        print(mymap)
        return resset
        