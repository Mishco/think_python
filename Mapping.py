class Mapping:
    def __init__(self, iterable):
        self.item_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.item_list.append(item)


    # private copy of original update() method
    __update = update

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.item_list.append(item)

class Employee:
    pass

