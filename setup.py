import os
import re
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def find_version(fname):
    '''Attempts to find the version number in the file names fname.
    Raises RuntimeError if not found.
    '''
    version = ''
    with open(fname, 'r') as fp:
        reg = re.compile(r'__version__ = [\'"]([^\'"]*)[\'"]')
        for line in fp:
            m = reg.match(line)
            if m:
                version = m.group(1)
                break
    if not version:
        raise RuntimeError('Cannot find version information')
    return version


__version__ = find_version(os.path.join("alert", "__init__.py"))

setup(
    name='osx_alert',
    version=__version__,
    long_description=read('README.md'),
    packages=['alert'],
    url='http://github.com/yoophi/osx_alert',
    license='MIT License',
    author='Pyunghyuk Yoo',
    author_email='yoophi@gmail.com',
    description='alert script for osx comandline',
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            "alert = alert:main"
        ]
    },
    install_requires=[
        'docopt==0.6.2',
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OSX',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
