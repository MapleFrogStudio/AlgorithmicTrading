import logging
from stocks import tsx

from stocks.tsx import TSX

logging.basicConfig(
    filename="logs_clean.log",
    filemode="w",
    level=logging.INFO,
    format="{asctime} {levelname:<8} {message}",
    style='{'
)

tsx = TSX()
test_db = 'TSX_Data.sqlite'
tsx.remove_duplicates(test_db)
tsx.dispose()
