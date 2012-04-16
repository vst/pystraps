# Copyright (C) 2012 Vehbi Sinan Tunalioglu
#
# This file is part of pystraps.
#
# pystraps is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pystraps is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pystraps. If not, see <http://www.gnu.org/licenses/>.

import versiontools_support
from setuptools import setup, find_packages
import os
import sys

PWD = os.path.abspath(os.path.dirname(__file__))
LONG_DESCRIPTION = open(os.path.join(PWD, "README.rst")).read()

setup(name="pystraps",
      version=":versiontools:pystraps",
      description="Convenient bootstrapping of Python projects",
      long_description=LONG_DESCRIPTION,
      classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Paste",
        ],
      keywords="python library setup bootstrap project",
      author="Vehbi Sinan Tunalioglu",
      author_email="vst@vsthost.com",
      url="https://github.com/vst/pystraps",
      license="License :: OSI Approved :: GNU General Public License (GPL)",
      packages=find_packages(exclude=["ez_setup", "examples", "tests"]),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
        "versiontools",
        "paste",
        "pastescript"
        ],
      entry_points="""
        [paste.paster_create_template]
        pystraps = pystraps:PackageTemplate
      """,
      paster_plugins=["pystraps"],
      )
