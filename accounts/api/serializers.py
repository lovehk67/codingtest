import json
import requests
from rest_framework import serializers

from accounts.models import User


def search_address(query, category):
    r = requests.get('http://api.vworld.kr/req/search', {
        'key': 'F232944C-8E07-3EA0-81D3-DF4F9FDAABD0',
        'service': 'search',
        'request': 'search',
        'version': '2.0',
        'size': '1',
        'page': '1',
        'query': query,
        'type': 'address',
        'category': category,
        'format': 'json',
        'errorformat': 'json'
    })
    data = json.loads(r.text)
    status = data['response']['status']  # OK, NOT_FOUND, ERROR
    if status == 'OK':
        address = data['response']['result']['items'][0]['address']
        return status, address['road'], address['parcel']
    return status, None, None


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'phone', 'address_input']

    def update(self, instance, validate_data):
        instance.id = validate_data.get('id', instance.id)
        instance.address_input = validate_data.get('address_input', instance.address_input)

        status, road, parcel = search_address(instance.address_input, 'road')  # 도로명주소 검색
        if status == 'OK':
            instance.address_new = road
            instance.address_old = parcel
        else:
            status, road, parcel = search_address(instance.address_input, 'parcel')  # 지번주소 검색
            if status == 'OK':
                instance.address_new = road
                instance.address_old = parcel
            else:
                instance.address_new = None
                instance.address_old = None

        instance.phone = validate_data.get('phone', instance.phone)
        instance.save()
        return instance

class UserPrintSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'phone', 'address_input', 'address_new', 'address_old']