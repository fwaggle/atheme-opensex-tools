# Tools for OpenSEX databases
(C) 2014 fwaggle <fwaggle@fwaggle.org>

I made this to scratch an itch, but it's not yet complete. At present it
will rather naively merge multiple databases and dump out a new DB. It
throws away a lot of information, including the user IDs.

It's currently unfinished and untested.

# Usage:

Merge two databases (throwing away newer records where older ones exist):

    ./merge.py atheme.db old.db

## Potential issues

* We currently chuck away the IDs and just start counting and assigning
  new ones. I have no idea about the repercussions of this.

* Nickname record collisions - this needs refactoring into it's own list,
  instead of being a child of the User object.
