def get_setup_cfg_file(params):
    """Get a ``setup.cfg`` file.

    Args:
        params (dict): Parameters for this project.

    Returns:
        tuple: Relative file path and string content of file.

    """
    bdist_wheel_universal = int(params.get("bdist_wheel_universal", 1))
    return "setup.cfg", _SETUP_CFG.format(bdist_wheel_universal)


_SETUP_CFG = """[bdist_wheel]
universal={0}

[aliases]
test=pytest
"""


def get_setup_py(params):
    """Get the ``setup.py`` file

    Args:
        params (dict): Parameters for this project.

    Returns:
        tuple: Relative file path and string content of file.

    """
    one_file_package = params.get('one_file_package', False)
    if one_file_package:
        return 'setup.py', _SETUP_PY_ONE_FILE.format(**params)
    else:
        return 'setup.py', _SETUP_PY_ONE_FILE.format(**params)


_SETUP_PY_ONE_FILE = """#!/usr/bin/env python
# -*- coding: utf-8 -*-
\"\"\"
Setup file for {project}
=============================

Created: {now}

\"\"\"

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

import os
import sys
import re
from codecs import open
from setuptools import setup


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist_wheel upload')
    sys.exit()


with open('{project}.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)


def read(f):
    return open(f, encoding='utf-8').read()


setup(
    name='{project}',
    version=version,
    author='{fullname}',
    author_email='{email}',
    description='',
    long_description=read('README.rst'),
    license={license},
    url='https://{git_host}/{username}/{project}',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
    keywords=[],
    py_modules=['{project}'],
    test_suite="tests",
    zip_safe=False,
    include_package_data=True,
    install_requires=read('requirements.txt').strip().splitlines(),
    setup_requires=['pytest-runner', ],
    tests_require=['pytest', ],
    package_data={},
    dependency_links=[],
    ext_modules=[],
    entry_points={},
)
"""

_SETUP_PY = """#!/usr/bin/env python
# -*- coding: utf-8 -*-
\"\"\"
Setup file for {project}
=============================

Created: {now}

\"\"\"

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

import os
import sys
import re
from codecs import open
from setuptools import setup, find_packages


with open('{0}/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)


def read(f):
    return open(f, encoding='utf-8').read()


setup(
    name='{project}',
    version=version,
    author='{fullname}',
    author_email='{email}',
    description='',
    long_description=read('README.rst'),
    license={license},
    url='https://{git_host}/{username}/{project}',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
    keywords=[],
    packages=find_packages(exclude=['tests', 'docs', 'examples']),
    include_package_data=True,
    install_requires=read('requirements.txt').strip().splitlines(),
    setup_requires=['pytest-runner', ],
    tests_require=['pytest', ],
    package_data={},
    dependency_links=[],
    ext_modules=[],
    entry_points={},
)

"""
