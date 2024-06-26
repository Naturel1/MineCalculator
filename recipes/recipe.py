class Recipe:
    def __init__(self, recipe: dict):
        # use type to identify the type of recipe
        pass

    def __str__(self) -> str:
        return self.name + " " + str(self.count) + " " + str(self.ingredients)
