import yaml, joblib
from pathlib import Path
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

def train_isoforest(X):
    # Robust default pipeline
    pipe = Pipeline([
        ("scaler", StandardScaler(with_mean=True, with_std=True)),
        ("clf", IsolationForest(n_estimators=200, contamination=0.02, random_state=1337))
    ])
    pipe.fit(X)
    return pipe

def save_model(pipe, out_path: str):
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(pipe, out_path)
