from rest_framework import serializers


class Levin():
    def __init__(self, s1, s2, levin_len, time):
        self.levin_len = levin_len
        self.s1 = s1
        self.s2 = s2
        self.time = time

class LevinSerializer(serializers.Serializer):
    levin_len = serializers.IntegerField()
    s1 = serializers.CharField()
    s2 = serializers.CharField()
    time = serializers.FloatField()