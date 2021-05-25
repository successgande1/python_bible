#Import random method
import random

#Create Abstract class
class Coin:
    #create constructor method
    def __init__(self, rare = False, clean = True, heads = True, **kwargs):

        #Loop throught the key values in keywords argument items
        for key,value in kwargs.items():
            #Set Attributes for key and value
            setattr(self,key,value)
        



        self.is_rare = rare
        self.is_clean = clean
        self.heads = heads

        if self.is_rare:
            self.value = self.original_value * 1.25
        else:
            self.value = self.original_value

        if self.is_clean:
            self.colour = self.original_colour
        else:
            self.colour = self.rusty_colour

    def rust(self):
        self.colour = self.rusty_colour

    def clean(self):
        self.clean = self.clean_colour

    def __del__(self):
        self.value = 'Money Spent'
        

    def flip(self):
        heads_option = [True, False]
        choice = random.choices(heads_option)
        self.heads = choice

class Naira(Coin):
    def __init__(self):
        data = {
            'original_colour':'Gold',
            'clean_colour':'Silver',
            'original_value':1,
            'diameter': 2.55,
            'num_edges':1,
            'mass':3.0,
            'rusty_colour':'yellowish'
        }

    #call the parent construction
        super().__init__(**data)

one_kobo = Naira()

one_kobo.__del__()

print(one_kobo.value)
       