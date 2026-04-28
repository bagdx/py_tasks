import sys


def get_path(n: int, m: int):

    result = []
    current_num = 1

    while True:
        result.append(str(current_num))
        current_num = (current_num + m - 1) % n

        if current_num == 0:
            current_num = n

        if current_num == 1:
            break

    return "".join(result)


def main():
    if len(sys.argv) != 5:
        print("Ошибка: введено неверное количество аргументов.")
        return

    n1, m1, n2, m2 = map(int, sys.argv[1:5])
    result = get_path(n1, m1) + get_path(n2, m2)
    print(result)


if __name__ == "__main__":
    main()
