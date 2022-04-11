import numpy as np

startingSudoku = """
                    024007000
                    600000000
                    003680415
                    431005000
                    500000032
                    790000060
                    209710800
                    040093000
                    310004750
                """

sudoku = np.array([[int(i) for i in line] for line in startingSudoku.split()])