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



# --------------------------------------------------------------------------------------
# SCL
# --------------------------------------------------------------------------------------
from ..ovr import *


if TYPCHK :

	from .scl import Scl as Slf




# ######################################################################################
# CLASS : SOURCE FILE LICENSER MODEL - ALTERNATIVE
# ######################################################################################
class Scl_Alt :

	"""
	### SourceCodeLicenser Model - Alternative
	"""


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# SCL ALTERNATIVE PUBLIC INSTANCE METHOD
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ======================================================================================
# CLEAN DEFAULT CONFIGURATIONS
# ======================================================================================
	def clnDfltCnfx(
		ctx : Slf
	) -> Slf :
		
		"""
		### Clean Default Configurations

		:return: This instant context.
		:rtype: Slf
		"""

		# remove configuration files.
		s.fldr.rm(
			# paths
			* (
				s.fs.gl( 
					# path
					f"{ ctx.sDstnFldr.pf }\\**\\.mt" 
					# Search Options
					# exclude_filter
					, xcl = [
						".dflt"
						, "__examples__"
					]
				) 
				+ s.fs.gl( 
					# path
					f"{ ctx.sDstnFldr.pf }\\**\\.scl" 
					# Search Options
					# exclude_filter
					, xcl = [
						".dflt"
						, "__examples__"
					]				) 
			)
		)



# ======================================================================================
# CLEAN GIT IGNORE LIST
# ======================================================================================
	def clnGitLst(
		ctx : Slf
	) -> Slf :
		
		"""
		### Clean .GitIgore List

		:param dst: Destination directory.
		:type dst: sFldr or sStr or Str

		:return: This instant context.
		:rtype: Slf
		"""

		# remove any defined in .gitignore
		if (
			(
				(
					# [ .gitignore_file ]
					_sGitIgnFl :=
						s.fl( 
							# path
							f"{ ctx.sDstnFldr.pf }\\.gitignore"
						)
				)
					.ex()
			)
			and (
				# [ gitignore_list ]
				_gitign_lst := 
					s.arr(
						* [
							ln
								for ln in _sGitIgnFl.rd()
									if( 
										not ln.sw( "#" )
										and not ln.sw( S_STR_LNBRK )
									)
						]
					)
			)
			and _gitign_lst
		) :
			
			
			_gitign_lst.ea(
				lambda i , v :
					_gitign_lst.ed(
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


			s.fldr.rm(
				# folder_paths
				* s.fs.gl( 
					# folder_path
					f"{ ctx.sDstnFldr.pf }\\**" 
					# Search Options
					# include_filter
					, icl = _gitign_lst
					# exclude_filter
					, xcl = [
						# * its import to avoid deletion of .git folder.
						"**/.git"
					]
				) 
			)


		return ctx



# ======================================================================================
# GET LICENSE TEXT
# ======================================================================================
	def gtLicTxt(
		ctx : Slf
	) -> sArr[ sStr ] :
		
		"""
		### Get License Text

		:return: List of string.
		:rtype: sArr[ sStr ]
		"""

		# Prechecks --------
		# [ license_format ]
		_fmt : Str = ctx.__gtLicFmt(
			# [ license_type ]
			_typ := 
				ctx.cnfx.gt( "SCL_LIC_TYP" )
		)


		if not _fmt :

			return s.arr()


		# Determine License Template --------
		# [ template_name ]
		_nm = ""


		# Apache
		if "aph" in _fmt :
			
			_nm = "aph-2.0" 


		# AGPL
		elif "agpl" in _fmt :

			_nm = "agpl" 


		# EPL
		elif "epl" in _fmt :

			_nm = "epl-2.0" 


		# BAD
		elif "bsd" in _fmt :


			if "2" in _typ :

				_nm = "bsd-2" 


			elif "3" in _typ :

				_nm = "bsd-3" 


		# GPL
		elif "gpl" in _fmt :


			if "2" in _typ :

				_nm = "gpl-2.0" 


			elif "3" in _typ :

				_nm = "gpl-3.0" 


		# LGPL
		elif "lgpl" in _fmt :

			_nm = "lgpl-2.1" 


		# MIT
		elif "mit" in _fmt :

			_nm = "mit"


		# MIT
		elif "moz" in _fmt :

			_nm = "moz-2.0"


		# MIT
		elif "ulic" in _fmt :

			_nm = "ulic"


		# Get License Text --------
		return ctx.prphrCnt(
			# template_content
			ctx.tplx.gt( 
				# key
				_nm
				# fallback
				, s.arr()
			)
		)



	# ********
	getLicenseText = gtLicTxt



# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# SCL ALTERNATIVE PRIVATE INSTANCE METHOD
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ======================================================================================
# __GET LICENSE FORMAT
# ======================================================================================
	def __gtLicFmt(
		ctx : Slf
		# type
		, typ__ : sStr
	) -> Str :
		
		"""
		### __Get License Format

		:return: Licese format.
		:rtype: Str
		"""

		# [ type ]
		_typ = typ__.lower()
		
		# [ types ]
		_typx = {
			# Apache
			"apache" : "aph"
			, "aph" : "aph"
			# BSD
			, "bsd" : "bsd"
			# EPL
			, "Eclipse Public License" : "epl"
			, "epl" : "epl"
			# MIT
			, "mit" : "mit"
			# GPL
			, "general public license" : "gpl"
			, "gpl" : "gpl"
			, "gnu" : "gpl"
			# AGPL
			, "affero general public license" : "agpl"
			, "agpl" : "agpl"
			# LGPL
			, "lesser general public license" : "lgpl"
			, "lgpl" : "lgpl"
			# Mozilla
			, "mozilla" : "moz"
			, "moz" : "moz"
			# The Unlicense
			, "the unlicense" : "ulic"
			, "ulic" : "ulic"
		}


		for k in _typx :

			if k in _typ :

				return _typx[ k ]


		return ""