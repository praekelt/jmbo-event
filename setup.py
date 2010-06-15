from setuptools import setup, find_packages

setup(
    name='panya-event',
    version='0.0.1',
    description='Panya event app.',
    long_description = open('README.rst', 'r').read(),
    author='Praekelt Foundation',
    author_email='dev@praekelt.com',
    license='BSD',
    url='http://github.com/praekelt/panya-event',
    packages = find_packages(),
    dependency_links = [
        'https://github.com/praekelt/panya/tarball/master#egg=panya',
    ],
    install_requires = [
        'panya',
    ],
    include_package_data=True,
    classifiers = [
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "Framework :: Panya",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
)
