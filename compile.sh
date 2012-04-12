#!/bin/bash

EXPECTED_ARGS=1
E_BADARGS=65

if [ $# -ne $EXPECTED_ARGS ]
then
  echo -e "Usage: `basename $0` <colstyle base name>"
  exit $E_BADARGS
fi

echo "Removing any old $1.style file"
rm -r $1.style
echo "Compiling new $1.style file"
./colrepl.py $1.colstyle > $1.style
