# PYQT-Interface-gen-access-DataBase

pyuic5 pichincha.ui -o pichincha.py

# Create execute file

pyinstaller --name="MyApplication" --hidden-import cmath  --windowed --onefile main.py


pyinstaller --name="Peritaje" --hidden-import=pkg_resources.py2_warn --onefile main.py

pyinstaller --name="Peritaje" --hidden-import=pkg_resources.py2_warn --onefile --noconsole main.py
