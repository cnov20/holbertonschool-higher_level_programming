#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    for char in dir(hidden_4):
        if '__' not in char:
            print(char)
