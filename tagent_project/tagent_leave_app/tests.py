from django.test import TestCase
from rest_framework.test import APITestCase
from .models import Employee, Leave
import datetime


class EmployeeAPITestCase(APITestCase):
    def setUp(self):
        employee = Employee.objects.create(
            emp_number ="TS000456",
            phone_number = "0996957885",
            first_name = "Jhon",
            last_name = "Doe",
        )

        leave = Leave.objects.create(
            employee_id = employee,
            start_date = datetime.datetime.now(),
            end_date = datetime.datetime.now(),
            days_of_leave = 20,
            status = "New"
        )

    def test(self):
        employee = Employee.objects.count()
        self.assertEqual(employee, 1)
       
    def test_1(self):
        leave = Leave.objects.count()
        self.assertEqual(leave, 1)