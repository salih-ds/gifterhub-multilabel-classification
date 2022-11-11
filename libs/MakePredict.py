import pandas as pd

class MakePredict():
    def __init__(self):
        pass

    def predict_gifts(self, clf, array, threshold=0.5):
        # make predict
        pred = clf.predict_proba(array)

        # create table with gifts and predict for all
        # load data about active gifts
        gid_pred = pd.read_csv('data/active_gifts_proba.csv')
        # create column with predict probability
        gid_pred['proba'] = pred[0]

        # sort in descending order of probability of success
        gid_pred = gid_pred.sort_values('proba', ascending=False)

        # clear gifts with probability below threshold
        gid_pred = gid_pred[gid_pred['proba'] >= threshold]
        # reset index
        gid_pred.reset_index(drop=True, inplace=True)

        return gid_pred


    def show_gifts(self, gid_pred):
        gifts_found = len(gid_pred)
        print(f'Найдено подарков: {gifts_found}')
        print('---' * 15)

        for i in range(gifts_found):
            print(f'{gid_pred["title"][i]} - {round(gid_pred["proba"][i] * 100)}%')

        print('---' * 15)