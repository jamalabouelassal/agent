import pandas as pd
import numpy as np
import re

def convert_time_to_days(text):
    if not isinstance(text, str):
        return np.nan
    text = text.lower()
    if "day" in text:
        num = re.findall(r"\d+", text)
        return int(num[0]) if num else 1
    elif "week" in text:
        num = re.findall(r"\d+", text)
        return int(num[0]) * 7 if num else 7
    elif "month" in text:
        num = re.findall(r"\d+", text)
        return int(num[0]) * 30 if num else 30
    elif "hour" in text:
        return 1
    else:
        return np.nan

def extract_num_applicants(text):
    if not isinstance(text, str):
        return np.nan
    if "less than" in text.lower():
        num = re.findall(r"\d+", text)
        return int(num[0]) if num else 5
    num = re.findall(r"\d+", text)
    return int(num[0]) if num else np.nan

def clean_jobs(df):
    df["time_posted"] = df["time_posted"].apply(convert_time_to_days)
    df["num_applicants"] = df["num_applicants"].apply(extract_num_applicants)
    mean_applicants = int(df["num_applicants"].mean(skipna=True)) if not df["num_applicants"].isna().all() else 0
    df["num_applicants"].fillna(mean_applicants, inplace=True)
    df.drop_duplicates(subset=["job_title", "company_name"], inplace=True)
    df.reset_index(drop=True, inplace=True)
    print(f"✅ Nettoyage terminé. Total final : {len(df)} offres.\n")
    return df
