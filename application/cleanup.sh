#!/bin/sh
rm -r ${PWD}/temp_json
mkdir -p -- "temp_json"
python3 ${PWD}/cleanup.py
mkdir -p -- "temp_json"