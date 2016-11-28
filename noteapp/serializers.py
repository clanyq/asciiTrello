from rest_framework import serializers
from noteapp.models import Note
from django.contrib.auth.models import User

# class NoteSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     text = serializers.CharField(required=False, allow_blank=True, max_length=255)
#
#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return Note.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.note = validated_data.get('note', instance.note)
#         instance.save()
#         return instance


class NoteSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(read_only=False)
    text = serializers.CharField(required=False, allow_blank=True, max_length=255)
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Note
        fields = ('id', 'text', 'owner')

class UserSerializer(serializers.ModelSerializer):
    text = serializers.PrimaryKeyRelatedField(many=True, queryset=Note.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'text')
