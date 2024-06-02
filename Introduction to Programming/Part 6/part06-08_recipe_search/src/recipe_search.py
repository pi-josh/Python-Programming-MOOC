# Write your solution here
def create_recipe_list(filename: str) -> list:
    """Returns a list of recipes from a given file"""
    recipes = []
    with open(filename) as file:
        recipe = []
        for line in file:
            line = line.strip()
            if line == "":
                if recipe:  # only add non-empty recipes
                    recipes.append(recipe)
                    recipe = []
            else:
                recipe.append(line)
        if recipe:  # add the last recipe if the file doesn't end with a blank line
            recipes.append(recipe)
    return recipes


def search_by_name(filename: str, word: str) -> list:
    """Searches the given file by name of recipe
    and returns as a list"""
    recipes = create_recipe_list(filename)
    found_recipes = []
    for recipe in recipes:
        name = recipe[0]
        if word.lower() in name.lower():
            found_recipes.append(name)
    return found_recipes


def search_by_time(filename: str, time: int) -> list:
    """Searches the given file for the preparation time of recipe
    and returns as a list"""
    recipes = create_recipe_list(filename)
    found_recipes = []
    for recipe in recipes:
        name = recipe[0]
        prep_time = int(recipe[1])
        if time >= prep_time:
            found_recipes.append(f"{name}, preparation time {prep_time} min")
    return found_recipes


def search_by_ingredient(filename: str, ingredient: str) -> list:
    """Searches the given file for the recipe with the ingredient given
    and returns as a list"""
    recipes = create_recipe_list(filename)
    found_recipes = []
    for recipe in recipes:
        name = recipe[0]
        prep_time = recipe[1]
        ingredients = recipe[2:]
        if ingredient in ingredients:
            found_recipes.append(f"{name}, preparation time {prep_time} min")
    return found_recipes


if __name__ == "__main__":
    #found_recipes = search_by_name("recipes2.txt", "oat")
    #found_recipes = search_by_time("recipes1.txt", 20)
    found_recipes = search_by_ingredient("recipes1.txt", "eggs")

    for recipe in found_recipes:
        print(recipe)