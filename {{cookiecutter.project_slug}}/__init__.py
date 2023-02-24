from __future__ import print_function
from ._version import get_versions

__author__ = "{{ cookiecutter.gitlab_username }}"
__email__ = "{{ cookiecutter.email }}"
__version__ = get_versions()["version"]
del get_versions
