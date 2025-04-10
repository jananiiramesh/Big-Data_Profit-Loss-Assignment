# Big-Data_Profit-Loss-Assignment (HDFS based)
# 🏬 Task 1: Store Profit and Loss (HDFS MapReduce)

## 📖 Story Background

You are provided data from a **retail chain in India** operating in multiple cities. Each store in the chain sells a unique combination of product categories — based on local consumer preferences. Your goal is to determine how many stores in each city are profitable and how many are operating at a loss.

Profitability is determined **only based on the top-selling product categories** of each store, and only if **sales data is available** for those categories.

---

## 🎯 Objective

For each city:
- ✅ Count the number of **profitable stores** (net profit > 0)
- ❌ Count the number of **loss-making stores** (net profit ≤ 0)

---

## 📌 Key Considerations

- Each store lists its top-selling `categories`.
- Sales data is present under `sales_data` for some categories (may include categories outside the top-selling ones).
- Only categories **present in both `categories` and `sales_data`** are used for net profit calculation.
- If no such category has sales data → the store is **excluded**.
- Net Profit for a store = Sum over each valid category:  
  `revenue - cogs`
- Store is **profitable** if net profit > 0, otherwise it’s **loss-making**.

---

## 🧾 Sample Input (`input.json`)

Each line is a JSON object representing a store.

```json
{"city": "Bangalore", "store_id": "ST01293", "categories": ["Electronics", "Groceries"], "sales_data": {"Electronics": {"revenue": 600000, "cogs": 500000}, "Groceries": {"revenue": 250000, "cogs": 270000}}}
{"city": "Chennai", "store_id": "ST04567", "categories": ["Pharmacy and Health", "Kitchen", "Toys and Stationery"], "sales_data": {"Kitchen": {"revenue": 800000, "cogs": 900000}, "Toys and Stationery": {"revenue": 300000, "cogs": 450000}, "Pharmacy and Health": {"revenue": 450000, "cogs": 470000}}}
{"city": "Mumbai", "store_id": "ST05432", "categories": ["Books and Magazines", "Pharmacy and Health"], "sales_data": {"Books and Magazines": {"revenue": 200000, "cogs": 150000}, "Pharmacy and Health": {"revenue": 350000, "cogs": 300000}}}
{"city": "Mumbai", "store_id": "ST08345", "categories": ["Groceries"], "sales_data": {"Groceries": {"revenue": 700000, "cogs": 650000}}}
{"city": "Chennai", "store_id": "ST06789", "categories": ["Home Decor", "Apparel"], "sales_data": {"Apparel": {"revenue": 850000, "cogs": 800000}, "Home Decor": {"revenue": 500000, "cogs": 450000}}}
{"city": "Bangalore", "store_id": "ST09874", "categories": ["Apparel"], "sales_data": {"Apparel": {"revenue": 620000, "cogs": 600000}}}

```
## Expected Output

```json
{"city": "Bangalore", "profit_stores": 2, "loss_stores": 0}
{"city": "Chennai", "profit_stores": 1, "loss_stores": 1}
{"city": "Mumbai", "profit_stores": 2, "loss_stores": 0}
