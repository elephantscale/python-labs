# win32-com.py
# `pip install pywin32`

import win32com.client as win32
excel = win32.gencache.EnsureDispatch('Excel.Application')

excel.Visible = True
_ = input("Press ENTER to quit:")

excel.Application.Quit()
