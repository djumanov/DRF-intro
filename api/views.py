from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from .serializers import CompaySerailizer, ProductSerailizer
from .models import Company, Product

@api_view(['GET'])
def get_companies(request: Request) -> Response:
    com = request.query_params['company']
    company = Company.objects.get(name=com)
    data = CompaySerailizer(company).data
    return Response({'company': data})


@api_view(['GET'])
def get_products(request: Request) -> Response:
    products = Product.objects.all()
    products_json = [ProductSerailizer(p).data for p in products]
    return Response({'products': products_json})