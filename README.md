# Bank Marketing Campaign: Funnel & Conversion Analysis

## 📌 Project Overview

This project focuses on analyzing a marketing funnel for a banking institution to identify conversion drop-offs, channel performance, and opportunities for growth. By analyzing over 45,000 records of direct marketing campaigns (phone calls), this study aims to provide data-driven recommendations to improve the lead-to-customer conversion rate for term deposits.

**Task:** Future Interns Data Science & Analytics – Task 3 (2026)

## 📊 The Marketing Funnel

To understand the customer journey, we defined a three-stage funnel:

1. **Stage 1: Targeted** – The total number of leads reached during the campaign.
2. **Stage 2: Engaged** – Leads who showed interest (defined as a call duration greater than the median of 180 seconds).
3. **Stage 3: Converted** – Leads who successfully subscribed to a term deposit.

## 🛠️ Tech Stack & Tools

* **Language:** Python 3.x
* **Libraries:** * `Pandas`: Data manipulation and cleaning.
* `Matplotlib` & `Seaborn`: Advanced data visualization and dashboarding.


* **Dataset:** [Bank Marketing Campaign Dataset (UCI Machine Learning Repository)](https://archive.ics.uci.edu/dataset/222/bank+marketing)


## 📈 Key Insights & Results

### 1. Funnel Performance

* **Overall Conversion Rate:** 11.7%
* **Engagement to Conversion:** While 49% of leads reach the "Engaged" stage, only a fraction convert, indicating a "leaky" middle-funnel where the closing pitch needs optimization.

### 2. High-Performance Segments

* **Previous Success:** Customers who converted in a previous campaign have a **64.7% conversion rate** in the current campaign. This is the single highest predictor of success.
* **Top Channels:** **Cellular** contacts outperform "Telephone" and "Unknown" methods by a significant margin.
* **Ideal Demographics:** **Students (28.6%)** and **Retired (22.7%)** individuals show the highest intent to subscribe

## 💡 Actionable Recommendations

Based on the analysis, the following strategies are recommended to increase ROI:

* **Lead Prioritization:** Prioritize leads marked as "success" in previous outcomes. These leads are 6x more likely to convert than the average lead.
* **Channel Strategy:** Phase out "unknown" contact methods and shift the marketing budget toward **Cellular-based** outreach.
* **Segment Targeting:** Develop tailored marketing messaging for **Retired** and **Student** demographics, as they have the highest conversion propensity.
* **Sales Training:** calls lasting longer than 3 minutes have high engagement but varied conversion. Training agents on "closing techniques" for long-duration calls could bridge the conversion gap.

---

## 🚀 How to Run the Project

1. Clone this repository:
```bash
git clone https://github.com/Krayolin15/FUTURE_DS_03

```

2. Install required libraries:
```bash
pip install pandas matplotlib seaborn

```

3. Run the analysis script:
```bash
python FUTURE_DS_03.py

```

## 📂 Project Structure

* `bank-full.csv`: The raw dataset used for analysis.
* `FUTURE_DS_03.py`: The main Python script containing data cleaning and visualization code.
* `marketing_funnel_dashboard.png`: The final visual output of the analysis.
* `funnel_metrics.csv`: Summary table of funnel performance.

---

## 🤝 Connect with Me

* **LinkedIn:** https://www.linkedin.com/in/krayolin-kisten-8b4075202/
* **Project Tag:** #FutureInterns #DataAnalytics #MarketingFunnel #Python

---
