def max_pairwise_product(numbers):
    index_one = -1
    num_one = 0
    for i in range(len(numbers)):
        if numbers[i] > num_one:
            num_one = numbers[i]
            index_one = i

    index_two = -1
    num_two = 0
    for j in range(len(numbers)):
        if numbers[j] > num_two and index_one != j:
            num_two = numbers[j]
            index_two = j

    return num_one*num_two


if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product(input_numbers))
