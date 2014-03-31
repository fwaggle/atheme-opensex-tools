# Tools for OpenSEX databases (atheme et al)
(C) 2014 fwaggle <fwaggle@fwaggle.org>

# Usage:

Merge two databases (throwing away newer records where older ones exist):

    ./merge.py atheme.db old.db

## Potential issues

* I don't know if memos are to/from users or nicks. Pretending users atm.
