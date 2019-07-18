import joblib
import numpy as np
from difflib import SequenceMatcher
import utils

model = joblib.load('categoriser_model.pkl')
scaler = joblib.load('min_max_scaling.pkl')


features = np.array(["same_mcc_group", "merchant_name_similarity", "merchant_name_shared_words",
            "merchant_name_longest_substring", "reference_text_similarity", "reference_text_shared_words",
            "reference_text_longest_substring"])


def is_same_mcc_group(g1, g2):
    if g1 == g2:
        return 1
    else:
        return 0


def similarity(s1, s2):
    seqmatch = SequenceMatcher(None, s1, s2)
    return seqmatch.ratio()


def shared_words(s1, s2):
    return utils.num_same_words(s1, s2)


def longest_substring(s1, s2):
    return utils.longest_substring(s1, s2)


def transaction_similarities(tx, txs):
    X = []
    for transaction in txs:
        X.append([
            is_same_mcc_group(tx.mcc, transaction.mcc),
            similarity(tx.merchant_name, transaction.merchant_name),
            shared_words(tx.merchant_name, transaction.merchant_name),
            longest_substring(tx.merchant_name, transaction.merchant_name),
            similarity(tx.reference_text, transaction.reference_text),
            shared_words(tx.reference_text, transaction.reference_text),
            longest_substring(tx.reference_text, transaction.reference_text)
        ])
    scaled_X = scaler.transform(X).astype(np.float)
    return model.predict(scaled_X)