import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)

# --- 1. Data Generation ---
# Create a date range for two years to show seasonal patterns
dates = pd.date_range(start="2023-01-01", end="2024-12-31", freq="D")
n_days = len(dates)
product_categories = ["Electronics", "Apparel", "Home Goods"]

# Create an empty list to store data records
records = []

# Generate data for each product category
for category in product_categories:
    # Base revenue with a slight upward trend
    base_revenue = np.linspace(start=100, stop=150, num=n_days)
    
    # Seasonal component (sine wave with a 365-day period)
    # We shift the phase for each category to make them distinct
    if category == "Electronics":
        phase_shift = 300 # Peaks in Q4 (holidays)
    elif category == "Apparel":
        phase_shift = 120 # Peaks in mid-year (summer/spring fashion)
    else:
        phase_shift = 0 # Peaks early in the year
        
    seasonal_effect = 30 * np.sin(2 * np.pi * (np.arange(n_days) + phase_shift) / 365)
    
    # Random noise to simulate real-world variability
    noise = np.random.normal(0, 10, n_days)
    
    # Combine components to get final revenue
    revenue = base_revenue + seasonal_effect + noise
    
    # Create a temporary DataFrame for this category
    temp_df = pd.DataFrame({
        "Date": dates,
        "Product_Category": category,
        "Revenue": revenue
    })
    records.append(temp_df)

# Concatenate all records into a single DataFrame
data = pd.concat(records, ignore_index=True)


# --- 2. Visualization ---
# Set professional Seaborn style and context
sns.set_style("whitegrid")
sns.set_context("talk")

# Create the figure with the required dimensions (8 inches * 64 dpi = 512 pixels)
plt.figure(figsize=(8, 8))

# Create the lineplot
lineplot = sns.lineplot(
    data=data,
    x="Date",
    y="Revenue",
    hue="Product_Category", # Creates separate lines for each category
    style="Product_Category", # Uses different line styles
    palette="viridis", # A professional and colorblind-friendly palette
    linewidth=2.5
)

# --- 3. Styling and Customization ---
# Add a clear and descriptive title
plt.title("Seasonal Revenue Patterns by Product Category", fontsize=18, weight='bold', pad=20)

# Set informative axis labels
plt.xlabel("Date", fontsize=14)
plt.ylabel("Revenue (in thousands USD)", fontsize=14)

# Improve legend
plt.legend(title="Product Category", loc="upper left")

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)


# --- 4. Export ---
# Save the figure with specified DPI to get 512x512 pixels
# bbox_inches='tight' ensures all elements (labels, title) fit in the saved image
plt.savefig("chart.png", dpi=64, bbox_inches="tight")




# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd
# import numpy as np

# # Set random seed for reproducibility
# np.random.seed(42)

# # Set Seaborn style and context
# sns.set_style("whitegrid")
# sns.set_context("talk")

# # Generate synthetic customer engagement data
# n_samples = 300
# data = pd.DataFrame({
#     "email_open_rate": np.clip(np.random.normal(0.5, 0.1, n_samples), 0, 1),
#     "click_through_rate": np.clip(np.random.normal(0.2, 0.05, n_samples), 0, 1),
#     "time_on_site": np.random.normal(120, 30, n_samples),  # in seconds
#     "pages_per_visit": np.random.normal(5, 1.5, n_samples),
#     "bounce_rate": np.clip(np.random.normal(0.4, 0.1, n_samples), 0, 1),
#     "conversion_rate": np.clip(np.random.normal(0.05, 0.02, n_samples), 0, 1),
# })

# # Compute correlation matrix
# corr = data.corr()

# # Create figure and heatmap
# plt.figure(figsize=(8, 8))  # 8 inches * 64 dpi = 512 pixels
# heatmap = sns.heatmap(
#     corr,
#     annot=True,
#     fmt=".2f",
#     cmap="coolwarm",
#     square=True,
#     linewidths=0.5,
#     cbar_kws={"shrink": 0.8}
# )

# # Add title
# plt.title("Customer Engagement Correlation Matrix", fontsize=16)

# # Save figure with required dimensions
# plt.savefig("chart.png", dpi=64, bbox_inches="tight")
