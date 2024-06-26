import json
import os

from recipes import Recipe

recipes_path: str = "./data/recipes/"

banned_recipes: list[str] = ["minecraft:crafting_special_armordye"]


def get_recipes_list(path: str) -> list[str]:
    return os.listdir(path)


def get_one_recipe(path: str, recipe_name: str) -> Recipe:
    with open(path + recipe_name, "r") as f:
        recipe_json: dict = json.load(f)
        recipe: Recipe = Recipe(recipe_json)
        return recipe


if __name__ == '__main__':
    recipe_list: list[str] = get_recipes_list("." + recipes_path)
    for i, x in enumerate(recipe_list):
        print(i, str(get_one_recipe("." + recipes_path, x)))
