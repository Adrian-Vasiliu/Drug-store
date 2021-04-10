from Repository.GenericFileRepository import GenericFileRepository
from Service.DrugService import DrugService
from Service.CardService import CardService
from Service.TransactionService import TransactionService
from UI.Console import Console

drug_repository = GenericFileRepository("drugs.pkl")
card_repository = GenericFileRepository("cards.pkl")
transaction_repository = GenericFileRepository("transactions.pkl")
drug_service = DrugService(drug_repository, transaction_repository)
card_service = CardService(card_repository, transaction_repository)
transaction_service = TransactionService(transaction_repository, drug_repository)
console = Console(drug_service, card_service, transaction_service)
console.run_console()
