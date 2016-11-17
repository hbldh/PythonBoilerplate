from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

import os
from codecs import open

from pyboilerplate._gitignore import get_gitignore_file
from pyboilerplate._license import get_license_file
from pyboilerplate._manifest import get_manifest_file


def create_boilerplate(path_to_deploy_in):
    if path_to_deploy_in is None:
        path_to_deploy_in = os.path.abspath(os.path.curdir)
    else:
        path_to_deploy_in = os.path.abspath(path_to_deploy_in)

    files = [
        get_gitignore_file(),
        get_license_file(),
        get_manifest_file()
    ]

    # Create all files.
    for f in files:
        dir_name, file_name = os.path.dirname(f[0]), os.path.basename(f[0])
        file_folder = os.path.join(path_to_deploy_in, *os.path.split(dir_name))
        if not os.path.exists(file_folder):
            os.makedirs(file_folder)
        with open(os.path.join(file_folder, file_name), 'w', encoding='utf-8') as ff:
            ff.write(f[1])


if __name__ == '__main__':

    import argparse
    parser = argparse.ArgumentParser("Python Boilerplate Creator")
    parser.add_argument('path', nargs='?', type=str, default='.', help="Path to create boilerplate in.")
    args = parser.parse_args()

    create_boilerplate(args.path)

