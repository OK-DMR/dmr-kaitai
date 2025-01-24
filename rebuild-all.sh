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
    bash -x -c "kaitai-struct-compiler -t python --python-package ${python_package} *.ksy"
    python3 -m black .
  fi
  cd ${dirbase}
done

python3 -m black okdmr
