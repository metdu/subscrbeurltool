!#/bin/bash

docker build . -t func_app
docker run -d -p 8085:8888  --name func_app func_app