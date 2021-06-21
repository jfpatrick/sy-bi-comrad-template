# SY-BI ComRAD Template

This is the repository for the SY-BI ComRAD Template code.

It can be used to bootstrap a ComRAD GUI project: the code provides a basic
structure that you only have to extend with your own interface and logic. 

## Getting started

#### Install
Assuming you have access to `bipy-gui-manager` ([see here](https://gitlab.cern.ch/bisw-python/bipy-gui-manager)),
type:
```
bipy-gui-manager new
```
This will start a wizard that will give you a customized copy of this template. Remember to specify that you want to create a ComRAD project, not a PyQt one.

#### Start
The application can already be started. To start it, type in the console the name of your project
(the one you gave to `bipy-gui-manager` while creating the project).

You should see the frame with a dummy application in the center, like this:

![](images/pyqt-template.gif)

Or a smaller window with an error. In the latter case, please report the error 
to the maintainers.

![](images/pyqt-error.png)

To obtain an empty template (without the demo application), type:
```
bipy-gui-manager new --no-demo
```

-------------------------------

## Contribute
If you are a developer and want to contribute, or you're taking over this project:

#### Setup
Do the following every time you begin working:
```
cd <your project's name>/
git pull
source activate.sh
```

Also, please keep this README up-to-date :)
