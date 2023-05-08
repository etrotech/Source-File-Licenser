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
from . import _defx as __defx




# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# EXPORT
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Debug Options  --------
# show time
SCL_DBG_OPN_ST : bool = __defx.get( "SCL_DBG_OPN_ST" , True )
"""
### Debug Option : Show Time
"""


# Condition  --------
# debug state
SCL_DBG_STT : bool = __defx.get( "SCL_DBG_STT" , True )
"""
### Debug State
"""