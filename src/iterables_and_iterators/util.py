import itertools

def calculate_probability(n, letters, k):
    total_indices = n
    indices_with_target_letter = sum(1 for letter in letters if letter == 'a')
    combinations = list(itertools.combinations(range(total_indices), k))
    count = sum(1 for combination in combinations if any(letters[i] == 'a' for i in combination))
    probability = count / len(combinations)
    return round(probability, 4)
if __name__ == "__main__":
    n = int(input().strip())
    letters = input().strip().split()
    k = int(input().strip())
    result = calculate_probability(n, letters, k)
    print(result)