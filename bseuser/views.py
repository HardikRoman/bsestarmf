from django.shortcuts import render
from .serializers import *
from rest_framework import generics
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from django.core.paginator import Paginator
from rest_framework.pagination import PageNumberPagination
# from urlparse import urlparse, urlunparse
from urllib.parse import urlparse, urlunparse, urlsplit, parse_qs, urlencode, urlunsplit
from django.http import QueryDict
import json

# def replace_query_param(url, attr, val):
#     (scheme, netloc, path, params, query, fragment) = urlparse(url)
#     query_dict = QueryDict(query).copy()
#     query_dict[attr] = val
#     query = query_dict.urlencode()
#     return urlunparse((scheme, netloc, path, params, query, fragment))

# def remove_query_param(url, key):
#     (scheme, netloc, path, query, fragment) = urlsplit(url)
#     query_dict = parse_qs(query, keep_blank_values=True)
#     query_dict.pop(key, None)
#     query = urlencode(sorted(list(query_dict.items())), doseq=True)
#     return urlunsplit((scheme, netloc, path, query, fragment))

# class MyPaginator(PageNumberPagination):
#     page_size = 3
#     page_size_query_param = 'size'

#     def get_next_link(self):
#         if not self.page.has_next():
#             return None
#         url = self.request.build_absolute_uri()
#         page_number = self.page.next_page_number()
#         abcd = replace_query_param(url, self.page_query_param, page_number)
#         return abcd.split('?')[-1]

#     def get_previous_link(self):
#         if not self.page.has_previous():
#             return None
#         url = self.request.build_absolute_uri()
#         page_number = self.page.previous_page_number()
#         if page_number == 0:
#             return remove_query_param(url, self.page_query_param)
#         abcd = replace_query_param(url, self.page_query_param, page_number)
#         return abcd.split('?')[-1]

class EmployeemasterList(generics.ListCreateAPIView):
    queryset = Employeemaster.objects.all()
    serializer_class = EmployeemasterSerializer
    # pagination_class = MyPaginator

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get_queryset(self):
        query_parems = self.request.query_params
        if query_parems :
            if query_parems.get('designation'):
                qs = Employeemaster.objects.filter(designation__name=query_parems.get('designation'))
            elif query_parems.get('range'):
                parems = json.loads(query_parems.get('range'))
                qs = Employeemaster.objects.all() [parems['start'] -1 : parems['end']]
            elif query_parems.get('id'):
                qs = Employeemaster.objects.filter(pk=int(query_parems.get('id')))
            else:
                qs = Employeemaster.objects.all()
        else:
            qs = Employeemaster.objects.all()
        return qs

class EmployeemasterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employeemaster.objects.all()
    serializer_class = EmployeemasterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        ids = kwargs.get('pk').split(',')
        if ids:
            queryset = Employeemaster.objects.filter(id__in=ids)
            queryset.delete()
        return self.destroy(request, *args, **kwargs)

    def get_queryset(self, *args, **kwargs):
        dataId = self.kwargs.get('pk').split(',')
        qs = Employeemaster.objects.all()
        return qs


class ClientmasterList(generics.ListCreateAPIView):
    queryset = Clientmaster.objects.all()
    serializer_class = ClientmasterSerializer

    def get_queryset(self):
        qs = Clientmaster.objects.all()
        return qs

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClientmasterDetail(generics.RetrieveDestroyAPIView):
    queryset = Clientmaster.objects.all()
    serializer_class = ClientmasterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BranchmasterList(generics.ListCreateAPIView):
    queryset = Branchmaster.objects.all()
    serializer_class = BranchmasterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BranchmasterDetail(generics.RetrieveDestroyAPIView):
    queryset = Branchmaster.objects.all()
    serializer_class = BranchmasterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DesignationList(generics.ListCreateAPIView):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DesignationDetail(generics.RetrieveDestroyAPIView):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CityList(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

    def get_queryset(self):
        qs = City.objects.filter(state=self.kwargs.get('pk'))
        return qs

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CityDetail(generics.RetrieveDestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StateList(generics.ListCreateAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer

    def get_queryset(self):
        qs = State.objects.filter(country=self.kwargs.get('pk'))
        return qs

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StateDetail(generics.RetrieveDestroyAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddressList(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def get_queryset(self):
        qs = Address.objects.filter(client=self.kwargs.get('pk'))
        return qs

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddressDetail(generics.RetrieveDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BankmasterList(generics.ListCreateAPIView):
    queryset = Bankmaster.objects.all()
    serializer_class = BankmasterSerializer

    # def get_queryset(self):
    #     qs = Bankmaster.objects.filter(client=self.kwargs.get('pk'))
    #     return qs

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BankmasterDetail(generics.RetrieveDestroyAPIView):
    queryset = Bankmaster.objects.all()
    serializer_class = BankmasterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CountryList(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CountryDetail(generics.RetrieveDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SuperdistributorList(generics.ListCreateAPIView):
    queryset = Superdistributor.objects.all()
    serializer_class = SuperdistributorSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SuperdistributorDetail(generics.RetrieveDestroyAPIView):
    queryset = Superdistributor.objects.all()
    serializer_class = SuperdistributorSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DistributorList(generics.ListCreateAPIView):
    queryset = Distributor.objects.all()
    serializer_class = DistributorSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DistributorDetail(generics.RetrieveDestroyAPIView):
    queryset = Distributor.objects.all()
    serializer_class = DistributorSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DematList(generics.ListCreateAPIView):
    queryset = Demat.objects.all()
    serializer_class = DematSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DematDetail(generics.RetrieveDestroyAPIView):
    queryset = Demat.objects.all()
    serializer_class = DematSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReferenceList(generics.ListCreateAPIView):
    queryset = Referencemaster.objects.all()
    serializer_class = ReferenceSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReferenceDetail(generics.RetrieveDestroyAPIView):
    queryset = Referencemaster.objects.all()
    serializer_class = ReferenceSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def home(request):
	return render(request, 'home.html')
