import pandas as pd

print("PANDAS CyberSecurity log Analyzer")

df = pd.read_csv("data-analytics/mock_security_logs.csv")

print ("Raw Log Data")
print (df)

print("Failed Suspesious Activities (Failed Login)")

failed_logins = df[df["Status"] == "Failed"]

print(failed_logins)

total_bytes = df["Bytes_Transferred"].sum()
print(f"/n📊 Total Network Banwidth : {total_bytes} Bytes")

failed_logins.to_csv("data-analytics/incident_report.cs", index=False)
print("💾 Security Report is Exported to data-analytics/incident_report.csv")