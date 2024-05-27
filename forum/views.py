from django.contrib.auth.models import User
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.
from forum.models import Message, Forum
from forum.serializers import MessageSerializer, ForumAddUserSerializer, DetailForumSerializer, \
    CreateForumSerializer, CreateMessageSerializer, ProfileSerializer, UserSerializer


# FORUMS VIEWS START

@swagger_auto_schema(
    tags=['Forums'],
    method='get',
)
@api_view(['GET'])
def forums_list_view(request):
    if request.method == 'GET':
        topics = Forum.objects.all()
        serializer = DetailForumSerializer(topics, many=True)
        return Response(serializer.data)


@swagger_auto_schema(
    tags=['Forums'],
    method='get',
)
@api_view(['GET'])
def forum_details_view(request, pk):
    """
    :param request:
    :param pk: Forum id
    :return: Forum details data
    """
    if request.method == 'GET':
        forum = Forum.objects.get(id=pk)
        serializer = DetailForumSerializer(forum)
        return Response(serializer.data)


@swagger_auto_schema(
    tags=['Forums'],
    method='post',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'title': openapi.Schema(type=openapi.TYPE_STRING),
            'description': openapi.Schema(type=openapi.TYPE_STRING),
            'creator': openapi.Schema(type=openapi.TYPE_INTEGER),
        },
        required=['title', 'creator']
    ),
    responses={
        201: 'Created',
        400: 'Bad Request',
    }
)
@api_view(['POST'])
def create_forum_view(request):
    """
    Create a new forum
    :param request:
    :param title: Title of the new forum
    :param description: Description of the new forum
    :param creator: User who created the new forum
    :return: Created new forum
    """
    if request.method == 'POST':
        serializer = CreateForumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    tags=['Forums'],
    method='PATCH',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'user': openapi.Schema(type=openapi.TYPE_INTEGER),
        },
        required=['user']
    ),
    responses={
        201: 'Created',
        400: 'Bad Request',
    }
)
@api_view(['PATCH'])
def join_forum_view(request, pk):
    """
    Join a forum
    :param request:
    :param pk:
    :return: updated forum
    """
    if request.method == 'PATCH':
        forum = Forum.objects.get(pk=pk)
        serializer = ForumAddUserSerializer(forum, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


# FORUMS VIEWS END

# MESSAGES VIEWS START

@swagger_auto_schema(
    tags=['Messages'],
    method='post',
    request_body=CreateMessageSerializer,
    responses={
        201: 'Created',
        400: 'Bad Request',
    }
)
@api_view(['POST'])
def create_message_view(request):
    """
    Create a new forum
    :param request:
    :param title: Title of the new message
    :param body: Body of the new message
    :param forum: Forum of the new message
    :param creator: User who created the new message
    :return: Created new forum
    """
    if request.method == 'POST':
        serializer = CreateMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# MESSAGES VIEWS END

# PROFILE VIEWS START


@swagger_auto_schema(
    tags=['UserProfile'],
    method='post',
    request_body=UserSerializer,
    responses={
        201: 'Created',
        400: 'Bad Request',
    }
)
@api_view(['POST'])
def create_user_view(request):
    """
    Create a new forum
    :param request:
    :param user: User model connect
    :param avatar: Profile avatar
    :return: Created new User Profile
    """
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    tags=['UserProfile'],
    method='post',
    request_body=ProfileSerializer,
    responses={
        201: 'Created',
        400: 'Bad Request',
    }
)
@api_view(['POST'])
def create_profile_view(request):
    """
    Create a new forum
    :param request:
    :param user: User model connect
    :param avatar: Profile avatar
    :return: Created new User Profile
    """
    if request.method == 'POST':
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    tags=['UserProfile'],
    method='get',
)
@api_view(['GET'])
def users_list_view(request):
    if request.method == 'GET':
        topics = User.objects.all()
        serializer = UserSerializer(topics, many=True)
        return Response(serializer.data)


@swagger_auto_schema(
    tags=['UserProfile'],
    method='get',
)
@api_view(['GET'])
def profile_details_view(request, pk):
    """
    :param request:
    :param pk: Forum id
    :return: Forum details data
    """
    if request.method == 'GET':
        forum = Forum.objects.get(id=pk)
        serializer = ProfileSerializer(forum)
        return Response(serializer.data)

# PROFILE VIEWS END
