from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

import os
from codecs import open
import datetime
import subprocess

from pyboilerplate._gitignore import get_gitignore_file
from pyboilerplate._license import get_license_file
from pyboilerplate._manifest import get_manifest_file
from pyboilerplate._readme import get_readme_file
from pyboilerplate._travis import get_travis_file
from pyboilerplate._setup import get_setup_cfg_file, get_setup_py
from pyboilerplate._requirements import get_requirements_txt


def create_boilerplate(path_to_deploy_in, project_name=''):

    params = _get_user_params()
    params["project"] = project_name

    if path_to_deploy_in is None:
        path_to_deploy_in = os.path.abspath(os.path.curdir)
    else:
        path_to_deploy_in = os.path.abspath(path_to_deploy_in)

    files = [
        get_gitignore_file(params),
        get_license_file(params),
        get_manifest_file(params),
        get_readme_file(params),
        get_travis_file(params),
        get_setup_cfg_file(params),
        get_setup_py(params),
        get_requirements_txt(params),
    ]

    # Create all files.
    for f in files:
        dir_name, file_name = os.path.dirname(f[0]), os.path.basename(f[0])
        file_folder = os.path.join(path_to_deploy_in, *os.path.split(dir_name))
        if not os.path.exists(file_folder):
            os.makedirs(file_folder)
        with open(os.path.join(file_folder, file_name), 'w', encoding='utf-8') as ff:
            ff.write(f[1])


def _get_user_params():
    return {
        "year": datetime.datetime.now().year,
        "now": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
        "fullname": subprocess.Popen(["git", "config", "user.name"],
                                     stdout=subprocess.PIPE).communicate()[0],
        "username": os.getenv('USER'),
        "email": subprocess.Popen(["git", "config", "user.email"],
                                  stdout=subprocess.PIPE).communicate()[0],
        "git_host": "github.com",
        "license": "MIT",
        "readme_format": "rst"
    }


if __name__ == '__main__':

    import argparse
    parser = argparse.ArgumentParser("Python Boilerplate Creator")
    parser.add_argument('path', nargs='?', type=str, default='.',
                        help="Path to create boilerplate in.")
    args = parser.parse_args()

    create_boilerplate(args.path)

