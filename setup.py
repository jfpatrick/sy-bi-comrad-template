"""
setup.py for be-bi-application-frame.

For reference see
https://packaging.python.org/guides/distributing-packages-using-setuptools/

"""
from pathlib import Path
from setuptools import setup, find_packages


HERE = Path(__file__).parent.absolute()
with (HERE / 'README.md').open('rt') as fh:
    LONG_DESCRIPTION = fh.read().strip()


REQUIREMENTS: dict = {
    'core': [
        "pyqt5",
        "pyqtgraph",
        "pyjapc",
        "papc",  # For the sandbox mode
        "comrad",  # Fot the CLogBox  - temporary, until CLogBox migrates to accwidgets!
        "accwidgets",  # For the plots
    ],
    'test': [
        "pytest",
        "pytest-qt",
        "pytest-cov",
        "pytest-random-order",
        "papc",  # For the sandbox mode
    ],
    'dev': [
    ],
    'doc': [
        'sphinx',
    ],
}

setup(
    name='be-bi-application-frame',
    version="0.0.1.dev1",

    author='Sara Zanzottera',
    author_email='sara.zanzottera@cern.ch',
    description='BE BI Application Frame',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url='',

    packages=find_packages(),
    python_requires='>=3.6, <4',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],

    install_requires=REQUIREMENTS['core'],
    extras_require={
        **REQUIREMENTS,
        # The 'dev' extra is the union of 'test' and 'doc', with an option
        # to have explicit development dependencies listed.
        'dev': [req
                for extra in ['dev', 'test', 'doc']
                for req in REQUIREMENTS.get(extra, [])],
        # The 'all' extra is the union of all requirements.
        'all': [req for reqs in REQUIREMENTS.values() for req in reqs],
    },
    entry_points={
        'console_scripts': [
            'empty-application-frame=be_bi_application_frame.main:main',
        ],
    },

)
