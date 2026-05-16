# 📊 Rule-Based Data Processor

## 📌 Overview

Rule-Based Data Processor is a Python pipeline designed to apply complex business rules to structured datasets in a fully vectorized manner.

The project focuses on transforming raw data into enriched information through conditional logic without using explicit loops, leveraging the high performance of Pandas and NumPy.

The goal is to simulate real-world corporate data processing scenarios, where data is transformed using operational rules rather than machine learning models.

---

## 📊 Automation Preview (Before & After)

Below is a practical demonstration of how the rule engine ingests raw data and outputs a fully feature-engineered analytical matrix.

### 1. Raw Input Dataset (`mock_warehouse_raw.xlsx`)
This is the unrefined operational data generated during runtime:

| product_id | quantity | customer_type | gross_spend | category_code | expiry_date | estimated_budget |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **P001** | 5 | Gold | 1200.00 | 1 | 2025-12-01 | 1000.00 |
| **P002** | 15 | Silver | 850.00 | 2 | 2027-08-20 | 900.00 |
| **P003** | 2 | Gold | 2000.00 | 3 | 2026-02-10 | 1500.00 |
| **P004** | 50 | Bronze | 300.00 | 4 | 2026-11-15 | 400.00 |
| **P005** | 8 | Gold | 950.00 | 99 | 2028-01-10 | 1000.00 |

### 2. Processed & Enriched Output (`warehouse_performance_report.xlsx`)
The final, optimized matrix after running the vectorized business rule execution layer. All calculated fields, mapping operations, and budget penalties are generated instantly without explicit loops:

| product_id | stock_status | applied_discount | category_name | tax_rate | expiration_status | budget_penalty | final_net_spend |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **P001** | Restock | 0.2 (20%) | Food | 0.04 (4%) | Expired | 300.00 | **1298.40** |
| **P002** | In Stock | 0.0 (0%) | Electronics | 0.10 (10%) | Active | 0.00 | **935.00** |
| **P003** | Restock | 0.2 (20%) | Luxury | 0.22 (22%) | Expired | 750.00 | **2702.00** |
| **P004** | In Stock | 0.0 (0%) | Apparel | 0.10 (10%) | Active | 0.00 | **330.00** |
| **P005** | Restock | 0.0 (0%) | Other | 0.10 (10%) | Active | 0.00 | **1045.00** |

> 💡 **Business Logic Notice:** Take a look at `P001` and `P003`—since their `gross_spend` exceeded the `estimated_budget`, the engine automatically computed and injected a dynamic `budget_penalty` into the financial pipeline before rendering the `final_net_spend`.

---

## ⚙️ Key Features

### 1. Vectorized logic (np.where)

Application of conditional rules without loops:

```bash
If Quantity < 10 → "Reorder"
Otherwise → "Available"
```

---

### 2. Multi-condition combined logic

Handling complex conditions:

```bash
Customer = "Gold"
Spending > 1000
→ 20% discount
```

---

### 3. Categorical mapping (.map)

Conversion of numeric codes into text labels:

```bash
1 → Food
2 → Electronics
3 → Luxury
4 → Clothing
```

---

### 4. Dynamic VAT calculation (np.select)

Application of different tax rates based on the category:

```bash
Food → 4%
Luxury → 22%
Default → 10%
```

---

### 5. Temporal logic

Date comparison to determine status:

```bash
Expired date → "Expired"
Otherwise → "In Progress"
```

---

### 6. Cross-column calculation

Penalty calculation based on multiple columns:

```bash
Spending vs Budget
Difference multiplied by a coefficient
```

---

## 🧠 Project Logic

This project implements an approach that is:

- rule-based
- deterministic
- vectorized

Based on:

- Pandas for data manipulation
- NumPy for optimized conditional operations
- business-style logic (advanced IF/ELSE statements)

---

## 📂 Expected Inputs

The DataFrame must contain columns such as:

```bash
Quantita
Tipo_Cliente
Spesa_Lorda
Codice_Categoria
Data_Scadenza
Budget_Stimato
```

---

## 📤 Output

The final dataset includes several new columns:

- Stato_Stock
- Sconto_Applicato
- Categoria_Testo
- Aliquota_IVA
- Stato_Scadenza
- Penale_Budget
- Spesa_Netta_Finale

---

## 🚀 Usage Example

```python
df_processed = apply_business_rules(df)
```

---

## 🧩 Technologies Used

```bash
pandas → data manipulation
numpy → vectorized operations and conditional logic
```

---

## 📌 Real-World Use Cases

This type of pipeline is typically used in:

- dynamic pricing systems
- inventory management
- sales analysis
- ERP and CRM automation
- financial reporting
- rule-based decision-making systems

---

## ⚖️ Technical Specifications

- fully vectorized approach
- no explicit loops (maximum performance)
- simulated business logic
- scalable on large datasets
- modular and reusable code

---

## 🧱 Current Limitations

- requires structured datasets
- relies on standardized column names
- does not handle dirty or unnormalized inputs
- does not include schema validation

---

## 🔄 Potential Extensions

```bash
SQL database integration
Rule configuration via JSON/YAML
Dynamic rules engine
Transformation logging
REST API for remote execution
KPI monitoring dashboard
```

---

## 🎯 Project Goal

The project is designed to simulate a business rules engine capable of transforming raw data into decision-making information through explicit and deterministic rules.
