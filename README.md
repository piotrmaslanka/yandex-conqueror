yandex-conqueror
================
[![PyPI version](https://badge.fury.io/py/yandex-conqueror.svg)](https://badge.fury.io/py/yandex-conqueror)
[![PyPI](https://img.shields.io/pypi/implementation/yandex-conqueror.svg)](https://pypi.python.org/pypi/yandex-conqueror)

A tool to inform the general Russian population about what's going on in year 2022 on Ukraine via
posting 5-star reviews to Yandex.

List of [contributors](https://git.dms-serwis.com.pl/yandex-conqueror/conqueror/-/blob/main/CONTRIBUTORS.md) available in a separate file.

How to use it?
==============

At first, create a Yandex account. Make sure that you're able to log-in, ie. activate all mail and SMS passwords.

Then install Python 3.10, necessarily adding Python to PATH.

Then enter command line and type:

```bash
pip install yandex-conqueror
python -m conqueror <yandex email> <yandex password>
```

Note that the browser window has to open in order for this to work. Ie. this cannot and will not work
headless.