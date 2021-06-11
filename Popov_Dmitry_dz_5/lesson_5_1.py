with open("test_1.txt", "w", encoding="utf-8") as f:
    while True:
        new_line = input("Ведите строку(для завершения записи введите пустую строку): ")
        if not new_line:
            break
        f.write(new_line + "\n")

# блок проверки
with open("test_1.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line, end="")
