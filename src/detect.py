import pandas as pd
import numpy as np

def detect(pipe, X):
    # IsolationForest returns -1 for anomalies
    preds = pipe.predict(X)
    scores = pipe.decision_function(X)
    is_fraud = (preds == -1).astype(int)
    return is_fraud, scores
