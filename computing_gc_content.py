def main():
    with open("./data/rosalind_gc.txt") as file:
        data = file.read()
        data = data.split(">")
        data.remove("")
        highest = ""
        highest_value = 0
        for i, string in enumerate(data):
            DNA_string = "".join(string.split("\n")[1:-1])
            value = (DNA_string.count("G") + DNA_string.count("C")) / len(DNA_string) * 100
            if value > highest_value:
                highest = string.split("\n")[0]
                highest_value = value
        print(highest, highest_value)



if __name__ == "__main__":
    main()
