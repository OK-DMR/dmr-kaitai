#!/bin/bash

packages=$(find * -iname '__init__.py')
dirbase=$(pwd)

for initfile in ${packages}
do
  dir=$(dirname ${initfile})
  python_package=$(echo $dir | sed 's/\//\./gi')
  # echo ${dir} "=>" ${python_package}
  cd ${dir}
  if [ "$(find -maxdepth 1 -type f -iname '*.ksy')" ]; then
    kaitai-struct-compiler -t python --python-package ${python_package} *.ksy
    black .
  fi
  cd ${dirbase}
done
