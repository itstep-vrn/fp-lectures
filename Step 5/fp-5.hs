n = 8

f l = map (:l) . filter (flip good l) $ [1..n]

good j = not . any (\(x,y) -> y==j || y-x==j || y+x==j) . zip [1..]

t = iterate (>>= f) [[]] !! n

main = putStrLn ("amount of variants: " ++ show (length t)) >> mapM print t