"""
setup.py for be-bi-application-frame.

If you are using this code as a bolierplate, remember to
update the information contained here to match your project!

For reference see
https://packaging.python.org/guides/distributing-packages-using-setuptools/

"""
from pathlib import Path
from setuptools import setup, find_packages


HERE = Path(__file__).parent.absolute()
with (HERE / 'README.md').open('rt') as fh:
    LONG_DESCRIPTION = fh.read().strip()

# List your dependencies here, according to their role.
# All necessary dependency *must* be listed under 'core'
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
    name='be-bi-application-frame',  # MODIFY: your application name
    version="0.0.1.dev1",  # MODIFY: the latest version of this package

    author='Sara Zanzottera',  # MODIFY: Your name
    author_email='sara.zanzottera@cern.ch',  # MODIFY: Your email
    description='BE BI Application Frame',  # MODIFY: Your project's short description
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
            # MODIFY: remove this line and add a pointer to the startup function of your app.
            # This means: 'empty-application-frame' launches "be_bi_application_frame/main.py:main()"
            'empty-application-frame=be_bi_application_frame.main:main',
        ],
    },
)
