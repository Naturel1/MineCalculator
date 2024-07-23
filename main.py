from recipes import Recipe
from utility import get_all_recipes, reformat_material_list, read_material_list

DATA_PATH: str = "./data/recipes/"
FILE_PATH: str = "../material_list_2024-07-22_23.28.34.txt"


def recipes_setup(file_path: str) -> dict[str, Recipe]:
    recipes: dict[str, Recipe] = {}
    for x in get_all_recipes(file_path):
        try:
            recipes[x.name] = x
        except AttributeError:
            continue
    return recipes


def items_setup(file_path: str) -> list[list[str]]:
    temp_item_list: list[str] = read_material_list(file_path)
    items_list: list[list[str]] = reformat_material_list(temp_item_list)
    return items_list


def main():
    recipes: dict[str, Recipe] = recipes_setup(DATA_PATH)
    items_list: list[list[str]] = items_setup(FILE_PATH)

    print(items_list)
    print(recipes)


if __name__ == '__main__':
    main()
