from setuptools import setup, find_packages

version = '1.0'

setup(
    name='emoneyge-py',
    version=version,
    description='Unofficial Python library for emoney.ge automation',
    author='Spartak Phalelashvili',
    author_email='phalelashvili@protonmail.com',
    license='MIT',
    packages=find_packages(),
    url='https://github.com/Phalelashvili/emoneyge-py',
    download_url='https://github.com/Phalelashvili/emoneyge-py/tarball/' + version,
    keywords=['emoney.ge', 'emoney', 'emoneyy', 'emoneygepy', 'emoneyge-py', 'emoney.ge automation', 'emoney automation'],
    install_requires=[
        "requests",
        "beautifulsoup4",
    ],
)