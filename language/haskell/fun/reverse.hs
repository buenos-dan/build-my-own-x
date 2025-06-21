










main :: IO()
main = do
    line <- getLine
    if null line
        then return()
        else do
            print $ unwords (reverse (words line))
            main
