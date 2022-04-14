#Time: O(n)
#Space:O(1)
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        counter = Counter(words[0])
        for word in words[1:]:
            cnt = Counter(word)
            for k in counter.keys():
                counter[k] = min(counter[k], cnt[k])
        return counter.elements()