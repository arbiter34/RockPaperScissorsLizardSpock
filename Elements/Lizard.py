from Elements import Element
class Lizard(Element.Element):
    type = "Lizard"
    
    def compareTo(self, element):
        if element.type == self.type:
            return ("Lizard equals Lizard", "Tie")
            
            
        elif element.type == "Paper":
            return ("Lizard eats Paper", "Win")
            
            
        elif element.type == "Spock":
            return ("Lizard poisons Spock", "Win")
            
        
        elif element.type == "Rock":
            return ("Rock crushes Lizard", "Lose")
            
            
        elif element.type == "Scissors":
            return ("Scissors decapitates Lizard", "Lose")
            
        else:
            return ("Invalid type", "Tie")
            
        