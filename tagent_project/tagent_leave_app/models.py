from django.db import models


class Employee(models.Model):
    emp_number = models.CharField(max_length=20, blank=False, null=False, default=None)
    phone_number = models.IntegerField(blank=False, null=False, default=None)
    first_name = models.CharField(max_length=50, blank=False, null=False, default=None)
    last_name = models.CharField(max_length=50, blank=False, null=False, default=None)

    def __str__(self):
        return self.emp_number


class Leave(models.Model):
    employee_id = models.ForeignKey(Employee, related_name='leave_ids', blank=False, null=False, on_delete=models.CASCADE)
    start_date = models.DateField(null=True, blank=True, default=None)
    end_date = models.DateField(null=True, blank=True, default=None)
    days_of_leave = models.IntegerField(blank=False, null=False, default=None)
    status = models.CharField(max_length=50, blank=False, null=False, default='New')

    def __str__(self):
        return self.status
