from analyzer import *
from ai_helper import *
import streamlit as st
from blf_parser import blf_to_dataframe
from datetime import datetime
from pathlib import Path

st.set_page_config(page_title="AI Automotive Testing Assistant", layout="wide")

st.title("🚗 AI Automotive Testing Assistant")
st.write("Upload a Vector **.blf** CAN log file for analysis.")

# Upload BLF file
uploaded_file = st.file_uploader(
    "Choose a .blf file",
    type=["blf"]
)

if uploaded_file is not None:

    try:
        # Parse BLF directly
        df = blf_to_dataframe(uploaded_file)

        # Save CSV automatically
        csv_data = df.to_csv(index=False).encode("utf-8")

        reports_dir = Path(__file__).resolve().parents[1] / "reports"
        reports_dir.mkdir(parents=True, exist_ok=True)
        converted_report_file = reports_dir / "converted_can_log.csv"
        df.to_csv(converted_report_file, index=False)

        st.success("✅ BLF file parsed successfully")

        # Summary metrics
        st.subheader("📊 Summary")

        summary = summarize(df)

        col1, col2, col3 = st.columns(3)

        col1.metric("Total Frames", summary["Total Frames"])
        col2.metric("Unique IDs", summary["Unique IDs"])
        col3.metric("Channels", summary["Channels"])

        # Raw log view
        st.subheader("📄 Parsed CAN Log")
        st.dataframe(df.head(100), use_container_width=True)

        # Download converted CSV
        st.download_button(
            label="⬇️ Download Converted CSV",
            data=csv_data,
            file_name="converted_can_log.csv",
            mime="text/csv"
        )

        # Abnormal frame detection
        st.subheader("⚠️ Abnormal Frame Analysis")

        abnormal = detect_abnormal_frames(df)

        if not abnormal.empty:
            st.error(f"Detected {len(abnormal)} abnormal events")
            st.dataframe(abnormal, use_container_width=True)

            abnormal_csv_data = abnormal.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="⬇️ Download Abnormal Frames CSV",
                data=abnormal_csv_data,
                file_name="abnormal_frames.csv",
                mime="text/csv"
            )

            report_file = reports_dir / f"abnormal_frames_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
            abnormal.to_csv(report_file, index=False)
            st.info(f"Saved abnormal frames CSV to reports: {report_file.name}")

            st.subheader("🤖 AI-Style Engineering Analysis")

            with st.spinner("Analyzing abnormal CAN frames with AI..."):
                ai_result = explain_failure(abnormal.to_string())
                st.markdown(ai_result)

            ai_report_file = reports_dir / f"ai_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            ai_report_file.write_text(ai_result, encoding="utf-8")
            st.info(f"Saved AI analysis report to reports: {ai_report_file.name}")

            st.download_button(
                label="⬇️ Download AI Analysis TXT",
                data=ai_result.encode("utf-8"),
                file_name="ai_analysis.txt",
                mime="text/plain"
            )

        else:
            st.success("✅ No abnormal CAN frames detected")

    except Exception as e:
        st.exception(e)

else:
    st.info("Upload a Vector .blf file to begin analysis.")