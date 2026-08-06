import can
import pandas as pd


def blf_to_dataframe(blf_file):
    """
    Convert Vector .blf CAN log to pandas DataFrame
    """

    records = []

    with can.BLFReader(blf_file) as log:
        for msg in log:

            # Convert bytes to hex string
            data_str = " ".join(f"{b:02X}" for b in msg.data)

            records.append({
                "Time": round(msg.timestamp, 6),
                "ID": f"0x{msg.arbitration_id:X}",
                "DLC": msg.dlc,
                "Data": data_str,
                "Channel": msg.channel,
                "IsExtended": msg.is_extended_id
            })

    df = pd.DataFrame(records)

    return df