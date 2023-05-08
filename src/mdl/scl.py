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

FwkMdlAbs = s.absx.FwkMdl
s_rdCnfx = s.utlx.rdCnfx



# --------------------------------------------------------------------------------------
# SOURCE FILE LICENSER
# --------------------------------------------------------------------------------------
from ..cnf.sclDbg import SCL_DBG_STT
from ..ovr import *
from .scl_alt import Scl_Alt
from .scl_dflt import Scl_Dflt
from .scl_io import Scl_Io
from .scl_sar import Scl_Sar




# ######################################################################################
# CLASS : SOURCE FILE LICENSER MODEL
# ######################################################################################
class Scl(
	# % alternative
	Scl_Alt
	# % default
	, Scl_Dflt
	# % i\o
	, Scl_Io
	# % search and replacement
	, Scl_Sar
	# spairaru framework model abstraction
	, FwkMdlAbs 
) :

	"""
	### SourceCodeLicenser Model
	"""


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# SPAIRARU CORE PUBLIC STATIC PROPERTY
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	# component_label
	_cpnt_lbl_ = [ 
		"scl" 
		, "SCL" 
	]

	# component_name
	_cpnt_nm_ = [ 
		"SourceCodeLicenser" 
	]
	
	# component_title
	_cpnt_ttl_ = "SourceCodeLicenser"



# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# SCL CORE PUBLIC INSTANCE ATTRIBUTE
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	# destination_folder
	__sDstnFldr : sFldr
	"""
	### Destination Folder
	"""


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# SCL CORE PUBLIC INSTANCE ATTRIBUTE
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ======================================================================================
# DESTINATION FOLDER
# ======================================================================================
	@attr
	def sDstnFldr(
		ctx : Slf
	) -> sFldr :

		"""
		### Destination Folder

		:return: Destination dictionary folder.
		:rtype: sFldr
		"""

		return ctx.__sDstnFldr



# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# PYTHON DEFAULT PUBLIC INSTANCE METHOD
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ======================================================================================
# __INITIATION__
# ======================================================================================
	def __init__(
		ctx : Slf
		# source_directory
		, src__ : sFldr | sStr | Str
	) -> Nul :

		"""
		### __Initiation__
	
		:param src__: Source directory.
		:type src__: sFldr or sStr or Str

		:return: No method return.
		:rtype: Non
		"""

		# SCL
		# Core Private Attributes --------
		# destination_folder
		ctx.__sDstnFldr = s.fldr( 
			# folder_path 
			src__ 
		)


		# SCL % DEFALT
		Scl_Dflt.__init__( ctx )



# ======================================================================================
# __STR__
# ======================================================================================
	def __str__( 
		ctx : Slf 
	) -> Str :

		return "<%s \'%s\' %s>" % (
			ctx._cpnt_lbl_[ 0 ]
			, ctx.sDstnFldr.pf 
			, hex( 
				id( ctx ) 
			) 
		)



# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# SCL CORE PUBLIC INSTANCE METHOD
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ======================================================================================
# LICENSE
# ======================================================================================
	def lic(
		ctx : Slf
		# Default Options
		# approves
		, apvx : sArr | Arr = []
		# configurations
		, cnfx : sDic | Dic = {}
		# ignores
		, ignx : sArr | Arr = []
		# templates
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
		, rc : Bool = fls
		# Alternative Options
		# cleanup_default_configurations
		, cu_dflt_cnfx : Bool = fls
		# cleanup_.gitignore_list
		, cu_git_lst : Bool = fls
		# make_license_text_file
		, mk_lic_txt_fl : Bool = fls 
	) -> Slf :
		
		"""
		### Licence

		:param apvx: Default approves; Defaults to empty array.
		:type apvx: sArr or Arr

		:param cnfx: Default configuraiton; Defaults to empty ditionary.
		:type cnfx: sDic or Dic

		:param ignx: Default ignores; Defaults to empty array.
		:type ignx: sArr or Arr

		:param tplx: Default templates; Defaults to empty ditionary.
		:type tplx: sDic or Dic

		:param ign_lnk: Ignore symbolic links; Defaults to false.
		:type ign_lnk: Bool

		:param kp_lnk: Keep symbolic links; Defaults to true.
		:type kp_lnk: Bool

		:param ovw: Overwrite if template alreasy present; Defaults to flase.
		:type ovw: Bool

		:param dist: Distribution directory; Defautls to empty string.
		:type dist: sFldr or sStr or Str

		:param flw_lnk: Follow symbolic link, licence original file; Defaults to false.
		:type flw_lnk: Bool

		:param rc: Recursive, apply licence to all files in all subfolders; Defaults to flase.
		:type rc: Bool

		:param cu_dflt_cnfx: Cleanup default configuration folders after licesing, preferred otpion when distribution folder is given; Defailts to false.
		:type cu_dflt_cnfx: Bool

		:param cu_git_lst: Cleanup any folders and files listing in .gitignore, preferred otpion when distribution folder is given; Defailts to false.
		:type cu_git_lst: Bool

		:param mk_lic_txt_fl: Create license text file; Defaults to flase.
		:type mk_lic_txt_fl: Bool

		:return: This instant context.
		:rtype: Slf
		"""

		# Precheck --------
		if not ctx.sDstnFldr.ex() :

			return ctx


		# Pre Option : Destination --------
		if( 
			dist
			and (
				# destionation_folder
				_sDistFldr :=
					s.fldr( 
						# folder_path
						dist 
					)
			)
     	) :


			# copy files to distination.
			_sDistFldr.rm(
				# FileSytem I/O Option
				# force
				f = tru
				# FileSystem Search Options
				# exclude_filter
				, xcl = [
					".git"
				]
			)


			ctx.sDstnFldr.cp2(
				# destination_path 
				_sDistFldr 
				# I\O Options
				# force
				, f = fls
				# ignore_symbolic_link
				, ign_lnk = ign_lnk
				# keep_symbolic_link
				, kp_lnk = kp_lnk
				# overwrite
				, ovw = tru
			)


			# license destination.
			(
				Scl(
					# source_directory
					_sDistFldr
				)
					.lic(
						# Default Options
						# approves
						apvx = apvx
						# configurations
						, cnfx = cnfx
						# ignores
						, ignx = ignx
						# templates
						, tplx = tplx
						# I\O Options
						# ignore_symbolic_link
						, ign_lnk = ign_lnk
						# keep_symbolic_link
						, kp_lnk = kp_lnk
						# overwrite
						, ovw = ovw
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


			return ctx


		# Pre Processes --------
		# prepair licensing.
		ctx.prpr(
			# Default Options
			# approves
			apvx = apvx
			# configurations
			, cnfx = cnfx
			# ignores
			, ignx = ignx
			# templates
			, tplx = tplx
		)


		# Main Execution : Current Directory --------
		if SCL_DBG_STT :

			(
				s.log
					.ifo( 
						# name
						f"+ { ctx.sDstnFldr.pf }" 
					)
					.prt()
			)


		# licence current directory.
		# [ source_code_file ]
		for sScFl in s.fs.flx( 
			# folder_path
			ctx.sDstnFldr.pf
			# Serach Options
			# include_patterns
			, icl = ctx.apvx
			# exclude_patterns
			, xcl = ctx.ignx
		) :
			

			if (
				# a : file is a symbolic link.
				sScFl.isLnk
				# b : follow_link is not enabled.
				and not flw_lnk
			) :

				continue


			if SCL_DBG_STT :

				(
					s.log
						.ifo( 
							# name
							f"-> { sScFl.pf }" 
						)
						.prt()
				)


			ctx.aplyTpl(
				# souce_code_file
				sScFl
				# template_content
				, (
					ctx.tplx[ sScFl.fnm ]
						if sScFl.fnm in ctx.tplx
						else ctx.tplx[ "@" ]
							if ctx.tplx.hs( "@" )
							else []
				)
				# I\O Options
				# overwrite
				, ovw = ovw
			)


		# Main Execution : Sub-directories --------
		if rc :

			# [ source_code_folder ]
			for sScFldr in s.fs.fldrx( 
				# folder_path
				ctx.sDstnFldr.pf 
				# Search Options
				# exclude_patterns
				, xcl = ctx.ignx
			) :


				if (
					# a : file is a symbolic link.
					sScFldr.isLnk
					# b : follow_link is not enabled.
					and not flw_lnk
				) :

					continue


				(
					Scl(
						# target_directory
						sScFldr.pf
					)
						.lic(
							# Default Options
							# approves
							apvx = ctx.foNonRcPtn( 
								# patterns
								ctx.apvx 
							)
							# configurations
							, cnfx = ctx.cnfx
							# ignores
							, ignx = ctx.foNonRcPtn( 
								# patterns
								ctx.ignx 
							)
							# templates
							, tplx = ctx.tplx 
							# I\O Options
							# ignore_symbolic_link
							, ign_lnk = ign_lnk
							# keep_symbolic_link
							, kp_lnk = kp_lnk
							# overwrite
							, ovw = ovw
							# Search Options
							# follow_link
							, flw_lnk = flw_lnk
							# recursive
							, rc = rc
						)
				)


		# Post Option : License Text File --------
		if( 
			mk_lic_txt_fl 
			and not (
				(
					# [ license text file ]
					_sLicTxtFl :=
						s.fl( 
							# path
							f"{ ctx.sDstnFldr.pf }\\LICENSE.txt"
						)
				)
					.ex()
			)
		) :
			
			_sLicTxtFl.mk(
				# lanes_of_stirng
				ctx.gtLicTxt()
			)


		# Post Option : Cleanup Default Configurations --------
		if cu_dflt_cnfx :

			ctx.clnDfltCnfx()

		
		# Post Option : Cleanup .gitignore List --------
		if cu_git_lst :

			ctx.clnGitLst()


		return ctx



	# ********
	license = lic



# ======================================================================================
# UNLICENSE
# ======================================================================================
	def ulic(
		ctx : Slf
		# Default Options
		# approves
		, apvx : sArr | Arr = []
		# configurations
		, cnfx : sDic | Dic = {}
		# ignores
		, ignx : sArr | Arr = []
		# templates
		, tplx : sDic | Dic = {}
		# Search Options
		# follow_link
		, flw_lnk : Bool = fls
		# recursive
		, rc : Bool = tru
		# Alternative Options
		# remove license text file
		, rm_lic_txt_fl : Bool = fls
	) -> Bool :
		
		"""
		### Unlicence

		:param apvx: Default approves; Defaults to empty array.
		:type apvx: sArr or Arr

		:param cnfx: Default configuraiton; Defaults to empty ditionary.
		:type cnfx: sDic or Dic

		:param ignx: Default ignores; Defaults to empty array.
		:type ignx: sArr or Arr

		:param tplx: Default templates; Defaults to empty ditionary.
		:type tplx: sDic or Dic

		:param flw_lnk: Follow symbolic link, licence original file; Defaults to false.
		:type flw_lnk: Bool

		:param rc: Recursive, apply licence to all files in all subfolders; Defaults to flase.
		:type rc: Bool

		:param rm_lic_txt_fl: Remove license text file; Defaults to flase.
		:type rm_lic_txt_fl: Bool

		:return: This instant context.
		:rtype: Slf
		"""
	
		# Precheck --------
		if not ctx.sDstnFldr.ex() :

			return ctx


		# Post Processes --------
		# prepair licensing.
		ctx.prpr(
			# Default Options
			# approves
			apvx = apvx
			# configurations
			, cnfx = cnfx
			# ignores
			, ignx = ignx
			# templates
			, tplx = tplx
		)


		# Main Execution : Current Directory --------
		if SCL_DBG_STT :

			(
				s.log
					.ifo( 
						# name
						f"+ { ctx.sDstnFldr.pf }" 
					)
					.prt()
			)


		# unlicence current directory.
		# [ source_code_file ]
		for sScFl in s.fs.flx( 
			# folder_path
			ctx.sDstnFldr.pf 
			# Search Options
			# include_patterns
			, icl = ctx.apvx
		) :


			if SCL_DBG_STT :

				(
					s.log
						.ifo( 
							# name
							f"- { sScFl.pf }" 
						)
						.prt()
				)

			
			if (
				# a : file is a symbolic link.
				sScFl.isLnk
				# b : follow_link is not enabled.
				and not flw_lnk
			) :
				
				continue


			ctx.tkoTpl(
				# souce_code_file
				sScFl
				# template_content
				, (
					ctx.tplx[ sScFl.fnm ]
						if sScFl.fnm in ctx.tplx
						else ctx.tplx[ "@" ]
							if ctx.tplx.hs( "@" )
							else []
				)
			)


		# Main Execution : Sub-directories --------
		if rc :

			# [ source_code_folder ]
			for sScFldr in s.fs.fldrx( 
				# folder_path
				ctx.sDstnFldr.pf 
				# Serach Options
				# exclude_patterns
				, xcl = ctx.ignx
			) :


				if (
					# a : file is a symbolic link.
					sScFldr.isLnk
					# b : follow_link is not enabled.
					and not flw_lnk
				) :

					continue
	

				(
					Scl(
						# source_directory
						sScFldr.pf
					)
						.ulic(
							# Default Options
							# approves
							apvx = ctx.foNonRcPtn( 
								# patterns
								ctx.apvx 
							)
							# configurations
							, cnfx = ctx.cnfx
							# ignores
							, ignx = ctx.foNonRcPtn( 
								# patterns
								ctx.ignx 
							)
							# templates
							, tplx = ctx.tplx 
							# Search Options
							# follow_link
							, flw_lnk = flw_lnk
							# recursive
							, rc = rc
						)
				)


		# Post Option : License Text File --------
		if( 
			rm_lic_txt_fl 
			and (
				(
					# [ license text file ]
					_sLicTxtFl :=
						s.fl( 
							# path
							f"{ ctx.sDstnFldr.pf }\\LICENSE.txt"
						)
				)
					.ex()
			)
		) :
				
			_sLicTxtFl.rm()


		return ctx



	# ********
	unlicense = ulic