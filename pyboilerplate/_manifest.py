def get_manifest_file():
    """Get a rudimentary ``MANIFEST.in`` file.

    Returns:
        tuple: Relative file path and string content of file.

    """
    content = """
    include LICENSE
    include README.rst
    """
    return 'MANIFEST.in', content
