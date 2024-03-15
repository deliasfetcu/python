from collections import OrderedDict

def word_occurrences(n, words):
    word_count = OrderedDict()

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    distinct_words_count = len(word_count)
    occurrences = list(word_count.values())

    return distinct_words_count, occurrences

if __name__ == "__main__":
    n = int(input())
    words = [input().strip() for _ in range(n)]

    distinct_count, occurrences = word_occurrences(n, words)
    
    print(distinct_count)
    print(" ".join(map(str, occurrences)))
