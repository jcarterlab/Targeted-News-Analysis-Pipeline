import pandas as pd
from news_monitoring_pipeline.identify_risk_headlines import number_headlines


def test_number_headlines_handles_none_or_empty():
    df = pd.DataFrame({'headline': ['Valid', None, '']})
    result = number_headlines(df)

    assert result == ['1. Valid', '2. ', '3. ']