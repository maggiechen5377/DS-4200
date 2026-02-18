import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/maggiechen/Documents/DS-4200/project/vgsales.csv')

fig, axes = plt.subplots(1, 2, figsize=(12, 4))

# 1. Top 10 genres by global sales
genre_sales = df.groupby('Genre')['Global_Sales'].sum().sort_values(ascending=False).head(10)
axes[0].bar(genre_sales.index, genre_sales.values, color='steelblue')
axes[0].set_title('Global Sales by Genre')
axes[0].set_xlabel('Genre')
axes[0].set_ylabel('Global Sales (millions)')
axes[0].tick_params(axis='x', rotation=45)

# 2. NA vs EU sales scatter (sample 200)
sample = df.dropna().sample(200, random_state=42)
axes[1].scatter(sample['NA_Sales'], sample['EU_Sales'], alpha=0.5, color='coral')
axes[1].set_title('NA vs EU Sales')
axes[1].set_xlabel('NA Sales (millions)')
axes[1].set_ylabel('EU Sales (millions)')

plt.tight_layout()
plt.savefig('vg_viz.png', dpi=120)
print("done")