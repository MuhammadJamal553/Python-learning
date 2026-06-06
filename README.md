# Python Learning Journey

A structured repository tracking my progress in foundational Python development, automation scripting, and cloud security integrations.

## Repository Structure

This project is organized into dedicated modules:
* **basics/**: Core language syntax and basic operations.
* **exercises/**: Practical coding challenges and problem-solving tasks.
* **mini-projects/**: Functional automation utilities and security tools.
* **notes/**: Conceptual documentation and learning summaries.

## Core Program Directory

### 🛠️ Basics Module
* **variables.py**: Demonstrates memory allocation, type casting, and primitive data type manipulation.
* **input_output.py**: Handles user terminal prompts and string sanitization.

### ☁️ Mini-Projects Module
* **iam_generator.py**: Automatically generates AWS-compliant IAM credential policies. It validates entries via conditional control flow and exports data to a physical `.json` file.

## How to Execute the Scripts

Ensure Python 3 is installed. Open your terminal at the root folder and run:

```bash
python basics/variables.py
python basics/input_output.py
python mini-projects/iam_generator.py
```

## Generated Artifacts
* `mini-projects/aws_policy.json`: The exported AWS permission configuration file.
