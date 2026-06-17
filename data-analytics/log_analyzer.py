import pandas as pd
import matplotlib.pyplot as plt

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


# ==========================================
# 📊 NEW: VISUAL DATA GRAPH GENERATOR (Matplotlib)
# ==========================================


print("\n 🎨 Genereating Cybersecurity Attact Dashboard Chart")


plt.figure(figsize=(8,5))

Country_counts.plot(kind = "bar", color=["crimson","orangered","darkorange"])
plt.title("CyberSecurity Incident Report: Failed Logins By Country: ", fontsize=14, fontweight="bold", pad=15)
plt.xlabel("Country Code :", fontsize=12, labelpad=10)
plt.ylabel("Number of Failed Logins :",fontsize=12, labelpad=10)
plt.xticks(rotation=0)
plt.grid(axis="y",linestyle="--",alpha=0.7)

plt.tight_layout()
plt.savefig("data-analytics/attack_dashboard.png")

print("\n 💾 Success! Security Chart is saved to data-analytics/attack_dashboard.png ")