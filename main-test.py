from main import Add


def TestAdd():
    assert Add(2, 3) == 5
    print("Add function works correctly")

def main():
    TestAdd()

if __name__ == '__main__':
    main()