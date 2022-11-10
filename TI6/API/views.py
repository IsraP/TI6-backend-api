from API.serializers import MamografiaSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from API.models import Mamografia
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from API.utils.mongo_utils import ObjectIdMapper

# Create your views here.

class MamografiaViewSet(viewsets.ModelViewSet):
    queryset = Mamografia.objects.all().order_by('-data_envio')
    serializer_class = MamografiaSerializer

@api_view(['GET', 'POST'])
def mamografia_list_or_add(request):
    if request.method == 'GET':
        searchFilter = request.GET.get('rotulo')

        if searchFilter != None:
            print(searchFilter)
            print('.' + searchFilter + '.')
            mamografias = Mamografia.objects.filter(rotulo__contains='.' + searchFilter + '.')
            serializer = MamografiaSerializer(mamografias, many=True)
        else:
            print("achei nada")

            return Response([])

            mamografias = Mamografia.objects.all()
            serializer = MamografiaSerializer(mamografias, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MamografiaSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PATCH', 'DELETE'])
def mamografia_detail(request, pk):
    try:
        id = ObjectIdMapper.to_internal_value(pk)

        mamografia = Mamografia.objects.get(pk=id)
    except Mamografia.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = MamografiaSerializer(mamografia)

        return JsonResponse(serializer.data)

    elif request.method == 'PATCH':
        data = JSONParser().parse(request)
        serializer = MamografiaSerializer(mamografia, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            
            return JsonResponse(serializer.data)

        return JsonResponse(serializer.errors, status = 400)

    elif request.method == 'DELETE':
        mamografia.delete()
        return HttpResponse(status=204)
