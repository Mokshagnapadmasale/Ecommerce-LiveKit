from fastmcp import FastMCP
import pandas as pd

products = pd.read_csv(r"C:\Users\moksh\Desktop\LiveKit-Ecommerce\MockData\products.csv")
orders = pd.read_csv(r"C:\Users\moksh\Desktop\LiveKit-Ecommerce\MockData\orders.csv")
delivery = pd.read_csv(r"C:\Users\moksh\Desktop\LiveKit-Ecommerce\MockData\delivery.csv")
returns = pd.read_csv(r"C:\Users\moksh\Desktop\LiveKit-Ecommerce\MockData\returns.csv")

products["product_id"] = products["product_id"].astype(str).str.strip().str.upper()
orders["order_id"] = orders["order_id"].astype(str).str.strip().str.upper()
orders["customer_id"] = orders["customer_id"].astype(str).str.strip().str.upper()
delivery["tracking_number"] = delivery["tracking_number"].astype(str).str.strip().str.upper()
returns["order_id"] = returns["order_id"].astype(str).str.strip().str.upper()

STORE_POLICIES = {
    "delivery_time": "Orders are delivered within 3 to 5 business days.",
    "return_window": "You can return any eligible product within 30 days of delivery.",
    "refund_method": "Refunds are issued back to the original payment method.",
    "return_conditions": "Items must be unused and in their original packaging.",
    "exchange_policy": "Exchanges are allowed only for damaged or defective products."
}

mcp = FastMCP(name="Ecommerce-mcp")

@mcp.tool()
def get_product(product_id: str):
    pid = product_id.strip().upper()
    row = products[products["product_id"] == pid]
    if row.empty:
        return {"error": f"Product {pid} not found"}
    return row.iloc[0].to_dict()

@mcp.tool()
def get_order_status(order_id: str):
    oid = order_id.strip().upper()
    row = orders[orders["order_id"] == oid]
    if row.empty:
        return {"error": f"Order {oid} not found"}
    return row.iloc[0].to_dict()

@mcp.tool()
def get_delivery_status(tracking_number: str):
    tn = tracking_number.strip().upper()
    row = delivery[delivery["tracking_number"] == tn]
    if row.empty:
        return {"error": f"Tracking number {tn} not found"}
    return row.iloc[0].to_dict()

@mcp.tool()
def get_return_status(order_id: str):
    oid = order_id.strip().upper()
    row = returns[returns["order_id"] == oid]
    if row.empty:
        return {"status": "No return found for this order"}
    return row.iloc[0].to_dict()

@mcp.tool()
def get_customer_orders(customer_id: str):
    cid = customer_id.strip().upper()
    rows = orders[orders["customer_id"] == cid]
    if rows.empty:
        return []
    return rows[["order_id", "product_id", "order_status", "delivery_status", "tracking_number"]].to_dict(orient="records")

@mcp.tool()
def get_store_policies():
    return STORE_POLICIES

if __name__ == "__main__":
    mcp.run(transport="sse")
