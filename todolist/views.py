from django.shortcuts import render
from todolist.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import *
from rest_framework import status
from rest_framework import filters
from rest_framework import generics, viewsets
from todolist.serializers import TodoSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
# ..............function based views.........
from .permissions import IsOwnerOrReadOnly


# @api_view(['GET', 'POST'])
# def Todo_list(request):
#	if request.method =='GET':
#		todos = TodoList.objects.all()
#		serializer = TodoSerializer(todos, many =True)
#		return Response(todos.data)


#	elif request.method =='POST':
#		serializer = TodoSerializer(data=request.data)
#		if serializer.is_valid():
#			serializer.save()
#			return Response(serializer.data, status=status.HTTP_201_CREATED)
#	return Response(serializer.errors, ststus=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET','PUT', 'DELETE'])
# def todo_detail(request, pk):

#	try:
#		todo = TodoList.objects.get(pk=pk)
#	except TodoList.DoesNotExist:
#		return Response(status=status.HTTP_404_NOT_FOUND)


#	if request.method =='GET':
#		serializer = TodoSerializer(todo)
#		return Response(serializer.data)


#	elif request.method =='PUT':
#		serializer = TodoSerializer(todo, data=request.data)
#		if serializer.is_valid():
#			serializer.save()
# return Response(serializer.data)
# return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#	elif request.method =='DELETE':
#		todo.delete()
#		return Response(status=status.HTTP_204_NO_CONTENT)

# ................end of function based views...........

#
# class Todo_List(generics.ListCreateAPIView):
#     queryset = TodoList.objects.all()
#     serializer_class = TodoSerializer
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['id', 'title']
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
#
#
#
#
# class Todo_Detail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = TodoList.objects.all()
#     serializer_class = TodoSerializer
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['id', 'title']
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]


class TodoViewSet(viewsets.ModelViewSet):
    queryset = TodoList.objects.all()
    serializer_class = TodoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'title']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


@api_view(['PUT', 'POST', 'GET'])
def change_status(request, pk):
    todo = TodoList.objects.get(pk=pk)
    if todo.choose == 'wt':
        todo.choose = 'wa'
        todo.save()
        global serializer
        serializer = TodoSerializer(todo, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response("", status=status.HTTP_400_BAD_REQUEST)
    # else:
    #     Todo_serializer = TodoSerializer(todo, data=request.data)
    #     if Todo_serializer.is_valid():
    #         Todo_serializer.save()
    #         return Response({"data": ''}, status=status.HTTP_200_OK)
    #     else:
    #         error_details = []
    #         for key in Todo_serializer.errors.keys():
    #             error_details.append({"field": key, "message": Todo_serializer.errors[key][0]})
    #         data = {
    #             "Error": {
    #                 "status": 400,
    #                 "message": "Your submitted data was not valid - please correct the below errors",
    #                 "error_details": error_details
    #             }
    #         }
    #         return Response(data, status=status.HTTP_400_BAD_REQUEST)
