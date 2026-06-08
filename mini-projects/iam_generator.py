import json
import sys

print ("===AWS IAM Policy Generator ===")

# 1. Gather inputs from the user
effect = input("Allow or Deny Access?(Enter 'Allow' or 'Deny'): ").strip().capitalize()
# Condition for Valid effect
if effect == "Allow":
    print("✔️  Acces Granted. Proceeding to the Next Step...")
elif effect == "Deny":
    print(f"🛑 Access Denied. Exiting program as Requested.")
    sys.exit()
else:
    print(f"❌ Invalid entry '{effect}'. Exiting program.")
    sys.exit()
service = input("Enter the Service (e.g: s3, ec2):").strip().lower()
action = input("Enter the Action :(e.g., ListBucket, StartInstances, *): ").strip()
resource = input("Enter the Resource ARN (or '*' for all resources): ").strip()
    # 2. Format the specific action string (e.g., "s3:ListBucket")
full_action = f"{service}:{action}"

# 3. Construct the Python dictionary (matches AWS JSON structure)
policy_dict = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": effect,
            "Action": full_action,
            "Resource": resource
        }
    ]
}
# 4. Convert the dictionary into a formatted JSON string
json_policy=json.dumps(policy_dict,indent=4)

print("\n==== GENERATED IAM POLICY ===\n")
print(json_policy)


# 5. Save the JSON string to a physical file
with open("mini-projects/aws_policy.json", "w") as file:
    file.write(json_policy)

print("Succes Policy Saved to mini-projects/aws_policy.json")