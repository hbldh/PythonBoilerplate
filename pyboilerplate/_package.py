def get_package(params):
    """Get the ``setup.py`` file

    Args:
        params (dict): Parameters for this project.

    Returns:
        tuple: Relative file path and string content of file.

    """
    one_file_package = params.get('one_file_package', False)
    if one_file_package:
        pass
