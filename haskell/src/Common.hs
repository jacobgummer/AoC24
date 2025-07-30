module Common
  ( readInputText,
    readInputLines,
  )
where

import qualified Data.Text as T
import qualified Data.Text.IO as TIO

-- Read whole file as Text
readInputText :: FilePath -> IO T.Text
readInputText = TIO.readFile

-- Read file as [Text] lines
readInputLines :: FilePath -> IO [T.Text]
readInputLines path = T.lines <$> TIO.readFile path
