from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        # here i'm putting form fields in order
        fields = ('username', 'password', 'password2', 'first_name', 'last_name',
                  'email', 'profile_image')
        extra_kwargs = {
            # to make the password invisible after the user is created
            'password': {'write_only': True},
        }

    # checking if passwords match
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError('Passwords do not match.')
        return data

    # validating the password
    def validate_password(self, password):
        if len(password) < 8:
            # raising an error in case the password is too short
            raise serializers.ValidationError('Пароль должен быть длиннее 8 символов')
        if not any(value.isdigit() for value in password):
            # raising an error in case password doesn't contain any numbers
            raise serializers.ValidationError('В пароле должны присутсвовать цифры')
        if not any(value.isupper() for value in password):
            # raising an error in case password doesn't contain any uppercase letters
            raise serializers.ValidationError('В пароле должны быть заглавные буквы')
        if not any(value.islower() for value in password):
            # raising an error in case password doesn't contain any lowercase letters
            raise serializers.ValidationError('В пароле должны быть прописные буквы')
        return password

    # overwriting create method to save the model properly
    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
        )
        profile_image = validated_data.get('profile_image')
        if profile_image:
            user.profile_image = profile_image

        # password hashing
        user.set_password(validated_data['password'])
        user.save()

        return user
