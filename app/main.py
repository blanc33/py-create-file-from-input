def main() -> None:
    f_name = input("Enter name of the file: ") + ".txt"
    f_content = ""
    while True:
        f_line = input("Enter new line of content: ")
        if f_line == "stop":
            break
        f_content += (f_line + "\n")
    with open(f_name, "w") as f:
        f.write(f_content)


if __name__ == "__main__":
    main()
