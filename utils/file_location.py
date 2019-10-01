import os

dir_path = os.path.dirname(os.path.realpath(__file__))


def get_absolute_path(relative_path_from_project_root):
    """
    Get full path, current working directory is root folder of this
    project
    """
    return os.path.join(dir_path, '..', relative_path_from_project_root)
