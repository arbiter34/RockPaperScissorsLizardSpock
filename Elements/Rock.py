from Elements import Element
class Rock(Element.Element):
    type = "Rock"
    
    def compareTo(self, element):
        if element.type == self.type:
            return ("Rock equals Rock", "Tie")
            
        elif element.type == "Paper":
            return ("Paper covers Rock", "Lose")
            
            
        elif element.type == "Lizard":
            return ("Rock crushes Lizard", "Win")
            
        
        elif element.type == "Spock":
            return ("Spock vaporizes Rock", "Lose")
            
            
        elif element.type == "Scissors":
            return ("Rock crushes Scissors", "Win")
            
        else:
            return ("Invalid type", "Tie")
            
        