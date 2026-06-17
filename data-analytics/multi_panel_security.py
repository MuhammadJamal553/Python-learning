# ==========================================
# 📊 ADVANCED: MULTI-PANEL SECURITY DASHBOARD
# ==========================================
import pandas as pd
import matplotlib.pyplot as plt
print("\n🎨 Genreating Multi-Panel Advance CyberSecurity Dashboard....")

df = pd.read_csv("basics/mock_security_logs.csv")

# 1. Recalculate and prepare data aggregates
country_counts = df[df["Status"] == "Failed"]["Country"].value_counts()
User_counts = df[df["Status"] == "Failed"]["Username"].value_counts()
device_type = df[df["Status"] == "Failed"]["Device_Type"].value_counts()

# Create a figure canvas with 3 subplots stacked vertically
fig, axes = plt.subplots(3,1, figsize=(10, 15))
fig.suptitle("🚨Enterprise Security Operations Center (SOC) Dashboard ", fontsize =16 ,fontweight="bold")


# Panel 1: Failed Logins By Country

country_counts.plot(kind="bar", ax=axes[0],color="crimson")
axes[0].set_title("Threat Vector: Failed Login by origin Country", fontsize=12, fontweight="bold")
axes[0].set_ylabel("Incident counts")
axes[0].grid(axis="y",linestyle="--",alpha=0.5)
axes[0].tick_params(axis= "x",rotation=0)

#Panel 2: Most Target Accounts (Brute Force Tracking)
User_counts.plot(kind="bar",ax=axes[1],color="Orangered")
axes[1].set_title("Target Analysis : User Accounts", fontsize=12, fontweight="bold")
axes[1].set_ylabel("Incident counts")
axes[1].grid(axis="y",linestyle="--",alpha=0.5)
axes[1].tick_params(axis ="x",rotation=0)

# Panel 3: Attacker Device Signatures
device_type.plot(kind="bar",ax=axes[2],color="darkorange")
axes[2].set_title("Signature Proffing : Spoofed Attackers Device Type")
axes[2].set_ylabel("Incident Counts")
axes[2].grid(axis = "y",linestyle="--",alpha=0.5)
axes[2].tick_params(axis="x",rotation=0)

# Clean up layouts and export the master dashboard
plt.tight_layout(rect= [0,0,1,0.96])# Leaves room for the main super-title
plt.savefig("data-analytics/multi_panel_dashboard.png",dpi=300)
plt.close()

print("💾Success: Advanced 3-Panel Dashboard saved to data-analytics/multi_panel_dashboard.png")
