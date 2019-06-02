import os
from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-minio-backend',
    version='0.0.2',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License | Copyright (c) 2019 Kristof Daja',
    description='The django-minio-backend provides a wrapper around the MinIO Python Library.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/theriverman/django-minio-backend',
    author='Kristof Daja (theriverman)',
    author_email='kristof@daja.hu',
    install_requires=[
        'Django>=2.0.1',
        'minio>=4.0.9',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Content Management System',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ],
)
