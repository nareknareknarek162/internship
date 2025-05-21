from task_11 import Dessert


class JellyBean(Dessert):
    def __init__(self, name=None, calories=None, flavor=None):
        super().__init__(name, calories)
        self._flavor = flavor

    @property
    def flavor(self):
        return self._flavor

    @flavor.setter
    def flavor(self, new_flavour):
        self._flavor = new_flavour

    def is_delicious(self):
        if self._flavor == "black licorice":
            return False
        return True