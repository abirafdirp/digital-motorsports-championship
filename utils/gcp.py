from functools import wraps

from django.conf import settings


def get_base_url():
    service = settings.GAE_SERVICE

    if service == 'default':
        version_service = settings.GAE_VERSION
    else:
        version_service = (
            f'{settings.GAE_VERSION}-dot-'
            f'{settings.GAE_SERVICE}'
        )

    url = (
        f'https://{version_service}-dot-'
        f'{settings.GOOGLE_CLOUD_PROJECT}.appspot.com/'
    )
    return url


def get_base_gcs_url():
    bucket_name = getattr(settings, 'GS_BUCKET_NAME', 'LOCAL')
    return f'gs://{bucket_name}/'


def slugify_for_gcs(decorated_function):
    @wraps(decorated_function)
    def wrapped(*args, **kwargs):
        result = decorated_function(*args, **kwargs)
        try:
            result = result.replace(' ', '_')
        except AttributeError:  # not string
            pass
        return result
    return wrapped
