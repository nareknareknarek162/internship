from task_11 import Dessert


class JellyBean(Dessert):
    def __init__(self, name=None, calories=None, flavour=None):
        super().__init__(name, calories)
        self._flavour = flavour

    @property
    def flavour(self):
        return self.flavour

    @flavour.setter
    def flavour(self, new_flavour):
        self._flavour = new_flavour

    def is_delicious(self):
        if self._flavour == 'black licorice':
            return False
        return True
