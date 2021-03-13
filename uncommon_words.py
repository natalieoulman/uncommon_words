class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:

        A = A.split()
        B = B.split()

        wordhash = collections.Counter(A+B)
        wordlst = []

        for key in wordhash:
            if wordhash[key] == 1:
                wordlst.append(key)
        return wordlst
