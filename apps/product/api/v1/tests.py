# customer/api/v1/tests.py
import requests
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User


class JWTAuthTest(APITestCase):
    def setUp(self):
        # Cria um usuário para testar a autenticação
        self.user = User.objects.create_user(
            username='testuser2', password='testpassword2')
        self.token = RefreshToken.for_user(
            self.user)  # Gera token para o usuário

    def test_jwt_auth(self):
        # debug
        print("self.user :: ", self.user)
        print("self.user.id :: ", self.user.id)
        print("self.user.username :: ", self.user.username)

        # Define o token no cabeçalho de autorização
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {self.token.access_token}')
        url = reverse('customer-list')
        response = self.client.get(url, follow=True)
        print("response.status_code :: ", response.status_code)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
