def get_manifest_file(params):
    """Get a rudimentary ``MANIFEST.in`` file.

    Args:
        params (dict): Parameters for this project.

    Returns:
        tuple: Relative file path and string content of file.

    """
    content = """
    include LICENSE
    include README.rst
    """
    return 'MANIFEST.in', content
