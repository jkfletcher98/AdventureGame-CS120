"""Adventure Game
    Player's get two choices
    Game continues untill player quits
    """


def main():
    currentKey = "start"
    keepGoing = True
    while keepGoing:
        if currentKey == "quit":
            keepGoing = False
        else:
            playNode
   
   
def playNode(currentKey, game):
    print(f"""{description}
            1) {menu1}
            2) {menu2}
            """)
    userChoice = input("Your choice: ")
    if userChoice == "1":
        currentKey = node1
    if userChoice == "2":
        currentkey = node2
    
    return currentKey
        
    
def gameDB():
    game = {
      "start": ["You don't remember how you got here. Something's following you.", "Turn right", "right", "Turn left", "left"], 
      "right": ["Why are these hallways so long? Where are you?", "Turn right", "right2", "Turn right", "right2"], 
      "right2": ["The spiral never ends. You'll be trapped here forever. It's getting closer.", "Turn right", "right3", "Turn right", "right3"], 
      "right3": ["A deadend. You never had a chance.", "Start over", "start", "Quit", "quit"], 
      "left": ["The air is getting harder to breathe. It's coming for you.", "Stop to catch your breath", "stop", "Keep going", "go"], 
      "stop": ["You're suffocating, The air can't get to your lungs. It's found you. You never had a chance.", "Start over", "start", "Quit", "quit"], 
      "go": ["You push forward. You're so tired. There's a ladder up ahead.", "Climb up", "climb", "Ignore it and go forward", "forward"], 
      "climb": ["You pull yourself up each rung. It watches you. It's not even trying to catch up.", "Look back", "look", "Keep climbing", "climb2"], 
      "look": ["Why did you look back? Now it has you. You never had a chance.", "Start over", "start", "Quit", "quit"], 
      "climb2": ["There's light up ahead. You reach for the next rung. It breaks. You fall. You were so close.", "Start over", "start", "Quit", "quit"], 
      "forward": ["You find a door. You're free!", "Where are you?", "where", "Where were you?", "look"], 
      "where": ["You're in your bed. It was a dream. ...right? What's that in the shadows at the corner of your room? It's here. It's always here. You'll never be alone.", "Start over", "start", "Quit", "quit"], 
     }
    
    (description, menu1, node1, menu2, node2) = node
    
    return game