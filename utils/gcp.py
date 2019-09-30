from functools import wraps

from django.conf import settings


def get_base_url():
    service = settings.GAE_SERVICE

    if service == 'default':
        version_service = settings.GAE_VERSION
    else:
        version_service = (
            '{gae_version}-dot-{gae_service}'.format(
                gae_version=settings.GAE_VERSION,
                gae_service=settings.GAE_SERVICE
            )
        )

    url = (
        'https://{version_service}-dot-{google_cloud_project}.appspot.com/'.format(  # nopep8
            version_service=version_service,
            google_cloud_project=settings.GOOGLE_CLOUD_PROJECT
        )
    )
    return url


def get_base_gcs_url():
    bucket_name = getattr(settings, 'GS_BUCKET_NAME', 'LOCAL')
    return 'gs://{bucket_name}/'.format(bucket_name=bucket_name)


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
