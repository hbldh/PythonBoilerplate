def get_setup_cfg_file(bdist_wheel_universal=True):
    """Get a ``.travis.yml`` for Travis CI building.

    Args:
        bdist_wheel_universal (bool): If package can be built into binary wheel.

    Returns:
        tuple: Relative file path and string content of file.

    """
    return "setup.cfg", _SETUP_CFG.format(int(bdist_wheel_universal))


_SETUP_CFG = """[bdist_wheel]
universal={0}

[aliases]
test=pytest
"""
