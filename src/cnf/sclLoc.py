# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# SPDX-FileCopyrightText: 2022~2023 Micah T.<micah.tominaga@gmail.com>, and other contributors
# SPDX-License-Identifier: GPL-3.0-or-later
# SourceCodeLicenser-Python sr1.0.0
# - its a source file header management utility base on Spairaru framework. 
# - developed for internal use originally, free for public use.
# - collaboration or service request, contact me.
# - a coffee donation will help to keep the package updated :)
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# EXPORT
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# NAMESPACE
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# root namespace
SCL_ROOT_NSPC : str = (
    "."
    	.join(
   			__name__ 
				.split(".")
				# xxx.cnf.sLoc
				# ↑↑↑
				[ :-2 ]
		)
)
"""
### Spairaru Root Namespace
"""



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# DIRECTORY
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# root directory
SCL_ROOT_DIR : str = (
	"\\"
		.join( 
			__file__
				.split( "\\" )
				# xxx\\cnf\\sLoc
				# ↑↑↑
				[ :-2 ] 
		)
)
"""
### Spairaru Root Directory
"""

# configuration directory
SCL_CNF_DIR : str = f"{SCL_ROOT_DIR}\\.sprr"
"""
### Spairaru Configuration Directory
"""""