from django.urls import path, include
from . import views

app_name = "bseuser"

urlpatterns = [
    path('', views.home, name='home'),
    path('ClientmasterList/', views.ClientmasterList.as_view(), name='Clientmaster'),
    path('BranchmasterList/', views.BranchmasterList.as_view(), name='Branchmaster'),
    path('DesignationList/', views.DesignationList.as_view(), name='Designation'),
    path('EmployeemasterList/', views.EmployeemasterList.as_view(), name='Employeemaster'),
    # path('EmployeemasterList/<str:pk>', views.EmployeemasterList.as_view(), name='Employeemaster'),

    path('CityList/<pk>', views.CityList.as_view(), name='City'),
    path('StateList/<pk>', views.StateList.as_view(), name='State'),
    path('AddressList/<pk>', views.AddressList.as_view(), name='Address'),
    path('CountryList/', views.CountryList.as_view(), name='Country'),

    path('BankmasterList/', views.BankmasterList.as_view(), name='Bankmaster'),

    path('SuperdistributorList/', views.SuperdistributorList.as_view(), name='Superdistributor'),
    path('DistributorList/', views.DistributorList.as_view(), name='Distributor'),
    path('ReferenceList/', views.ReferenceList.as_view(), name='Reference'),

    path('DematList/', views.DematList.as_view(), name='Demat'),

    path('ClientmasterDetail/<pk>', views.ClientmasterDetail.as_view(), name='ClientmasterDetail'),
    path('BranchmasterDetail/<pk>', views.BranchmasterDetail.as_view(), name='BranchmasterDetail'),
    path('DesignationDetail/<pk>', views.DesignationDetail.as_view(), name='DesignationDetail'),
    path('EmployeemasterDetail/<str:pk>', views.EmployeemasterDetail.as_view(), name='EmployeemasterDetail'),

    path('CityDetail/<pk>', views.CityDetail.as_view(), name='CityDetail'),
    path('StateDetail/<pk>', views.StateDetail.as_view(), name='StateDetail'),
    path('AddressDetail/<pk>', views.AddressDetail.as_view(), name='AddressDetail'),
    path('CountryDetail/<pk>', views.CountryDetail.as_view(), name='CountryDetail'),

    path('BankmasterDetail/<pk>', views.BankmasterDetail.as_view(), name='BankmasterDetail'),

    path('SuperdistributorDetail/<pk>', views.SuperdistributorDetail.as_view(), name='SuperdistributorDetail'),
    path('DistributorDetail/<pk>', views.DistributorDetail.as_view(), name='DistributorDetail'),
    path('ReferenceDetail/<pk>', views.ReferenceDetail.as_view(), name='ReferenceDetail'),

    path('DematDetail/<pk>', views.DematDetail.as_view(), name='DematDetail'),
]