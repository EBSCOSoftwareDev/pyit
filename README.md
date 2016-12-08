# pyit
Python package for Ops scripts

# how to build

### One time only - beginner python env setup
```
#Doing this because the MAC OSX environment is too old to do proper development in
#Cannot use any of the SSL tools like twine
brew install python --with-brewed-openssl
```
#### Change Bash Profile to load from homebrew by default
```
vim ~/.bash_profile
```
```
# Set architecture flags
export ARCHFLAGS="-arch x86_64"
# Ensure user-installed binaries take precedence
export PATH=/usr/local/bin:$PATH
# Load .bashrc if it exists
test -f ~/.bashrc && source ~/.bashrc
```
```
source ~/.bash_profile
```

#### Install needed tools
```
pip install pip --upgrade
pip install setuptools --upgrade
pip install wheel virtualenv twine
```

### To Build
```
python setup.py sdist bdist_wheel
```

# How to do development in a virtual environment
```
cd "top/level/directory"
virtualenv venv
source venv/bin/activate
python setup.py develop #Does a symbolic link so code changes are immediately active
```

### When done
```
deactivate
rm -rf ./venv
```


# How to ship
## One time only for each package name - like pyit
```
#-r is the pypi destination based on the .pypirc file
twine register -r pypitest -u ***** -p ****** --config-file ./.pypirc dist/pyit-0.0.1-py2-none-any.whl
```

## To upload new version
```
#-r is the pypi destination based on the .pypirc file
twine upload -r pypitest -u **** -p **** --config-file ./.pypirc dist/pyit-0.0.2.tar.gz
```