class Dessert:
    def __init__(self, name=None, calories=None):
        self._name = name
        self._calories = calories

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def calories(self):
        return self._calories

    @calories.setter
    def calories(self, new_calories):
        self._calories = new_calories

    def is_healthy(self):
        if isinstance(self._calories, int):
            if self._calories < 200:
                return True
            return False
        return False

    @staticmethod
    def is_delicious():
        return True
