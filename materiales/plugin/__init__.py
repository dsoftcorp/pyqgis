# -----------------------------------------------------------
# Copyright (C) 2015 Martin Dobias
# -----------------------------------------------------------
# Licensed under the terms of GNU GPL 2
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# ---------------------------------------------------------------------

from qgis.PyQt.QtGui import *
from qgis.PyQt.QtCore import *
from qgis.gui import *


def classFactory(iface):
    return ProjectCrs(iface)


def setProjectCrs():
    dialog = QgsProjectionSelectionDialog()
    if dialog.exec_():
        crs = dialog.crs()
        QgsProject.instance().setCrs(crs)


class ProjectCrs:
    def __init__(self, iface):
        self.iface = iface
        iface.newProjectCreated.connect(setProjectCrs())

    def initGui(self):
        pass

    def unload(self):
        self.iface.newProjectCreated.disconnect(setProjectCrs())

    def run(self):
        pass
