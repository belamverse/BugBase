from rest_framework import serializers
from .models import Bug, Repository

class RepositorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Repository
        fields = ['id', 'name', 'owner', 'github_url', 'created_at']


class BugSerializer(serializers.ModelSerializer):
    repository = RepositorySerializer(read_only=True)
    repository_id = serializers.PrimaryKeyRelatedField(
        queryset=Repository.objects.all(), source='repository', write_only=True
    )

    class Meta:
        model = Bug
        fields = [
            'id',
            'title',
            'description',
            'issue',
            'label',
            'status',
            'due_date',
            'repository',
            'repository_id',
            'created_by',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['created_by', 'created_at', 'updated_at']


