# Project Name

_Here goes the project description_

## Getting started

#### Install

Assuming Python 3.6 is installed and `acc-pyqt` is active in your shell
([more info here](https://wikis.cern.ch/display/ACCPY/PyQt+distribution)), type:
```shell
pip install project-name
```
To make sure the installation was successful, type:
```bash
project-name
```
You should see the application starting up.

## Usage

To start the application, type:
```bash
project-name
```

_Detail how to use the application, how does it look like, where to find more documentation, etc..._

## Contribute
If you are a developer and want to contribute, or you're taking over this project:

#### Install
To get a ready-to-edit installation, do the following:

- Clone the repo:
```shell
git clone https://:@gitlab.cern.ch:8443/cern-username/project-name.git
```
- Setup the virtual environment:
```bash
cd project-name/
source /acc/local/share/python/acc-py-pyqt/setup.sh
acc-py venv venv
source venv/bin/activate
```
- Do a full install of the app
```bash
pip install -e .[all]
```

#### Setup
Before starting to work, type:
```shell
cd project-name/
git pull
source activate.sh
```

`source activate.sh` will activate the virtualenvs in the right order and set the
env vars required by Qt Designer to work with `accwidgets`.

#### Tests
You can run tests with:

```shell
python -m pytest --random-order
```
Note that the tests will automatically regenerate the views before running.

To see the coverage report, type:
```shell
python -m pytest --cov=project-name
```

If the tests hang, probably Qt is swallowing errors without exiting. Note that
this can happen for the same reasons on GitLab CI. To see the stacktrace,
re-run the tests as:

```shell
python -m pytest --vv --log-cli-level=DEBUG
```
