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
# --------------------------------------------------------------------------------------
# SPAIRARU
# --------------------------------------------------------------------------------------
from .. import s

s_rdCnfx = s.utlx.rdCnfx



# --------------------------------------------------------------------------------------
# SCL
# --------------------------------------------------------------------------------------
from ..ovr import *

if TYPCHK :

	from .scl import Scl as Slf




# ######################################################################################
# CLASS : SOURCE FILE LICENSER - LOADING
# ######################################################################################
@nmlz
class Scl_Dflt :

	"""
	### SourceCodeLicenser Model - Loading
	"""


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# SCL CORE PRIVATE INSTANCE ATTRIBUTE
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	# current_approves
	__apvx : sArr[ sStr ]
	"""
	### Approves
	"""

	# current_configurations
	__cnfx : sDic
	"""
	### Configurations
	"""

	# current_ignores
	__ignx : sArr[ sStr ]
	"""
	### Ignores
	"""

	# current_templates
	__tplx : sDic[ Str , sArr[ sStr ] ]
	"""
	### Templates
	"""


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# PYTHON DEFAULT PUBLIC INSTANCE METHOD
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ======================================================================================
# __INITIATION__
# ======================================================================================
	def __init__(
		ctx : Slf
	) -> Nul :


		# current_approves
		ctx.__apvx = s.arr()

		# current_configurations
		ctx.__cnfx = s.dic()

		# current_ignores
		ctx.__ignx = s.arr()

		# current_templates
		ctx.__tplx = s.dic()



# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# SCL DEFAULT PUBLIC INSTANCE ATTRIBUTE
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ======================================================================================
# APPROVES
# ======================================================================================
	@attr
	def apvx(
		ctx : Slf
	) -> sArr :

		"""
		### Approves

		:return: List of approves.
		:rtype: sArr
		"""

		return ctx.__apvx



	# ********
	approves = apvx



# ======================================================================================
# CONFIGURATION
# ======================================================================================
	@attr
	def cnfx(
		ctx : Slf
	) -> sDic :

		"""
		### Configurations

		:return: Dictionary of configurations.
		:rtype: sDic
		"""

		return ctx.__cnfx



	# ********
	configurations = cnfx



# ======================================================================================
# IGNORES
# ======================================================================================
	@attr
	def ignx(
		ctx : Slf
	) -> sArr :

		"""
		### Ignores

		:return: List of ignores.
		:rtype: sArr
		"""

		return ctx.__ignx



	# ********
	ignores = ignx



# ======================================================================================
# TEMPLATES
# ======================================================================================
	@attr
	def tplx(
		ctx : Slf
	) -> sDic :

		"""
		### Templates

		:return: Dictionary of templates.
		:rtype: sDic
		"""

		return ctx.__tplx



	# ********
	templates = tplx



# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# SCL DEFAULT PUBLIC INSTANCE METHOD
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ======================================================================================
# FILTER OUT NON RECURSIVE PATTERN
# ======================================================================================
	def foNonRcPtn(
		ctx : Slf
		# patterns
		, ptnx__ : sArr | Arr
	) -> sArr[ sStr ] :

		"""
		Filter Out Non Recursive Pattern

		:return: List of recursive glob pattern.
		:rtype: sArr[ sStr ]
		"""

		# * only **/ is recursive.
		# [ recursive pattern ]
		_sRcPtn = s.rgx( r"^\*\*[\/|\\]" )


		return s.arr(
			* [
				ptn
					for ptn in ptnx__
						if _sRcPtn.mhx( ptn )
			]
		)



# ======================================================================================
# LOAD APPROVES
# ======================================================================================
	def ldApvx(
		ctx : Slf
		# defaults
		, dfltx__ : sArr | Arr
	) -> sArr[ sStr ] :

		"""
		### Load Approves

		:param dfltx__: Default approves; Defaults to empty array.
		:type dfltx__: sArr or Arr

		:return: This instant context.
		:rtype: Slf
		"""

		# [ approve_list ] 
		_apv_lst : sArr[ sStr ] = s.arr()


		# Get Files --------
		# [ approve_files ]
		_sApvFlx = (
			s.fs.gl(
				# folder_path
				f"{ ctx.sDstnFldr.pf }\\.mt\\**\\*.apv" 
			)
			+ s.fs.gl(
				# folder_path
				f"{ ctx.sDstnFldr.pf }\\.scl\\**\\*.apv" 
			)
		)


		# [ approve_file ]
		for sApvFl in _sApvFlx :

			_apv_lst += sApvFl.rd()


		# Post Processes --------
		# exclude comment and empty lane pattern.
		# [ exclude pattern ]
		_sXclPtn = s.rgx( 
			# pattern_text
			r"^(?!\#|\;|$).*" 
		)


		_apv_lst = _apv_lst.fltr(
			# handler 
			lambda i , v :
				tru
					if _sXclPtn.mhx( 
						# source_text
						v 
					)
					else fls
		)


		_apv_lst.ea(
			# handler 
			lambda i , v :
				_apv_lst.ed(
					# key
					i
					# value
					, v.rplc(
						# finders_and_replacements
						{ 
							"\r\n" : ""
							, "\n" : ""
							, "\r" : ""
						}
					)
				) 
		)


		if dfltx__ :

			_apv_lst = ( 
				s.arr( * dfltx__ ) 
				+ _apv_lst
			)


		_apv_lst.unq()


		return _apv_lst



	# ********
	loadApproves = ldApvx



# ======================================================================================
# LOAD CONFIGURATIONS
# ======================================================================================
	def ldCnfx(
		ctx : Slf
		# defaults
		, dfltx__ : sDic | Dic
	) -> sDic :

		"""
		### Load Configurations

		:param dfltx__: Default configuraiton; Defaults to empty ditionary.
		:type dfltx__: sDic or Dic

		:return: This instant context.
		:rtype: Slf
		"""

		# Get Files --------
		# [ configuration_dictionary ] 
		_cnf_dic = s.dic(
			** s_rdCnfx( 
				# folder_path
				f"{ ctx.sDstnFldr.pf }\\.mt" 
				# Configuration File Defult Options
				# default_section
				, dflt_sec = "scl"
			)
		)


		_cnf_dic += s.dic(
			** s_rdCnfx( 
				# folder_path
				f"{ ctx.sDstnFldr.pf }\\.scl" 
				# Configuration File Defult Options
				# default_section
				, dflt_sec = "scl"
			)
		)


		# Post Process --------
		if dfltx__ :

			_cnf_dic = (
				s.dic( ** dfltx__ ) 
				+ _cnf_dic
			)
		

		return _cnf_dic



	# ********
	loadConfigurations = ldCnfx



# ======================================================================================
# LOAD IGNORES
# ======================================================================================
	def ldIgnx(
		ctx : Slf
		# defaults
		, dfltx__ : sArr | Arr
	) -> sArr[ sStr ] :

		"""
		### Load Ignores

		:param dfltx__: Default ignores; Defaults to empty array.
		:type dfltx__: sArr or Arr

		:return: This instant context.
		:rtype: Slf
		"""

		# [ ignoree_list ] 
		_ign_lst : sArr[ sStr ] = s.arr()


		# Get Files --------
		# [ ignoree_files ] 
		_sIgnFlx = (
			s.fs.gl(
				# folder_path
				f"{ ctx.sDstnFldr.pf }\\.mt\\**\\*.ign" 
			)
			+ s.fs.gl(
				# folder_path
				f"{ ctx.sDstnFldr.pf }\\.scl\\**\\*.ign" 
			)
		)


		# [ ignoree_file ] 
		for sIgnFl in _sIgnFlx :

			_ign_lst += sIgnFl.rd()


		# Post Process --------
		# comment and empty lane pattern
		# [ exclude pattern ]
		_sXclPtn = s.rgx( r"^(?!\#|\;|$).*" )


		_ign_lst = _ign_lst.fltr(
			# handler 
			lambda i , v :
				tru
					if _sXclPtn.mhx( 
						# source_text
						v 
					)
					else fls
		)

		_ign_lst.ea(
			# handler 
			lambda i , v :
				_ign_lst.ed(
					# key
					i
					# value
					, v.rplc(
						# finders_and_replacements
						{ 
							"\r\n" : ""
							, "\n" : ""
							, "\r" : ""
						}
					)
				) 
		)


		if dfltx__ :

			_ign_lst = ( 
				s.arr( * dfltx__ ) 
				+ _ign_lst
			)


		_ign_lst.unq()


		return _ign_lst



	# ********
	loadIgnores = ldIgnx



# ======================================================================================
# LOAD TEMPLATES
# ======================================================================================
	def ldTplx(
		ctx : Slf
		# defaults
		, dfltx__ : sDic | Dic
	) -> sDic[ Str , sArr[ sStr ] ] :

		"""
		### Load Templates

		:param dfltx__: Default templates; Defaults to empty ditionary.
		:type dfltx__: sDic or Dic

		:return: This instant context.
		:rtype: Slf
		"""

		# [ template_dictionary ] 
		_tpl_dic = s.dic()


		# Get Files --------
		# [ template_files ] 
		_sTplFlx = (
			s.fs.gl(
				# folder_path
				f"{ ctx.sDstnFldr.pf }\\.mt\\**\\*.tpl" 
			)
			+ s.fs.gl(
				# folder_path
				f"{ ctx.sDstnFldr.pf }\\.scl\\**\\*.tpl" 
			)
		)


		# [ template_files ] 
		for sTplFl in _sTplFlx :

			_tpl_dic[ sTplFl.nm ] = sTplFl.rd()
	

		# Post Process --------
		if dfltx__ :

			_tpl_dic = (
				s.dic( ** dfltx__ ) 
				+ _tpl_dic
			)


		return _tpl_dic



	# ********
	loadTemplates = ldTplx



# ======================================================================================
# PREPAIR
# ======================================================================================
	def prpr(
		ctx : Slf
		# Default Options
		# approves
		, apvx : sArr | Arr = []
		# configuration
		, cnfx : sDic | Dic = {}
		# ignores
		, ignx : sArr | Arr = []
		# template
		, tplx : sDic | Dic = {}
	) -> Slf :

		"""
		### Prepare

		:param apvx: Default approves; Defaults to empty array.
		:type apvx: sArr or Arr
	
		:param cnfx: Default configuraiton; Defaults to empty ditionary.
		:type cnfx: sDic or Dic

		:param ignx: Default ignores; Defaults to empty array.
		:type ignx: sArr or Arr

		:param tplx: Default templates; Defaults to empty ditionary.
		:type tplx: sDic or Dic

		:return: This instant context.
		:rtype: Slf
		"""

		# [ current_approves ]
		ctx.__apvx = ctx.ldApvx(
			# defaults
			apvx
		)
	
		# [ current_configurations ]
		ctx.__cnfx = ctx.ldCnfx(
			# defaults
			cnfx
		)

		# [ current_ignores ]
		ctx.__ignx = ctx.ldIgnx(
			# defaults
			ignx
		)


		# [ current_templates ]
		ctx.__tplx = ctx.ldTplx(
			# defaults
			tplx
		)


		return ctx



	# ********
	prepare = prpr