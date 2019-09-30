from django.db import models
from django.utils import timezone


class TimeStampedModel(models.Model):
    time_created = models.DateTimeField(blank=True, null=True,
                                        verbose_name='Created')
    time_updated = models.DateTimeField(blank=True, null=True,
                                        verbose_name='Updated')

    @property
    def time_created_without_microseconds(self):
        return self.time_created.strftime('%d-%m-%Y %H:%M:%S')

    def get_model_name(self):
        return 'app_label}.{model_name}'.format(
            app_label=self._meta.app_label,
            model_name=self._meta.model_name
        )

    def save(self, *args, **kwargs):
        now = timezone.now()
        if not self.time_created:
            self.time_created = now

        self.time_updated = now
        super().save(*args, **kwargs)

    class Meta:
        abstract = True
        ordering = ('-time_created',)
