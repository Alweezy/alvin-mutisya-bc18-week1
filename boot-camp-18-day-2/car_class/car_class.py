class Car(object):
    # setting some default values
    num_of_doors = 4
    num_of_wheels = 4

    def __init__(self, name='General', model='GM', car_type='saloon', speed=0):
        self.name = name
        self.model = model
        self.car_type = car_type
        self.speed = speed
        if self.name is 'Porshe' or self.name is 'Koenigsegg':
            self.num_of_doors = 2
        elif self.car_type is 'trailer':
            self.num_of_wheels = 8
        else:
            self

    def is_saloon(self):
        '''
            Determine between saloon and trailer
        '''
        if self.car_type is not 'trailer':
            return True
        return False

    def drive(self, speed):
        '''
            Check the car type and return appropriate speed
        '''
        if self.car_type is 'trailer':
            self.speed = speed * 11
        else:
            self.speed = 10 ** speed
        return self