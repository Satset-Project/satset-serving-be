import pandas as pd
from typing import Any
import numpy as np

def replace_nan_with_null(data: Any) -> Any:
    if isinstance(data, dict):
        return {key: replace_nan_with_null(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [replace_nan_with_null(item) for item in data]
    elif isinstance(data, float) and np.isnan(data):
        return None
    else:
        return data