import sys
import json


def fill_values(obj, values_map):

    if isinstance(obj, dict):

        if obj.get("id") in values_map:
            obj["value"] = values_map[obj["id"]]

        for v in obj.values():
            fill_values(v, values_map)

    elif isinstance(obj, list):
        for item in obj:
            fill_values(item, values_map)

    return obj


def main():
    if len(sys.argv) != 4:
        print("Ошибка: программа ожидает 3 файла")
        return

    with open(sys.argv[1], "r", encoding="utf-8") as f:
        data = json.load(f)
    values_map = {item["id"]: item["value"] for item in data["values"]}

    with open(sys.argv[2], "r", encoding="utf-8") as f:
        tests_data = json.load(f)

    fill_values(tests_data, values_map)

    with open(sys.argv[3], "w", encoding="utf-8") as f:
        json.dump(tests_data, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    main()
