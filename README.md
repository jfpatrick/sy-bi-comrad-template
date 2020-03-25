# BE-BI Application Frame

This is the repository for the BE-BI Base Application Frame code.

It can be used to bootstrap a PyQt GUI project and it to wrap existing applications,
to provide them with the standard frame of BE-BI Expert Applications.


## Getting started

#### Install
Assuming Python 3.6 is installed and `acc-pyqt` is active in your shell
([more info here](https://wikis.cern.ch/display/ACCPY/PyQt+distribution)), type:
```
git clone https://:@gitlab.cern.ch:8443/szanzott/be-bi-application-frame.git
cd be-bi-application-frame/
source /acc/local/share/python/acc-py-pyqt/setup.sh
acc-py venv venv
source venv/bin/activate
pip install -e .[all]
```

## Usage
To start the GUI as a standalone application, type

```
empty-application-frame
```

You should see the frame with a dummy application in the center, like this:

![](images/empty-frame.png)

Or a smaller window with an error. In the latter case, please report the error to the maintainers.


## Contribute
If you are a developer and want to contribute, or you're taking over this project:

#### Setup
Do the following every time you begin working:
```
cd be-bi-application-frame/
git pull
source activate.sh
```

#### Test
The unit tests are run with `pytest`, which is setup by default (thanks to `acc-py`) and can be run by
```
python -m pytest
```
from the root project directory.

To see the coverage report, type:
```
python -m pytest --cov=be-bi-application-frame
```

If the tests hang, probably Qt is swallowing errors without exiting. Note that
this can happen for the same reasons on GitLab CI. To see the stacktrace,
re-run the tests as:
```
python -m pytest --vv --log-cli-level=DEBUG
```

