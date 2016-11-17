
from urllib import urlopen


def get_gitignore_file(envs_to_include=None):
    """Request a `.gitignore` from gitignore.io.

    Default: `jetbrains,linux,windows,visualstudiocode,sublimetext,python,c,c++`

    Args:
        envs_to_include (str): Operating Systems, IDEs and programming languages to add gitignore entries for.

    Returns:
        tuple: Relative file path and string content of file.

    """
    if not envs_to_include:
        envs_to_include = "jetbrains,linux,windows,visualstudiocode,sublimetext,python,c,c++"
    url = "https://www.gitignore.io/api/{0}".format(envs_to_include)
    r = urlopen(url)
    return '.gitignore', r.read()
