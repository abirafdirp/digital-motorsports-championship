from django.http import HttpRequest

from . import gcp, managers


def is_user_in_group(user, group_name):
    return user.groups.filter(name=group_name).exists()


def get_base_url(request: HttpRequest):
    return '{scheme}://{host}'.format(
        scheme=request.scheme,
        host=request.get_host()
    )
