class Recipe:
    def __init__(self, recipe: dict):
        self.ingredients: dict[str, int] = {}
        match recipe["type"]:
            case "minecraft:crafting_shaped":
                self.count: int = recipe["result"]["count"]
                ressources_dico: dict[chr, str] = {x: (
                    recipe["key"][x][0].get("item", recipe["key"][x][0].get("tag")) if isinstance(recipe["key"][x],
                                                                                                  list) else
                    recipe["key"][x].get("item", recipe["key"][x].get("tag"))) for x in recipe["key"]}
                for x in ressources_dico:
                    self.ingredients[ressources_dico[x]] = str(recipe["pattern"]).count(x)
            case "minecraft:crafting_shapeless":
                self.count: int = recipe["result"]["count"]
                for x in recipe["ingredients"]:
                    if isinstance(x, list):
                        x = x[-1]
                    key = x.get("item", x.get("tag"))
                    if key:
                        self.ingredients[key] = 1
            case "minecraft:stonecutting":
                self.count: int = recipe["result"]["count"]
                self.ingredients[recipe["ingredient"]["item"]] = 1
            case "minecraft:smelting" | "minecraft:campfire_cooking" | "minecraft:smoking" | "minecraft:blasting":
                self.count: int = 1
                if isinstance(recipe["ingredient"], list):
                    raise ValueError("multiple ingredient in blasting")
                key = recipe["ingredient"].get("item", recipe["ingredient"].get("tag"))
                if key:
                    self.ingredients[key] = 1
            case "minecraft:smithing_transform":
                self.count: int = recipe["result"]["count"]
                self.ingredients[recipe["base"]["item"]] = 1
                self.ingredients[recipe["template"]["item"]] = 1
            case "minecraft:crafting_special_armordye" | "minecraft:crafting_special_bannerduplicate" | \
                 "minecraft:smithing_trim" | "minecraft:crafting_special_bookcloning" | \
                 "minecraft:crafting_decorated_pot" | "minecraft:crafting_special_firework_rocket" | \
                 "minecraft:crafting_special_firework_star_fade" | "minecraft:crafting_special_firework_star" | \
                 "minecraft:crafting_special_mapcloning" | "minecraft:crafting_special_mapextending" | \
                 "minecraft:crafting_special_repairitem" | "minecraft:crafting_special_shielddecoration" | \
                 "minecraft:crafting_special_shulkerboxcoloring" | "minecraft:crafting_special_suspiciousstew" | \
                 "minecraft:crafting_special_tippedarrow":
                raise ValueError(recipe["type"])
            case _:
                raise NotImplementedError(recipe["type"])
        self.name: str = recipe["result"]["id"]
        self.type: str = recipe["type"]

    def __str__(self) -> str:
        return self.name + " " + str(self.count) + " " + str(self.ingredients) + " " + self.type
