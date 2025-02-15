import cx_Freeze
import sys
import os
base = None
if sys.platform == 'win64':
    base = "wind64GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\MAJID HUSSAIN\AppData\Local\Programs\Python\Python311\tcl\tcl8.6"    
os.environ['TK_LIBRARY'] = r"C:\Users\MAJID HUSSAIN\AppData\Local\Programs\Python\Python311\tcl\tk8.6"

excecutables = [cx_Freeze.Executable("login.py",base=base,icon='profile.ico')]

cx_Freeze.setup(
    name = "IMS",
    options = {'build_exe':{"packages":["tkinter","os","sys"],"include_files":['tcl86t.dll','tk86t.dll','profile.ico',"employee.py","product.py","dashboard.py","category.py","product.py","sales.py","supplier.py","billing.py"]}},
    version = "1.00",
    description = "Municipal Committee MIS system | Developed by Majid Hussain Meerani ",
    excecutables =excecutables
)