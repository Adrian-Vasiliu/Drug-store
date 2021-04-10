from Domain.Transaction import Transaction


class TransactionService:
    def __init__(self, transaction_repository, drug_repository):
        self.__repo = transaction_repository
        self.__repo_drug = drug_repository

    def add(self, id_transaction, id_drug, id_card, no_pieces, date, time):
        drug = self.__repo_drug.read(int(id_drug))
        price = drug.get_price() * float(no_pieces)
        discount = 0
        if id_card != '':
            if not drug.get_prescription():
                discount = 10
            else:
                discount = 15
            price -= price / 100 * discount
        entity = Transaction(id_transaction, id_drug, id_card, no_pieces, date, time, price)
        self.__repo.add(entity)
        return discount, price

    def read(self, id_entity=None):
        if id_entity is None:
            return self.__repo.read()
        return self.__repo.read(id_entity)

    def update(self, id_transaction, id_drug, id_card, no_pieces, date, time):
        drug = self.__repo_drug.read(int(id_drug))
        price = drug.get_price() * float(no_pieces)
        discount = 0
        if id_card != '':
            if not drug.get_prescription():
                discount = 10
            else:
                discount = 15
            price -= price / 100 * discount
        entity = Transaction(id_transaction, id_drug, id_card, no_pieces, date, time, price)
        self.__repo.update(entity)
        return discount, price

    def delete(self, id_entity):
        self.__repo.delete(id_entity)

    def transactions_after_days(self, start_day, end_day):
        transactions = []
        for transaction in self.__repo.read():
            if start_day <= transaction.get_date().day <= end_day:
                transactions.append(transaction)
        return transactions
