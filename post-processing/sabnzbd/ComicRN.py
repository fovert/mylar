#!/usr/bin/env python
#
##############################################################################
### SABNZBD POST-PROCESSING SCRIPT                                         ###
#
# Move and rename comics according to Mylar's autoProcessComics.cfg
#
# NOTE: This script requires Python to be installed on your system.
##############################################################################

#module loading
import sys
import autoProcessComics

#the code.
if len(sys.argv) < 2:
    print "No folder supplied - is this being called from SABnzbd or NZBGet?"
    sys.exit()
elif len(sys.argv) >= 3:
    sys.exit(autoProcessComics.processEpisode(sys.argv[1], sys.argv[3]))
else:
    sys.exit(autoProcessComics.processEpisode(sys.argv[1]))
