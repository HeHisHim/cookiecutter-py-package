
""" {{cookiecutter.project_slug}} 's entry_points"""

def cmd_entry():  # pragma: no cover
    pass


def version():
    """ 显示当前版本 """
    import {{cookiecutter.project_slug}}
    print({{cookiecutter.project_slug}}.__version__)
