def main():
    with open("./data/rosalind_dna.txt") as file:
        line = file.read()
        a_count = line.count("A")
        c_count = line.count("C")
        g_count = line.count("G")
        t_count = line.count("T")
        print(a_count, c_count, g_count, t_count)


if __name__ == "__main__":
    main()
