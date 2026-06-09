import pandas as pd
#Heading
print("PANDAS CyberSecurity log Analyzer")
# Anylyzing Data Path
df = pd.read_csv("data-analytics/mock_security_logs.csv")
# Printing the Data
print ("Raw Log Data")
print (df)

# For Finding the Failed Or Suspesious logins
print("Failed Suspesious Activities (Failed Login)")

failed_logins = df[df["Status"] == "Failed"]

print(failed_logins)
# Total Bytes That are Used
total_bytes = df["Bytes_Transferred"].sum()
print(f"/n📊 Total Network Banwidth : {total_bytes} Bytes")

# Saving a Report As A CSV of Failed Login for Analyzing
failed_logins.to_csv("data-analytics/incident_report.cs", index=False)
print("💾 Security Report is Exported to data-analytics/incident_report.csv")