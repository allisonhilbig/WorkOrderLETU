# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from rest_framework import views

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
