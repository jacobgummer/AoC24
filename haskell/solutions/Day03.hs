import Common
import qualified Data.Text as T
import System.Environment (getArgs)
import Text.Regex.TDFA
import Text.Regex.TDFA.Text ()

main :: IO ()
main = do
  args <- getArgs
  case length args of
    1 -> do
      input <- readInputLines "data/inputs/day03.txt"
      case args of
        ["p1"] -> print $ part1 input
        ["p2"] -> print $ part2 input
        _ -> putStrLn "Usage: ./day 03 p1|p2 [-t]"
    2 -> do
      input <- readInputLines "data/tests/day03.txt"
      case args of
        ["p1", "-t"] -> print $ part1 input
        ["p2", "-t"] -> print $ part2 input
        _ -> putStrLn "Usage: ./day 03 p1|p2 [-t]"
    _ -> putStrLn "Usage: ./day 03 p1|p2 [-t]"

regex :: T.Text
regex = "mul\\([[:digit:]]+,[[:digit:]]+\\)"

extractNumbers :: T.Text -> [Int]
extractNumbers t =
  map (read . T.unpack) $
    T.splitOn "," $
      T.dropEnd 1 $
        T.drop 4 t

part1 :: [T.Text] -> Int
part1 input =
  let matches = map (\line -> getAllTextMatches (line =~ regex :: AllTextMatches [] T.Text)) input
      nums = extractNumbers <$> concat matches
   in sum $ product <$> nums

regex2 :: T.Text
regex2 = "don't\\(\\)|mul\\([0-9]+,[0-9]+\\)|do\\(\\)"

part2 :: [T.Text] -> Int
part2 input =
  let matches = concatMap (\line -> getAllTextMatches (line =~ regex2 :: AllTextMatches [] T.Text)) input
      res = fst $ foldl goDO (0, True) matches
   in res
  where
    goDO (acc, isEnabled) m =
      case m of
        "do()" -> (acc, True)
        "don't()" -> (acc, False)
        _ ->
          if isEnabled
            then (acc + product (extractNumbers m), True)
            else (acc, False)
