#Time: O(n)
#Space:O(1)
class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        s = sentence.split()
        vowel = set("aieouAIEOU")
        res = ""
        for idx, word in enumerate(s):
            if word[0] not in vowel:
                word = word[1:] + word[0]
            word = word + "ma" + "a" * (idx+1)
            res += word + " "
        return res[:-1]