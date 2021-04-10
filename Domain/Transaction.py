from Domain.Entity import Entity
import datetime


class Transaction(Entity):

    def __init__(self, transaction_id, drug_id, card_id, no_pieces, date, time, price):
        super().__init__(transaction_id)
        self.__drug_id = int(drug_id)
        if card_id == '':
            self.__card_id = None
        else:
            self.__card_id = int(card_id)
        self.__price = float(price)
        self.__no_pieces = int(no_pieces)
        date_string = date.split('.')
        self.__date = datetime.datetime(int(date_string[2]), int(date_string[1]), int(date_string[0]))
        time_string = time.split(':')
        self.__time = datetime.time(int(time_string[0]), int(time_string[1]), int(time_string[2]))

    def get_drug_id(self):
        return self.__drug_id

    def get_card_id(self):
        return self.__card_id

    def get_no_pieces(self):
        return self.__no_pieces

    def get_date(self):
        return self.__date

    def get_time(self):
        return self.__time

    def get_price(self):
        return self.__price

    def __str__(self):
        return "ID: {0}, Drug ID: {1}, Card ID: {2}, No. pieces: {3}, Date: {4}, Time: {5}, Price paid: {6}.".format(
            self.get_id(),
            self.get_drug_id(),
            self.get_card_id(),
            self.get_no_pieces(),
            self.get_date().strftime("%d.%m.%Y"),
            self.get_time(),
            self.get_price())

    def __eq__(self, other):
        if isinstance(other, Transaction):
            return self.get_id() == other.get_id() and self.get_drug_id() == other.get_drug_id() and\
                self.get_card_id() == other.get_card_id() and self.get_no_pieces() == other.get_no_pieces() and\
                self.get_date() == other.get_date and self.get_time() == other.get_time

    def __ne__(self, other):
        return not(self == other)
