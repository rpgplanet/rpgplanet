from setuptools import setup, find_packages
import rpghrac

setup(
    name = 'rpghrac',
    version = rpghrac.__versionstr__,
    description = 'RPG hrac',
    long_description = '\n'.join((
        'RPG hrac',
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

