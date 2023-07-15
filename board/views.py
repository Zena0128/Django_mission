from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveAPIView, \
    UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from . import models
from .models import Board, Comment
from .permissions import IsOwnerOrReadOnly
from .serializers import BoardSerializer, CommentSerializer, BoardSerializerWithPk


class BoardList(ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


class BoardDetail(RetrieveAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializerWithPk
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrReadOnly]


class BoardDetailUpdate(UpdateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializerWithPk
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        comments = Comment.objects.filter(post=Board.objects.get(id=self.request.path.split("/")[-3])).all()
        serializer.save(comments=comments)


class BoardDetailDestroy(DestroyAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializerWithPk
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrReadOnly]


class CommentList(ListCreateAPIView):
    serializer_class = CommentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_queryset(self):
        return Comment.objects.filter(post=Board.objects.get(id=self.request.path.split("/")[-3])).all()

    def perform_create(self, serializer):
        user = self.request.user
        post = Board.objects.get(id=self.request.path.split("/")[-3])
        serializer.save(user=user, post=post)


class SameUniversity(ListAPIView):
    serializer_class = BoardSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        university = self.request.user.university
        return Board.objects.select_related('user').filter(user__university=university).all()  # user 테이블 참조

