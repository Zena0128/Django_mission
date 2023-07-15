from rest_framework import serializers

from .models import Board, Comment


class CommentSerializer(serializers.ModelSerializer):
    isAnonymous = serializers.BooleanField(write_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'post', 'user', 'created_at',  'comment', 'isAnonymous']
        read_only_fields = ['user', 'created_at', 'post']

    def to_representation(self, instance):
        rep = super(CommentSerializer, self).to_representation(instance)
        rep['user'] = instance.user.nickname
        rep['created_at'] = instance.created_at.strftime("%Y-%m-%d")
        if instance.isAnonymous:
            rep['user'] = 'ANONYMOUS'
        return rep


class BoardSerializer(serializers.ModelSerializer):
    isAnonymous = serializers.BooleanField(write_only=True)

    class Meta:
        model = Board
        fields = ['id', 'user', 'title', 'body', 'isAnonymous']
        read_only_fields = ['user']

    def to_representation(self, instance):
        rep = super(BoardSerializer, self).to_representation(instance)
        if instance.isAnonymous:
            rep['user'] = 'ANONYMOUS'
        return rep


class BoardSerializerWithPk(serializers.ModelSerializer):
    isAnonymous = serializers.BooleanField(write_only=True)
    comments = CommentSerializer(many=True, required=False)  # 이거 주석 처리하면 comments에 comment list가 아니라 comment id가 나옴

    class Meta:
        model = Board
        fields = ['id', 'user', 'title', 'body', 'comments', 'isAnonymous']
        read_only_fields = ['user', 'comments']

    def to_representation(self, instance):
        rep = super(BoardSerializerWithPk, self).to_representation(instance)
        if instance.isAnonymous:
            rep['user'] = 'ANONYMOUS'
        return rep


