from django.core.management.base import BaseCommand
from api.models import DutyPlace, SecurityGuard, DutyTime
from datetime import time

class Command(BaseCommand):
    help = 'Populates the database with sample data'

    def handle(self, *args, **kwargs):
        duty_places = [
            {'name': 'Place 1', 'address': 'Address 1'},
            {'name': 'Place 2', 'address': 'Address 2'},
        ]

        for place_data in duty_places:
            place = DutyPlace(**place_data)
            place.save()

        # Güvenlik görevlileri oluşturma
        security_guards = [
            {'name': 'Guard 1', 'surname': 'Surname 1', 'date_of_birth': '1990-01-01', 'years_of_experience': 5, 'place_id': 1},
            {'name': 'Guard 2', 'surname': 'Surname 2', 'date_of_birth': '1985-02-15', 'years_of_experience': 8, 'place_id': 2},
            {'name': 'Guard 3', 'surname': 'Surname 3', 'date_of_birth': '1980-02-14', 'years_of_experience': 10, 'place_id': 1},
            {'name': 'Guard 4', 'surname': 'Surname 4', 'date_of_birth': '1988-03-13', 'years_of_experience': 5, 'place_id': 2},
            {'name': 'Guard 5', 'surname': 'Surname 5', 'date_of_birth': '1999-04-10', 'years_of_experience': 3, 'place_id': 1},
            {'name': 'Guard 6', 'surname': 'Surname 6', 'date_of_birth': '2000-05-12', 'years_of_experience': 2, 'place_id': 2},
        ]

        for guard_data in security_guards:
            guard = SecurityGuard(**guard_data)
            guard.save()

        duty_times = [
            {'guard_id': 1, 'start_time': time(9, 0), 'end_time': time(18, 0), 'duty': 'Bir islem yapilmalidir'},
            {'guard_id': 2, 'start_time': time(8, 0), 'end_time': time(17, 0), 'duty': 'Bir islem yapilmalidir'},
            {'guard_id': 3, 'start_time': time(7, 0), 'end_time': time(16, 0), 'duty': 'Bir islem yapilmalidir'},
            {'guard_id': 4, 'start_time': time(6, 0), 'end_time': time(13, 0), 'duty': 'Bir islem yapilmalidir'},
            {'guard_id': 5, 'start_time': time(10, 0), 'end_time': time(19, 0), 'duty': 'Bir islem yapilmalidir'},
            {'guard_id': 6, 'start_time': time(12, 0), 'end_time': time(20, 0), 'duty': 'Bir islem yapilmalidir'},
        ]

        for time_data in duty_times:
            duty_time = DutyTime(**time_data)
            duty_time.save()

        self.stdout.write(self.style.SUCCESS('Sample data has been populated successfully.'))