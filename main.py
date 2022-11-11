from joblib import load
import warnings
warnings.filterwarnings('ignore')

from libs.PostRequestSimulator import PostRequestSimulator
from libs.DataArray import DataArray
from libs.MakePredict import MakePredict
from libs.DialogBot import DialogBot

# load model
clf = load('models/best_model.pkl')

# hello words
DialogBot().hello()

while True:
    # submit form and get list with feature
    form = PostRequestSimulator().submit_post_request()
    body_post = PostRequestSimulator().request_to_feature_list(form)

    # create feature array, load X column names
    line_df, X_base_cols = DataArray().create_array(body_post)

    # generate double-feature for array
    final_array = DataArray().feature_engineering(line_df, X_base_cols)

    # make probability for all gift, create table with suitable gifts
    gid_pred = MakePredict().predict_gifts(clf, final_array)

    # show result
    MakePredict().show_gifts(gid_pred)