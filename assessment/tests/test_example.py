# def test_example():
#     assert 1 == 1

from django.test import TestCase, Client
from django.urls import reverse

class BusinessInformationAddTestCase(TestCase):
    
    def setUp(self):
        from apps.businessinfo.models import BusinessInfo
        
        # Set up any necessary data for your tests
        self.client = Client()
        self.model_instance = BusinessInfo.objects.create(
            name="Nokia",
            logo_image="https://www.nokia.com/themes/custom/onenokia_reskin/logo.svg",
            about_us="Nokia is a Finnish multinational communications corporation engaged in the manufacturing of mobile devices and network infrastructure.",
            location="Espoo, Southern Finland, Finland",
            employee_size="10001",
            website_link="www.nokia.com",
            founder_name="Ankur Bhan, Frederic Idestam, Leo Mechelin, Stevie Case",
            founded_date="May 12, 1865"
        )

    def test_view_function(self):
        # Test a view function
        from apps.businessinfo.views import BusinessInformationAdd, BusinessInformationDelete, BusinessInformationUpdate, BusinessInformationListing, BusinessInformationSearch, AddFormpageView, ListFormpageView, IndexFormpageView
        response = self.client.get(reverse(BusinessInformationAdd))  # Replace 'your_view_name' with the actual view name
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Expected content in the response')

    def test_model_method(self):
        # Test a method on a model
        result = self.model_instance.post()  # Call the method you want to test
        self.assertEqual(result, {"message":"Business information data added successfully"})  # Replace 'expected_result' with the expected outcome

    # Add more test cases as needed
