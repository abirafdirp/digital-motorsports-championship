from django.core.serializers import base, python
from django.core.management import call_command


def load_fixture(apps, fixture_name, app_label=None, managers=None):
    """
    This piece of code is an improvement over
    https://stackoverflow.com/a/39743581

    In the original code, the natural primary and foreign does not work.
    After I investigated it, all the models use the default managers.

    So I decided to monkey-patch them too.

    To use manager parameters, you can refer to the following example

    managers=[
        {"model_name": 'world.WorldBorder',
        "manager_class": WorldBorderManager},
        {........}
    ]

    This means that you must analyze and find out which models needs their
    managers to be monkey-patched. (just try to run this function without
    managers argument, it will raise errors so you can get to see which
    models needs its managers monkey-patched)
    """
    if managers is None:
        managers = []

    old_get_model = python._get_model

    # Define new _get_model() function here, which utilizes the apps argument
    # to get the historical version of a model.
    def _get_model(model_identifier):
        try:
            model = apps.get_model(model_identifier)
        except (LookupError, TypeError):
            raise base.DeserializationError(
                "Invalid model identifier: '{}'".format(model_identifier)
            )
        else:
            for manager in managers:
                model_name = manager['model_name']
                manager_class = manager['manager_class']
                manager_instance = manager_class()

                Model = apps.get_model(model_name)
                manager_instance.model = Model
                Model._meta.default_manager = manager_instance

            return model

    # Replace the _get_model() function on the module,
    # so loaddata can utilize it.
    python._get_model = _get_model

    try:
        # why did I have app_label parameter? :/
        if app_label is not None:
            call_command('loaddata', fixture_name, app_label=app_label,
                         verbosity=3)
        else:
            call_command('loaddata', fixture_name, verbosity=3)
    finally:
        # Restore old _get_model() function
        python._get_model = old_get_model
