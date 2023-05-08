# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# SPDX-FileCopyrightText: 2022~2023 Micah T.<micah.tominaga@gmail.com>, and other contributors
# SPDX-License-Identifier: GPL-3.0-or-later
# SourceCodeLicenser-Python sr1.0.0
# - its a source file header management utility base on Spairaru framework. 
# - developed for internal use originally, free for public use.
# - collaboration or service request, contact me.
# - a coffee donation will help to keep the package updated :)
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# IMPORT
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
from .. import s

s_rdCnfx = s.utlx.rdCnfx



# --------------------------------------------------------------------------------------
# FRAME CALIBER
# --------------------------------------------------------------------------------------
from .sclLoc import SCL_CNF_DIR , SCL_ROOT_DIR , SCL_ROOT_NSPC




# ######################################################################################
# USER DEFINES
# ######################################################################################
_defx = s_rdCnfx( 
	# fodler path
	SCL_CNF_DIR
	# Configuration File Options
	, dflt_sec = "scl"
	# Module File Options
	# rectifiable root
	, root = SCL_ROOT_DIR
	# resolver location
	, rslvr = SCL_ROOT_NSPC
	# scope
	, scp = "rltv"
)