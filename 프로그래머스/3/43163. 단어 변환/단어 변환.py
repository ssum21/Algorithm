from collections import deque

def solution(begin, target, words):
    len_words = len(words)
    len_word = len(words[0])
    queue = deque([(begin, 0)])
    visited = set()
    while queue:
        pop_word, dist = queue.popleft()
        if pop_word == target:
            return dist
        for word in words:
            num = 0
            for i in range(len_word):
                if(pop_word[i] != word[i]):
                    num += 1
            if num == 1 and word not in visited:
                queue.append((word, dist+1))
                visited.add(word)
                
    answer = 0
    return answer