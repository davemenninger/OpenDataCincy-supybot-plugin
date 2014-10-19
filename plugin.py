###
# Copyright (c) 2014, Dave Menninger
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions, and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions, and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#   * Neither the name of the author of this software nor the name of
#     contributors to this software may be used to endorse or promote products
#     derived from this software without specific prior written consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

###

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks

from urllib2 import urlopen
from json import load
from random import randint

class OpenDataCincy(callbacks.Plugin):
    """This plugin gets data from the Open Data Cincy data catalog."""
    pass

    def odc(self, irc, msg, args, query):
        """usage: odc types - lists available types;    odc <type> - returns a random entry of <type>
        """
        url = "http://www.opendatacincy.org/api/"
        response = urlopen(url)
        j = load(response)
        if( query == 'types' ):
            types = ""
            for type in j:
                types += type + " "
            irc.reply("types of data available are: " + types)
        elif ( query in j ):
            url = j[query]
            response = urlopen(url)
            d = load(response)
            d['count']
            url = j[query] + str( randint(1, d['count']) )
            irc.reply( 'url: ' + url )
            response = urlopen(url)
            a_result = load(response)
            desc = a_result['description']
            irc.reply( 'desc: ' + desc )
            if ( 'latitude' in a_result and 'longitude' in a_result ):
                lat = a_result['latitude']
                long = a_result['longitude']
                map_url = 'http://www.openstreetmap.org/?mlat=' + str(lat) + '&mlon=' + str(long) + '#map=19/' + str(lat) + '/' + str(long) + '&layers=C'
                irc.reply( "map: " + map_url )

    odc = wrap(odc, ['text'])
        
Class = OpenDataCincy


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
