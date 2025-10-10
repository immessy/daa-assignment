def read_file(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()
            print(data)
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print("Unexpected error:", e)

read_file("daa.txt")
