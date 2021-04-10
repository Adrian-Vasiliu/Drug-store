from Domain.Card import Card


class CardService:
    def __init__(self, card_repository, transaction_repository):
        self.__repo = card_repository
        self.__repo_transaction = transaction_repository
        self.__actions_history = []

    def add(self, id_card, first_name, last_name, cnp, birthday_date, registration_date):
        entity = Card(id_card, first_name, last_name, cnp, birthday_date, registration_date)
        self.__repo.add(entity)
        self.__actions_history.append(lambda: self.delete(id_card))

    def read(self, id_entity=None):
        if id_entity is None:
            return self.__repo.read()
        return self.__repo.read(id_entity)

    def update(self, id_card, first_name, last_name, cnp, birthday_date, registration_date):
        old_entity = self.__repo.read(id_card)
        self.__actions_history.append(lambda: self.update(id_card, old_entity.get_first_name(),
                                                          old_entity.get_last_name(),
                                                          old_entity.get_cnp(),
                                                          old_entity.get_birthday_date().strftime("%d.%m.%Y"),
                                                          old_entity.get_registration_date().strftime("%d.%m.%Y")))
        entity = Card(id_card, first_name, last_name, cnp, birthday_date, registration_date)
        self.__repo.update(entity)

    def delete(self, id_entity):
        entity = self.__repo.read(id_entity)
        self.__actions_history.append(lambda: self.add(id_entity, entity.get_first_name(), entity.get_last_name(),
                                                       int(entity.get_cnp()),
                                                       entity.get_birthday_date().strftime("%d.%m.%Y"),
                                                       entity.get_registration_date().strftime("%d.%m.%Y")))
        self.__repo.delete(id_entity)

    def undo_redo(self):
        self.__actions_history.pop()()

    def discount_of_cards(self):
        discount_cards = []
        discount_of_cards = {}
        for transaction in self.__repo_transaction.read():
            if transaction.get_card_id() is not None:
                if transaction.get_card_id() not in discount_of_cards:
                    discount_of_cards[transaction.get_card_id()] = 0
                    card = self.__repo.read(transaction.get_card_id())
                    discount_cards.append(card)
                discount_of_cards[transaction.get_card_id()] += transaction.get_price()
        discount_cards = sorted(discount_cards, key=lambda c: discount_of_cards[c.get_id()], reverse=True)
        return discount_cards
