from rest_framework import serializers

class CompaySerailizer(serializers.Serializer):
    name = serializers.CharField()
    website = serializers.CharField()
    logo = serializers.CharField()


class ProductSerailizer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()
    ram = serializers.IntegerField()
    price = serializers.FloatField()

    # brand = serializers.ForeignKey()