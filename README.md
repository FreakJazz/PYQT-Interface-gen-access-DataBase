# PYQT-Interface-gen-access-DataBase


# Create execute file

pyinstaller --name="MyApplication" --hidden-import cmath  --windowed --onefile main.py


pyinstaller --hidden-import=pkg_resources.py2_warn --onefile example.py

pyinstaller --hidden-import=pkg_resources.py2_warn --onefile --noconsole example.py