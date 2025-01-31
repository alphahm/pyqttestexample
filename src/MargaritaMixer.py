# Copyright 2011 Voom, Inc.
#
# PyQt QTest Example is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyQt QTest Example is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PyQt QTest Example.  If not, see <http://www.gnu.org/licenses/>.

import sys
from PyQt5.QtWidgets import QWidget, QApplication

from Ui_MargaritaMixer import Ui_MargaritaMixer


class MargaritaMixer(QWidget):
    def __init__(self):
        super(MargaritaMixer, self).__init__()

        self.ui = Ui_MargaritaMixer()
        self.ui.setupUi(self)

    @property
    def jiggers(self):
        """Return the total volume of the margaritas in units of jiggers.
        One jigger is 0.0444 liters.
        """
        jiggersTequila = self.ui.tequilaScrollBar.value()
        jiggersTripleSec = self.ui.tripleSecSpinBox.value()
        jiggersLimeJuice = float(self.ui.limeJuiceLineEdit.text())
        jiggersIce = self.ui.iceHorizontalSlider.value()
        return jiggersTequila + jiggersTripleSec + jiggersLimeJuice + jiggersIce

    @property
    def liters(self):
        """Return the total volume of the margaritas in liters."""
        return 0.0444 * self.jiggers

    @property
    def speedName(self):
        speedButton = self.ui.speedButtonGroup.checkedButton()
        if speedButton is None:
            return None
        return speedButton.text()

    def accept(self):
        """Execute the command in response to the OK button."""
        print(f"The volume of drinks is {self.liters} liters ({self.jiggers} jiggers).")
        print(f'The blender is running at speed "{self.speedName}"')
        self.close()

    def reject(self):
        """Cancel."""
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = MargaritaMixer()
    myapp.show()
    sys.exit(app.exec_())
