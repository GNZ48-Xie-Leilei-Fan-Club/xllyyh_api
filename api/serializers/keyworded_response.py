from rest_framework_json_api import serializers

from api.models.keyworded_response import KeywordedResponse

class KeywordedResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeywordedResponse
        fields = '__all__' 

    id = serializers.IntegerField(read_only=True)
    keyword = serializers.CharField(read_only=True)
    response = serializers.CharField(read_only=True)
