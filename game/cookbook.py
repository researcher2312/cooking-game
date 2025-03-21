from json import load
from pathlib import Path

RECIPES_FILENAME = "recipes.json"


recipes_file = Path(__file__).resolve().parent / RECIPES_FILENAME
with open(recipes_file, "rt") as file:
    recipes = load(file)


class Cookbook:
    def combination_possible(self, action: str, ingredients: list[str]) -> bool:
        return any(
            r["action"] == action and sorted(r["ingredients"]) == sorted(ingredients)
            for r in recipes
        )

    def get_combination(self, action: str, ingredients: list[str]) -> str:
        for r in recipes:
            if r["action"] == action and sorted(r["ingredients"]) == sorted(
                ingredients
            ):
                return r["name"]

    def test_combinations(self) -> None:
        assert self.get_combination("cut", ["apple"]) == "sliced apple"
        assert self.get_combination("boil", ["apple"]) == "boiled apple"
        assert self.get_combination("add", ["water", "flour"]) == "dough"
        assert self.get_combination("add", ["flour", "water"]) == "dough"
        assert not self.get_combination("add", ["flour", "apple"])
        print("Cookbook test succesful")


if __name__ == "__main__":
    cookbook = Cookbook()
    cookbook.test_combinations()
