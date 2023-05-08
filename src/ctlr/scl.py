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
# PYTHON
# --------------------------------------------------------------------------------------
from datetime import datetime



# --------------------------------------------------------------------------------------
# SPAIRARU
# --------------------------------------------------------------------------------------
from .. import s

FltrblCtlrAbs = s.absx.FltrblCtlr
FwkCtlrAbs = s.absx.FwkCtlr



# --------------------------------------------------------------------------------------
# SOURCE FILE LICENSER
# --------------------------------------------------------------------------------------
from ..cnf.sclDbg import SCL_DBG_STT
from ..cnf.sclLoc import SCL_ROOT_DIR
from ..ovr import *
from ..mdl.scl import Scl as SclMdl




# ######################################################################################
# CLASS : SOURCE FILE LICENSER CONTROLLER
# ######################################################################################
@nmlz
class Scl(
	# spairaru filterable controller abstraction
	FltrblCtlrAbs
	# framework controller abstraction
	, FwkCtlrAbs[ 
		# famework model
		SclMdl 
	]
) :

	"""
	### SourceCodeLicenser Controller
	"""


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# SPAIRARU CORE PUBLIC STATIC PROPERTY
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	# label
	_cpnt_lbl_ = SclMdl._cpnt_lbl_

	# title
	_cpnt_ttl_ = SclMdl._cpnt_ttl_

	# component name
	_cpnt_nm_ = SclMdl._cpnt_nm_



# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# FRAMEWORK PUBLIC STATIC PROPERTY
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	# famework model
	_fwk_mdl_ = SclMdl



# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# SPAIRARU DEFAULT PUBLIC STATIC METHOD
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ======================================================================================
# __CONSTRUCTOR__
# ======================================================================================
	@clsmtd
	def __cstr__( 
		cst : Cls[ Slf ] 
	) -> Nul :


		# FILTERABLE
		FltrblCtlrAbs.__cstr__.__func__( cst )



# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# SCL CORE PUBLIC STATIC METHOD
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ======================================================================================
# LICENSE
# ======================================================================================
	@clsmtd
	def lic(
		cst : Cls[ Slf ]
		# source_directory
		, src__ : sFldr | sStr | Str
		# Default Options
		# approves
		, apvx : sArr | Arr = []
		# configuration
		, cnfx : sDic | Dic = {}
		# ignores
		, ignx : sArr | Arr = []
		# template
		, tplx : sDic | Dic = {}
		# I\O Options
		# ignore_symbolic_link
		, ign_lnk : Bool = fls
		# keep_symbolic_link
		, kp_lnk : Bool = tru
		# overwrite
		, ovw : Bool = fls
		# Locational Options
		# distribution_directory
		, dist : sFldr | sStr | Str = ""
		# Search Options
		# follow_link
		, flw_lnk : Bool = fls
		# recursive
		, rc : Bool = tru
		# Alternative Options
		# cleanup_default_configurations
		, cu_dflt_cnfx : Bool = fls
		# cleanup_.gitignore_list
		, cu_git_lst : Bool = fls
		# make_license_text_file
		, mk_lic_txt_fl : Bool = fls 
	) -> Cls[ Slf ] :	
		
		"""
		### License

		:param src__: Source directory.
		:type src__: sFldr or sStr or Str

		:param apvx__: Default approves; Defaults to empty array.
		:type apvx__: sArr or Arr

		:param cnfx: Default configuraiton; Defaults to empty ditionary.
		:type cnfx: sDic or Dic

		:param ignx: Default ignores; Defaults to empty array.
		:type ignx: sArr or Arr

		:param tplx__: Default templates; Defaults to empty ditionary.
		:type tplx__: sDic or Dic

		:param ign_lnk: Ignore symbolic links; Defaults to false.
		:type ign_lnk: Bool

		:param kp_lnk: Keep symbolic links; Defaults to true.
		:type kp_lnk: Bool

		:param ovw: Overwrite if template alreasy present; Defaults to flase.
		:type ovw: Bool

		:param dist: Distination directory; Defautls to empty string.
		:type dist: sStr or Str

		:param flw_lnk: Follow symbolic link, licence original file; Defaults to false.
		:type flw_lnk: Bool

		:param rc: Recursive, apply licence to all files in all subfolders; Defaults to flase.
		:type rc: Bool

		:param cu_dflt_cnfx: Cleanup default configuration folders after licesing, preferred otpion when distribution folder is given; Defailts to false.
		:type cu_dflt_cnfx: Bool

		:param cu_git_lst: Cleanup any folders and files listing in .gitignore, preferred otpion when distribution folder is given; Defailts to false.
		:type cu_git_lst: Bool

		:param mk_lic_txt_fl: Create license text file; Defaults to false.
		:type mk_lic_txt_fl: Bool

		:return: This class constant.
		:rtype: Cls[ Slf ]
		"""

		# Post Processes --------
		if SCL_DBG_STT :
			(
				s.log
					.ifo( 
						# name
						f"initiating..." 
					)
					.prt()
			)


		# get defaults.
		# [ .dflt_directory ]
		_sclDflt = cst.__ldDfltx()


		# Main --------
		if SCL_DBG_STT :

			(
				s.log
					.ifo( 
						# name
						f"start licensing..." 
					)
					.prt()
			)


		# license target.
		(
			SclMdl(
				# source_directory
				src__
			)
				.lic(
					# Default Options
					# approves
					apvx = _sclDflt.apvx + apvx
					# configurations
					, cnfx = _sclDflt.cnfx + cnfx
					# ignores
					, ignx = _sclDflt.ignx + ignx
					# templates
					, tplx = _sclDflt.tplx + tplx
					# I\O Options
					# ignore_symbolic_link
					, ign_lnk = ign_lnk
					# keep_symbolic_link
					, kp_lnk = kp_lnk
					# overwrite
					, ovw = ovw
					# Locational Options
					# distribution_directory
					, dist = dist
					# Search Options
					# follow_link
					, flw_lnk = flw_lnk
					# recursive
					, rc = rc
					# Alternative Options
					# cleanup_default_configurations
					, cu_dflt_cnfx = cu_dflt_cnfx
					# cleanup_.gitignore_list
					, cu_git_lst = cu_git_lst
					# make_license_text_file
					, mk_lic_txt_fl = mk_lic_txt_fl 
				)
		)


		if SCL_DBG_STT :
			
			(
				s.log
					.ifo( 
						# name
						f"done." 
					)
					.prt()
			)


		return cst



	# ********
	license = lic



# ======================================================================================
# UNLICENSE
# ======================================================================================
	@clsmtd
	def ulic(
		cst : Cls[ Slf ]
		# source_directory
		, src__ : sFldr | sStr | Str
		# Default Options
		# approves
		, apvx : sArr | Arr = []
		# configuration
		, cnfx : sDic | Dic = {}
		# ignores
		, ignx : sArr | Arr = []
		# template
		, tplx : sDic | Dic = {}
		# Search Options
		# follow_link
		, flw_lnk : Bool = fls
		# recursive
		, rc : Bool = tru
		# Alternative Options
		# remove_license_text_file
		, rm_lic_txt_fl : Bool = fls 
	) -> Cls[ Slf ] :	
		
		"""
		### Unlicense

		:param src__: Target directory.
		:type src__: sStr or Str

		:param apvx__: Default approves; Defaults to empty array.
		:type apvx__: sArr or Arr

		:param cnfx: Default configuraiton; Defaults to empty ditionary.
		:type cnfx: sDic or Dic

		:param ignx: Default ignores; Defaults to empty array.
		:type ignx: sArr or Arr

		:param tplx__: Default templates; Defaults to empty ditionary.
		:type tplx__: sDic or Dic

		:param rc: Recursive, apply licence to all files in all subfolders; Defaults to flase.
		:type rc: Bool

		:param rm_lic_txt_fl: Remove license text file; Defaults to false.
		:type rm_lic_txt_fl: Bool

		:return: This class constant.
		:rtype: Cls[ Slf ]
		"""

		# Post Processes --------
		if SCL_DBG_STT :
		
			(
				s.log
					.ifo( 
						# name
						f"initiating..." 
					)
					.prt()
			)


		# get defaults.
		# [ .dflt_directory ]
		_sclDflt = cst.__ldDfltx()


		# Main --------
		if SCL_DBG_STT :
			
			(
				s.log
					.ifo( 
						# name
						f"start unlicensing..." 
					)
					.prt()
			)


		# unlicense target.
		(	
			SclMdl(
				# source_directory
				src__
			)
				.ulic(
					# Default Options
					# approves
					apvx = _sclDflt.apvx + apvx
					# configurations
					, cnfx = _sclDflt.cnfx + cnfx
					# ignores
					, ignx = _sclDflt.ignx + ignx
					# templates
					, tplx = _sclDflt.tplx + tplx
					# Search Options
					# follow_link
					, flw_lnk = flw_lnk
					# recursive
					, rc = rc
					# Alternative Options
					# remove_license_text_file
					, rm_lic_txt_fl = rm_lic_txt_fl
				)
		)


		if SCL_DBG_STT :

			(
				s.log
					.ifo( 
						# name
						f"done." 
					)
					.prt()
			)


		return cst



	# ********
	unlicense = ulic



# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# SCL CORE PRIVATE STATIC METHOD
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ======================================================================================
# __LOAD DEFAULTS
# ======================================================================================
	@clsmtd
	def __ldDfltx(
		cst : Cls[ Slf ]
	) -> SclMdl :

		"""
		### __Load Defaults

		:return: This class constant.
		:rtype: Cls[ Slf ]
		"""

		# Get Defaults --------
		# [ .dflt_directory ]
		_sclDfl = (
			SclMdl(
				f"{ SCL_ROOT_DIR }\\.dflt" 
			)
				.prpr()
		)


		# Post Process --------
		# current_year
		_sclDfl.cnfx[ "SCL_CUR_YR" ] = datetime.now().year


		return _sclDfl