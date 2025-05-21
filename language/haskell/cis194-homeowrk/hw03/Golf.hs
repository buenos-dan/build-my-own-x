module Golf where
import Data.Char (digitToInt, intToDigit)
import Data.List (transpose)

skips :: [a] -> [[a]]
skips xs = [everyNth n xs | n <- [1..length xs]]
  where
    everyNth n ys = [y | (i, y) <- zip [1..] ys, i `mod` n == 0]


localMaxima :: [Integer] -> [Integer]
localMaxima xs = [b | (a, b, c) <- filter isMiddleBiggest (zip3 (999 : init xs) xs (tail xs ++ [999]))]
    where isMiddleBiggest (a, b, c) = b > a && b > c

-- " * * \n==========\n0123456789\n"

histogram :: [Integer] -> String
histogram xs = let slots = [ constructSlot num xs ++ "=" ++ [intToDigit (fromIntegral num)] | num <- [0..9]]
    in unlines (transpose slots)

constructSlot :: Integer -> [Integer] -> String
constructSlot n [] = []
constructSlot n (x:xs) | x == n    = (constructSlot n xs) ++ "*"
                       | otherwise = " " ++ (constructSlot n xs)

main :: IO()
main = do
    print $ skips "ABCD"
    print $ skips "hello!"

    print $ localMaxima [2,9,5,6,1] == [9,6]
    print $ localMaxima [2,3,4,1,5] == [4]
    print $ localMaxima [1,2,3,4,5] == []

    print $ [0..9]

    putStrLn ""
    putStr (histogram [3, 5])
    putStrLn ""
    putStr (histogram [1,1,1,5])
    putStrLn ""
    putStr (histogram [1,4,5,4,6,6,3,4,2,4,9])
