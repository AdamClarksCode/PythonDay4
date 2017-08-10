import unittest

class Stock(object):
	def __init__(self, ID, totalOwned, available):
		self.stockID = ID
		self.totalOwned = totalOwned
		self.available = available

class Book(Stock):
	def __init__(self, stockID, totalOwned, available, isbn, title, author, publisher, publishDate, genre):
		Stock.__init__(self, stockID, totalOwned, available)
		self.isbn = isbn
		self.title = title
		self.author = author
		self.publisher = publisher
		self.publishDate = publishDate
		self.genre = genre

class Newspaper(Stock):
	def __init__(self, stockID, totalOwned, available, id, publisher, isTabloid, publicationDate):
		Stock.__init__(self, stockID, totalOwned, available)
		self.id = id
		self.publisher = publisher
		self.isTabloid = isTabloid
		self.publicationDate = publicationDate

class MediaResource(Stock):
	def __init__(self, stockID, totalOwned, available, id, type, productName):
		Stock.__init__(self, stockID, totalOwned, available)
		self.id = id
		self.type = type
		self.productName = productName

class Person(object):
	def __init__(self, id, name, title, gender, joinDate):
		self.id = id
		self.name = name
		self.title = title
		self.gender = gender
		self.joinDate = joinDate
		
class Loans(Person):
	def __init__(self, id, name, title, gender, joinDate, loanID, stockID, startDate, dueDate, hasBeenReturned):
		Person.__init__(self, id, name, title, gender, joinDate)
		self.loanID = loanID
		self.stockID = stockID
		self.startDate = startDate
		self.dueDate = dueDate
		self.hasBeenReturned = hasBeenReturned
		
def CheckOutItem(loanee, loanID, stockID, loanDate, dueDate):
	completedLoan = Loans(loanee.id, loanee.name, loanee.title, loanee.gender, loanee.joinDate, loanID, stockID, loanDate, dueDate, False)
	return completedLoan
	
def CheckInItem(toCheckIn):
	toCheckIn.hasBeenReturned = True
	return toCheckIn

def AddItem(ID, totalOwned, available):
	newItem = Stock(ID, totalOwned, available)
	return newItem
	
def RemoveItem(listOfItems, idToRemove):
	listToReturn = []
	for item in listOfItems:
		if item.stockID != idToRemove:
			listToReturn = listToReturn + [item]
	return listToReturn
	
def UpdateItem(toUpdate, newID, newOwned, newAvailable):
	toUpdate.stockID = newID
	toUpdate.totalOwned = newOwned
	toUpdate.available = newAvailable
	return toUpdate
	
def RegisterPerson(id, name, title, gender, joinDate):
	personToReturn = Person(id, name, title, gender, joinDate)
	return personToReturn
	
def DeletePerson(listOfPersons, idToRemove):
	listToReturn = []
	for person in listOfPersons:
		if person.id != idToRemove:
			listToReturn = listToReturn + [person]
	return listToReturn

def UpdatePerson(toUpdate, newID, newName, newTitle, newGender, newJoinDate):
	toUpdate.id = newID
	toUpdate.name = newName
	toUpdate.title = newTitle
	toUpdate.gender = newGender
	toUpdate.joinDate = newJoinDate
	return toUpdate

def SavePersons(listOfPersons):
	file = open("persons.txt","w")
	for i in listOfPersons:
		file.write(str(i.id) + "," + i.name + "," + i.title + "," + i.gender + "," + i.joinDate + ";")
	file.close()
	return "Success"

def LoadPersons():
	file = open("persons.txt","r")
	listRaw = file.read().split(";")
	listOfPersons = []
	for i in listRaw:
		if i != "":
			tempList = i.split(",")
			tempPerson = Person(int(tempList[0]), tempList[1], tempList[2], tempList[3], tempList[4])
			listOfPersons = listOfPersons + [tempPerson]
	return listOfPersons
	
def SaveLoans(listOfLoans):
	file = open("loans.txt","w")
	for i in listOfLoans:
		file.write(str(i.id) + "," + i.name + "," + i.title + "," + i.gender + "," + i.joinDate + "," + str(i.loanID) + "," + str(i.stockID) + "," + i.startDate + "," + i.dueDate + "," + str(i.hasBeenReturned) + ";")
	file.close()
	return "Success"
	
def LoadLoans():
	file = open("loans.txt","r")
	listRaw = file.read().split(";")
	listOfLoans = []
	for i in listRaw:
		if i != "":
			tempList = i.split(",")
			tempLoan = Loans(int(tempList[0]), tempList[1], tempList[2], tempList[3], tempList[4], int(tempList[5]), int(tempList[6]), tempList[7], tempList[8], tempList[9])
			listOfLoans = listOfLoans + [tempLoan]
	return listOfLoans

def SaveMediaResources(listOfMedia):
	file = open("mediaResources.txt","w")
	for i in listOfMedia:
		file.write(str(i.stockID) + "," + str(i.totalOwned) + "," + str(i.available) + "," + str(i.id) + "," + i.type + "," + i.productName + ";")
	file.close()
	return "Success"

def LoadMedia():
	file = open("mediaResources.txt","r")
	listRaw = file.read().split(";")
	listOfMedia = []
	for i in listRaw:
		if i != "":
			tempList = i.split(",")
			tempMedia = MediaResource(int(tempList[0]), int(tempList[1]), int(tempList[2]), int(tempList[3]), tempList[4], tempList[5])
			listOfMedia = listOfMedia + [tempMedia]
	return listOfMedia

def SaveNewspapers(listOfNewspapers):
	file = open("Newspapers.txt","w")
	for i in listOfNewspapers:
		file.write(str(i.stockID) + "," + str(i.totalOwned) + "," + str(i.available) + "," + str(i.id) + "," + i.publisher + "," + str(i.isTabloid) + "," + i.publicationDate + ";")
	file.close()
	return "Success"

def LoadNewspapers():
	file = open("Newspapers.txt","r")
	listRaw = file.read().split(";")
	listOfPapers = []
	for i in listRaw:
		if i != "":
			tempList = i.split(",")
			tempPaper = Newspaper(int(tempList[0]), int(tempList[1]), int(tempList[2]), int(tempList[3]), tempList[4], bool(tempList[5]), tempList[6])
			listOfPapers = listOfPapers + [tempPaper]
	return listOfPapers

def SaveBooks(listOfBooks):
	file = open("Books.txt","w")
	for i in listOfBooks:
		file.write(str(i.stockID) + "," + str(i.totalOwned) + "," + str(i.available) + "," + i.isbn + "," + i.title + "," + i.author + "," + i.publisher + "," + i.publishDate + "," + i.genre + ";")
	file.close()
	return "Success"
	
def LoadBooks():
	file = open("Books.txt","r")
	listRaw = file.read().split(";")
	listOfBooks = []
	for i in listRaw:
		if i != "":
			tempList = i.split(",")
			tempBook = Book(int(tempList[0]), int(tempList[1]), int(tempList[2]), tempList[3], tempList[4], bool(tempList[5]), tempList[6], tempList[7], tempList[8])
			listOfBooks = listOfBooks + [tempBook]
	return listOfBooks
class TestLibrary(unittest.TestCase):
	def test_Stock(self):
		testStock = Stock(1, 10, 8)
		self.assertEqual(1, testStock.stockID)
	def test_Book(self):
		testBook = Book(1, 10, 8, "9781621151593", "Mogworld", "Yahtzee Croshaw", "Dark Horse Books", "23/10/2009", "Fantasy")
		self.assertEqual("Mogworld", testBook.title)
	def test_Newspaper(self):
		testPaper = Newspaper(2, 1, 1, 1, "The Guardian", False, "09/08/2017")
		self.assertEqual("The Guardian", testPaper.publisher)
	def test_MediaResource(self):
		testMedia = MediaResource(3, 1, 0, 1, "Camera", "Nikkon 2209")
		self.assertEqual("Nikkon 2209", testMedia.productName)
	def test_Person(self):
		testPerson = Person(1, "Amanda Hugandkiss", "Miss", "Female", "09/08/2017")
		self.assertEqual("Amanda Hugandkiss", testPerson.name)
	def test_Loans(self):
		testLoan = Loans(1, "Amanda Hugandkiss", "Miss", "Female", "09/08/2017", 1, 1, "09/08/2017", "23/08/2017", False)
		self.assertEqual("23/08/2017", testLoan.dueDate)
	def test_CheckOutItem(self):
		testPerson = Person(1, "Amanda Hugandkiss", "Miss", "Female", "09/08/2017")
		testStock = Stock(1, 10, 8)
		testLoan = CheckOutItem(testPerson, 1, testStock.stockID, "10/08/2017", "24/08/2017")
		self.assertEqual(False, testLoan.hasBeenReturned)
	def test_CheckInItem(self):
		testLoan = Loans(1, "Amanda Hugandkiss", "Miss", "Female", "09/08/2017", 1, 1, "09/08/2017", "23/08/2017", False)
		testLoan = CheckInItem(testLoan)
		self.assertEqual(True, testLoan.hasBeenReturned)
	def test_AddItem(self):
		testStock = AddItem(30, 999, 888)
		self.assertEqual(30, testStock.stockID)
	def test_RemoveItem(self):
		testStock1 = Stock(30, 999, 888)
		testStock2 = Stock(1, 10, 8)
		listOfStock = [testStock1, testStock2]
		listOfStock = RemoveItem(listOfStock, 1)
		self.assertEqual(len(listOfStock), 1)
	def test_UpdateItem(self):
		testStock = Stock(1, 10, 8)
		testStock = UpdateItem(testStock, 1, 5, 3)
		self.assertEqual(testStock.available, 3)
	def test_RegisterPerson(self):
		testPerson = RegisterPerson(1, "Amanda Hugandkiss", "Miss", "Female", "09/08/2017")
		self.assertEqual(testPerson.name, "Amanda Hugandkiss")
	def test_DeletePerson(self):
		testPerson1 = Person(1, "Amanda Hugandkiss", "Miss", "Female", "09/08/2017")
		testPerson2 = Person(2, "Ben Dover", "Mr", "Male", "09/08/2017")
		PersonList = [testPerson1, testPerson2]
		PersonList = DeletePerson(PersonList, 2)
		self.assertEqual(len(PersonList), 1)
	def test_UpdatePerson(self):
		testPerson = Person(2, "Ben Dover", "Mr", "Male", "09/08/2017")
		testPerson = UpdatePerson(testPerson, 2, "I P Freely", "Mr", "Male", "10/08/2017")
		self.assertEqual(testPerson.name, "I P Freely")
	def test_SavePersons(self):
		testPerson1 = Person(1, "Amanda Hugandkiss", "Miss", "Female", "09/08/2017")
		testPerson2 = Person(2, "Ben Dover", "Mr", "Male", "09/08/2017")
		PersonList = [testPerson1, testPerson2]
		successfull = SavePersons(PersonList)
		self.assertEqual(successfull, "Success")
	def test_LoadPersons(self):
		listOfPersons = LoadPersons()
		self.assertEqual(listOfPersons[0].id, 1)
	def test_SaveLoans(self):
		testLoan1 = Loans(1, "Amanda Hugandkiss", "Miss", "Female", "09/08/2017", 1, 1, "09/08/2017", "23/08/2017", False)
		testLoan2 = Loans(2, "Ben Dover", "Mr", "Male", "09/08/2017", 2, 2, "10/08/2017", "24/08/2017", False)
		listOfLoans = [testLoan1, testLoan2]
		successfull = SaveLoans(listOfLoans)
		self.assertEqual(successfull, "Success")
	def test_LoadLoans(self):
		listOfLoans = LoadLoans()
		self.assertEqual(listOfLoans[0].id, 1)
	def test_SaveMediaResources(self):
		testMedia1 = MediaResource(3, 1, 0, 1, "Camera", "Nikkon 2209")
		testMedia2 = MediaResource(4, 3, 2, 2, "Tape Recorder", "Sony 9843")
		listOfMedia = [testMedia1, testMedia2]
		successfull = SaveMediaResources(listOfMedia)
		self.assertEqual(successfull, "Success")
	def test_LoadMedia(self):
		listOfMedia = LoadMedia()
		self.assertEqual(listOfMedia[0].id, 1)
	def test_SaveNewspapers(self):
		testPaper1 = Newspaper(2, 1, 1, 1, "The Guardian", False, "09/08/2017")
		testPaper2 = Newspaper(5, 1, 1, 5, "The Sun", True, "10/08/2017")
		listOfPapers = [testPaper1, testPaper2]
		successfull = SaveNewspapers(listOfPapers)
		self.assertEqual(successfull, "Success")
	def test_LoadNewspapers(self):
		listOfPapers = LoadNewspapers()
		self.assertEqual(listOfPapers[0].id, 1)
	def test_SaveBooks(self):
		testBook1 = Book(1, 10, 8, "9781621151593", "Mogworld", "Yahtzee Croshaw", "Dark Horse Books", "23/10/2009", "Fantasy")
		testBook2 = Book(6, 10, 10, "1783522577", "Terrible Old Games You've Probably Never Heard Of", "Stuart Ashens", "Unbound Digital", "03/12/2015", "Non-Fiction")
		listOfBooks = [testBook1, testBook2]
		successfull = SaveBooks(listOfBooks)
		self.assertEqual(successfull, "Success")
	def test_LoadBooks(self):
		listOfBooks = LoadBooks()
		self.assertEqual(listOfBooks[0].isbn, "9781621151593")
if __name__ == '__main__':
	unittest.main()