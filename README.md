Python Tic Tac Toe
========
A typical Tic Tac Toe game written in [Python](http://www.python.org/).

Dependencies
========
[Python 2.x](http://www.python.org/).

Installation
========
If you're using OSX, Python 2.x is likely already installed. To verify that your system has Python installed, use:

```
python --version
```

If you do not have Python installed, you can install it using [Homebrew](http://brew.sh/):

```
brew install python
```

One advantage is that Homebrew will also install [pip](https://pypi.python.org/pypi/pip), a popular Python package manager. Note that a fresh brew install of python will take several minutes and is entirely optional. You will be able to play the game and run the tests as long as you have Python installed.

Playing
========
The game is currently configured to be run in the terminal. To play, clone the repo and then cd into the newly created directory. After that, type:

```
python play.py
```

Testing
========
You can run the tests using pytest. It's easy to [install py.test](http://pytest.org/latest/getting-started.html) yourself. I recommend using [pip](https://pypi.python.org/pypi/pip), which Homebrew will automatically install. Assuming you have pip, use the following command:

```
pip install -U pytest
```

If you've installed py.test yourself, you can simply use the following command to run the tests:

```
py.test
```

The tests are written using [PyUnit](http://docs.python.org/2/library/unittest.html).
