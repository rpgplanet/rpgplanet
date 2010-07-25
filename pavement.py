from paver.easy import *
from paver.setuputils import setup

from setuptools import find_packages

VERSION = '0.1'

setup(
    name = 'rpgplanet',
    version = VERSION,
    description = 'RPG planet',
    long_description = '\n'.join((
        'RPG planet',
        '',
    )),
    author = 'Almad',
    author_email='bugs@almad.net',
    license = 'BSD',

    packages = find_packages(
        exclude = ('docs', 'tests',)
    ),
    
    include_package_data = True,

    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    entry_points = {
        'setuptools.file_finders': ['dummy = setuptools_entry:dummylsfiles'],
        'setuptools.installation': ['eggsecutable = rpgplanet.manage'],
    },
    setup_requires = [
        'setuptools_dummy',
    ],
    install_requires = [
        'setuptools>=0.6b1',
    ],
)

@task
@needs('setuptools.command.sdist')
def sdist():
    """ Custom sdist """

@task
def deploy_production():
    """ Deploy to production server """
    sh('fab deploy')