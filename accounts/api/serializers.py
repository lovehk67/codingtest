from rest_framework import serializers
from accounts.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'phone', 'address_input']

    def update(self, instance, validate_data):
        print(validate_data)
        instance.id = validate_data.get('id', instance.id)
        instance.address_input = validate_data.get('address_input', instance.address_input)

        print(instance.address_input)
        #여기서 address_input으로 도로명주소, 지번주소 검색

        instance.address_new = 'address new'
        instance.address_old = 'address old'
        instance.phone = validate_data.get('phone', instance.phone)
        instance.save()
        return instance
