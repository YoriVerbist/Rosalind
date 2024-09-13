def main():
    with open("./data/rosalind_rna.txt") as file:
        DNA_string = file.read()
    print(DNA_string.replace("T", "U"))


if __name__ == "__main__":
    main()
