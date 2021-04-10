from Domain.Entity import Entity
import datetime


class Card(Entity):

    def __init__(self, id_card, first_name, last_name, cnp, birthday_date, registration_date):
        super().__init__(id_card)
        self.__first_name = first_name
        self.__last_name = last_name
        self.__cnp = int(cnp)
        date_string = birthday_date.split('.')
        self.__birthday_date = datetime.datetime(int(date_string[2]), int(date_string[1]), int(date_string[0]))
        date_string2 = registration_date.split('.')
        self.__registration_date = datetime.datetime(int(date_string2[2]), int(date_string2[1]),
                                                     int(date_string2[0]))

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_cnp(self):
        return self.__cnp

    def get_birthday_date(self):
        return self.__birthday_date

    def get_registration_date(self):
        return self.__registration_date

    def __str__(self):
        return "ID: {0}, First name: {1}, Last name: {2}, CNP: {3}, Birthday date: {4}, Registration date: {5}.".format(
            self.get_id(),
            self.get_first_name(),
            self.get_last_name(),
            self.get_cnp(),
            self.get_birthday_date().strftime("%d.%m.%Y"),
            self.get_registration_date().strftime("%d.%m.%Y"))

    def __eq__(self, other):
        if isinstance(other, Card):
            return self.get_id() == other.get_id() and self.get_first_name() == other.get_first_name() and\
                self.get_last_name() == other.get_last_name() and self.get_cnp() == other.get_cnp() and\
                self.get_birthday_date() == other.get_birthday_date and\
                self.get_registration_date() == other.get_registration_date()

    def __ne__(self, other):
        return not(self == other)
