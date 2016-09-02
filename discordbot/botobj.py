#Class for managing the bot's use
#State is 0 while not in use, 1 when it is
class bot:
    def _init_(self, client):
        self.client = client
        self.state = 0

    def getClient(self):
        return self.client

    def getState(self):
        return self.state

    def setState(self, newState):
        self.state = newState