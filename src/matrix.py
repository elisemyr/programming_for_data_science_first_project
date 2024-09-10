#1.1
class Matrix:
    def __init__(self, data):
        self.data =data

    def __str__(self):
        matrix_str = ""
        for row in self.data:
            row_str=""
            for elem in row:
                row_str+=str(elem) + " "
            matrix_str +=row_str.strip()+ "\n"
        return matrix_str.strip()

    def shape(self):
        return (len(self.data), len(self.data[0]) if self.data else 0)
class DenseMatrix(Matrix):
    pass
class SparseMatrix(Matrix):
    def __init__(self, data):
        self.data =self.convert_to_sparse(data)

    def convert_to_sparse(self, data):
        sparse_data = {}
        for row, col, val in data:
            if val!=0:
                sparse_data[(row, col)] = val
        return sparse_data

    def __str__(self):
        matrix_str =""
        for(row, col), val in sorted(self.data.items()):
            matrix_str += f"({row}, {col}): {val}\n"
        return matrix_str.strip()

    def shape(self):
        max_row= max(col_row[0] for col_row in self.data.keys()) \
            if self.data \
            else 0
        max_col= max(col_row[1] for col_row in self.data.keys()) \
            if self.data \
            else 0
        return (max_row + 1, max_col + 1)


#1.2
class Matrix:
    def __init__(self, data):
        self.data = data

    def shape(self):
        rows = len(self.data)
        cols = len(next(iter(self.data), []))  # Safe way to get length of first row
        return rows, cols

class DenseMatrix(Matrix):
    def multiply_vector(self, vector):
        result = []
        for row in self.data:
            sum_result = 0
            for i, value in enumerate(row):
                sum_result += value * vector[i]
            result.append(sum_result)
        return result

    def add(self, other):
        result_data = []
        for i, row in enumerate(self.data):
            new_row = []
            for j, value in enumerate(row):
                new_row.append(value + other.data[i][j])
            result_data.append(new_row)
        return DenseMatrix(result_data)

    def norm_l1(self):
        col_sums = [0] * self.shape()[1]
        for row in self.data:
            for i, value in enumerate(row):
                col_sums[i] += abs(value)
        return max(col_sums)

class SparseMatrix(Matrix):
    def multiply_vector(self, vector):
        result = [0] * self.shape()[0]
        for (row, col), value in self.data.items():
            result[row] += value * vector[col]
        return result

    def add(self, other):
        result_data = self.data.copy()
        for (row, col), value in other.data.items():
            result_data[(row, col)] = result_data.get((row, col), 0) + value
        return SparseMatrix([(k[0], k[1], v) for k, v in result_data.items()])

    def norm_l1(self):
        col_sums = {}
        for (row, col), value in self.data.items():
            col_sums[col] = col_sums.get(col, 0) + abs(value)
        return max(col_sums.values()) if col_sums else 0

    def _convert_to_sparse(self, data):
        return dict(((row, col), val) for row, col, val in data if val != 0)

    def shape(self):
        max_row = max((key[0] for key in self.data.keys()), default=-1) + 1
        max_col = max((key[1] for key in self.data.keys()), default=-1) + 1
        return max_row, max_col


