class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap1={}
        hashmap2={}
        for letters in s:
            if letters not in hashmap1:
                hashmap1[letters]=1
            else:
                hashmap1[letters]+=1 
        for letters in t:
            if letters not in hashmap2:
                hashmap2[letters]=1
            else:
                hashmap2[letters]+=1 
        return hashmap1==hashmap2