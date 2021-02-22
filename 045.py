import datetime
import Utilities

start_time = datetime.datetime.now()

max_i = 10000000000
a_tri = Utilities.TriangularNumbers(max_i)
a_pent = Utilities.PentagonalNumbers(max_i)
a_hex = Utilities.HexagonalNumbers(max_i)
a = (a_tri.intersection(a_pent)).intersection(a_hex)
print(a)

stop_time = datetime.datetime.now()
print(stop_time - start_time)
