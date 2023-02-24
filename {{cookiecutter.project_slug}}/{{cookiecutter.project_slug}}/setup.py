
"""A setuptools based setup module for {{ cookiecutter.project_slug }}"""
from setuptools import setup, find_packages
import versioneer


{%- set license_classifiers = {
    'MIT license': 'License :: OSI Approved :: MIT License',
    'BSD license': 'License :: OSI Approved :: BSD License',
    'ISC license': 'License :: OSI Approved :: ISC License (ISCL)',
    'Apache Software License 2.0': 'License :: OSI Approved :: Apache Software License',
    'GNU General Public License v3': 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
} %}

setup(
    name="{{ cookiecutter.project_slug }}",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="{{ cookiecutter.project_short_description }}",
    author="{{ cookiecutter.gitlab_username }}",
    author_email='{{ cookiecutter.email }}',
    packages=find_packages(include=['{{ cookiecutter.project_slug }}', '{{ cookiecutter.project_slug }}.*']),
    entry_points={
        'console_scripts': [
            '{{ cookiecutter.project_slug }}={{ cookiecutter.project_slug }}.__main__:cmd_entry',
        ],
    },
    include_package_data=True,
{%- if cookiecutter.open_source_license in license_classifiers %}
    license="{{ cookiecutter.open_source_license }}",
{%- endif %}
    python_requires=">=3.6",
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
{%- if cookiecutter.open_source_license in license_classifiers %}
        '{{ license_classifiers[cookiecutter.open_source_license] }}',
{%- endif %}
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    ext_modules=[],
    keywords='{{ cookiecutter.project_slug }}',
)
