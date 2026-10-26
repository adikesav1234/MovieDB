from django.shortcuts import render
from MovieApp.models import MovieDb
from MovieApp.serializers import MovieSerializers
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class MovieListView(APIView):
    def get(self,request):
        qs=MovieDb.objects.all()
        serializer_instance=MovieSerializers(qs,many=True)
        return Response(data=serializer_instance.data)
    def post(self,request):
        form_data=request.data
        serializer_instance=MovieSerializers(data=form_data)
        if serializer_instance.is_valid():
            actual_data=serializer_instance.validated_data
            MovieDb.objects.create(**actual_data)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors,status=400)

class MovieRetrieveUpdateDeelete(APIView):
    def get(self,request,pk):
        qs=MovieDb.objects.get(id=pk)
        serializer_instance=MovieSerializers(qs)
        return Response(data=serializer_instance.data)

    def put(self,request,pk):
        form_data=request.data
        serializer_instaance=MovieSerializers(data=form_data)
        if serializer_instaance.is_valid():
            original_data=serializer_instaance.validated_data
            MovieDb.objects.filter(id=pk).update(**original_data)
            return Response(data=serializer_instaance.data)
        else:
            return Response(data=serializer_instaance.errors)

    def delete(self,request,pk):
        qs=MovieDb.objects.filter(id=pk).delete()
        return Response({"message": "deleted successfully...!"})
