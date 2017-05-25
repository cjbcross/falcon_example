#!/bin/bash

uwsgi --http :9090 --wsgi-file server.py --callable api --py-autoreload 3
