# from django.urls import reverse
# from rest_framework.test import APITestCase
# from rest_framework import status
# from users.models import User


# # class UserRegistrationAPIViewTestCase(APITestCase):
# #     def test_registration(self):
# #         url = reverse("user_view")
# #         user_data = {
# #             "email":"testuser@gmail.com",
# #             "password":"password",
# #         }
# #         print(response.data)
# #         response = self.client.post(url, user_data)
# #         self.assertEqual(response.status_code, 200)


# class LoginUserTest(APITestCase):
#     def setUp(self):
#         self.data= {"username":"john", "password":"johnpassword"}
#         self.user = User.objects.create_user('John', 'johnpassword')

#     def test_login(self):
#         response = self.client.post(response('token_obtain_pair'), self.data)
#         self.assertEqual(response.status_code, 200)