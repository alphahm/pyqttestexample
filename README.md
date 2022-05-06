# MargaritaMixer PyQt QtTest Example Code

**MargaritaMixer** demonstrates how to unit test GUIs created with [PyQt](https://doc.qt.io/qtforpython/), the
Python binding of the popular Qt UI and application framework using
[Qt Test](https://doc.qt.io/qt-5/qttest-index.html).

**MargaritaMixer** is tested with PyQt5 and Python 3.9. To download and run the unit test:

```
git clone https://jmcgeheeiv@bitbucket.org/jmcgeheeiv/pyqttestexample
```

```
python3 -m virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

```
cd pyqttestexample/src
python MargaritaMixerTest.py
```

If you change the `pyqttestexample/src/MargaritaMixer.ui` user interface definition (such as with Qt Designer), you will need to recreate `Ui_MargaritaMixer.py` before running **MargaritaMixer** again::

```
pyuic5 -o src/Ui_MargaritaMixer.py src/MargaritaMixer.ui
```

## Credits
* Original author: John McGehee and copyright: [Voom, Inc.](http://www.voom.net)
* Companion article of the original repository: [Test PyQt GUIs with QTest and unittest](http://johnnado.com/pyqt-qtest-example), offline at the time of writing.