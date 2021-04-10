from Domain.Drug import Drug


class DrugService:
    def __init__(self, drug_repository, transaction_repository):
        self.__repo = drug_repository
        self.__repo_transaction = transaction_repository
        self.__actions_history = []

    def add(self, id_drug, name, producer, price, prescription):
        entity = Drug(id_drug, name, producer, price, prescription)
        self.__repo.add(entity)
        self.__actions_history.append(lambda: self.delete(id_drug))

    def read(self, id_entity=None):
        if id_entity is None:
            return self.__repo.read()
        return self.__repo.read(id_entity)

    def update(self, id_drug, name, producer, price, prescription):
        old_entity = self.__repo.read(id_drug)
        if prescription:
            prescription = "yes"
        else:
            prescription = "no"
        self.__actions_history.append(lambda: self.update(id_drug, old_entity.get_name(), old_entity.get_producer(),
                                                          old_entity.get_price(), prescription))
        entity = Drug(id_drug, name, producer, price, prescription)
        self.__repo.update(entity)

    def delete(self, id_entity):
        entity = self.__repo.read(id_entity)
        prescription = entity.get_prescription()
        if prescription:
            prescription = "yes"
        else:
            prescription = "no"
        self.__actions_history.append(lambda: self.add(id_entity, entity.get_name(), entity.get_producer(),
                                                       entity.get_price(), prescription))
        self.__repo.delete(id_entity)

    def undo_redo(self):
        self.__actions_history.pop()()

    def search_drugs(self, drug_property, keyword):
        search_list = []
        if drug_property == "name":
            for drug in self.__repo.read():
                if keyword == drug.get_name():
                    search_list.append(drug)
        elif drug_property == "producer":
            for drug in self.__repo.read():
                if keyword == drug.get_producer():
                    search_list.append(drug)
        elif drug_property == "price":
            for drug in self.__repo.read():
                if float(keyword) == drug.get_price():
                    search_list.append(drug)
        elif drug_property == "prescription":
            for drug in self.__repo.read():
                prescription = drug.get_prescription()
                if prescription:
                    prescription = "yes"
                else:
                    prescription = "no"
                if keyword == prescription:
                    search_list.append(drug)
        return search_list

    def order_drugs_decreasing_by_sales(self):
        sales = {}
        drugs = self.__repo.read()
        for drug in drugs:
            sales[drug.get_id()] = 0
        for transaction in self.__repo_transaction.read():
            sales[transaction.get_drug_id()] += transaction.get_no_pieces()
        drugs = sorted(drugs, key=lambda d: sales[d.get_id()], reverse=True)
        return drugs

    def increase_drugs_below_price_with_percentage(self, price, percentage):
        for drug in self.__repo.read():
            if drug.get_price() < price:
                new_price = drug.get_price()
                new_price += drug.get_price() / 100 * percentage
                id_drug = drug.get_id()
                name = drug.get_name()
                producer = drug.get_producer()
                prescription = drug.get_prescription()
                if prescription:
                    prescription = "yes"
                else:
                    prescription = "no"
                self.update(id_drug, name, producer, new_price, prescription)
