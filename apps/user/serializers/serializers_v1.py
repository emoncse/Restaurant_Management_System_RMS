from rest_framework import serializers

from apps.user.models import User


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128, allow_blank=False, allow_null=False)

    class Meta:
        model = User
        exclude = [
            'id',
            'is_active',
            'is_staff',
            'is_superuser',
            'last_login',
            'created_at',
            'updated_at',
            'login_attempt',
            'user_permissions',
            'groups'
        ]


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = [
            'id',
            'is_active',
            'is_staff',
            'is_superuser',
            'last_login',
            'created_at',
            'updated_at',
            'login_attempt',
            'user_permissions',
            'groups'
        ]


class UserListSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField(read_only=True, required=False)

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"

    class Meta:
        model = User
        fields = ['id', 'full_name', 'email', 'username', 'profile_pic', 'role']


class UserRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = [
            'id',
            'password',
            'two_factor',
            'is_active',
            'is_staff',
            'is_superuser',
            'last_login',
            'created_at',
            'updated_at',
            'login_attempt',
            'user_permissions',
            'groups'
        ]
