#!/usr/bin/python3
# encoding: utf-8
""" {{cookiecutter.project_slug}} 's entry_points"""

def entry_point():  # pragma: no cover
    pass


def version():
    """ 显示当前版本 """
    import {{cookiecutter.project_slug}}
    print({{cookiecutter.project_slug}}.__version__)


if __name__ == '__main__':
    entry_point()
