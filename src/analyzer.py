import pandas as pd

def detect_abnormal_frames(df):
    abnormalities = []

    # Invalid payloads
    invalid = df[df["Data"].astype("string").str.startswith("7F", na=False)]

    if not invalid.empty:
        invalid = invalid.copy()
        invalid["Issue"] = "Invalid Payload"
        abnormalities.append(invalid)

    # Timing analysis
    df = df.copy()
    df["Gap"] = df["Time"].diff()

    timeout = df[df["Gap"] > 0.2]

    if not timeout.empty:
        timeout = timeout.copy()
        timeout["Issue"] = "Message Timeout"
        abnormalities.append(timeout)

    if abnormalities:
        result = pd.concat(abnormalities, ignore_index=True)

        # Keep only unique values in the Data column
        result = result.drop_duplicates(subset=["Data"], keep="first")

        return result

    return pd.DataFrame()


def summarize(df):
    return {
        "Total Frames": len(df),
        "Unique IDs": df["ID"].nunique(),
        "Channels": df["Channel"].nunique()
    }