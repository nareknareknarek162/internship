class Desserts:
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
        if isinstance(new_calories, (int, float)):
            self._calories = new_calories
        else:
            raise TypeError('Введите числовое значение калорийности')

    def is_healthy(self):
        if self._calories < 200:
            return True
        return False

    @staticmethod
    def is_delicious():
        return True
