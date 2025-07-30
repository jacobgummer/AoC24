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
        ["t1"] -> print $ part1 input
        ["t2"] -> print $ part2 input
        _ -> putStrLn "Usage: ./day 01 t1|t2 [-t]"
    2 -> do
      input <- readInputLines "data/tests/day01.txt"
      case args of
        ["t1", "-t"] -> print $ part1 input
        ["t2", "-t"] -> print $ part2 input
        _ -> putStrLn "Usage: ./day 01 t1|t2 [-t]"
    _ -> putStrLn "Usage: ./day 01 t1|t2 [-t]"

part1 :: [T.Text] -> Int
part1 input = undefined

part2 :: [T.Text] -> Int
part2 input = undefined
