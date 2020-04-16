#!/bin/bash
echo "You will be able to launch jupyter notebook in the following url: http://localhost:8888/lab"
docker run -it -v "${PWD}/src":"/home/jovyan" -p 8888:8888 vizu-jupyter-image