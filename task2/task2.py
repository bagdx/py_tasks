import sys


def read_ellipse_coords(filename: str):
    with open(filename, "r", encoding="utf-8") as f:
        x0, y0 = map(float, f.readline().split())
        rx, ry = map(float, f.readline().split())

    return x0, y0, rx, ry


def read_points_coords(filename: str):
    points = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                x, y = map(float, line.split())
                points.append((x, y))
    return points


def calc_position(x, y, x0, y0, rx, ry):
    value = ((x - x0) ** 2 / rx**2) + ((y - y0) ** 2 / ry**2)
    if abs(value - 1) < 10 ** (-10):
        return 0
    elif value < 1:
        return 1
    else:
        return 2


def main():
    if len(sys.argv) != 3:
        print("Ошибка: программа ожидает 2 файла")
        return

    ellipse_file = sys.argv[1]
    points_file = sys.argv[2]

    x0, y0, rx, ry = read_ellipse_coords(ellipse_file)
    points = read_points_coords(points_file)

    for x, y in points:
        result = calc_position(x, y, x0, y0, rx, ry)
        print(result)


if __name__ == "__main__":
    main()
