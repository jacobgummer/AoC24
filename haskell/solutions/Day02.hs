import Common
import qualified Data.Text as T
import System.Environment (getArgs)

main :: IO ()
main = do
  args <- getArgs
  case length args of
    1 -> do
      input <- readInputLines "data/inputs/day02.txt"
      case args of
        ["p1"] -> print $ part1 input
        ["p2"] -> print $ part2 input
        _ -> putStrLn "Usage: ./day 02 p1|p2 [-t]"
    2 -> do
      input <- readInputLines "data/tests/day02.txt"
      case args of
        ["p1", "-t"] -> print $ part1 input
        ["p2", "-t"] -> print $ part2 input
        _ -> putStrLn "Usage: ./day 02 p1|p2 [-t]"
    _ -> putStrLn "Usage: ./day 02 p1|p2 [-t]"

parseLine :: T.Text -> [Int]
parseLine = map parseInt . T.words

part1 :: [T.Text] -> Int
part1 input =
  let parsed = parseLine <$> input
      diffs = (\r -> zipWith (-) (tail r) r) <$> parsed
   in sum $ checkReport <$> diffs
  where
    checkReport :: [Int] -> Int
    checkReport r =
      if all (\lvl -> 1 <= lvl && lvl <= 3) r
        || all (\lvl -> -3 <= lvl && lvl <= -1) r
        then 1
        else 0

removeAt :: Int -> [a] -> [a]
removeAt i xs = take i xs ++ drop (i + 1) xs

boolToInt :: Bool -> Int
boolToInt True = 1
boolToInt False = 0

part2 :: [T.Text] -> Int
part2 input =
  let parsed = parseLine <$> input
      checked = boolToInt . checkIfTolerated <$> parsed
   in sum checked
  where
    checkIfTolerated :: [Int] -> Bool
    checkIfTolerated r =
      any (checkReport . diffs . (`removeAt` r)) [0 .. length r - 1]

    diffs :: [Int] -> [Int]
    diffs xs = zipWith (-) (tail xs) xs

    checkReport :: [Int] -> Bool
    checkReport r =
      all
        (\lvl -> 1 <= lvl && lvl <= 3)
        r
        || all (\lvl -> -3 <= lvl && lvl <= -1) r
