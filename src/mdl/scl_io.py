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
# CLASS : SOURCE FILE LICENSER MODEL - I\O
# ######################################################################################
class Scl_Io :

	"""
	### SourceCodeLicenser Model - I\O
	"""


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# SCL I\O PUBLIC INSTANCE METHOD
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ======================================================================================
# APPLY TEMPLATE
# ======================================================================================
	def aplyTpl(
		ctx : Slf
		# souce_code_file
		, sScFl__ : sFl
		# template_content
		, tpl_cnt__ : sArr[ sStr | Str ] | Arr[ sStr | Str ]
		# I\O Options
		# overwrite
		, ovw : Bool = fls
	) -> Slf :

		"""
		### Apply Template

		:param sScFl__: Source file, spairaru file object.
		:type sScFl__: sFl

		:param tpl_cnt__: Template content, lanes of strings.
		:type tpl_cnt__: sArr[ sStr | Str ] or Arr[ sStr | Str ]

		:param ovw: Overwrite if template alreasy present; Defaults to flase.
		:type ovw: Bool

		:return: This instant context.
		:rtype: Slf
		"""

		# Precheck --------
		if not tpl_cnt__ :

			return ctx
		

		# Main Executions --------
		with sScFl__ :


			# [ target_content ]
			_tgt_cnt = sScFl__.rd()


			# comment template.
			_tpl_cnt = ctx.cmntoCnt(
				# lanes_of_content
				ctx.prphrCnt(
					# lanes_of_content
					tpl_cnt__
				)
				# processing_langurage_type
				, sScFl__.ext
			)


			# if overwrite is enabled, remove current template.
			if ovw :

				_tgt_cnt = ctx.tkoTpl( 
					# target_content
					_tgt_cnt
					# template_content
					, _tpl_cnt
				)


			# [ target_length ]
			_tgt_len = len( _tgt_cnt )

			# [ first_lane_of_target ]
			_1st_ln = ctx.__dtrmFstLn(
				# lanes_of_string
				_tgt_cnt
			) 

			# [ template_length ]
			_tpl_len = len( _tpl_cnt )



			# abjust taregt last lane.
			if ( 
				# 1. first lane is not 0 .
				_1st_ln != 0
				# 2. last lane is first lane.
				and _tgt_len == _1st_ln
				# 3. last lane is not end with lanebreak.
				and not _tgt_cnt[ _1st_ln - 1 ].ew( S_STR_LNBRK )
			) :	

				_tgt_cnt[ _1st_ln - 1 ] += S_STR_LNBRK


			# abjust template last lane.
			if ( 
				# 1. has template.
				_tpl_len
				# 2. last lane is not end with lanebreak.
				and not _tpl_cnt[ _tpl_len - 1 ].ew( S_STR_LNBRK )
			) :	

				_tpl_cnt[ _tpl_len - 1 ] += S_STR_LNBRK


			# determine if license if already applied.
			if(
				_tgt_len >= _tpl_len
				and _tgt_cnt.hs( _1st_ln )
				and _tgt_cnt[ _1st_ln ] == _tpl_cnt[ 0 ]
				and _tgt_cnt[ _tpl_len + _1st_ln - 1 ] == _tpl_cnt[ _tpl_len - 1 ]
			) :
								
				return ctx


			# add new template.
			sScFl__.rwr(
				# lanes_of_stirng
				_tgt_cnt[ :_1st_ln ] 
				+ _tpl_cnt 
				+ _tgt_cnt[ _1st_ln: ]
			)


		return ctx



	# ********
	applyTemplate = aplyTpl



# ======================================================================================
# TAKEOUT TEMPLATE
# ======================================================================================
	# MODIFIY CONTENT ********
	@ovld( Arr , Arr )
	def tkoTpl(
		ctx : Slf
		# souce_code_content
		, sc_cnt__ : sArr[ sStr | Str ] | Arr[ sStr | Str ]
		# template_content
		, tpl_cnt__ : sArr[ sStr | Str ] | Arr[ sStr | Str ]
	) -> sArr[ sStr ] :

		"""
		### Takeout Template

		:param sc_cnt__: Target content, lanes of strings.
		:type sc_cnt__: sArr[ sStr | Str ] or Arr[ sStr | Str ]

		:param tpl_cnt__: Template content, lanes of strings.
		:type tpl_cnt__: sArr[ sStr | Str ] or Arr[ sStr | Str ]

		:return: _description_
		:rtype: _type_
		"""

		# [ template_length ]
		_tpl_len = len( tpl_cnt__ )


		# Removal --------
		# [ first_lane_of_target ]
		_1st_ln = ctx.__dtrmFstLn(
			# lanes_of_string
			sc_cnt__
		) 


		if( 
			not sc_cnt__
			or not tpl_cnt__
			# file not contains template
			or not sc_cnt__.hs( _1st_ln )
			# first lane of template not matching
			or not sc_cnt__[ _1st_ln ].startswith( tpl_cnt__[ 0 ] )
			# last lane of template not matching
			or sc_cnt__[ _tpl_len + _1st_ln - 1 ].startswith( tpl_cnt__[ 0 ] )
		) :
			
			return sc_cnt__


		return(
			sc_cnt__[ :_1st_ln ] 
			+ sc_cnt__[ ( _tpl_len + _1st_ln): ]
		)



	# MODIFIY FILE ********
	@ovld( sFl , Arr )
	def tkoTpl(
		ctx : Slf
		# souce_code_file
		, sScFl__ : sFl
		# template_content
		, tpl_cnt__ : sArr[ sStr ]
	) -> Slf :

		"""
		### Takeout Template

		:param sScFl__: Source file, spairaru file object.
		:type sScFl__: sFl

		:param tpl__: Template content, lanes of strings.
		:type tpl__: sArr[ sStr | Str ] or Arr[ sStr | Str ]

		:return: This instant context.
		:rtype: Slf
		"""

		sScFl__.rwr(
			# lanes_of_stirng
			ctx.tkoTpl(
				# souce_code_content
				sScFl__.rd()
				# template_content
				, ctx.cmntoCnt(
					# lanes_of_content
					ctx.prphrCnt(
						# lanes_of_content
						tpl_cnt__
					)
					# processing_langurage_type
					, sScFl__.ext
				)
			)
		)


		return ctx



	# ********
	takeoutTemplate = tkoTpl



# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# SCL I\O PRIVATE INSTANCE METHOD
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ======================================================================================
# __DETERMINE FIRST LANE
# ======================================================================================
	def __dtrmFstLn(
		ctx
		# souce_code_content
		, cnt__ : sArr[ sStr | Str ] | Arr[ sStr | Str ]
	) -> Int :
		
		"""
		### ___Determine First Lane

		:param cnt__: Content, lanes of strings.
		:type cnt__: sArr[ sStr | Str ] or Arr[ sStr | Str ]

		:return: Index of first lane to apply template
		:rtype: Int
		"""

		# First Lane by Type --------
		# php : <? or <?php
		# shell : #!
		_sFstLnPtn = s.rgx(
			# pattern_text
			r'^(\#\!|\<\?)'
		)


		if( 
			# 1. no lanes.
			not cnt__
			# 2. first lane not matching. 
			or not _sFstLnPtn.mhx( cnt__[ 0 ] )
		) :

			return 0


		return 1