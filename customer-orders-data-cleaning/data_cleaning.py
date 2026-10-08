import pandas as pd
df = pd.read_excel("dirty_customer_orders.xlsx", engine="openpyxl")

df = df.dropna(how="all")

clean_amount = df["OrderAmount"].astype(str)

clean_amount = clean_amount.str.replace(" USD", "", regex=False)

clean_amount = clean_amount.str.replace("(", "-", regex=False)

clean_amount = clean_amount.str.replace(")", "", regex=False)

clean_amount = clean_amount.str.replace(",", "", regex=False)

clean_amount = clean_amount.str.replace("$", "", regex=False)

clean_amount = pd.to_numeric(clean_amount, errors="coerce")

df["CleanOrderAmount"] = clean_amount

df = df[df["OrderAmount"] != "OrderAmount"]

df = df.drop(columns=["OrderAmount"])

dates = pd.to_datetime(df["SignupDate"], errors="coerce")

dates = pd.to_datetime(df["SignupDate"], format="mixed", errors="coerce")

df["SignupDate"] = dates

df["Name"] = df["Name"].str.strip()

df["Name"] = df["Name"].str.replace("  "," ",regex=False)

df["Name"] = df["Name"].str.title()

df["Email"] = df["Email"].str.strip()

df["Email"] = df["Email"].str.lower()

df["Phone"] = df["Phone"].str.replace("(", "", regex=False)
df["Phone"] = df["Phone"].str.replace(")", "", regex=False)
df["Phone"] = df["Phone"].str.replace("-", "", regex=False)
df["Phone"] = df["Phone"].str.replace(".", "", regex=False)
df["Phone"] = df["Phone"].str.replace(" ", "", regex=False)

country_map = {
    "Canada": "Canada",
    "canada": "Canada",
    "CA": "Canada",

    "USA": "United States",
    "usa": "United States",
    "US": "United States",
    "U.S.A.": "United States",
    "United States": "United States",
    "united states": "United States",

    "UK": "United Kingdom",
    "U.K.": "United Kingdom",
    "United Kingdom": "United Kingdom",
    "Britain": "United Kingdom",
    "england": "United Kingdom",

    "Saudi Arabia": "Saudi Arabia",
    "saudi arabia": "Saudi Arabia",
    "S. Arabia": "Saudi Arabia",
    "KSA": "Saudi Arabia",

    "Germany": "Germany",
    "germany": "Germany",
    "DE": "Germany",

    "Australia": "Australia",
    "australia": "Australia",
    "AUS": "Australia"
}

df["Country"] = df["Country"].map(country_map)

category_map = {
    "SPORTS" : "Sports",
    "sports" : "Sports",
    "Sport" : "Sports",
    "Sports" : "Sports",

    "ELECTRONICS" : "Electronics",
    "electronics" : "Electronics",
    "Electronics" : "Electronics",
    "Electronic" : "Electronics",

    "Book" : "Books",
    "BOOKS" : "Books",
    "Books" : "Books",

    "TOYS" : "Toys",
    "toys" : "Toys",
    "Toys" : "Toys",
    "Toy" : "Toys",

    "CLOTHING" : "Clothing",
    "clothing" : "Clothing",
    "Clothing" : "Clothing",
    "Cloths" : "Clothing",

    "Apparel" : "Clothing",

    "Home&Garden" : "Home & Garden",
    "Home & garden" : "Home & Garden",
    "Home & Garden" : "Home & Garden"
}

df["Category"] = df["Category"].map(category_map)

df = df.drop_duplicates()

df["CustomerID"] = df["CustomerID"].astype(int)

df = df.reset_index(drop=True)