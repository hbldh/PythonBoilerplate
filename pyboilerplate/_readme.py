def get_readme_file(params):
    """Get a rudimentary ``MANIFEST.in`` file.

    Args:
        params (dict): Parameters for this project.

    Returns:
        tuple: Relative file path and string content of file.

    """
    if params.get('readme_format').lower() == 'md':
        readme_format = params.get('readme_format').lower()
        content = """"# {project}

        ## Description

        ## Installation

        ```
        $ pip install git+https://{git_host}/{username}/{project}
        ```

        ## Usage

        ```python
        import {project}
        ```

        ## Testing

        Test by running

        ```sh
        $ python setup.py test
        ```

        or directly using [pytest](http://doc.pytest.org/en/latest/)

        ```
        $ py.test tests
        ```

        ## Documentation

        """.format(**params)
    else:
        readme_format = 'rst'
        content = """{project}
        =======================

        Description
        -----------

        Installation
        ------------

        .. code:: sh

            $ pip install git+https://{git_host}/{username}/{project}

        Usage
        -----

        .. code:: python

            import {project}

        Testing
        -------

        Test by running

        .. code:: sh

            $ python setup.py test


        or directly using `pytest <http://doc.pytest.org/en/latest/>`_

        .. code:: sh

            $ py.test tests

        Documentation
        -------------

        """.format(**params)

    return 'README.' + readme_format, content
