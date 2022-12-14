# Generated by Django 4.0.5 on 2022-08-01 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bookings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='CarMake',
            field=models.TextField(choices=[(0, ' Nissan '), (1, ' Audi '), (2, ' BMW '), (3, ' Chevrolet '), (4, ' Citroen '), (5, ' Fiat '), (6, ' Ford '), (7, ' Honda '), (8, ' Hyundai '), (9, ' Kia '), (10, ' Mercedes-Benz '), (11, ' Renault '), (12, ' Suzuki '), (13, ' Toyota '), (14, ' Volkswagen '), (15, ' Volvo '), (16, ' Mazda '), (17, ' Jaguar '), (18, ' Jeep '), (19, ' Porsche '), (20, ' Kia '), (21, ' Land Rover '), (22, ' Mini'), (23, ' Mitsubishi Motors'), (24, ' Subaru'), (25, ' Chrysler'), (26, ' Dodge'), (27, ' Tesla'), (28, ' Alfa Romeo'), (29, ' Bentley'), (30, ' Other')], max_length=25, verbose_name='Car make'),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='CustName',
            field=models.TextField(max_length=25, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='EngineType',
            field=models.TextField(choices=[(1, ' Electric car '), (2, ' Hybrid car '), (3, ' Petrol car '), (4, ' Diesel car ')], max_length=25, verbose_name='Engine type'),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='Reg',
            field=models.TextField(max_length=25, verbose_name='Registration number'),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='VehicleType',
            field=models.TextField(choices=[(0, ' Convertible '), (1, '  SUV '), (2, ' Station wagon '), (3, ' Hatchback '), (4, ' Coupe '), (5, ' Pickup truck '), (6, ' Minivan '), (7, ' Sports car '), (8, ' Truck '), (9, ' Van '), (10, ' Crossover '), (11, ' Motorcycle '), (12, ' Limousine '), (13, ' Bus '), (14, ' Roadster '), (15, ' Recreational vehicle '), (16, ' Other ')], max_length=25, verbose_name='Vehicle type'),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='date',
            field=models.DateField(help_text='DD-MM-YYYY', verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='email',
            field=models.TextField(max_length=25, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='number',
            field=models.TextField(max_length=25, verbose_name='Phone number'),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='timeslot',
            field=models.IntegerField(blank=True, choices=[(0, '09:00-09:30'), (1, '10:00-10:30'), (2, '11:00-11:30'), (3, '12:00-12:30'), (4, '13:00-13:30'), (5, '14:00-14:30'), (6, '15:00-15:30'), (7, '16:00-16:30'), (8, '17:00-17:30')], verbose_name='Time'),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='type',
            field=models.TextField(choices=[(0, ' Repair/fault '), (1, ' Major Repair '), (2, ' Major service '), (3, ' Annual service '), (4, ' Pre NCT '), (5, ' Emissions test '), (6, ' Winter service '), (7, ' Others ')], max_length=25, verbose_name='Type of appointment'),
        ),
    ]
