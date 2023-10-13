import random

class Randomizer:
    @staticmethod
    def select_random_from_list(items):
        """Select a random item from the provided list."""
        return random.choice(items)

    @staticmethod
    def select_random_weighted(items, weights):
        """Select a random item based on provided weights."""
        return random.choices(items, weights=weights, k=1)[0]

    @staticmethod
    def shuffle_list(items):
        """Return a shuffled version of the provided list."""
        shuffled_items = items.copy()
        random.shuffle(shuffled_items)
        return shuffled_items

    @staticmethod
    def random_percentage():
        """Return a random percentage (0 to 100)."""
        return random.randint(0, 100)

    @staticmethod
    def random_range(start, end):
        """Return a random number between start and end, inclusive."""
        return random.randint(start, end)


# Testing the Randomizer
if __name__ == "__main__":
    print(Randomizer.select_random_from_list(["apple", "banana", "cherry"]))
    print(Randomizer.select_random_weighted(["apple", "banana", "cherry"], [0.1, 0.6, 0.3]))
    print(Randomizer.shuffle_list([1, 2, 3, 4, 5]))
    print(Randomizer.random_percentage())
    print(Randomizer.random_range(10, 20))
