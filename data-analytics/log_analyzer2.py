import pandas as pd
import matplotlib.pyplot as plt

print("Pandas Security Log Analyzer...")

try:
    df = pd.read_csv("basics/mock_security_logs.csv")
except FileNotFoundError:
    print("Error : basics/mock_security_logs.csv not Found")
    exit()


#Printing the Data

print("\n Raw Log Data")
print(df)

# 2. Aggregation: Group and count attacks by country location

print("Top Suspicious login by country")
country_counts = df[df["Status"] == "Failed"]["Country"].value_counts()
print(country_counts)

# 3. Advanced Filtering: Multi-condition lookup
print("Highest Risk Threats (Failed Status and No MFA Enabled): ")
highest_risk_threats = df[(df["Status"]=="Failed") & (df["MFA_Triggered"] == "No")]
print(highest_risk_threats)

# 4. Critical Statistical Metric: Find out average bandwidth of successful logins
avg_bytes_Success = df[df["Status"] == "Success"]["Bytes_Transferred"].mean()
print(f"\n The Baseline Bytes Transffered on Succefull Login{avg_bytes_Success:.2f}")

# Save Incident Report

highest_risk_threats.to_csv("basics/incident_report.csv", index = False)
print("The Incident Report is Saved to: basics/incident_report.csv")


# ==========================================
# 📊 VISUAL DATA GRAPH GENERATOR (Matplotlib)
# ==========================================

print("\n🎨 Generating CyberSecurity Attack Dashboard")
if not country_counts.empty:
    plt.figure(figsize=(8,5))


    country_counts.plot(kind= "bar", cmap="plasma")

    plt.title("\n CyberSecurity Incedent Report: Failed Logins By Country ",fontsize=14,fontweight="bold",pad=15)
    plt.xlabel("Country Code :" ,fontsize=12, labelpad=10)
    plt.ylabel("Failed Logins",fontsize=12,labelpad=10)
    plt.xticks(rotation=0)
    plt.grid(axis="y",linestyle="--",alpha=0.7)


    plt.tight_layout()
    plt.savefig("basics/attack_dashboard.png")
    plt.close()
    print("💾 Success! Security Dashboard is Saved to basics/attack_dashboard.png")

else:
    print("⚠️ No Failed logins discovered to map onto the Dashboard.")


