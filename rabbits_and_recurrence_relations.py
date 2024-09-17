def main():
    with open("./data/rosalind_fib.txt") as file:
        numbers = file.read().split(" ")
        months = int(numbers[0])
        pairs = int(numbers[1])
        lookup = {
            1: 1,
            2: 1,
        }
        for i in range(1, months + 1):
            if i not in lookup:
                lookup[i] = lookup[i-1] + lookup[i-2] * pairs
            print(lookup[i])
        print(months, pairs, lookup)

if __name__ == "__main__":
    main()
