from rest_framework.views import APIView
from .models import TodoModel
from .serializers import TodoModelSerializer, TodoCreateSerializer, TodoUpdateSerializer
from rest_framework.response import Response
from rest_framework import status


class TodoModelGetView(APIView):

    def get(self,request):
        todos = TodoModel.objects.all()
        todoserializer = TodoModelSerializer(todos,many = True)
        return Response(todoserializer.data, status.HTTP_200_OK)
    
    def put(self, request, pk,  *args, **kwargs):
        try:
           todo =  TodoModel.objects.get(pk = pk)
        except TodoModel.DoesNotExist:
            return Response({"Error":"Model not found "}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = TodoUpdateSerializer(todo, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Changed Successfully"},status=status.HTTP_201_CREATED)        
        return Response({"erros":"Error","detail":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk,  *args, **kwargs):
        try:
           todo =  TodoModel.objects.get(pk = pk)
        except TodoModel.DoesNotExist:
            return Response({"Error":"Model not found "}, status.HTTP_404_NOT_FOUND)
        
        todo.delete()
        return Response({"message":"Deleted"}, status.HTTP_200_OK)
        


class TodoModelCreateView(APIView):

    def post(self,request,*args, **kwargs):
        serializer = TodoCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Created Successfully"},status=status.HTTP_201_CREATED)        
        return Response({"erros":"Error","detail":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)




