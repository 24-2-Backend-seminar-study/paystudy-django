from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import KakaoPay
import requests
import json

from django.conf import settings

pay_key = settings.KAKAO_PAY_KEY
cid = settings.CID

payready_url = 'https://open-api.kakaopay.com/online/v1/payment/ready'

pay_header = {
    'Content-Type': 'application/json',
    'Authorization': f'SECRET_KEY {pay_key}'
}

class PayReadyView(APIView):
    def post(self, request):
        pay_data = request.data

        # user = request.user
        # if not user.is_authenticated:
        #     return Response({"detail": "please signin."}, status=status.HTTP_401_UNAUTHORIZED)
        
        pay_data['cid'] = cid
        pay_data = json.dumps(pay_data)

        response = requests.post(payready_url, headers=pay_header, data=pay_data)
        response_data = response.json()

        if response.status_code == 200:
            KakaoPay.objects.create(
                tid=response_data['tid'],
                partner_order_id=request.data['partner_order_id'],
                partner_user_id=request.data['partner_user_id'],
                point=int(request.data['item_name'].split(' ')[0]),
                # user=user
            )

        return Response(response.json(), status=response.status_code)



