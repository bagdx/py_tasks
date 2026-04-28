import sys


def find_min_steps(nums: list):

    sorted_nums = sorted(nums)
    median = sorted_nums[len(nums) // 2]
    min_steps = sum(abs(num - median) for num in nums)

    return min_steps


def main():

    if len(sys.argv) != 2:
        print("Ошибка: программа ожидает 1 аргумент (имя файла)")
        return

    with open(sys.argv[1], "r", encoding="utf-8") as f:
        nums = [int(num.strip()) for num in f]

    count = find_min_steps(nums)
    print(
        count
        if count <= 20
        else "20 ходов недостаточно \
             для приведения всех элементов массива к одному числу."
    )


if __name__ == "__main__":
    main()
