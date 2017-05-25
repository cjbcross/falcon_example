#!/bin/bash

gunicorn -b 127.0.0.1:9090 -w 10 server:api
