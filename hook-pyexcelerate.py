"""
PyInstaller hook for PyExcelerate
(C) 2014 Kevin Zhang
"""

import os

from pyexcelerate.Writer import _TEMPLATE_PATH
datas = [
	(os.path.join(_TEMPLATE_PATH, '*'), 'pyexcelerate/templates')
]
