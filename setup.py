from setuptools import setup, find_packages
import rpgplanet

setup(
    name = 'rpgplanet',
    version = rpgplanet.__versionstr__,
    description = 'RPG planet',
    long_description = '\n'.join((
        'RPG planet',
        '',
    )),
    author = 'Almad',
    author_email='bugs@almad.net',
    license = 'BSD',

    packages = find_packages(
        where = '.',
        exclude = ('docs', 'tests')
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
        'setuptools.installation': ['eggsecutable = rpghrac.manage'],
    },
    install_requires = [
        'setuptools>=0.6b1',
    ],
)

