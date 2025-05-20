
-- Validating credit Card Numbers
cardNumber :: Integer
cardNumber = 3333000030303333

toDigits :: Integer -> [Integer]
toDigits x
    | x <= 0    = []
    | otherwise = toDigits (x `div` 10) ++ [x `mod` 10]

toDigitsRev :: Integer -> [Integer]
toDigitsRev x 
    | x <= 0    = []
    | otherwise = x `mod` 10 : toDigitsRev (x `div` 10)

doubleEveryOther :: [Integer] -> [Integer]
doubleEveryOther x = reverse $ [if i `mod` 2 == 1 then a*2 else a | (a, i) <- zip x_rev [0..]]
    where x_rev = reverse x


sumDigits' :: Integer -> Integer
sumDigits' 0 = 0
sumDigits' x = (x `mod` 10) + sumDigits' (x `div` 10)

sumDigits :: [Integer] -> Integer
sumDigits x = sum (map sumDigits' x)

calcRemainder :: Integer -> Integer
calcRemainder x = x `div` 10

validate :: Integer -> Bool
validate x 
    | remainder == 0 = True
    | otherwise      = False
    where remainder = sum_num `mod` 10
          sum_num = sumDigits (doubleEveryOther (toDigits x))





-- The Towers of Hanoi
type Peg = String
type Move = (Peg, Peg)
hanoi :: Integer -> Peg -> Peg -> Peg -> [Move]

hanoi x p1 p2 p3
    | x == 1    = [(p1, p2)]
    | x == 2    = [(p1, p3), (p1, p2), (p3, p2)]
    | otherwise = (hanoi (x-1) p1 p3 p2) ++ [(p1, p2)] ++ (hanoi (x-1) p3 p2 p1)







main :: IO()
main = do
    print $ toDigits 1234               --  [1,2,3,4]
    print $ toDigitsRev 1234            --  [4,3,2,1]
    print $ doubleEveryOther [8,7,6,5]  -- [16,7,12,5]
    print $ doubleEveryOther [1,2,3]    -- [1, 4, 3]
    print $ sumDigits [16,7,12,5]       -- 22
    print $ validate 4012888888881881   --True
    print $ validate 4012888888881882   --False

    print $ length (hanoi 3 "a" "b" "c")    -- [("a","c"),("a","b"),("c","b")]
    print $ length (hanoi 15 "a" "b" "c")   -- 32767
