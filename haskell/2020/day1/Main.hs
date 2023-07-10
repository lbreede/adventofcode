import System.IO

main :: IO ()
main = do
  contents <- readFile "example.txt"
  let linesOfFile = lines contents
      integers = map read linesOfFile :: [Int]
      pairs = [(x, y) | x <- integers, y <- integers, x /= y, x + y == 2020]
      result = case pairs of
        [(x, y)] -> x * y
        _ -> error "No two entries sum to 2020"
  print result