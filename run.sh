#!/bin/bash
gunicorn --reload -b 0.0.0.0:8100 -w 4 \
         --access-logformat '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s %(D)s "%(f)s" "%(a)s"' \
         --access-logfile access_gunicorn.log --error-logfile error_gunicorn.log --log-level normal \
         --capture-output \
         ws:App
