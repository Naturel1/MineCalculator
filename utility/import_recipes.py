import json
import os

from recipes import Recipe


def get_recipes_list(path: str) -> list[str]:
    return os.listdir(path)


def get_one_recipe(path: str, recipe_name: str) -> Recipe | None:
    with open(path + recipe_name, "r") as f:
        recipe_json: dict = json.load(f)
        try:
            recipe: Recipe = Recipe(recipe_json)
            return recipe
        except ValueError:
            return


def get_all_recipes(path: str) -> list[Recipe]:
    for x in get_recipes_list(path):
        yield get_one_recipe(path, x)


if __name__ == '__main__':
    recipes_path: str = "../data/recipes/"
    recipe_list: list[str] = get_recipes_list(recipes_path)
    for _recipe in get_all_recipes(recipes_path):
        print(_recipe)
