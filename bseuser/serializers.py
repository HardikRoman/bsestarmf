from rest_framework import serializers, pagination
from .models import *


class BankmasterSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Bankmaster

class NomineemasterSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Nomineemaster

class ClientmasterSerializer(serializers.ModelSerializer):
    bank = BankmasterSerializer(many=True)
    nominee = NomineemasterSerializer(many=True)
    class Meta:
        fields = '__all__'
        model = Clientmaster

class BranchmasterSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Branchmaster

class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Designation

class EmployeemasterSerializer(serializers.ModelSerializer):
    reporting_aurthority_first_name= serializers.CharField(source='reporting_aurthority.first_name', read_only=True)
    reporting_aurthority_last_name= serializers.CharField(source='reporting_aurthority.last_name', read_only=True)
    reporting_aurthority_middle_name= serializers.CharField(source='reporting_aurthority.middle_name', read_only=True)
    designation_name= serializers.CharField(source='designation.name', read_only=True)
    branch_name= serializers.CharField(source='branch.branch_name', read_only=True)

    class Meta:
        # fields = '__all__'
        fields = ('id', 'first_name', 'last_name', 'middle_name', 'reporting_aurthority', 'designation', 'branch', 'date_of_birth', 'email',
            'emp_id', 'is_active', 'reporting_aurthority_first_name', 'reporting_aurthority_last_name', 'reporting_aurthority_middle_name', 'designation_name', 'branch_name')
        model = Employeemaster

# class PaginatedEmployeemasterSerializer(pagination.PaginationSerializer):
#     class Meta:
#         object_serializer_class = EmployeemasterSerializer


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = City

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = State

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Country

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Address

class SuperdistributorSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Superdistributor

class DistributorSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Distributor

class DematSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Demat

class ReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Referencemaster