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

__version__ = (0, 0, 0, "dev", 0)
from paste.script import templates
from datetime import datetime

TEMPLATE_VARIABLES = [
    templates.var("description", "Gives a one-line description of the package",
                  default="(TODO: Missing description)"),
    templates.var("keywords", "Defines keywords (tags) for the package",
                  default="(TODO: Missing keywords)"),
    templates.var("author", "Defines the author name of the package",
                  default="(TODO: Missing author name)"),
    templates.var("author_email", "Defines the author email of the package",
                  default="(TODO: Missing author email)"),
    templates.var("url", "Defines the URL of homepage for the package",
                  default="(TODO: Missing homepage URL)"),
    templates.var("year", "Defines the year which copyright is valid since",
                  default="(TODO: Missing copyright year)"),
    templates.var("zip_safe", "Either of True/False: "
                  "Indicates if the package can be distributed as a .zip file",
                  default=False),
    ]


class PackageTemplate(templates.Template):
    summary = "Template for creating a basic Python package"
    _template_dir = "templates"
    vars = TEMPLATE_VARIABLES
