# Overview of useful python resources & common commands

## Resources

- [PEP-8](https://realpython.com/python-pep8/)
- [Writing Structure](https://docs.python-guide.org/writing/structure/)
- [Google's Python Writing Guide](https://google.github.io/styleguide/pyguide.htm)

## Common Commands

To create virtual environment:
>py -m venv env

To activate
>env\Scripts\activate

To install
>py -m pip install .
>py -m pip install .[dev]

Pre-commit setup
>pre-commit install
>pre-commit run --all-files
>pre-commit autoupdate

Ruff
ruff format                   # Format all files in the current directory.
ruff format path/to/code/     # Format all files in `path/to/code` (and any subdirectories).
ruff format path/to/file.py   # Format a single file
