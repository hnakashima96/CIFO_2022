import numpy as np

startingSudoku = """
                    530070000
                    600195000
                    098000060
                    800060003
                    400803001
                    700020006
                    060000280
                    000419005
                    000080079
                """

grid = np.array([[int(i) for i in line] for line in startingSudoku.split()])
