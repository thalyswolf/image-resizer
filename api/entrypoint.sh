#!/bin/bash
cd /home/images-resize \
&& export PYTHONDONTWRITEBYTECODE=1 \
&& uvicorn main:app --host=0.0.0.0 --port=80 --reload
