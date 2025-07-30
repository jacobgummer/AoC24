#!/bin/sh

if [ "$#" -lt 2 ]; then
  echo "Usage: $0 <day> <t1|t2> [-t]"
  exit 1
fi

DAY=$(printf "%02d" "$1")
shift
EXECUTABLE="day${DAY}"

cabal run -v0 "$EXECUTABLE" -- "$@"
