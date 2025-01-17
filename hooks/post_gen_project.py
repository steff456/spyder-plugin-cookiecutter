"""
Does the following:

"""

from __future__ import print_function
import os
from subprocess import call

# Get the root project directory
PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)


def init_git():
    """Start git repository"""
    try:
        call(['git', 'init'])
    except Exception:
        print("git isn't avalaible, please install git and run:\n  $ git init")


# 1. Moves gitattributes to .gitattributes
# Having a .gitattributes with wrong syntax (because it has some jinja syntax)
# cause some annoying warnings

old_gitattributes = os.path.join(PROJECT_DIRECTORY, 'gitattributes')
new_gitattributes = os.path.join(PROJECT_DIRECTORY, '.gitattributes')

os.rename(old_gitattributes, new_gitattributes)


# 2. Create empty assets directory

assets_dir = os.path.join(PROJECT_DIRECTORY,
                          '{{ cookiecutter.project_name }}',
                          'assets')

os.mkdir(assets_dir)
