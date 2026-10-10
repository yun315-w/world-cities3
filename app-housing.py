import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("California Housing Data (1990) by Qianyun Wei")

df = pd.read_csv("housing.csv")

# 按最低房价筛选
house_value = st.slider(
    "Minimal Median House Value",
    min_value=0,
    max_value=500001,
    value=200000,
)

st.subheader("See more filters in the sidebar:")

# 按位置类型筛选，默认全部选中
location_types = df["ocean_proximity"].unique().tolist()

selected_locations = st.sidebar.multiselect(
    "Choose the location type",
    options=location_types,
    default=location_types,
)

# 按收入水平筛选
income_level = st.sidebar.radio(
    "Choose income level",
    options=["Low", "Medium", "High"],
)

filtered_df = df[
    (df["median_house_value"] >= house_value)
    & (df["ocean_proximity"].isin(selected_locations))
].copy()

if income_level == "Low":
    filtered_df = filtered_df[filtered_df["median_income"] <= 2.5]
elif income_level == "Medium":
    filtered_df = filtered_df[
        (filtered_df["median_income"] > 2.5)
        & (filtered_df["median_income"] < 4.5)
    ]
else:
    filtered_df = filtered_df[filtered_df["median_income"] >= 4.5]

# 显示地图
if filtered_df.empty:
    st.info("No districts match these filters. Please adjust the filters.")
else:
    st.map(filtered_df[["latitude", "longitude"]])

# 显示房价直方图，30 个 bins
st.subheader("Distribution of Median House Value")

fig, ax = plt.subplots(figsize=(10, 5))
ax.hist(
    filtered_df["median_house_value"],
    bins=30,
    edgecolor="black",
)
ax.set_xlabel("Median House Value (US Dollars)")
ax.set_ylabel("Number of Districts")
ax.set_title("Median House Value of Filtered Districts")

st.pyplot(fig)
plt.close(fig)