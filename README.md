# chttrack - condition httrack

I ran into a problem where an error message was on a site I wanted to mirror regularly.
The HTTP status code was still 200 and thus httrack destroyed the working mirror of the site.
So I hacked a wrapper around httrack to disable mirror updates when certain strings are in the page.