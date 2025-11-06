# Python Data Automation Demo

A simple two-script project that demonstrates **data extraction, transformation, and export** using Python.  
The program reads employee data from a CSV file, calculates a 5% raise for each employee, and exports the results as a structured JSON file.

---

## Project Overview
This project simulates a small data engineering workflow:

1. **Read CSV Data**  
   - Script: `scripts/01_read_csv.py`  
   - Reads `data/sample.csv` and displays formatted employee information.

2. **Transform & Export**  
   - Script: `scripts/02_transform.py`  
   - Adds a 5% salary increase and saves the updated data as `data/updated_employees.json`.

---

## Skills Practiced
- Python fundamentals (loops, lists, dictionaries)
- File I/O and data parsing
- Working with the `csv` and `json` modules
- Basic data transformation logic
- Clean project organization and modular scripts
- Git and GitHub workflow (clone, commit, push)

---

## Tech Stack
| Category | Tools Used |
|-----------|-------------|
| **Language** | Python 3 |
| **Libraries** | csv, json |
| **IDE / Tools** | VS Code, GitHub |
| **Data Format** | CSV → JSON |

---

## How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/SpencerLamphere/python-data-automation-demo.git
   cd python-data-automation-demo
