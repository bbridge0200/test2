# -*- coding: utf-8 -*-

"""Top-level package for test2."""

__author__ = "Beatrice Bridge"
__email__ = "beatrice.bridge@alleninstitute.org"
# Do not edit this string manually, always use bumpversion
# Details in CONTRIBUTING.md
__version__ = "0"


def get_module_version():
    return __version__


from .example import Example  # noqa: F401
