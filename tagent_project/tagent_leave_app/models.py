from django.db import models


class Employee(models.Model):
    emp_number = models.CharField(max_length=20, blank=False, null=False, default=None)
    phone_number = models.IntegerField(blank=True, null=True, default=None)
    first_name = models.CharField(max_length=50, blank=True, null=True, default=None)
    last_name = models.CharField(max_length=50, blank=True, null=True, default=None)

    def __str__(self):
        return self.emp_number


class Leave(models.Model):
    employee_id = models.ForeignKey(Employee, related_name='leave_ids', blank=False, null=False, on_delete=models.CASCADE)
    start_date = models.DateField(null=False, blank=False, default=None)
    end_date = models.DateField(null=False, blank=False, default=None)
    days_of_leave = models.IntegerField(blank=True, null=True, default=None)
    status = models.CharField(max_length=50, blank=False, null=False, default='New')

    def __str__(self):
        return self.status
