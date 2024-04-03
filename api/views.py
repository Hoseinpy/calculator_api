from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import CalculatorSerializer
from rest_framework.request import Request


class CalculatorApiView(APIView):
    
    def calculator_result(self, num1, operators, num2):
            result = 0
            if operators == '+':
                x = num1 + num2
                result += x
            elif operators == '-':
                x = num1 - num2
                result += x
            elif operators == '*':
                x = num1 * num2
                result += x
            elif operators == '/':
                if num1 == 0:
                    return Response({'status': 'in num1 operator / cannot value 0'}, status.HTTP_406_NOT_ACCEPTABLE)
                
                x = num1 / num2
                result += x

            elif operators == '**':
                x = num1 ** num2
                result += x

            elif operators == '%':
                x = num1 % num2
                result += x

            return result
    
    def post(self, request: Request):
        serializer = CalculatorSerializer(data=request.data)
        if serializer.is_valid():
            operators = serializer.data.get('operators')
            num1  = serializer.data.get('num1')
            num2  = serializer.data.get('num2')

            result = self.calculator_result(num1, operators, num2)

            
            return Response(f'{result}', status.HTTP_200_OK)
        
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)