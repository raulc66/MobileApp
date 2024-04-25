class Level1:
    def __init__(self):
        
        self.color_combinations = [
        'red','green', 'blue',
        'green','blue', 'yellow',
        'blue', 'yellow', 'purple'

        ]

        self.target_combinations = [
            
            'red','green', 
            'green','blue',
            'blue','yellow',
            'yellow','purple'


        ]
        self.patterns = [
        [('red','green','blue')]
        ]

class Level2:
    def __init__(self):
        self.color_combinations = [
        
        'red','green', 'blue',
        'green','blue', 'yellow',
        'blue', 'yellow', 'purple'
        
        ]
        self.target_combinations = [
            
            'red','green', 
            'green','blue',
            'blue','yellow',
            'yellow','purple'

        ]

        self.patterns = [
            [('red', 'green', 'blue')],
            [('green','blue','yellow')]

        ]

        self.patterns = [
            [('red', 'green', 'blue')],
            [('green', 'blue', 'yellow')],
            [('blue', 'yellow', 'purple')]
            
        ]

class Level3:
    def __init__(self):
        self.color_combinations = [

        'red','green', 'blue',
        'green','blue', 'yellow',
        'blue', 'yellow', 'purple'
        ]

        self.target_combinations = [
        
            'red','green', 
            'green','blue',
            'blue','yellow',
            'yellow','purple'
        ]       