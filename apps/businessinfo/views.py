from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from core.validations import check_invalid
from core.response_format import message_response
from .models import BusinessInfo
from datetime import datetime
from django.db.models import Q
from django.views import View
# Create your views here.

class BusinessInformationAdd(APIView):
    @staticmethod
    def post(request):
        name = request.data.get('name', None)
        logo_image = request.data.get('logo_image', None)
        about_us = request.data.get('about_us', None)
        location = request.data.get('location', None)
        employee_size = request.data.get('employee_size', None)
        website_link = request.data.get('website_link', None)
        founder_name = request.data.get('founder_name', None)
        founded_date = request.data.get('founded_date', None)
        check_invalid([name,logo_image,about_us,location,employee_size,website_link,founder_name,founded_date])
        
        # Convert the input date string to a datetime object
        founded_date = datetime.strptime(founded_date, "%b %d, %Y")

        # Format the datetime object as "YYYY-MM-DD"
        formatted_founded_date = founded_date.strftime("%Y-%m-%d")

        try:
            business_obj = BusinessInfo.objects.create(
                name=name,
                logo_image=logo_image,
                about_us=about_us,
                location=location,
                employee_size=employee_size,
                website_link=website_link,
                founder_name=founder_name,
                founded_date=formatted_founded_date,
            
            )
            return Response(message_response("Business information data added successfully"), status=200)
        except Exception as e:
            return Response(message_response("INVALID_INPUT"), status=200)
        
class BusinessInformationUpdate(APIView):
    @staticmethod
    def post(request):
        id = request.data.get('id', None)
        name = request.data.get('name', None)
        logo_image = request.data.get('logo_image', None)
        about_us = request.data.get('about_us', None)
        location = request.data.get('location', None)
        employee_size = request.data.get('employee_size', None)
        website_link = request.data.get('website_link', None)
        founder_name = request.data.get('founder_name', None)
        founded_date = request.data.get('founded_date', None)
        check_invalid([id,name,logo_image,about_us,location,employee_size,website_link,founder_name,founded_date])
        
        # Convert the input date string to a datetime object
        founded_date = datetime.strptime(founded_date, "%b %d, %Y")

        # Format the datetime object as "YYYY-MM-DD"
        formatted_founded_date = founded_date.strftime("%Y-%m-%d")

        try:
            business_information_value = BusinessInfo.objects.get(id=id, is_active=True)

            if business_information_value:
                business_information_value.name = name
                business_information_value.logo_image = logo_image
                business_information_value.about_us = about_us
                business_information_value.location = location
                business_information_value.name = name
                business_information_value.employee_size = employee_size
                business_information_value.website_link = website_link
                business_information_value.founder_name = founder_name
                business_information_value.founded_date = formatted_founded_date
                business_information_value.save()
            return Response(message_response("Business information data updated successfully"), status=200)
        except Exception as e:
            return Response(message_response("INVALID_INPUT"), status=200)
        
class BusinessInformationDelete(APIView):
    @staticmethod
    def post(request):
        id = request.data.get('id', None)
        check_invalid([id])

        try:
            business_information_value = BusinessInfo.objects.get(id=id, is_active=True)
            print(business_information_value.is_active)
            if business_information_value:
                business_information_value.is_active=False
                business_information_value.save()
            return Response(message_response("Business information data deleted successfully"), status=200)
        except Exception as e:
            return Response(message_response("INVALID_INPUT"), status=200)
        
class BusinessInformationListing(APIView):
    @staticmethod
    def get(request):
        
        try:
            business_information = BusinessInfo.objects.filter(is_active=True)
            if business_information:
                business_info_list = []
                for business_information_value in business_information:
                    business_info_value = {
                        "id":business_information_value.id,
                        "name":business_information_value.name,
                        "logo_image":business_information_value.logo_image,
                        "about_us":business_information_value.about_us,
                        "location":business_information_value.location,
                        "employee_size":business_information_value.employee_size,
                        "website_link":business_information_value.website_link,
                        "founder_name":business_information_value.founder_name,
                        "founded_date":business_information_value.founded_date,
                        "created_at":business_information_value.created_at,
                        "is_active":business_information_value.is_active
                    }
                    business_info_list.append(business_info_value)
            
                return Response(message_response(business_info_list), status=200)
        except Exception as e:
            return Response(message_response("INVALID_INPUT"), status=200)
        
class BusinessInformationSearch(APIView):
    @staticmethod
    def post(request):
        
        search_term = request.data.get('search_term', None)
        check_invalid([search_term])
        search_term_query = Q(name__icontains=search_term)

        try:
            business_information = BusinessInfo.objects.filter(search_term_query, is_active=True)
            if business_information:
                business_info_list = []
                for business_information_value in business_information:
                    business_info_value = {
                        "id":business_information_value.id,
                        "name":business_information_value.name,
                        "logo_image":business_information_value.logo_image,
                        "about_us":business_information_value.about_us,
                        "location":business_information_value.location,
                        "employee_size":business_information_value.employee_size,
                        "website_link":business_information_value.website_link,
                        "founder_name":business_information_value.founder_name,
                        "founded_date":business_information_value.founded_date,
                        "created_at":business_information_value.created_at,
                        "is_active":business_information_value.is_active
                    }
                    business_info_list.append(business_info_value)
            
                return Response(message_response(business_info_list), status=200)
        except Exception as e:
            return Response(message_response("INVALID_INPUT"), status=200)

class IndexFormpageView(View):
    template_name = 'index.html'

    def get(self, request):
        # Logic for handling GET request
        return render(request, self.template_name)
          
class AddFormpageView(View):
    template_name = 'add.html'

    def get(self, request):
        # Logic for handling GET request
        return render(request, self.template_name)
    
class ListFormpageView(View):
    template_name = 'list.html'

    def get(self, request):
        # Logic for handling GET request
        return render(request, self.template_name)