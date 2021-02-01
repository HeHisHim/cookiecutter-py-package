#!/usr/bin/python3
# encoding: utf-8
""" {{cookiecutter.project_slug}} 's entry_points"""
import fire


def cli_run():
    """
    默认函数 触发fire包
    https://github.com/google/python-fire
    """
    fire.Fire()


def ipython():
    """打开ipython命令"""
    from IPython import embed
    embed()


def version():
    """显示当前版本"""
    import {{cookiecutter.project_slug}}
    print({{cookiecutter.project_slug}}.__version__)


if __name__ == '__main__':
    cli_run()
