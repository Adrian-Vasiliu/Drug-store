from Domain.Entity import Entity
from Exceptions import PrescriptionError


class Drug(Entity):

    def __init__(self, id_drug, name, producer, price, prescription):
        super().__init__(id_drug)
        self.__name = name
        self.__producer = producer
        self.__price = float(price)
        self.__prescription = prescription
        if prescription == "yes":
            self.__prescription = True
        elif prescription == "no":
            self.__prescription = False
        else:
            raise PrescriptionError

    def get_name(self):
        return self.__name

    def get_producer(self):
        return self.__producer

    def get_price(self):
        return self.__price

    def get_prescription(self):
        return self.__prescription

    def __str__(self):
        if self.get_prescription():
            prescription = "yes"
        else:
            prescription = "no"
        return "ID: {0}, Name: {1}, Producer: {2}, Price: {3}, Prescription: {4}.".format(self.get_id(),
                                                                                          self.get_name(),
                                                                                          self.get_producer(),
                                                                                          self.get_price(),
                                                                                          prescription)

    def __eq__(self, other):
        if isinstance(other, Drug):
            return self.get_id() == other.get_id() and self.get_name() == other.get_name() and\
                self.get_producer() == other.get_producer() and self.get_price() == other.get_price() and\
                self.get_prescription() == other.get_prescription()

    def __ne__(self, other):
        return not(self == other)
