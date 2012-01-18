=======================================================
 *pystraps*: A Python package skeleton generation tool
=======================================================

*pystraps* is a simple Paste create script which creates a Python
package skeleton aiming convenience for Python developers.

To bootsrap a Python package, you may use following instructions.

Setting up the virtual environment
==================================

The easiest way to manage your virtual environments is to use the
``virtualenvwrapper`` package available on Debian GNU/Linux based
distributions through the following command::

  $ sudo apt-get install virtualenvwrapper

Create a virtual environment (regardless of the present working
directory)::

  $ mkvirtualenv zama

Installing pystraps
===================

To install *pystraps*, issue the following command::

  $ pip install https://github.com/vst/pystraps/tarball/master

Bootstrapping your Python package
=================================

Assuming that your python package is called ``zingo``, issue the
following command and answer the questions. You may simply hit
``enter`` to leave them unanswered. Unanswered questions will be
marked as *TODO* in the package source files which you can alter at
anytime later::

  $ paster create -t pystraps zingo

This command will create the following layout::

  $ tree zingo
  zingo
  ├── _gitignore
  ├── LICENSE.txt
  ├── README.rst
  ├── setup.py
  ├── zingo
  │ ├── __init__.py
  │ └── __init__.pyc
  └── zingo.egg-info
      ├── dependency_links.txt
      ├── entry_points.txt
      ├── not-zip-safe
      ├── PKG-INFO
      ├── SOURCES.txt
      └── top_level.txt

  2 directories, 12 files

Note that, in case that you use *git*, the ``_gitignore`` will not
function unless it is moved to ``.gitignore``.::

  $ cd zingo
  $ mv _gitignore .gitignore
