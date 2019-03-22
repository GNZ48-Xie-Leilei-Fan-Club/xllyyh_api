from rest_framework_json_api import serializers

from api.chatbot.models.keyworded_response import KeywordedResponse, IgnoreNumber

class KeywordedResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeywordedResponse
        fields = '__all__' 

    id = serializers.IntegerField(read_only=True)
    keyword = serializers.CharField(read_only=True)
    response = serializers.CharField(read_only=True)


class IgnoreNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = IgnoreNumber
        fields = '__all__' 

    id = serializers.IntegerField(read_only=True)
    number = serializers.CharField(read_only=True)
    note = serializers.CharField(read_only=True)
    