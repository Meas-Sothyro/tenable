import pandas as pd
import shutil, tempfile, os
from fastapi import UploadFile
from services.deduplication import deduplicate_va_data
from services.excel_processing import save_to_excel
from utils.plugin_output import extract_plugin_output_info

async def process_files(files: list[UploadFile], output_filename: str):
    combined_va_df = pd.DataFrame()
    combined_hardening_df = pd.DataFrame()

    for file in files:
        df = await read_csv_file(file)
        if 'VA' in file.filename:
            combined_va_df = process_va_file(df, file, combined_va_df)
        elif 'Hardening' in file.filename:
            combined_hardening_df = process_hardening_file(df, file, combined_hardening_df)

    # Save to Excel
    save_to_excel(combined_va_df, combined_hardening_df, output_filename)

async def read_csv_file(file: UploadFile) -> pd.DataFrame:
    temp_dir = tempfile.mkdtemp()
    temp_file_path = os.path.join(temp_dir, file.filename)
    with open(temp_file_path, 'wb') as temp_file:
        shutil.copyfileobj(file.file, temp_file)
    df = pd.read_csv(temp_file_path)
    os.remove(temp_file_path)
    return df

def process_va_file(df: pd.DataFrame, file: UploadFile, combined_va_df: pd.DataFrame) -> pd.DataFrame:
    site_value = "DC" if "DC" in file.filename else "DR"
    df.insert(df.columns.get_loc('IP Address') + 1, "Site", site_value)
    combined_va_df = pd.concat([combined_va_df, df], ignore_index=True)
    return deduplicate_va_data(combined_va_df)

def process_hardening_file(df: pd.DataFrame, file: UploadFile, combined_hardening_df: pd.DataFrame) -> pd.DataFrame:
    df['Severity'] = df.apply(lambda row: 'PASSED' if 'Result: PASSED' in row['Plugin Output'] 
                              else ('FAILED' if 'Result: FAILED' in row['Plugin Output'] 
                                    else ('Manual Review' if 'Result: WARNING' in row['Plugin Output'] 
                                          else row['Severity'])), axis=1)
    site = 'DC' if 'DC' in file.filename else 'DR'
    df.insert(2, 'Site', site)
    plugin_output_data = df['Plugin Output'].apply(extract_plugin_output_info)
    plugin_output_df = pd.DataFrame(plugin_output_data.tolist())
    return pd.concat([combined_hardening_df, pd.concat([df, plugin_output_df], axis=1)], ignore_index=True)
