from setuptools import setup
from jobs.version import VERSION

description='A library for analytic processing: including runs ad hoc queries against database to generate reports and ML results'
try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError, RuntimeError):
    long_description = description

setup(
    name='pyolap',
    packages=['pyolap'],
    version=VERSION,
    description=description,
    long_description=long_description,
    author='Michael Shi',
    url='https://github.com/shi1412/pyspark-olap-pipeline',
    keywords=['pyspark', 'fault-tolerant', 'olap', 'machine-learning', 'deep-learning'],
    install_requires=['pyspark==2.4.5'],
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.7',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'console_scripts': [
           
        ],
    },
)