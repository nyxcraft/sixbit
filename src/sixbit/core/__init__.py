"""sixbit.core -- shared foundation for the sixbit framework.

sixbit recreates original PDP-10 software in Python, running classic programs
from their original FORTRAN-10 source on the forterp interpreter under a
TOPS-10-style monitor.

``sixbit`` is a PEP 420 namespace package. This distribution provides
``sixbit.core``; individual programs ship as their own sibling distributions
(for example ``sixbit-empire`` -> ``sixbit.games.empire``) that add to the
shared namespace without this package having to know about them in advance.

This is an early pre-alpha release that establishes the name and layout;
functionality lands in subsequent versions.
"""

__version__ = "0.0.1"
