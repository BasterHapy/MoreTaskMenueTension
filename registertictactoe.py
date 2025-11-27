# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause
from __future__ import annotations
from tictactoe import TicTacToe  
from tictactoeplugin import TicTacToePlugin
from PySide6.QtDesigner import QPyDesignerCustomWidgetCollection

if __name__ == '__main__':
    QPyDesignerCustomWidgetCollection.addCustomWidget(TicTacToePlugin())
