FILE_PATH: str = "../material_list_2024-07-22_23.28.34.txt"


def read_material_list(file_path: str) -> list[str]:
    with open(file_path, "r") as f:
        return [line.strip() for line in f.readlines()]


def reformat_material_list(material_list: list[str]) -> list[list[str]]:
    material_list_reformatted: list[list[str]] = []
    material_list_cropped: list[str] = material_list[3:-3]
    material_list_cropped.pop(1)
    for material in material_list_cropped:
        material_list_reformatted.append(material.replace(" ", "").strip("|").split("|"))
    return material_list_reformatted


if __name__ == "__main__":
    FILE_PATH_TEMP: str = "../../material_list_2024-07-22_23.28.34.txt"
    _material_list: list[str] = read_material_list(FILE_PATH_TEMP)
    print(reformat_material_list(_material_list))
