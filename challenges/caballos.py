import random

class Caballo(object):
    def __init__(self, name):
        self.name = name
        self.progress = 0
        
    def turn(self):
        stepsToMove = random.randrange(6)
        self.progress += stepsToMove
        return stepsToMove
        
ny = Caballo("Nyquist")
ap = Caballo("American Pharoah")
turn = 1

print("Welcome to the race between " + ny.name, "and " + ap.name)
print("--Start the Race --")

# While Loop that simmulates the race
while ny.progress < 20 and ap.progress < 20:
    print("On turn %s" % turn, "   ",
        ny.name, "takes", ny.turn(), "steps, progress is", ny.progress, "      ", 
        ap.name, "takes", ap.turn(), "steps, progress is", ap.progress)
    turn += 1

if ap.progress < 20:
    print("--- Result:   The winner is %s!!! ---" % ny.name)
elif ny.progress < 20:
    print("--- Result:   The winner is %s!!! ---" % ap.name)
else:
    print("--- Result:   It's a tie ---")