def wordBreak(s, wordDict):
    word_set = set(wordDict)
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = TrueS
                break
    return dp[n]
s = input("Enter a string: ")
wordDict = input("Enter dictionary words (space-separated): ").split()
if wordBreak(s, wordDict):
    print("Output: True — The string can be segmented using the given words.")
else:
    print("Output: False — The string cannot be segmented using the given words.")