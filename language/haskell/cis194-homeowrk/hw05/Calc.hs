
import ExprT
import Parser (parseExp)

lit :: Integer -> ExprT
lit = Lit

add :: ExprT -> ExprT -> ExprT
add = Add

mul :: ExprT -> ExprT -> ExprT
mul = Mul

eval :: ExprT -> Integer
eval (Lit x  ) = x
eval (Add x y) = eval x + eval y
eval (Mul x y) = eval x * eval y

evalStr :: String -> Maybe Integer
evalStr = parseExp id (+) (*)


main :: IO()
main = do
    print $ eval (Mul (Add (Lit 2) (Lit 3)) (Lit 4))    -- 20
    print $ parseExp Lit Add Mul "(2+3)*4"
    print $ evalStr "(2+3)*4"
    print $ mul (add (lit 2) (lit 3)) (lit 4)
    




