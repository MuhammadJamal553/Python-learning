import pandas as pd
#Heading
print("PANDAS CyberSecurity log Analyzer")
# Anylyzing Data Path
df = pd.read_csv("data-analytics/mock_security_logs.csv")
# Printing the Data
print ("Raw Log Data")
print (df)

# 2. Aggregation: Group and count attacks by country location
print("Top Suspesious Login Attempts By Country")
Country_counts = df[df["Status"] == "Failed"]["Country"].value_counts()
print(Country_counts)
# 3. Advanced Filtering: Multi-condition lookup (& operator)
# Looking for high-risk profiles: Failed logins where MFA was completely skipped/not triggered
print("\n🚨 HIGHES RISK THREATS (Failed Status AND No MFA Enabled):")
high_risk_threats = df[(df["Status"] == "Failed") & (df["MFA_Triggered"] == "No")]
print(high_risk_threats[["Timestamp", "Username", "IP_Address", "Country"]])

# 4. Critical Statistical Metric: Find out average bandwidth of successful logins
avg_bytes_success = df[df["Status"] == "Success"]["Bytes_Transferred"].mean()
print(f"\nThe Baseline Bytes Transfered On Successfull Login {avg_bytes_success}")

high_risk_threats.to_csv("data-analytics/incident_report.csv", index=False )
print("The Incident Report Is Save to data-analytics/incident_report.csv")