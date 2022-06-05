#!/bin/bash

packages=$(find * -iname '__init__.py')
dirbase=$(pwd)

mkdir -p ${dirbase}/build/java

for initfile in ${packages}
do
  dir=$(dirname ${initfile})
  java_package="cz."$(echo $dir | sed 's/\//\./gi')
  cd ${dir}
  if [ "$(find -maxdepth 1 -type f -iname '*.ksy')" ]; then
    bash -x -c "kaitai-struct-compiler --outdir ${dirbase}/build/java/ -t java --java-package ${java_package} *.ksy"
  fi
  cd ${dirbase}
done
