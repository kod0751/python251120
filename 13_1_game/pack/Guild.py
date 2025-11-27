class Guild:
    def __init__(self, id):
        self.__name = self
        self.__users = []
    
    def addUser(self, user):
        self.__users.append(user)

    def getRanker(self):
        ranker = self.__users[0]
        for user in self.__users[1:]:
            if user.getLevel() > ranker.getLevel():
                ranker = user
        return ranker

    def getBestSales(self):
        sales = self.__users[0]
        for user in self.__users[1:]:
            if len(user.getInven()) > len(sales.getInven()):
                sales = user
        return sales

    def getUsers(self):
        return self.__users 