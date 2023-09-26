from django.db import models


class DutyPlace(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class SecurityGuard(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    years_of_experience = models.IntegerField()
    place = models.ForeignKey(DutyPlace, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.surname}"


class DutyTime(models.Model):
    guard = models.ForeignKey(SecurityGuard, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    duty = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f"{self.guard} - {self.start_time} to {self.end_time}"