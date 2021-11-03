from stocks.tsx import TSX
from stocks.gui import RootWin


if __name__ == "__main__":
    print("App started")

    tsx = TSX("TSX_Data.sqlite")
    root = RootWin(tsx)

    root.mainloop()