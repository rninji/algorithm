import sys
N = int(sys.stdin.readline())
words = [[] for _ in range(50)]
for _ in range(N):
    word = sys.stdin.readline().rstrip()
    if word not in words[len(word)-1]:
        words[len(word)-1].append(word)
for i in range(50):
    words[i].sort()
    for word in words[i]:
        print(word)