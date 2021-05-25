#Create an Abstract Copy class
class Copier:
    def __init__(self, name, make, paper_size):
        self.name =  name
        self.make = make
        self.paper_size = paper_size


    def power_on_gen(self, fuel, choke, ignition):
        if not self.fuel == 1:
            print('You need to Put in Fuel First')
        else:
            if not self.choke and self.ignition:
                print('You must put on the Choke and Ignition')
            else:
                print('You can now put on the power supply switch')
        
            


    #Make a copy method
    def make_copy(self, paper_size):
        if self.paper_size == 'A4':
            print('You have Photocopied Your Document')
        else:
            print('Only A4 Papers are allowed')
    def __str__(self):
        return f'{self.name} is working'

class Hp(Copier):
    #Constructor Method
    def __init__(self, paper, fuel, choke, ignition):
        self.fuel = fuel
        self.choke = choke
        self.ignition = ignition
        self.paper = paper
        #Call the parent constructor and pack down the data
        super().__init__('MPF 3025', 'HP', 'A4')

    #Make a copy method
    def make_copy(self):
        copypaper = input('Enter Paper in the Trial: ')
        while copypaper not in 'A4, A2, A5':
            copypaper = input('Pls Enter the Right Paper Size: ')
        if copypaper:
            print('You have Photocopied Your Document')
        else:
            print('Check Trial, Paper has Jam') 

class Gen(Copier):
    def __init__(self, fuel):
        self.fuel = fuel
        

        super().__init__('HP', 'HP', 'A4')

    def power_on_gen(self, fuel, choke):
        if fuel == 10 and choke == 'on':
            print('You can now put on the Ignition')
        else:
            print('You need to put in atleast 10 littres and Choke on first')


        

Billa_yamaha = Gen(10)

Billa_yamaha.power_on_gen(2, 'on')

