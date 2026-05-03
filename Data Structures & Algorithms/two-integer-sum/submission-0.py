class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for i,n in enumerate(nums):
            ext=target-n
            if ext in hashmap:
                return [hashmap[ext],i]
            hashmap[n]=i
        return

        