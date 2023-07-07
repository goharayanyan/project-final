import json 
from django.http import HttpResponse


def data_status_bid(data, status_code=200, status_message="Body description is located below"):
    if status_code == 204 or status_code == 201:
        return HttpResponse(
            status=status_code,
            content_type="text/plain;charset=UTF-8"
        )
    else:
        return HttpResponse(
            json.dumps(data),
            status=status_code,
            reason=status_message,
            content_type="application/json",
        )

def data_status_notif(data, status_code=200, status_message="The format is located below"):

        return HttpResponse(
            json.dumps(data),
            status=status_code,
            reason=status_message,
            content_type="application/json"
        )
 
def data_status_creative(data, status_code=201, status_message=" "):
        return HttpResponse(
            content=json.dumps(data),
            status=status_code,
            reason=status_message,
            content_type="text/plain;charset=UTF-8"
        )


def data_status_campaign(data, status_code=201, status_message="The format is located below"):
    return HttpResponse(
        content=json.dumps(data),
        status=status_code,
        reason=status_message,
        content_type="application/json"
    )

def ok_status(data):
    return HttpResponse(
        status=200,
        content_type="application/json",
    )


def status_configue(data, status_code=200):
    return HttpResponse(
        status=status_code,
        content_type="application/json",
    )