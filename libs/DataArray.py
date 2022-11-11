import numpy as np
import pandas as pd

class DataArray():
    def __init__(self):
        pass

    # create feature array
    def create_array(self, body_post):
        # load column names
        with open('data/X_base_cols.txt') as file:
            X_base_cols = file.read()
        # text to list
        X_base_cols = eval(X_base_cols)
        # create dataframe template
        line_df = pd.DataFrame(np.zeros((1, 28)), columns=X_base_cols)
        # set 1 for names from form
        for i in body_post:
            line_df[i] = 1

        return line_df, X_base_cols

    # generate double-feature
    def feature_engineering(self, line_df, X_base_cols):
        # load double-feature names
        with open('data/double_list_clear.txt') as file:
            generate_features = file.read()
        # text to list
        generate_features = eval(generate_features)
        # generate feauters
        for i in generate_features:
            line_df[i] = 0

        for i in range(len(line_df)):
            for dd in generate_features:  # list with double-feature
                counter = 0
                for n in X_base_cols:  # list with base feauter
                    if n in dd:
                        if line_df[n][i] == 1:
                            counter += 1
                if counter == 2:
                    line_df[dd][i] = 1

        return line_df