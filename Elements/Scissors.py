from Elements import Element
class Scissors(Element.Element):
    type = "Scissors"
    
    def compareTo(self, element):
        if element.type == self.type:
            return ("Scissors equals Scissors", "Tie")
            
            
        elif element.type == "Rock":
            return ("Rock crushes Scissors", "Lose")
            
            
        elif element.type == "Lizard":
            return ("Scissors decapitates Lizard", "Win")
            
        
        elif element.type == "Spock":
            return ("Spock smashes Scissors", "Lose")
            
            
        elif element.type == "Paper":
            return ("Scissors cuts Paper", "Win")
            
        else:
            return ("Invalid type", "Lose")
            
        