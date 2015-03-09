from Elements import Element
class Spock(Element.Element):
    type = "Spock"
    
    def compareTo(self, element):
        if element.type == self.type:
            return ("Spock equals Spock", "Tie")
            
            
        elif element.type == "Paper":
            return ("Paper disproves Spock", "Lose")
            
            
        elif element.type == "Lizard":
            return ("Lizard poisons Spock", "Lose")
            
        
        elif element.type == "Rock":
            return ("Spock vaporizes Rock", "Win")
            
            
        elif element.type == "Scissors":
            return ("Spock smashes Scissors", "Win")
            
        else:
            return ("Invalid type", "Tie")
            
        