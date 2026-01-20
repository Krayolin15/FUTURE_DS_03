import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('bank-full.csv', sep=';')
df['converted'] = df['y'].apply(lambda x: 1 if x == 'yes' else 0)

# Metrics
stage1_count = len(df)
stage2_count = len(df[df['duration'] > 180])
stage3_count = df['converted'].sum()

funnel_df = pd.DataFrame({
    'Stage': ['Targeted', 'Engaged', 'Converted'],
    'Count': [stage1_count, stage2_count, stage3_count]
})
funnel_df['Conversion_Rate'] = (funnel_df['Count'] / stage1_count * 100).round(2)

# Categorical Performance
channel_perf = df.groupby('contact')['converted'].mean().sort_values(ascending=False).reset_index()
channel_perf['converted'] *= 100

job_perf = df.groupby('job')['converted'].mean().sort_values(ascending=False).reset_index()
job_perf['converted'] *= 100

poutcome_perf = df.groupby('poutcome')['converted'].mean().sort_values(ascending=False).reset_index()
poutcome_perf['converted'] *= 100

# Plotting
plt.figure(figsize=(16, 12))

# Chart 1: Marketing Funnel
plt.subplot(2, 2, 1)
sns.barplot(x='Count', y='Stage', data=funnel_df, hue='Stage', palette='Blues_d', legend=False)
plt.title('Marketing Funnel: Targeted vs. Converted', fontsize=14)
for i, v in enumerate(funnel_df['Count']):
    plt.text(v, i, f" {v} ({funnel_df['Conversion_Rate'][i]}%)", va='center', fontweight='bold')

# Chart 2: Conversion by Contact Method
plt.subplot(2, 2, 2)
sns.barplot(x='converted', y='contact', data=channel_perf, hue='contact', palette='viridis', legend=False)
plt.title('Conversion Rate by Channel (%)', fontsize=14)

# Chart 3: Conversion by Job Category
plt.subplot(2, 2, 3)
sns.barplot(x='converted', y='job', data=job_perf, hue='job', palette='rocket', legend=False)
plt.title('Conversion Rate by Job Type (%)', fontsize=14)

# Chart 4: Previous Outcome Success
plt.subplot(2, 2, 4)
sns.barplot(x='converted', y='poutcome', data=poutcome_perf, hue='poutcome', palette='magma', legend=False)
plt.title('CR % Based on Previous Campaign Outcome', fontsize=14)

plt.tight_layout()
plt.savefig('marketing_funnel_dashboard.png')
print("Dashboard saved successfully without warnings.")