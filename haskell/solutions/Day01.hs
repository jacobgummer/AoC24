{-# LANGUAGE OverloadedStrings #-}

import Common
import qualified Data.Text as T
import System.Environment (getArgs)

main :: IO ()
main = do
  args <- getArgs
  case length args of
    1 -> do
      input <- readInputLines "data/inputs/day01.txt"
      case args of
        ["1"] -> print $ part1 input
        ["2"] -> print $ part2 input
        _ -> putStrLn "Usage: day01 -- 1|2 [-t]"
    2 -> do
      input <- readInputLines "data/tests/day01.txt"
      case args of
        ["1", "-t"] -> print $ part1 input
        ["2", "-t"] -> print $ part2 input
        _ -> putStrLn "Usage: day01 -- 1|2 [-t]"
    _ -> putStrLn "Usage: day01 -- 1|2 [-t]"

part1 :: [T.Text] -> T.Text
part1 = head

part2 :: [T.Text] -> Int
part2 = T.length . T.concat
