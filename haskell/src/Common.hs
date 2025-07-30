module Common
  ( readInputText,
    readInputLines,
    parseInt,
  )
where

import qualified Data.Text as T
import qualified Data.Text.IO as TIO
import qualified Data.Text.Read as TR

-- Read whole file as Text
readInputText :: FilePath -> IO T.Text
readInputText = TIO.readFile

-- Read file as [Text] lines
readInputLines :: FilePath -> IO [T.Text]
readInputLines path = T.lines <$> TIO.readFile path

parseInt :: T.Text -> Int
parseInt txt = case TR.decimal txt of
  Right (n, rest) | T.null rest -> n
  _ -> error $ "Invalid integer: " ++ T.unpack txt
