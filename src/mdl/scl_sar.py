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
# CLASS : SOURCE FILE LICENSER MODEL - SEARCH AND REPLACMENT
# ######################################################################################
class Scl_Sar :

	"""
	### SourceCodeLicenser Model - Search and Replacement
	"""


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# SCL SAR PUBLIC INSTANCE METHOD
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ======================================================================================
# COMMENT OUT CONTENT
# ======================================================================================
	def cmntoCnt(
		ctx
		# lanes_of_content
		, cnt__ : sArr[ sStr | Str ] | Arr[ sStr | Str ]
		# processing_langurage
		, lng__ : sStr | Str
	) -> sArr[ sStr ] :
		
		"""
		### Comment Out Content

		:param cnt__: Content, lanes of strings.
		:type cnt__: sArr[ sStr | Str ] or Arr[ sStr | Str ]

		:param lng__: Processing langurage type.
		:type lng__: sStr or Str

		:return: Commented template.
		:rtype: sArr[ sStr ]
		"""

		# [ lanes_of_content ]
		_lnx = s.arr()


		# CSS
		# Java 
		# Javascript ]
		# PHP
		# TypeScript
		# Swift
		if lng__ in [
			"css"
			, "java"
			, "js"
			, "php"
			, "ts"
			, "swift"
		] :

			_lnx += [ 
				s.str( f"/*{ S_STR_LNBRK }" ) 
			]

			_lnx += [
				s.str( ln )
					if ln.sw( "\t" )
					else s.str( f"\t{ln}" )
						for ln in cnt__
			]

			_lnx += [ 
				s.str( f"{ S_STR_LNBRK }*/{ S_STR_LNBRK }" ) 
			]


		# Html
		# Xml
		if lng__ in [
			"html"
			, "xml"
		] :

			_lnx += [ 
				s.str( f"<!--{ S_STR_LNBRK }" ) 
			]

			_lnx += [
				s.str( ln )
					if ln.sw( "\t" )
					else s.str( f"\t{ln}" )
						for ln in cnt__
			]

			_lnx += [ 
				s.str( f"{ S_STR_LNBRK }-->{ S_STR_LNBRK }" ) 
			]


		# .ini
		# .conf
		# Python
		elif lng__ in [
			"ini"
			, "cnf"
			, "conf"
			, "py"
		] :

			_lnx += [
				s.str( ln )
					if ln.sw( "# " )
					else s.str( f"# { ln }" )
						for ln in cnt__
			]


		# Batch
		elif lng__ in [
			"cmd"
		] :

			_lnx += [
				s.str( ln )
					if ln.sw( "REM " )
					else s.str( f"REM { ln }" )
						for ln in cnt__
			]


		# Shell
		elif lng__ in [
			"sh"
		] :

			_lnx += [ 
				s.str( f"<<com{ S_STR_LNBRK }" ) 
			]

			_lnx += [
				s.str( ln )
					if ln.sw( "\t" )
					else s.str( f"\t{ln}" )
						for ln in cnt__
			]

			_lnx += [ 
				s.str( f"{ S_STR_LNBRK }com{ S_STR_LNBRK }" ) 
			]


		return _lnx



	# ********
	commentOutContent = cmntoCnt



# ======================================================================================
# PARAPHRASE CONTENT
# ======================================================================================
	def prphrCnt(
		ctx : Slf
		# lanes_of_content
		, cnt__ : sArr[ sStr | Str ] | Arr[ sStr | Str ]
	) -> sArr[ sStr ] :
		
		"""
		### Paraphrase Content

		:param cnt__: Lanes of strings.
		:type cnt__: sArr[ sStr | Str ] or Arr[ sStr | Str ]

		:return: This instant context.
		:rtype: Slf
		"""

		# [ lanes ]
		_lnx = s.arr()

		# [ pattern ]
		_sPtn = s.rgx( r"\{\{\%(.+?)\}\}" )


		for ln in cnt__ :


			for var in _sPtn.grpx( ln ) :

				if( 
					# a. configuration key exists
					var in ctx.cnfx 
					# b. configuration value not empty
					and ctx.cnfx[ var ] 
				) :

					ln = ln.rplc( 
						# finder
						"{{%" + var + "}}" 
						# replacement
						# * ensure configuration value is in string.
						, str( ctx.cnfx[ var ] )
					)


			_lnx += [ ln ]


		return _lnx



	# ********
	paraphraseContent = prphrCnt