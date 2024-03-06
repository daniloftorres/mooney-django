from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from apps.customer.models import Customer  # Importe seu modelo Customer
# Importe o serializer apropriado
from apps.customer.api.v1.serializers import CustomerSerializer

# Oauth2
from oauth2_provider.contrib.rest_framework import OAuth2Authentication, TokenHasReadWriteScope
from rest_framework.permissions import AllowAny
from rest_framework import generics, status, views
from rest_framework.response import Response
from oauth2_provider.contrib.rest_framework import TokenHasScope


class CustomerViewSetOAuth2Old(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    # Especifica que apenas a autenticação OAuth2 é permitida para esta visualização
    authentication_classes = [OAuth2Authentication]
    # Utiliza as permissões padrões que exigem que o usuário esteja autenticado
    permission_classes = [IsAuthenticated, TokenHasReadWriteScope]
    # Limita as ações permitindo apenas GET e POST
    # permission_classes = [AllowAny]  # Temporariamente para teste
    http_method_names = ['*']


class CustomerViewSetOAuth2(generics.GenericAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    # Especifica que apenas a autenticação OAuth2 é permitida para esta visualização
    authentication_classes = [OAuth2Authentication]
    # Utiliza as permissões padrões que exigem que o usuário esteja autenticado
    permission_classes = [IsAuthenticated, TokenHasReadWriteScope]
    # Limita as ações permitindo apenas GET e POST
    # permission_classes = [AllowAny]  # Temporariamente para teste
    http_method_names = ['get']

    def post(self, request):

        return Response({"status": True}, status=status.HTTP_201_CREATED)

    def get(self, request):

        token = request.auth  # request.auth contém o token de acesso
        if token:
            escopo = token.scope
            print("escopo :: ", escopo)
        else:
            print("escopo else:: ", token)

        return Response({
            'status': 'success',
            'message': 'Você está autenticado com Password!',
        }, status=status.HTTP_200_OK)


class OAuth2ClientCredentials(APIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [TokenHasScope]

    required_scopes = ['read', 'write']  # Defina os escopos necessários aqui

    def get(self, request):
        token = request.auth
        print("dentro do get#######")
        if token:
            escopo = token.scope
            print("Token válido com escopo:", escopo)
            # Verifique se o escopo do token contém 'read' e 'write'
            if 'read' in escopo and 'write' in escopo:
                return Response({
                    'status': 'success',
                    'message': 'Você está autenticado com OAuth2!',
                }, status=status.HTTP_200_OK)
            else:
                print("Token não tem os escopos necessários.")
        else:
            print("Nenhum token foi fornecido.")

        return Response({
            "detail": "You do not have permission to perform this action. eita"
        }, status=status.HTTP_403_FORBIDDEN)
