def get_readme_file(project_name='', readme_format='rst'):
    """Get a rudimentary ``MANIFEST.in`` file.

    Args:
        readme_format (str): `rst` for reStructured Text or `md` for Markdown.

    Returns:
        tuple: Relative file path and string content of file.

    """
    if readme_format.lower() == 'md':
        content = """"# {0}

        ## Description

        ## Installation

        ```
        $ pip install git+https://www.github.com/hbldh/{0}
        ```

        ## Usage

        ```python
        import {0}
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

        """.format(project_name)
    else:
        readme_format = 'rst'
        content = """{0}
        =======================

        Description
        -----------

        Installation
        ------------

        .. code:: sh

            $ pip install git+https://www.github.com/hbldh/{0}

        Usage
        -----

        .. code:: python

            import {0}

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

        """.format(project_name)

    return 'README.' + readme_format, content
