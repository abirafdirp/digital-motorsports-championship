from django.core.exceptions import PermissionDenied


class TimeStampedModelAdminMixin:
    def get_exclude(self, request, obj=None):
        super_fields = super().get_exclude(request, obj)
        if super_fields:
            return tuple(super_fields) + ('time_created', 'time_updated')
        else:
            return ('time_created', 'time_updated')


class VersionOnlyViewableBySuperUserMixin:
    def history_view(self, request, object_id, extra_context=None):
        if not request.user.is_superuser:
            raise PermissionDenied
        return super().history_view(request, object_id, extra_context)
