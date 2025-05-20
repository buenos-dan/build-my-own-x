{-# OPTIONS_GHC -Wall #-}
module LogAnalysis where
import Log

parseMessage :: String -> LogMessage
parseMessage msg = case words msg of
    ("E" : severity : timestamp : rest) -> LogMessage (Error (read severity)) (read timestamp) (unwords rest) 
    ("I" : timestamp : rest)            -> LogMessage Info    		      (read timestamp) (unwords rest)
    ("W" : timestamp : rest) 		-> LogMessage Warning                 (read timestamp) (unwords rest)
    _                                   -> Unknown msg

parse :: String -> [LogMessage]
parse log = [ parseMessage msg | msg <- lines log ]


insert :: LogMessage -> MessageTree -> MessageTree
insert (Unknown _) tree = tree
insert logmsg Leaf = Node Leaf logmsg Leaf
insert logmsg@(LogMessage _ query _) (Node lhs cur@(LogMessage _ target _) rhs) 
    | query <= target = Node (insert logmsg lhs) cur rhs
    | otherwise       = Node lhs cur (insert logmsg rhs)

build :: [LogMessage] -> MessageTree
build [] = Leaf
build (logmsg : rest) = insert logmsg (build rest)

inOrder :: MessageTree -> [LogMessage]
inOrder Leaf = []
inOrder (Node lhs  logmsg rhs) = (inOrder lhs) ++ [logmsg] ++ (inOrder rhs)

whatWentWrong :: [LogMessage] -> [String]
whatWentWrong x = [msg | logmsg@(LogMessage (Error s) _ msg) <- (inOrder (build x)), s >= 50]

main :: IO()
main = do
    print $ parseMessage "E 2 562 help help"
    print $ parseMessage "I 29 la la la"
    print $ parseMessage "This is not in the right format"

    messages <- testParse parse 10 "error.log"
    print messages

    putStrLn ""
    messages <- testWhatWentWrong parse whatWentWrong "error.log"
    print messages

