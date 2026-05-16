
import os
import pandas as pd
import numpy as np

"""
RULE-BASED DATA PROCESSOR - PRO VERSION
---------------------------------------
Demonstrated Skills:
1. Vectorized Logic Selection: High-performance use of np.select and np.where to eliminate slow for-loops.
2. Multi-Condition Masking: Advanced execution of combined boolean conditional statements.
3. Categorical Mapping: Highly efficient database-style translation using dictionaries and .map().
4. Datetime Math: Real-time temporal delta calculations relative to the current timestamp.
5. Cross-Column Arithmetic: Conditional mathematical operations computed across separate columns.
"""

def apply_business_rules(df, fixed_coefficient=1.5):
    """
    Applies 6 complex business rules to the dataset using highly optimized, vectorized operations.
    Enriches the original DataFrame by appending the newly calculated columns.
    """
    # Create a deep copy to prevent the classic "SettingWithCopyWarning" in Pandas
    processed_df = df.copy()
    
    # --- RULE 1: Base Threshold (np.where) ---
    # If quantity < 10 -> "Restock", otherwise "In Stock"
    processed_df['stock_status'] = np.where(processed_df['quantity'] < 10, "Restock", "In Stock")
    
    # --- RULE 2: Combined Logical Masking ---
    # If customer_type is "Gold" AND gross_spend > 1000 -> 20% discount, otherwise 0%
    gold_condition = (processed_df['customer_type'] == "Gold") & (processed_df['gross_spend'] > 1000)
    processed_df['applied_discount'] = np.where(gold_condition, 0.20, 0.0)
    
    # --- RULE 3: Categorical Mapping (.map) ---
    # Translates numeric database codes into clean human-readable text categories
    category_map = {
        1: "Food",
        2: "Electronics",
        3: "Luxury",
        4: "Apparel"
    }
    processed_df['category_name'] = processed_df['category_code'].map(category_map).fillna("Other")
    
    # --- RULE 4: Differentiated Tax Calculation (np.select) ---
    # If category_name is "Food" -> 4%, if "Luxury" -> 22%, fallback standard rate -> 10%
    tax_conditions = [
        processed_df['category_name'] == "Food",
        processed_df['category_name'] == "Luxury"
    ]
    tax_choices = [0.04, 0.22]
    processed_df['tax_rate'] = np.select(tax_conditions, tax_choices, default=0.10)
    
    # --- RULE 5: Temporal/Datetime Rule ---
    # Normalizes current time and compares it directly with expiration dates
    # If expiry_date < today -> "Expired", otherwise "Active"
    today = pd.Timestamp.now().normalize()
    expiration_dates = pd.to_datetime(processed_df['expiry_date'])
    processed_df['expiration_status'] = np.where(expiration_dates < today, "Expired", "Active")
    
    # --- RULE 6: Cross-Column Financial Arithmetic ---
    # If gross_spend exceeds the estimated_budget, calculate a penalty fee:
    # Penalty = (gross_spend - estimated_budget) * fixed_coefficient. Otherwise, 0.0
    spending_delta = processed_df['gross_spend'] - processed_df['estimated_budget']
    processed_df['budget_penalty'] = np.where(
        processed_df['gross_spend'] > processed_df['estimated_budget'],
        spending_delta * fixed_coefficient,
        0.0
    )
    
    # --- FINAL SYNTHESIS LOGIC (Consolidating previous metrics) ---
    # Computes the net total price factoring in the dynamic discount, tax rate, and penalty fee
    discounted_spend = processed_df['gross_spend'] * (1 - processed_df['applied_discount'])
    processed_df['final_net_spend'] = (discounted_spend * (1 + processed_df['tax_rate'])) + processed_df['budget_penalty']
    
    # Clean up financial floats by rounding to standard currency decimals
    processed_df['budget_penalty'] = processed_df['budget_penalty'].round(2)
    processed_df['final_net_spend'] = processed_df['final_net_spend'].round(2)
    
    return processed_df


# --- DYNAMIC DEMO USE CASE EXECUTION & EXPORT LAYER ---
if __name__ == "__main__":
    print("=== STARTING RULE ENGINE ISOLATED UNIT TESTING & EXPORT ===\n")

    input_file = "mock_warehouse_raw.xlsx"

    # 1. Verification of the simulated environment file
    if not os.path.exists(input_file):
        raise FileNotFoundError(
            f"[ERROR] Target data source '{input_file}' not found. Please run 'test.py' first to initialize the dataset."
        )

    # 2. Ingest the raw data created by test.py
    print(f"[INGESTION] Reading production dataset: '{input_file}'")
    df_test = pd.read_excel(input_file)
    
    # 3. Running evaluation through the rule engine
    print("[PROCESSING] Driving dataset through high-performance vectorized rules...")
    df_result = apply_business_rules(df_test, fixed_coefficient=1.5)
    
    # 4. Export the complete enriched dataset into ONE single file
    output_file = "warehouse_performance_report.xlsx"
    df_result.to_excel(output_file, index=False)
    print(f"[EXPORT] Complete analytical matrix successfully saved to: '{output_file}'")

    print(f"\n=== ENGINE EVALUATION PIPELINE SUCCEEDED: SINGLE FILE '{output_file}' GENERATED ===")
