import pandas as pd


class FileReader:
    query = []

    def extract_query(self, file_path):
        try:
            df = pd.read_json(file_path)

            for i in range(0, len(df.values)):
                self.query.append(df.values[i][0])  # Append only the first element of each array
            return self.query

        except Exception as e:
            return e

    def __init__(self, file_path):
        self.query = self.extract_query(file_path)
