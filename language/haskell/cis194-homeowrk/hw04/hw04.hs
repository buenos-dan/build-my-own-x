fun1 :: [Integer] -> Integer
fun1 [] = 1
fun1 (x:xs)
    | even x = (x - 2) * fun1 xs
    | otherwise = fun1 xs

fun1' :: [Integer] -> Integer
fun1' xs = foldr (\x y -> if even x then (x-2)*y else y) 1 xs


fun2 :: Integer -> Integer
fun2 1 = 0
fun2 n | even n = n + fun2 (n `div` 2)
       | otherwise = fun2 (3 * n + 1)

fun2' :: Integer -> Integer
fun2' = sum . filter even . takeWhile (/= 1) . iterate collatz
  where
    collatz n
      | even n    = n `div` 2
      | otherwise = 3 * n + 1



data Tree a = Leaf
            | Node Integer (Tree a) a (Tree a)
            deriving (Show, Eq)

depth :: (Tree a) -> Integer
depth Leaf = -1
depth (Node d _ _ _) = d


-- Create a node with the correct depth
makeNode :: Tree a -> a -> Tree a -> Tree a
makeNode l x r = Node h l x r
  where h = 1 + max (depth l) (depth r)

foldTree :: [a] -> Tree a
foldTree xs = foldr (buildTree) Leaf xs
    where buildTree x Leaf = (Node 0 Leaf x Leaf)
          buildTree x (Node d lhs n rhs)
              | depth lhs <= depth rhs  = makeNode (buildTree n lhs) x rhs
              | depth lhs > depth rhs  = makeNode lhs x (buildTree n rhs)


xor :: [Bool] -> Bool
xor xs = foldr (flip) False xs
    where flip input state = if input then not state else state

map' :: (a -> b) -> [a] -> [b]
map' f = foldr (\x acc -> f x : acc) []

{-
cartProd :: [Integer] -> [Integer] -> [(Integer, Integer)]
cartProd xs ys = [(x,y) | x <- xs, y <- ys, x <= y]
-}

-- generate all the odd prime numbers up to 2n + 2.
sieveSundaram :: Integer -> [Integer]
sieveSundaram n = let ys = [(i+j+2*i*j) | i <- [1..n], j <- [1..n], i <= j]
    in map (+1) . map (*2) $ filter (`notElem` ys) [1..n]


main :: IO()
main = do
    putStrLn "Test fun1:"
    print $ fun1 [6, 8, 11, 15]  == fun1' [6, 8, 11, 15]
    print $ fun1 [4, 21, 38]     == fun1' [4, 21, 38]

    putStrLn "Test fun2:"
    print $ fun2 48  == fun2' 48
    print $ fun2 32  == fun2' 32
    print $ fun2 121 == fun2' 121
    print $ fun2 78 == fun2' 78

    putStrLn "Test foldTree:"
    print $ foldTree "ABCDEFGHIJ"

    putStrLn "Test more folds:"
    print $ xor [False, True, False] == True
    print $ xor [False, True, False, False, True] == False

    print $ map (+2) [1, 2, 3] == map' (+2) [1, 2, 3]

    putStrLn "Test sieveSundaram:"
    print $ sieveSundaram 10
    print $ sieveSundaram 49
