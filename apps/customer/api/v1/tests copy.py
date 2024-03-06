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
            username='testuser', password='testpassword')
        self.token = RefreshToken.for_user(
            self.user)  # Gera token para o usuário

    def test_jwt_auth_old(self):
        # Define o token no cabeçalho de autorização
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {self.token.access_token}')

        url = reverse('customer-list')

        print(" access_token :: ", self.token.access_token)
        print("response url", url)

        # Faz a requisição e recebe a resposta
        response = self.client.get(url, follow=True)
        # Para visualizar cadeias de redirecionamento
        print("response.redirect_chain :: ", response.redirect_chain)
        print("response.status_code :: ", response.status_code)
        print("response.headers :: ", response.headers)

        """
        full_url = response.wsgi_request.build_absolute_uri()
        print("response full_url", full_url)
        # Imprime o status da resposta
        print("response.status_code", response.status_code)
        # Imprime os cabeçalhos da resposta
        print("response.headers", response.headers)
        """

        # test com request
        """url = "http://localhost:8000/v1/customer"
        payload = {}
        headers = {
            'Authorization': f'Bearer {self.token.access_token}'
        }
        response_2 = requests.request(
            "GET", url, headers=headers, data=payload)
        print("test com request status return :: ", response_2.status_code)
        print("test com request headers return :: ", response_2.headers)
"""
        # Verifica se o status da resposta é 200 OK, indicando sucesso na autenticação
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_jwt_auth(self):
        # Define o token no cabeçalho de autorização
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {self.token.access_token}')
        url = reverse('customer-list')
        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
