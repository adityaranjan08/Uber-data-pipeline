# Uber-data-pipeline

---

## ✅ Problem:

You're getting this error because **PowerShell doesn’t allow script execution** by default.

```
running scripts is disabled on this system
```

---

## ✅ Solution: Temporarily Allow Script Execution

### 🔓 Step 1: Open PowerShell as Administrator

1. Click Start → type `powershell`
2. Right-click → **Run as Administrator**

---

### ⚙️ Step 2: Change Execution Policy (Temporary & Safe)

In the **admin PowerShell window**, run this:

```bash
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then press `Y` (if prompted).

✅ This allows scripts to run **only in the current session** (it’s safe and reversible).

---

### ▶️ Step 3: Now Activate Your Environment

In the same PowerShell session, run:

```bash
cd C:\Users\adity\Documents\GitHub\Uber-data-pipeline
.\venv\Scripts\activate
```

You should now see:

```
(venv) PS C:\Users\adity\Documents\GitHub\Uber-data-pipeline>
```

Boom! 🎯 You're inside the virtual environment.

---

Let me know once this works — then we'll go to:

Boom! 💥 That’s exactly what we wanted, Ayush — now your virtual environment is activated and ready for action.

---

## ✅ **Step 1.4: Install Required Packages**

Now inside your activated terminal (`(venv)` showing), install the core libraries you need for the pipeline.

### 🔹 Run this:

```bash
pip install pandas openpyxl office365-rest-python-client
```

Explanation:

| Package                        | Use                                                                   |
| ------------------------------ | --------------------------------------------------------------------- |
| `pandas`                       | For loading, transforming, and saving CSV/Excel data                  |
| `openpyxl`                     | Required to read/write `.xlsx` Excel files using pandas               |
| `office365-rest-python-client` | For SharePoint file ingestion via API (optional for future expansion) |

---


---

## ✅ Step 1.5: Save Dependencies

Run this command to freeze the installed packages into a file:

```bash
pip freeze > requirements.txt
```

This creates a `requirements.txt` file in your project folder, which is useful for:

* Recreating the same environment later
* Sharing the project with others
* Deploying to a server

📁 Example content:

```
pandas==2.2.2
openpyxl==3.1.2
office365-rest-python-client==2.4.17
```

---

 `requirements.txt` is correctly populated, let’s move to the final part of Step 1.

---

## ✅ STEP 1.6: Create the Folder Structure for Your Data Pipeline

📌 Purpose: Organize your project files into logical directories for raw data, staging, processed outputs, scripts, and logs.

---

### 🪜 Step-by-Step Commands (in PowerShell)

Make sure you’re still inside your project folder:

```
C:\Users\adity\Documents\GitHub\Uber-data-pipeline
```

Then run these one by one or all together:

```bash
mkdir data
mkdir data\raw
mkdir data\staging
mkdir data\processed
mkdir data\final
mkdir src
mkdir logs
```

---

### ✅ Expected Folder Structure

After running the above, type:

```bash
tree /f
```

And you should see something like:

```
Uber-data-pipeline
│   README.md
│   requirements.txt
│
├───data
│   ├───final
│   ├───processed
│   ├───raw
│   └───staging
│
├───logs
├───src
└───venv
```

Each folder has its purpose:

| Folder           | Purpose                                             |
| ---------------- | --------------------------------------------------- |
| `data/raw`       | Original files (mocking SharePoint downloads)       |
| `data/staging`   | Renamed/validated versions of raw files             |
| `data/processed` | Cleaned/merged files after transformations          |
| `data/final`     | Final analytics-ready outputs (for Power BI, etc.)  |
| `src`            | Python scripts (ingestion, staging, cleaning, etc.) |
| `logs`           | Logs and audit trails (optional)                    |

---




---


