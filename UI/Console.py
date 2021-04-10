from Exceptions import DuplicateIdException
from Exceptions import IdNotFoundError
from Exceptions import PrescriptionError


class Console:

    def __init__(self, drug_service, card_service, transaction_service):
        self.__drug_service = drug_service
        self.__card_service = card_service
        self.__transaction_service = transaction_service

    def run_console(self):
        work = True
        while work:
            print("\n"
                  "1. Drugs\n"
                  "2. Cards\n"
                  "3. Transactions\n"
                  "x. Exit\n")
            option = input("Option: ")
            if option == '1':
                self.__menu_drugs()
            elif option == '2':
                self.__menu_cards()
            elif option == '3':
                self.__menu_transactions()
            elif option == 'x':
                work = False
            else:
                print("Invalid option!")

    def __menu_drugs(self):
        work = True
        while work:
            print("\n"
                  "1. Add a drug\n"
                  "2. Update\n"
                  "3. Delete\n"
                  "4. Search a drug by a property\n"
                  "5. Show drugs decreasing by sales\n"
                  "6. Increase drugs below a price with a percentage\n"
                  "7. Undo/redo the action\n"
                  "a. Show all\n"
                  "b. Back")
            option = input("\nOption: ")
            if option == '1':
                self.__add_drug()
            elif option == '2':
                self.__update_drug()
            elif option == '3':
                self.__delete_drug()
            elif option == '4':
                self.__search_drugs()
            elif option == '5':
                self.__show_drugs_decreasing_by_sales()
            elif option == '6':
                self.__increase_drugs_below_price_with_percentage()
            elif option == '7':
                self.__drug_service.undo_redo()
                print("\nDone!")
            elif option == 'a':
                self.__show_drugs()
            elif option == 'b':
                work = False
            else:
                print("\nInvalid option!")

    def __show_drugs(self):
        print('')
        for drug in self.__drug_service.read():
            print(drug)

    def __add_drug(self):
        try:
            property1 = int(input('\nID: '))
            property2 = input("Name: ")
            property3 = input("Producer: ")
            property4 = input("Price: ")
            property5 = input('Prescription ("yes" or "no"): ')
            self.__drug_service.add(property1, property2, property3, property4, property5)
            print('\nThe drug was added')
        except DuplicateIdException:
            print("\nThe typed ID already exists\nRetry!")
        except ValueError as error:
            print('')
            print(error, "\nRetry!")
        except PrescriptionError:
            print('\nError: "Prescription" must be "yes" or "no"!\nRetry!')

    def __update_drug(self):
        try:
            property1 = int(input("\nUpdate the drug with ID: "))
            property2 = input("Name: ")
            if property2 == '':
                property2 = self.__drug_service.read(property1).get_name()
            property3 = input("Producer: ")
            if property3 == '':
                property3 = self.__drug_service.read(property1).get_producer()
            property4 = input("Price: ")
            if property4 == '':
                property4 = self.__drug_service.read(property1).get_price()
            property5 = input('Prescription ("yes" or "no"): ')
            if property5 == '':
                property5 = self.__drug_service.read(property1).get_prescription()
                if property5:
                    property5 = "yes"
                else:
                    property5 = "no"
            self.__drug_service.update(property1, property2, property3, property4, property5)
            print("\nDrug updated")
        except IdNotFoundError:
            print("\nTyped ID doesn't exist!\nRetry!")
        except ValueError as error:
            print('')
            print(error, "\nRetry!")

    def __delete_drug(self):
        try:
            drug_id = int(input("\nDelete the drug with ID: "))
            self.__drug_service.delete(drug_id)
            print("\nDrug deleted")
        except IdNotFoundError:
            print("\nTyped ID doesn't exist!\nRetry!")
        except ValueError as error:
            print('')
            print(error, "\nRetry!")

    def __search_drugs(self):
        drug_property = input("\nProperty: ")
        if drug_property in ["name", "producer", "price", "prescription"]:
            keyword = input("What " + drug_property + '?' + '\n')
            print('')
            try:
                for drug in self.__drug_service.search_drugs(drug_property, keyword):
                    print(drug)
            except ValueError as error:
                print(error, "\nRetry!")
        else:
            print('\n' + '"' + drug_property + '"' + " isn't a property of a drug\nRetry!")

    def __show_drugs_decreasing_by_sales(self):
        print('')
        for drug in self.__drug_service.order_drugs_decreasing_by_sales():
            print(drug)

    def __increase_drugs_below_price_with_percentage(self):
        try:
            price = float(input("\nBelow price: "))
            percentage = float(input("Percentage (%): "))
            self.__drug_service.increase_drugs_below_price_with_percentage(price, percentage)
            print("\nDone!")
        except ValueError as error:
            print('')
            print(error, "\nRetry!")

    def __menu_cards(self):
        work = True
        while work:
            print("\n"
                  "1. Add a card\n"
                  "2. Update\n"
                  "3. Delete\n"
                  "4. Show cards after discount\n"
                  "5. Undo/redo the action\n"
                  "a. Show all\n"
                  "b. Back\n")
            option = input("Option: ")
            if option == '1':
                self.__add_card()
            elif option == '2':
                self.__update_card()
            elif option == '3':
                self.__delete_card()
            elif option == '4':
                self.__show_cards_after_discount()
            elif option == '5':
                self.__card_service.undo_redo()
                print("\nDone!")
            elif option == 'a':
                self.__show_cards()
            elif option == 'b':
                work = False
            else:
                print('\nInvalid option!')

    def __show_cards(self):
        print('')
        for card in self.__card_service.read():
            print(card)

    def __add_card(self):
        try:
            property1 = int(input("\nID: "))
            property2 = input("First name: ")
            property3 = input("Last name: ")
            property4 = input("CNP: ")
            property5 = input("Birthday date (dd.mm.yyyy): ")
            property6 = input("Registration date (dd.mm.yyyy): ")
            self.__card_service.add(property1, property2, property3, property4, property5, property6)
            print('\nThe card was added')
        except DuplicateIdException:
            print("\nThe typed ID already exists\nRetry!")
        except ValueError as error:
            print('')
            print(error, "\nRetry!")
        except IndexError:
            print("\nDate wrong typed!\nRetry!")

    def __update_card(self):
        try:
            property1 = int(input("\nID: "))
            property2 = input("First name: ")
            if property2 == '':
                property2 = self.__card_service.read(property1).get_first_name()
            property3 = input("Last name: ")
            if property3 == '':
                property3 = self.__card_service.read(property1).get_last_name()
            property4 = input("CNP: ")
            if property4 == '':
                property4 = self.__card_service.read(property1).get_cnp()
            property5 = input("Birthday date (dd.mm.yyyy): ")
            if property5 == '':
                property5 = self.__card_service.read(property1).get_birthday_date().strftime("%d.%m.%Y")
            property6 = input("Registration date (dd.mm.yyyy): ")
            if property6 == '':
                property6 = self.__card_service.read(property1).get_registration_date().strftime("%d.%m.%Y")
            self.__card_service.update(property1, property2, property3, property4, property5, property6)
            print("\nCard updated")
        except IdNotFoundError:
            print("\nTyped ID doesn't exist!\nRetry!")
        except ValueError as error:
            print('')
            print(error, "\nRetry!")
        except IndexError:
            print("\nDate wrong typed!\nRetry!")

    def __delete_card(self):
        try:
            card_id = int(input("\nDelete the card with ID: "))
            self.__card_service.delete(card_id)
            print("\nCard deleted")
        except IdNotFoundError:
            print("\nTyped ID doesn't exist!\nRetry!")
        except ValueError as error:
            print('')
            print(error, "\nRetry!")

    def __show_cards_after_discount(self):
        for card in self.__card_service.discount_of_cards():
            print(card)

    def __menu_transactions(self):
        work = True
        while work:
            print("\n"
                  "1. Add a transaction\n"
                  "2. Update\n"
                  "3. Delete\n"
                  "4. Show transactions after a days interval\n"
                  "5. Delete transactions after a days interval\n"
                  "a. Show all\n"
                  "b. Back\n")
            option = input("Option: ")
            if option == '1':
                self.__add_transaction()
            elif option == '2':
                self.__update_transaction()
            elif option == '3':
                self.__delete_transaction()
            elif option == '4':
                self.__show_transactions_after_days()
            elif option == '5':
                self.__delete_transactions_after_days()
            elif option == 'a':
                self.__show_transactions()
            elif option == 'b':
                work = False
            else:
                print('\nInvalid option!')

    def __show_transactions(self):
        print('')
        for transaction in self.__transaction_service.read():
            print(transaction)

    def __add_transaction(self):
        try:
            property1 = int(input("\nID: "))
            property2 = input("Drug ID: ")
            property3 = input("Card ID (optional): ")
            property4 = input("Number of pieces: ")
            property5 = input("Date (dd.mm.yyyy): ")
            property6 = input("Time (hh:mm:ss): ")
            discount, price = self.__transaction_service.add(property1, property2, property3, property4, property5,
                                                             property6)
            print('\nThe transaction was added')
            print("Discount granted: " + str(discount) + '%')
            print("Price Paid:", price)
        except DuplicateIdException:
            print("\nThe typed ID already exists\nRetry!")
        except ValueError as error:
            print('')
            print(error, "\nRetry!")
        except IndexError:
            print("\nDate or time wrong typed!\nRetry!")

    def __update_transaction(self):
        try:
            property1 = int(input("\nID: "))
            property2 = input("Drug ID: ")
            if property2 == '':
                property2 = self.__transaction_service.read(property1).get_drug_id()
            property3 = input("Card ID (optional): ")
            property4 = input("Number of pieces: ")
            if property4 == '':
                property4 = self.__transaction_service.read(property1).get_no_pieces()
            property5 = input("Date (dd.mm.yyyy): ")
            if property5 == '':
                property5 = self.__transaction_service.read(property1).get_date().strftime("%d.%m.%Y")
            property6 = input("Time (hh:mm:ss): ")
            if property6 == '':
                property6 = str(self.__transaction_service.read(property1).get_time())
            discount, price = self.__transaction_service.update(property1, property2, property3, property4, property5,
                                                                property6)
            print("\nTransaction updated")
            print("Discount granted: " + str(discount) + '%')
            print("Price Paid:", price)
        except IdNotFoundError:
            print("\nTyped ID doesn't exist!\nRetry!")
        except ValueError as error:
            print('')
            print(error, "\nRetry!")
        except IndexError:
            print("\nDate or time wrong typed!\nRetry!")

    def __delete_transaction(self):
        try:
            transaction_id = int(input("\nDelete the transaction with ID: "))
            self.__transaction_service.delete(transaction_id)
            print("\nTransaction deleted")
        except IdNotFoundError:
            print("\nTyped ID doesn't exist!\nRetry!")
        except ValueError as error:
            print('')
            print(error, "\nRetry!")

    def __show_transactions_after_days(self):
        try:
            start_day = int(input("\nStart day: "))
            end_day = int(input("End day: "))
            print('')
            for transaction in self.__transaction_service.transactions_after_days(start_day, end_day):
                print(transaction)
        except ValueError as error:
            print('')
            print(error, "\nRetry!")

    def __delete_transactions_after_days(self):
        try:
            start_day = int(input("\nStart day: "))
            end_day = int(input("End day: "))
            for transaction in self.__transaction_service.transactions_after_days(start_day, end_day):
                self.__transaction_service.delete(transaction.get_id())
            print("\nDone!")
        except ValueError as error:
            print('')
            print(error, "\nRetry!")
