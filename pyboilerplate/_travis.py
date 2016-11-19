def get_travis_file(project_name=''):
    """Get a ``.travis.yml`` for Travis CI building.

    Args:
        project_name (str): The name of this project.

    Returns:
        tuple: Relative file path and string content of file.

    """
    return ".travis.yml", _content.format(project_name)


_content = """language: python
sudo: false
python:
  - 2.7
  - 3.4
  - 3.5
  - "3.6-dev"
  # PyPy versions
  - "pypy"
  - "pypy3"
matrix:
  allow_failures:
    - python: "3.6-dev"
    - python: "nightly"
    - python: "pypy"
    - python: "pypy3"
branches:
  only:
    - master
    - develop
install:
  - "pip install pytest"
  - "pip install pytest-cov"
  - "pip install python-coveralls"
  - "pip install -e ."
script: py.test tests/ --cov {0} --cov-report term-missing
after_success:
  - coveralls

"""
