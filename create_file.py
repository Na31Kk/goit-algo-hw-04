def create_file(path, data):
    with open(path, "w", encoding="utf-8") as file:
        for line in data:
            file.write(line + "\n")