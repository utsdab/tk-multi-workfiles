# Copyright (c) 2014 Shotgun Software Inc.
# 
# CONFIDENTIAL AND PROPRIETARY
# 
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit 
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your 
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights 
# not expressly granted therein are reserved by Shotgun Software Inc.

"""

"""

import sgtk
from sgtk.platform.qt import QtCore, QtGui

from .ui.task_widget import Ui_TaskWidget

class TaskWidget(QtGui.QWidget):
    """
    """
    
    def __init__(self, parent=None):
        """
        Construction
        """
        QtGui.QWidget.__init__(self, parent)
        
        # set up the UI
        self._ui = Ui_TaskWidget()
        self._ui.setupUi(self)

        self._background_styles = {}
        self._background_styles["normal"] = {
            "background-color": "rgb(0, 0, 0, 0)",
            "border-bottom-style": "solid",
            "border-bottom-width": "1px",
            "border-bottom-color": "rgb(64,64,64)"
        }
        self._background_styles["selected"] = self._background_styles["normal"].copy() 
        self._background_styles["selected"]["background-color"] = "rgb(0, 174, 237)"

        self._desc_styles = {}
        self._desc_styles["normal"] = {}
        self._desc_styles["selected"] = self._desc_styles["normal"].copy()
        self._desc_styles["selected"]["color"] = "rgb(255, 255, 255)"

    def set_selected(self, selected=True):
        
        bg_style = self._build_style_string("background", self._background_styles["selected" if selected else "normal"])
        self._ui.background.setStyleSheet(bg_style)
        
        desc_style = self._build_style_string("description_label", self._desc_styles["selected" if selected else "normal"])
        self._ui.description_label.setStyleSheet(desc_style)
        
        self._ui.jump_btn.setVisible(selected)

    def _build_style_string(self, ui_name, style):
        """
        """
        return "#%s {%s}" % (ui_name, ";".join(["%s: %s" % (key, value) for key, value in style.iteritems()]))            