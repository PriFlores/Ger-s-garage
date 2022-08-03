from django.db import models


class Staff(models.Model):
    name = models.TextField(max_length=25)

    def get_bookings(self):
        return Bookings.objects.filter(booking=self)

    def __str__(self):
        return self.name

class Bookings(models.Model):
    class Meta:
        unique_together = ('staff', 'date', 'timeslot')
    CAR_MAKES = [(0,' Nissan '),
                 (1,' Audi '),
                 (2,' BMW '),
                 (3,' Chevrolet '),
                 (4,' Citroen '),
                 (5,' Fiat '),
                 (6,' Ford '),
                 (7,' Honda '),
                 (8,' Hyundai '),
                 (9,' Kia '),
                 (10,' Mercedes-Benz '),
                 (11,' Renault '),
                 (12,' Suzuki '),
                 (13,' Toyota '),
                 (14,' Volkswagen '),
                 (15,' Volvo '),
                 (16,' Mazda '),
                 (17,' Jaguar '),
                 (18,' Jeep '),
                 (19,' Porsche '),
                 (20,' Kia '),
                 (21,' Land Rover '),
                 (22,' Mini'),
                 (23,' Mitsubishi Motors'),
                 (24,' Subaru'),
                 (25,' Chrysler'),
                 (26,' Dodge'),
                 (27,' Tesla'),
                 (28,' Alfa Romeo'),
                 (29,' Bentley'),
                 (30,' Other'), ]

    TIMESLOT_LIST = (
        (0, '09:00-09:30'),
        (1, '10:00-10:30'),
        (2, '11:00-11:30'),
        (3, '12:00-12:30'),
        (4, '13:00-13:30'),
        (5, '14:00-14:30'),
        (6, '15:00-15:30'),
        (7, '16:00-16:30'),
        (8, '17:00-17:30'),


    )
    CAR_TYPE = [
        (0, ' Convertible '),
        (1, '  SUV '),
        (2, ' Station wagon '),
        (3, ' Hatchback '),
        (4, ' Coupe '),
        (5, ' Pickup truck '),
        (6, ' Minivan '),
        (7, ' Sports car '),
        (8, ' Truck '),
        (9, ' Van '),
        (10, ' Crossover '),
        (11, ' Motorcycle '),
        (12, ' Limousine '),
        (13, ' Bus '),
        (14, ' Roadster '),
        (15, ' Recreational vehicle '),
        (16, ' Other '), ]
    Engine_TYPES = [(1, ' Electric car '),
                    (2, ' Hybrid car '),
                    (3, ' Petrol car '),
                    (4, ' Diesel car '), ]
    APP_TYPE = [(0, ' Repair/fault '),
                (1, ' Major Repair '),
                (2, ' Major service '),
                (3, ' Annual service '),
                (4, ' Pre NCT '),
                (5, ' Emissions test '),
                (6, ' Winter service '),
                (7, ' Others '), ]

    STATUS =[(0,'Booked'),
            (1, ' In Progress'),
            (2, ' Scrapped '),
            (3, ' Fixed '),]
    CustName = models.TextField( 'Name',max_length=25)
    Reg = models.TextField('Registration number',max_length=25)
    timeslot = models.IntegerField('Time',choices=TIMESLOT_LIST, blank=True)
    date = models.DateField('Date',help_text='DD-MM-YYYY')
    type = models.IntegerField( 'Type of appointment',choices=APP_TYPE)
    number = models.TextField('Phone number',max_length=25)
    email = models.TextField('email',max_length=25)
    VehicleType = models.IntegerField('Vehicle type',choices=CAR_TYPE)
    CarMake = models.IntegerField('Car make',choices=CAR_MAKES)
    EngineType = models.IntegerField('Engine type',choices=Engine_TYPES)
    status = models.IntegerField('Status', choices=STATUS)
    staff = models.ForeignKey('Staff', on_delete=models.CASCADE)

    def __str__(self):

        return '{},{},{},{},{},{}'.format(self.id,self.CustName,self.date,self.type,self.staff,self.status)

    @property
    def VehicleTypes(self):
        return self.CAR_TYPE[self.VehicleType][1]

    @property
    def BookingStatus(self):
        return self.STATUS[self.Status][1]

    @property
    def EngineTypes(self):
        return self.Engine_TYPES[self.EngineType][1]

    @property
    def CarMakes(self):
        return self.CAR_MAKES[self.CarMake][1]

    @property
    def time(self):
        return self.TIMESLOT_LIST[self.timeslot][1]




