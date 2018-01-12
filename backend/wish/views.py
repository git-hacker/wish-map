# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse

from .models import Wish

def get_wishes(request):
    wish_list = Wish.objects.all()
    ret = []
    for wish in wish_list:
        ret.append({'ID': wish.id,
                    'user-id': wish.mp_user.id,
                    'wish-title': wish.title,
                    'wish-type': "Good",
                    'wish-desc': wish.detail,
                    'status': wish.status,
                    'geo': {'long': wish.long, 'lat': wish.lat},
                    'bannar-url': 'http://abc.com/a.jpg',
                    'img-urls': ['xxx', 'bbb'],
                    'solutions': [{'solution-desc': 'xxx', 'is-choose': True}, ],})
    return JsonResponse(ret, safe=False)
