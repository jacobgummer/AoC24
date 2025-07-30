#!/usr/bin/env bash

# Exit on error
set -e

if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <day-number>"
  exit 1
fi

# Format day number with leading zero (e.g., 3 -> 03)
DAY=$(printf "%02d" "$1")
DAYNAME="day${DAY}"
FILENAME="solutions/Day${DAY}.hs"

if [ -e "$FILENAME" ]; then
  echo "File $FILENAME already exists."
  exit 1
fi

# Create required directories
mkdir -p solutions
mkdir -p data/inputs
mkdir -p data/tests

# Create DayNN.hs
cat >"$FILENAME" <<EOF
import Common
import qualified Data.Text as T
import System.Environment (getArgs)

main :: IO ()
main = do
  args <- getArgs
  case length args of
    1 -> do
      input <- readInputLines "data/inputs/day${DAY}.txt"
      case args of
        ["p1"] -> print \$ part1 input
        ["p2"] -> print \$ part2 input
        _ -> putStrLn "Usage: ./day ${DAY} p1|p2 [-t]"
    2 -> do
      input <- readInputLines "data/tests/day${DAY}.txt"
      case args of
        ["p1", "-t"] -> print \$ part1 input
        ["p2", "-t"] -> print \$ part2 input
        _ -> putStrLn "Usage: ./day ${DAY} p1|p2 [-t]"
    _ -> putStrLn "Usage: ./day ${DAY} p1|p2 [-t]"

part1 :: [T.Text] -> Int
part1 input = undefined

part2 :: [T.Text] -> Int
part2 input = undefined
EOF

# Create empty input files
touch "data/inputs/day${DAY}.txt"
touch "data/tests/day${DAY}.txt"

# Append executable stanza to .cabal file if not already present
CABAL_FILE=$(find . -maxdepth 1 -name "*.cabal" | head -n 1)

if grep -q "^executable ${DAYNAME}$" "$CABAL_FILE"; then
  echo "Executable '${DAYNAME}' already exists in ${CABAL_FILE}."
else
  echo "" >>"$CABAL_FILE"
  cat >>"$CABAL_FILE" <<EOF
executable ${DAYNAME}
    import:           warnings
    main-is:          Day${DAY}.hs
    hs-source-dirs:   solutions
    default-language: Haskell2010
    default-extensions: OverloadedStrings
    build-depends:    
        base ^>=4.18.3.0
        , aoc24
        , text
        , vector
        , linear
        , split
        , containers
        , mtl
EOF
  echo "Added 'executable ${DAYNAME}' to ${CABAL_FILE}"
fi

echo "Created:"
echo "  $FILENAME"
echo "  data/inputs/day${DAY}.txt"
echo "  data/tests/day${DAY}.txt"
