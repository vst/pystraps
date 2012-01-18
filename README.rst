=======================================================
 *pystraps*: A Python package skeleton generation tool
=======================================================

*pystraps* is a simple Paste create script which creates a Python
package skeleton aiming convenience for Python developers.

To bootstrap a Python package, you may use following instructions.

Setting up the virtual environment
==================================

The easiest way to manage your virtual environments is to use the
``virtualenvwrapper`` package available on Debian GNU/Linux based
distributions through the following command::

  $ sudo apt-get install virtualenvwrapper

Create a virtual environment (regardless of the present working
directory)::

  $ mkvirtualenv --no-site-packages zama

Installing pystraps
===================

To install *pystraps*, issue the following command::

  $ pip install https://github.com/vst/pystraps/tarball/master

Bootstrapping your Python package
=================================

Assuming that your Python package is called ``zingo``, issue the
following command and answer the questions. You may simply hit
``enter`` to leave them unanswered. Unanswered questions will be
marked as *TODO* in package source files which you can alter at
anytime later::

  $ paster create -t pystraps zingo

This command will create the following layout::

  $ tree zingo
  zingo
  ├── docs
  │   ├── make.bat
  │   ├── Makefile
  │   └── source
  │       ├── conf.py
  │       ├── index.rst
  │       ├── _static
  │       │   └── README
  │       └── _templates
  │           └── README
  ├── _gitignore
  ├── LICENSE.txt
  ├── README.rst
  ├── setup.py
  ├── zingo
  │   ├── __init__.py
  │   ├── __init__.pyc
  │   ├── scripts
  │   │   ├── __init__.py
  │   │   └── packageinfo.py
  │   └── tests
  │       ├── __init__.py
  │       └── packageinfo.py
  └── zingo.egg-info
      ├── dependency_links.txt
      ├── entry_points.txt
      ├── not-zip-safe
      ├── PKG-INFO
      ├── requires.txt
      ├── SOURCES.txt
      └── top_level.txt

8 directories, 23 files

Note that, in case that you use *git*, the ``zingo/_gitignore`` will
not function unless the file is renamed to ``.gitignore``::

  $ mv zingo/_gitignore zingo/.gitignore

Installing your package
=======================

For development purposes you can install your package with::

  $ pip install -e ./zingo

Additionally, ``./zingo/development.pip`` includes some Python
development tools such as ``Sphinx``, ``pep8`` and ``coverage``. To
install them::

  $ pip install -r ./zingo/development.pip

Packaging amd Distributing
==========================

To distribute your package, you can issue the command:

  $ python setup.py sdist

Running tests
=============

There is a sample test case generated for you. To run it::

  $ python -m "zingo.tests.packageinfo"

Running the sample script
=========================

Apart from the test case, there is also a sample script which is
installed while installing the package: ``zingo-packageinfo``. This
script provides a short version (as plain text) and a long version
(both as plain text and HTML) of ``zingo``\'s package information::

  $ zingo-packageinfo shorter
  $ zingo-packageinfo longer -f txt
  $ zingo-packageinfo longer -f html

Editing and generating documentation
====================================

To edit and generate the documentation, simply go to the docs folder::

  $ cd zingo/docs

The documentation is Sphinx-ready. To generate the HTML documentation::

  $ make html
