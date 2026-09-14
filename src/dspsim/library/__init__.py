import atexit

from dspsim.library._library import *

# Attempt to link with the dspsim framework
try:
    import dspsim.framework as _framework

    set_global_context_factory(_framework.get_global_context_factory())
except ImportError:
    pass

# Prevent nb leak warnings.
atexit.register(reset_global_context_factory)
