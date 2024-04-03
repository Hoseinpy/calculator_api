from rest_framework import serializers


OPERATORS_CHOICES = {
    '+': 'addition',
    '-': 'subtraction',
    '*': 'multiplication',
    '/': 'division',
    '**': 'double_asterisks',
    '%': 'Modulus'
}

class CalculatorSerializer(serializers.Serializer):
    num1 = serializers.IntegerField()
    operators = serializers.ChoiceField(choices=OPERATORS_CHOICES)
    num2 = serializers.IntegerField()