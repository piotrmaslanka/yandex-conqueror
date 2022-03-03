#!/bin/bash
set -e

wait-for-cassandra cassandra
coverage run -m nose2 -vv -F
coverage combine || true
coverage report || true