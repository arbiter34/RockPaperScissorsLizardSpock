from Elements import Element
class Paper(Element.Element):
    type = "Paper"
    
    def compareTo(self, element):
        if element.type == self.type:
            return ("Paper equals Paper", "Tie")
            
            
        elif element.type == "Rock":
            return ("Paper covers Rock", "Win")
            
            
        elif element.type == "Lizard":
            return ("Lizard eats Paper", "Lose")
            
        
        elif element.type == "Spock":
            return ("Paper disproves Spock", "Win")
            
            
        elif element.type == "Scissors":
            return ("Scissors cuts Paper", "Lose")
            
        else:
            return ("Invalid type", "Lose")
            
        