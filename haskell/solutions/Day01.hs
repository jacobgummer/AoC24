import Common
import Data.List (sort)
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

parseLine :: T.Text -> [Int]
parseLine = map parseInt . T.words

part1 :: [T.Text] -> Int
part1 input =
  let parsed = parseLine <$> input
      left = head <$> parsed
      right = (!! 1) <$> parsed
      diffs = abs <$> zipWith (-) (sort left) (sort right)
   in sum diffs

count :: (Eq a) => a -> [a] -> Int
count x = length . filter (== x)

part2 :: [T.Text] -> Int
part2 input =
  let parsed = parseLine <$> input
      left = head <$> parsed
      right = (!! 1) <$> parsed
      similarities = (\x -> x * count x right) <$> left
   in sum similarities
