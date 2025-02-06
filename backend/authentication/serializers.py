from rest_framework import serializers as s
from .models import User
from apps.helpers.unexpected_keys import unexpected_key_names


# Create your serializers here.
class UserSerializer(s.ModelSerializer):
    confirm_password = s.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "password",
            "confirm_password",
        ]
        extra_kwargs = {"id": {"read_only": True}, "password": {"write_only": True}}

    def validate(self, data):
        if data["password"] != data["confirm_password"]:
            raise s.ValidationError({"message": "Passwords do not match."})
        return data

    def create(self, validated_data):
        validated_data.pop("confirm_password")
        return User.objects.create_user(**validated_data)

    def to_internal_value(self, data):
        unexpected_key_names(allowed=self.fields.keys(), incoming=data.keys())

        return super().to_internal_value(data)


class LoginSerializer(s.ModelSerializer):

    class Meta:
        model = User
        fields = ["id", "email", "password"]
        extra_kwargs = {"email": {"validators": []}}

    def validate(self, data):

        user = User.objects.filter(email=data["email"]).first()

        if not user:
            raise s.ValidationError({"message": "This email is not registered yet."})

        is_valid_password = user.check_password(raw_password=data["password"])
        if not is_valid_password:
            raise s.ValidationError({"message": "Password is not correct."})

        return {"user": user}
