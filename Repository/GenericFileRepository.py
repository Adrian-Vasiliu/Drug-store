import pickle
from Exceptions import DuplicateIdException
from Exceptions import IdNotFoundError


class GenericFileRepository:

    def __init__(self, file_name):
        self.__file = file_name
        self.__storage = self.__read_file()

    def __read_file(self):
        try:
            with open(self.__file, 'rb') as f:
                dictionary = pickle.load(f)
                return dictionary
        except FileNotFoundError:
            print("Warning: file not found!")
            return {}
        except EOFError:
            return {}

    def __write_file(self):
        try:
            with open(self.__file, 'wb') as f:
                pickle.dump(self.__storage, f)
        except FileNotFoundError:
            print("Warning: file not found and can't safe data!")

    def add(self, entity):
        if entity.get_id() in self.__storage:
            raise DuplicateIdException
        self.__storage[entity.get_id()] = entity
        self.__write_file()

    def read(self, id_entity=None):
        if id_entity is None:
            return self.__storage.values()
        if id_entity not in self.__storage:
            raise IdNotFoundError
        return self.__storage[id_entity]

    def update(self, entity):
        if entity.get_id() not in self.__storage:
            raise IdNotFoundError
        self.__storage[entity.get_id()] = entity
        self.__write_file()

    def delete(self, id_entity):
        if id_entity not in self.__storage:
            raise IdNotFoundError
        del self.__storage[id_entity]
        self.__write_file()
