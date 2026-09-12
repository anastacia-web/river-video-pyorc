import inspect
import pyorc

print("pyorc version:", pyorc.__version__)

# After a valid transect is created, inspect the installed methods first:
#
# print(inspect.signature(piv.transect.get_v_surf))
# print(inspect.signature(piv.transect.get_v_bulk))
# print(inspect.signature(piv.transect.get_q))
#
# Do not invent a discharge value.
