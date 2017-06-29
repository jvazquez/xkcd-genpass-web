'''
Created on Jun 29, 2017

@author: jvazquez
'''
import json
from flask import Blueprint, Response, request
from xkcdpass import xkcd_password as xp

web = Blueprint('web', __name__)


@web.route('/', methods=["GET"])
def webgen():
    arguments = {"wordfile": None}

    if request.args.get("min", None):
        min_lenght = request.args.get("min")
        arguments["min_length"] = min_lenght

    if request.args.get("max", None):
        max_lenght = request.args.get("max")
        arguments["max_length"] = max_lenght

    acrostic = request.args.get("acrostic", None)

    wordfile = xp.locate_wordfile()
    arguments["wordfile"] = wordfile
    mywords = xp.generate_wordlist(**arguments)

    if acrostic:
        your_password = xp.generate_xkcdpassword(mywords,
                                                 acrostic=acrostic)
    else:
        your_password = xp.generate_xkcdpassword(mywords)

    your_pwd_len = len(your_password)
    return Response(json.dumps({"password": your_password,
                                "len": your_pwd_len}),
                    status=200,
                    content_type="application/json")
