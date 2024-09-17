def main():
    with open("./data/rosalind_revc.txt") as file:
        DNA_string = file.read()
        reverse_complement = ""
        for char in DNA_string[::-1]:
            if char == "A":
                reverse_complement += "T"
            if char == "T":
                reverse_complement += "A"
            if char == "C":
                reverse_complement += "G"
            if char == "G":
                reverse_complement += "C"
        print(reverse_complement)



if __name__ == "__main__":
    main()
