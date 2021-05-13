#!/usr/bin/python3
# encoding: utf-8
""" {{cookiecutter.project_slug}} 's entry_points"""
from {{cookiecutter.project_slug}}.factory import create_app
app = application = create_app()

def entry_point():  # pragma: no cover
    app.run(host='0.0.0.0', port=10110, debug=True)


def version():
    """ 显示当前版本 """
    import {{cookiecutter.project_slug}}
    print({{cookiecutter.project_slug}}.__version__)


if __name__ == '__main__':
    entry_point()
