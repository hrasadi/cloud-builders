#!/bin/bash

DOCKER_ARGS="${@}"

# Append UCL tag if '__UCL__' file exists in the workdir
if [[ -f './__UCL__' ]]; then
  UCL_LABEL="ucl=$(cat __UCL__)"
  DOCKER_ARGS+=" --label $UCL_LABEL"
  echo "Docker arguments updated because UCL tag was present. New arguments are: ${DOCKER_ARGS}"
fi

/usr/bin/docker $DOCKER_ARGS
