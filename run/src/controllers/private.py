#!/usr/bin/env python3


import os
import requests


from flask import Blueprint,render_template,request,redirect,url_for,session

from ..models.model import *

pichu = Blueprint('private',__name__,url_prefix='/admin')