import pandas as pd

def deduplicate_va_data(df: pd.DataFrame) -> pd.DataFrame:
    conditions = [
        (df['Plugin Name'].str.startswith("Microsoft Edge")) & 
        (df['Plugin Name'].str.contains("Vulnerabilities|Vulnerability|CVE", case=False, na=False)),
        
        (df['Plugin Name'].str.startswith("RHEL")) & 
        (df['Plugin Name'].str.contains("RHSA", case=False, na=False)),
        
        (df['Plugin Name'].str.startswith("KB")) & 
        (df['Plugin Name'].str.contains("Security Update", case=False, na=False)),
        
        (df['Plugin Name'].str.startswith("Security Updates")),
        
        (df['Plugin Name'].str.startswith("VMware Tools")) & 
        (df['Plugin Name'].str.contains("Bypass", case=False, na=False)),
        
        (df['Plugin Name'].str.startswith("Ubuntu"))
    ]

    dedup_df_list = []
    non_dedup_df = df.copy()

    for condition in conditions:
        matching_rows = df[condition]
        dedup_df = matching_rows.drop_duplicates(subset=['Site', 'IP Address'])
        dedup_df_list.append(dedup_df)
        non_dedup_df = non_dedup_df[~((df['Site'].isin(dedup_df['Site'])) & 
                                     (df['IP Address'].isin(dedup_df['IP Address'])) & condition)]

    combined_dedup_df = pd.concat(dedup_df_list + [non_dedup_df], ignore_index=True)
    return combined_dedup_df
