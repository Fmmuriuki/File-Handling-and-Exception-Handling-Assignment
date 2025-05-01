while True:
    filename = input("Enter filename (or 'quit'): ")
    if filename.lower() == "quit":
        break

    try:
        with open(filename, "r") as file:
            print(f"File exists! First line: {file.readline().strip()}")
    except FileNotFoundError:
        print(f"Error: '{filename}' does not exist.")
    except PermissionError:
        print(f"Error: Cannot read '{filename}' (permission denied).")
    except Exception as e:
        print(f"Error: {e}")

    finally:
