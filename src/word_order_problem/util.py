def word_counting(n, words):
    counting_the_word = {}
    for word in words:
        if word in counting_the_word:
            counting_the_word[word] += 1
        else:
            counting_the_word[word] = 1
    return counting_the_word
def main():
    n = int(input().strip())
    words = [input().strip() for _ in range(n)]

    word_count =word_counting(n, words)

    distinct_words = len(word_count)
    print(distinct_words)

    occurrences = ' '.join(map(str, word_count.values()))
    print(occurrences)