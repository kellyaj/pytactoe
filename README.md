Python Tic Tac Toe
========
A typical Tic Tac Toe game written in [Python](http://www.python.org/).

Dependencies
========
The game itself only depends on [Python 2.x](http://www.python.org/).

The tests rely on [pytest](http://pytest.org/latest/) and [mock](http://www.voidspace.org.uk/python/mock/).

Installation
========

### Recommended Installation:

I highly recommend installing Python using [Homebrew](http://brew.sh/):

```
brew install python
```

Note that a fresh Homebrew installation of Python may take several minutes. Homebrew will also install pip, a popular Python package manager.

The tests are run using pytest. After the Homebrew installation completes, install pytest using:

```
pip install -U pytest
```

Finally, you'll need to install mock:

```
pip install -U mock
```

That's it! You're ready to go.

### Unrecommended Installation:
You likely can use the version of Python that comes pre-installed with your system (not recommended) or [install Python manually](http://www.python.org/download/) (also not recommended)

You will need a Python package manager to install pytest. I recommend [installing pip](http://www.pip-installer.org/en/latest/installing.html).

```
pip install -U pytest
```

Followed by:

```
pip install -U mock
```

If you're using pip, you're done!

If you're not using pip, you'll have to use [easy_install](http://pythonhosted.org/distribute/easy_install.html). This will require an additional step.

```
easy_install -U pytest
```

Followed by:

```
easy_install -U mock
```
If you're using easy_install, you're done!

Playing
========
The game is currently configured to be run in the terminal. To play, clone the repo and then cd into the newly created directory. After that, type:

```
python play.py
```

Testing
========
Assuming everything was installed properly, you can simply use the following command to run the tests:

```
py.test -v
```
