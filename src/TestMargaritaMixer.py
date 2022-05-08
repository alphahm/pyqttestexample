# Copyright 2011 Voom, Inc.
#
# This file is part of the Voom PyQt QTest Example.
# See http://www.voom.net/pyqt-qtest-example/ for documentation.
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
from PyQt5.QtWidgets import QApplication
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
import pytest

import MargaritaMixer

@pytest.fixture(scope="class", autouse=True)
def app():
    return QApplication(sys.argv)

@pytest.fixture(scope="class")
def form():
    return MargaritaMixer.MargaritaMixer()

class TestMargaritaMixer:
    """Test the margarita mixer GUI"""
    @pytest.fixture    
    def zero_form(self, form):
        """Set all ingredients to zero in preparation for setting just one
        to a nonzero value.
        """
        form.ui.tequilaScrollBar.setValue(0)
        form.ui.tripleSecSpinBox.setValue(0)
        form.ui.limeJuiceLineEdit.setText("0.0")
        form.ui.iceHorizontalSlider.setValue(0)
        return form

    def test_defaults(self, form):
        """Test the GUI in its default state"""
        assert form.ui.tequilaScrollBar.value() == 8
        assert form.ui.tripleSecSpinBox.value() == 4
        assert form.ui.limeJuiceLineEdit.text() == "12.0"
        assert form.ui.iceHorizontalSlider.value() == 12
        assert form.ui.speedButtonGroup.checkedButton().text() == "&Karate Chop"

        # Class is in the default state even without pressing OK
        assert form.jiggers == 36.0
        assert form.speedName == "&Karate Chop"

        # Push OK with the left mouse button
        okWidget = form.ui.buttonBox.button(form.ui.buttonBox.Ok)
        QTest.mouseClick(okWidget, Qt.LeftButton)
        assert form.jiggers == 36.0
        assert form.speedName == "&Karate Chop"

    def test_tequilaScrollBar(self, zero_form):
        """Test the tequila scroll bar"""
        form = zero_form

        # Test the maximum.  This one goes to 11.
        form.ui.tequilaScrollBar.setValue(12)
        assert form.ui.tequilaScrollBar.value() == 11

        # Test the minimum of zero.
        form.ui.tequilaScrollBar.setValue(-1)
        assert form.ui.tequilaScrollBar.value() == 0

        form.ui.tequilaScrollBar.setValue(5)

        # Push OK with the left mouse button
        okWidget = form.ui.buttonBox.button(form.ui.buttonBox.Ok)
        QTest.mouseClick(okWidget, Qt.LeftButton)
        assert form.jiggers == 5

    def test_tripleSecSpinBox(self, zero_form):
        """Test the triple sec spin box.
        Testing the minimum and maximum is left as an exercise for the reader.
        """
        form = zero_form
        form.ui.tripleSecSpinBox.setValue(2)

        # Push OK with the left mouse button
        okWidget = form.ui.buttonBox.button(form.ui.buttonBox.Ok)
        QTest.mouseClick(okWidget, Qt.LeftButton)
        assert form.jiggers == 2

    def test_limeJuiceLineEdit(self, zero_form):
        """Test the lime juice line edit.
        Testing the minimum and maximum is left as an exercise for the reader.
        """
        form = zero_form
        # Clear and then type "3.5" into the lineEdit widget
        form.ui.limeJuiceLineEdit.clear()
        QTest.keyClicks(form.ui.limeJuiceLineEdit, "3.5")

        # Push OK with the left mouse button
        okWidget = form.ui.buttonBox.button(form.ui.buttonBox.Ok)
        QTest.mouseClick(okWidget, Qt.LeftButton)
        assert form.jiggers == 3.5

    def test_iceHorizontalSlider(self, zero_form):
        """Test the ice slider.
        Testing the minimum and maximum is left as an exercise for the reader.
        """
        form = zero_form
        form.ui.iceHorizontalSlider.setValue(4)

        # Push OK with the left mouse button
        okWidget = form.ui.buttonBox.button(form.ui.buttonBox.Ok)
        QTest.mouseClick(okWidget, Qt.LeftButton)
        assert form.jiggers == 4

    def test_liters(self, zero_form):
        """Test the jiggers-to-liters conversion."""
        form = zero_form
        assert form.liters == 0.0
        form.ui.iceHorizontalSlider.setValue(1)
        assert form.liters == 0.0444
        form.ui.iceHorizontalSlider.setValue(2)
        assert form.liters == 0.0444 * 2

    def test_blenderSpeedButtons(self, form):
        """Test the blender speed buttons"""
        form.ui.speedButton1.click()
        assert form.speedName == "&Mix"
        form.ui.speedButton2.click()
        assert form.speedName == "&Whip"
        form.ui.speedButton3.click()
        assert form.speedName == "&Puree"
        form.ui.speedButton4.click()
        assert form.speedName == "&Chop"
        form.ui.speedButton5.click()
        assert form.speedName == "&Karate Chop"
        form.ui.speedButton6.click()
        assert form.speedName == "&Beat"
        form.ui.speedButton7.click()
        assert form.speedName == "&Smash"
        form.ui.speedButton8.click()
        assert form.speedName == "&Liquefy"
        form.ui.speedButton9.click()
        assert form.speedName == "&Vaporize"


if __name__ == "__main__":
    pytest.main(sys.argv)
