from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from .serializers import CompaySerailizer, ProductSerailizer
from .models import Company, Product

@api_view(['GET'])
def get_companies(request: Request) -> Response:
    company = Company.objects.get(id=1)
    data = CompaySerailizer(company).data
    return Response({'company': data})
