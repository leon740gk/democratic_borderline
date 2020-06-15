from rest_framework import serializers

from api.person.models import Person, PersonsAddress, BorderCrossing, ForbiddenStaff


class PersonAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonsAddress
        fields = (
            'street',
            'street2',
            'city',
            'state',
            'zip_code',
            'country',
        )


class ForbiddenStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForbiddenStaff
        fields = ('name', )


class BorderCrossSerializer(serializers.ModelSerializer):
    border_cross_type = serializers.CharField(source='get_border_cross_type_display')
    forbidden_stuff_withdrawn = serializers.SerializerMethodField()

    class Meta:
        model = BorderCrossing
        fields = (
            'date_of_border_cross',
            'border_cross_type',
            'allowed_pass',
            'forbidden_stuff_withdrawn',
        )

    def get_forbidden_stuff_withdrawn(self, obj):
        return ForbiddenStaffSerializer(obj.forbidden_stuff_withdrawn, many=True).data


class PersonSerializer(serializers.ModelSerializer):
    marital_status = serializers.CharField(source='get_marital_status_display')
    living_address = serializers.SerializerMethodField()
    border_crosses = serializers.SerializerMethodField()

    class Meta:
        model = Person
        fields = (
            'first_name',
            'last_name',
            'date_of_birth',
            'marital_status',
            'married_with',
            'living_address',
            'phone_number',
            'height',
            'nationality',
            'color_of_eyes',
            'border_crosses',
        )

    def get_living_address(self, obj):
        return PersonAddressSerializer(obj.living_address).data

    def get_border_crosses(self, obj):
        return BorderCrossSerializer(obj.border_crosses.all(), many=True).data
