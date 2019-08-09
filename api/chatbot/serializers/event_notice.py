from rest_framework_json_api import serializers

from api.models.event_notice import NewMemberNotice

class NewMemberNoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewMemberNotice
        fields = '__all__' 

    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(read_only=True)
    response = serializers.CharField(read_only=True)
