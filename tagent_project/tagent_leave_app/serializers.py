from rest_framework import serializers
from .models import Employee, Leave


class EmployeeSerializer(serializers.ModelSerializer):
    leave_ids = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    emp_number = serializers.CharField(required=True, allow_null=False, allow_blank=False)

    class Meta:
        model = Employee
        fields = ("id", "emp_number", "phone_number", "first_name", "last_name", "leave_ids")

        def create(self, validate_data):
            print(validate_data)
            employee = Employee.objects.create(
                employee_number = validate_data["emp_number"],
                phone_number = validate_data["phone_number"],
                first_name = validate_data["first_name"],
                last_name = validate_data["last_name"],
            )
            employee.save()
            
            return employee


class LeaveSerializer(serializers.ModelSerializer):
    start_date = serializers.DateField(required=True, allow_null=False)
    end_date = serializers.DateField(required=True, allow_null=False)

    class Meta:
        model = Leave
        fields = ("id", "employee_id", "start_date", "end_date", "days_of_leave", "status")

        def create(self, validate_data):
            leave = Leave.objects.create(
                start_date = validate_data["start_date"],
                end_date = validate_data["end_date"],
                days_of_leave = validate_data["days_of_leave"],
                status = validate_data["status"]
            )
            leave.save()

            return leave
