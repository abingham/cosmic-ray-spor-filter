from pathlib import Path
from setuptools import setup, find_packages


setup(
    name='cosmic-ray-spor-filter',
    version="1.0.0",
    packages=find_packages('src'),

    author='Austin Bingham',
    author_email='austin.bingham@gmail.com',
    description='Spor-based filter for Cosmic Ray mutation testing',
    license='MIT',
    keywords='',
    url='http://github.com/abingham/cosmic-ray-spor-filter',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
    ],
    platforms='any',
    include_package_data=True,
    package_dir={'': 'src'},
    # package_data={'cosmic-ray-spor-filter': . . .},
    install_requires=[
        'cosmic-ray',
        'spor-python',
    ],
    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax, for
    # example: $ pip install -e .[dev,test]
    extras_require={
        'dev': ['bumpversion'],
        # 'doc': ['sphinx', 'cartouche'],
        'test': ['hypothesis', 'pytest'],
    },
    entry_points={
        'console_scripts': [
           'cosmic-ray-spor-filter = cosmic_ray_spor_filter.cli:main',
        ],
    },
    long_description=Path('README.rst').read_text(encoding='utf-8'),
)
