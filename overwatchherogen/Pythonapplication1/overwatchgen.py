#Overwatch team generator by Colby Nishimura


class hero:
	def __init__(self, name, gameRole, realRole, strength):
		self.name = name
		self.gameRole = gameRole
		self.strength = strength
        self.realRole = realRole
	def getRole(gameRole):
		return self.gameRole
	def getName(name):
		return self.name
	def getStrength(strength):
		return self.strength
    def getRealRole(realRole):
        return self.realRole
    def setRole(role):
        self.role = role
	def setName(name):
		self.name = name
	def setstrength(strength):
		self.strength = strength
print("Creating dictionary...")
HERODICT = {}
HERODICT['Genji'] = hero("Genji", "offense", 'assassin', "2")
HERODICT['Mccree'] = hero("Mccree", "offense", 'dps', "3")
HERODICT['Pharah'] = hero("Pharah", "offense", 'dps', "5")
HERODICT['Reaper'] = hero("Reaper", 'offense', 'assassin', '3')
HERODICT['Soldier'] = hero('Soldier', 'offense', 'dps', '4')
HERODICT['Tracer'] = hero('Tracer', 'offense', 'assassin','3')
HERODICT['Bastion'] = hero('Bastion', 'defense', 'dps', '2')
HERODICT['Hanzo'] = hero('Hanzo', 'defense', 'sniper', '3')
HERODICT['Junkrat'] = hero('Junkrat', 'defense', 'dps', '3')
HERODICT['Mei'] = hero('Mei', 'defense', 'tankdps','3')
HERODICT['Torbjorn'] = hero('Torbjorn', ' defense', 'builder', '3')
HERODICT['Widowmaker'] = hero('Widowmaker', 'defense', 'sniper', '3')
HERODICT['D.Va'] = hero('D.Va', 'tank', 'assassin', '1')
HERODICT['Reinhardt'] = hero('Reinhardt', 'tank', 'tank', '5')
HERODICT['Roadhog'] = hero('Roadhog', 'tank', 'tank', '4')
HERODICT['Winston'] = hero("Winston", 'tank', 'assassin', '3')
HERODICT['Zarya'] = hero('Zarya', 'tank', 'tankdps', '5')
HERODICT['Ana'] = hero('Ana', 'support', 'healer', '3')
HERODICT['Lucio'] = hero('Lucio', 'support', 'healer', '5')
HERODICT['Mercy'] = hero('Mercy', 'support', 'healer', '5')
HERODICT['Symmetra'] = hero('Symmetra', 'support', 'builder', '2')
HERODICT['Zenyatta'] = hero('Zenyatta', 'support', 'healerdps', '3')
print("Dictionary Complete!")
if __name__ == "__main__":
	print("Begin")
	herolist= []
	heronames = list(HERODICT.keys())
	print(heronames)
	heronum = int(input("Welcome to the Overwatch Team Generator. Input number of current heroes:"))
	for i in range(0, 6-heronum):
		if(i == 0):
			while(True):
				currenthero = input("Input name of "+str(i+1)+"st hero:")
				if currenthero not in heronames:
					print("Invalid name. Please try again")
				else:
					herolist.append(currenthero)
					break
		elif(i == 1):
			while(True):
				currenthero = input("Input name of "+str(i+1)+"nd hero:")
				if currenthero not in heronames:
					print("Invalid name. Please try again")
				else:
					herolist.append(currenthero)
					break
		elif(i == 2):
			while(True):
				currenthero = input("Input name of "+str(i+1)+"rd hero:")
				if currenthero not in heronames:
					print("invalid name. Please try again")
				else:
					herolist.append(currenthero)
					break
		elif(i == 3 or i == 4):
			while(True):
				currenthero = input("Input name of "+str(i+1)+"th hero:")
				if currenthero not in heronames:
					print("Invalid name. Please try again")
				else:
					herolist.append(currenthero)
					break
	print(herolist)
while(len(herolist) != 6):
    if(herolist.count('Mercy') == 0):
        herolist.append('Mercy')
    elif(herolist.count('Lucio') == 0):
        herolist.append('Lucio')
    elif(herolist.count('Soldier') == 0):
        herolist.append('Soldier')
    