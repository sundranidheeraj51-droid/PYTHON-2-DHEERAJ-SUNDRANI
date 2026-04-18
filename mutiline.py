with open("output.txt", "w") as f:
    while True:
        line = input("Enter text (stop to end): ")
        if line == "stop":
            break
        f.write(line + "\n")