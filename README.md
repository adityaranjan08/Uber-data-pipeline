# Uber-data-pipeline

---

## ✅ Problem:

You're getting this error because **PowerShell doesn’t allow script execution** by default.

```
running scripts is disabled on this system
```

---

## ✅ Solution: Temporarily Allow Script Execution

### Open PowerShell as Administrator

1. Click Start → type `powershell`
2. Right-click → **Run as Administrator**

---

### Change Execution Policy (Temporary & Safe)

In the **admin PowerShell window**, run this:

```bash
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then press `Y` (if prompted).

✅ This allows scripts to run **only in the current session** (it’s safe and reversible).

---

###  Now Activate Your Environment

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

## Install Required Packages**

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

## Save Dependencies

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

## Create the Folder Structure for Your Data Pipeline

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


---

##  Ingestion Script (`ingest_sharepoint.py`)

📌 **Goal**: Simulate SharePoint file ingestion by copying files from `data/raw/` to a mock SharePoint folder (`data/sharepoint/`) and prepare for staging.

---

###  Script File Location

Create a new Python file inside the `src/` directory:

```
src/ingest_sharepoint.py
```

---




Run this command:

```bash
mkdir data\sharepoint
```

This mimics the SharePoint source for your pipeline.

---


In your terminal (from project root):

```bash
python src/ingest_sharepoint.py
```

You should see:

```
Ingested 'uber_rides_jan.csv' to SharePoint folder.
```

And you’ll find a copy of the CSV inside:
```
data/sharepoint/
```

---


| Task                        | Status |
|-----------------------------|--------|
| `ingest_sharepoint.py` created | ✅    |
| Simulated SharePoint folder created | ✅ |
| Raw file copied to sharepoint dir | ✅ |

---



---

##  Create `stage_files.py`

📌 **Goal**:  
Simulate a staging area where we:
- Copy files from `data/sharepoint/` to `data/staging/`
- Rename them with a timestamp to avoid name clashes and track load date

---

###  File Location
Create the file:
```
src/stage_files.py
```

---





###  Run the Script

Make sure you're in the root folder:

```bash
python src/stage_files.py
```

Example output:
```
Staged: uber_rides_jan.csv as 20250623_145705_uber_rides_jan.csv
```

---

###  Check Your Folder

You should now see a copy in:

```
data/staging/
```

✅ With a **timestamp-prefixed filename**, like:
```
20250623_145705_uber_rides_jan.csv
```

---

##  Step Complete 🎉

| Task                                 | Status |
|--------------------------------------|--------|
| Created `stage_files.py`             | ✅     |
| Renamed + copied files to staging    | ✅     |
| Prepared for transformation stage    | ✅     |

---

---

##  `transform_data.py` — Data Cleaning & Transformation

📌 **Goal**:  
Read the staged files, clean them (remove nulls), and combine them into a single **processed** and **final** output.

---

### File Location

Create:
```
src/transform_data.py
```

---

### 🧠 What This Script Will Do:
1. Load all `.csv` files from `data/staging/`
2. Drop empty rows
3. Assign a unique `trip_id` if needed
4. Concatenate them into a single DataFrame
5. Save to:
   - `data/processed/processed.csv`
   - `data/final/final_output.csv`

---



###  How to Run It

```bash
python src/transform_data.py
```

✅ Output:
```
✅ Transformation complete. Final file saved to: data/final/final_output.csv
```

---

### 🔎 Check Your Output

Now you’ll find:
- Clean, merged file in `data/processed/processed.csv`
- Final CSV in `data/final/final_output.csv`

Open it in Excel or VS Code to verify.

---

## Done 

| Task                            | Status |
|----------------------------------|--------|
| Read and cleaned staged files    | ✅     |
| Dropped nulls, standardized cols | ✅     |
| Merged into processed + final    | ✅     |

---

