# Project Name

_Here goes the project description_

## Getting started

### Documentation

You can find the API description and general documentation [at this link](https://acc-py.web.cern.ch/gitlab/gitlab-group/sy-bi-pyqt-template).

### Launch

You can launch this application in several ways.

#### [BI Python GUI Manager](https://gitlab.cern.ch/bisw-python/bipy-gui-manager)

If the app has been deployed to the operational folder, you can launch it with:

```bash
/user/bdisoft/operational/python/gui/bipy-gui-manager run -o sy-bi-pyqt-template
```

If the app has been deployed to the development folder, you can launch it with:

```bash
/user/bdisoft/operational/python/gui/bipy-gui-manager run -d sy-bi-pyqt-template
```

#### [BI Launcher](https://gitlab.cern.ch/bisw-java-fwk/bi-launcher)

If it has been registered in the BI Launcher, you can launch it in this way:

```bash
/user/bdisoft/operational/tools/bi-launcher/launcher <app name in the Launcher>
```

Ask the developers for the application name if you don't know it,
or execute the command above without the application name and look for it in the
window that opens.

#### [Acc-Py](https://wikis.cern.ch/display/ACCPY/Getting+started+with+Acc-Py)

If the app has been deployed to the operational folder, you can launch it with:

```bash
source /acc/local/share/python/acc-py/base/pro/setup.sh
acc-py app run --deploy-base= /user/bdisoft/operational/python/gui/deployments sy-bi-pyqt-template
```

If the app has been deployed to the development folder, you can launch it with:

```bash
source /acc/local/share/python/acc-py/base/pro/setup.sh
acc-py app run --deploy-base= /user/bdisoft/development/python/gui/deployments sy-bi-pyqt-template
```

## Usage

_Detail how to use the application, how does it look like, where to find more documentation, etc..._


## Contribute
If you are a developer and want to contribute, or you're taking over this project:

#### Install
To get a ready-to-edit installation, do the following:

- Clone the repo:
```bash
git clone https://:@gitlab.cern.ch:8443/cern-username/project-name.git
```

- Setup the virtual environment:

```bash
cd project-name/
source /acc/local/share/python/acc-py/base/2020.11/setup.sh
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

`source activate.sh` will activate the virtualenvs in the right order, and alias `bipy-gui-manager` and `pycharm`.

#### Tests
You can run tests with:

```shell
python -m pytest --random-order
```

Note that the tests will automatically regenerate the views before running.

To see the coverage report, type:

```shell
python -m pytest --cov=project_name
```

If the tests hang, probably Qt is swallowing errors without exiting. Note that
this can happen for the same reasons on GitLab CI. To see the stacktrace,
re-run the tests as:

```shell
python -m pytest --vv --log-cli-level=DEBUG
```

## Support

To get help, please contact the project author at this email address: author@cern.ch
