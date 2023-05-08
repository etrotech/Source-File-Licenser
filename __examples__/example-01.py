import os

# import source file licenser
from scl import scl


# [ input_root ]
_ipu_root = f"{ os.path.dirname( __file__ ) }\\test_inputs"

# [ output_root ]
_opu_root = f"{ os.path.dirname( __file__ ) }\\test_outputs"




# ######################################################################################
# Example 1. License Input_Directory.
# ######################################################################################
# scl.lic( 
#     # source_directory
#     _ipu_root 
#     # overwrite
#     # * rebuild license header if already exists.
#     , ovw = True 
# )




# ######################################################################################
# Example 2. Copy Input_Directory to Distination_Directory and license it.
# ######################################################################################
scl.lic( 
    # source_directory
    _ipu_root 
	# distribution_directory
	, dist = _opu_root
    # overwrite
	# * rebuild license header if already exists.
    , ovw = True 
    # cleanup_default_configurations
	, cu_dflt_cnfx = True
	# make_license_text_file
	, mk_lic_txt_fl = True
)




# ######################################################################################
# Example 3. Unlicense Directory.
# ######################################################################################
# scl.ulic( _opu_root )