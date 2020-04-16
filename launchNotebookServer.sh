#!/bin/bash
docker run -it -v "${PWD}/src":"/home/jovyan" -p 8888:8888 vizu-jupyter-image