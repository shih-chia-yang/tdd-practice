class Participant:
    def __init__(self,name):
        self.name=name
        self.points=0
        self.__choose_symbol=""

    @property
    def choose_symbol(self):
        return self.__choose_symbol

    def choose(self):
        symbols=['rock','paper','scissor']
        while self.__choose_symbol not in symbols:
            choice=input(f'{self.name} ,select rock,paper,scissor: ')
            if isinstance(choice,str)==True and choice in symbols:
                self.__choose_symbol=choice
            else:
                print('you must select on in {rock,paper,scissor}')
        print(f'{self.name} selects {self.__choose_symbol}')
    def toNumericalChoice(self):
        switcher={"rock":0,"paper":1,"scissor":2}
        return(switcher[self.__choose_symbol])
    def addPoing(self):
        self.points+=1

class GameRound:
    def __init__(self,p1,p2):
        self.__rule=[[0,-1,1],[1,0,-1],[-1,1,0]]
        p1.choose()
        p2.choose()
        result=self.compareChoices(p1,p2)
        if(result>0):
            p1.addPoing()
        if(result<0):
            p2.addPoing()
    def compareChoices(self,p1,p2):
        return self.__rule[p1.toNumericalChoice()][p2.toNumericalChoice()]
    def getResultAsString(self,result):
        res={0:"draw",1:"win",-1:"loss"}
        return res[result]

class Game:
    def __init__(self):
        self.endGame=False
        self.participant=Participant('player1')
        self.secondParticipant=Participant('player2')
        self.resultString="It's a Draw"
    def Start(self):
        GameRound(self.participant,self.secondParticipant)
        self.checkEndCondition()
    def determineWinner(self):
        if self.participant.points > self.secondParticipant.points:
            self.resultString = "Winner is {name}".format(name=self.participant.name)
        elif self.participant.points < self.secondParticipant.points:
            self.resultString = "Winner is {name}".format(name=self.secondParticipant.name)
        print(self.resultString)
    def checkEndCondition(self):
        answer = input("Continue game y/n: ")
        if answer == 'y':
            GameRound(self.participant, self.secondParticipant)
            self.checkEndCondition()
        else:
            print("Game ended, {p1name} has {p1points}, and {p2name} has {p2points}".format(p1name = self.participant.name, p1points= self.participant.points, p2name=self.secondParticipant.name, p2points=self.secondParticipant.points))
            self.determineWinner()
            self.endGame = True


game =Game()
game.Start()