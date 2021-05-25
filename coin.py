#Import the random method
import random

#Create a Pound Class
class Pound:

    #Class constructor Method
    def __init__(self, rare = False):

        self.rare = rare

        if rare:
            self.value = 2.5
        else:
            self.value = 1.0
        self.colour = 'gold'
        self.diameter = 2.5
        self.thickness = 3.5
        self.num_edges = 1
        self.heads = True
    #Coin Rust Method  
    def rust(self):
        self.colour = 'greenish'

    #Coin Clean Rust Colour
    def clean(self):
        self.colour = 'gold'

#coin1 = Pound()
#coin1.rust()
#print(coin1.colour)

#coin1.clean()
#print(coin1.colour)

    def flip(self):
        heads_options = [True, False]
        self.heads = random.choices(heads_options)

coin1 = Pound()
coin1.flip()
print(coin1.heads)



