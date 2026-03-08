# Medi-Loc

Healthcare infrastructure platform for medication adherence monitoring and auditable review workflows.

## Problem

Senior-care providers often lack reliable operational visibility into medication adherence and misuse. Manual review workflows are slow, inconsistent, and difficult to audit, making it harder for staff to identify risks and intervene quickly.

## Solution

Medi-Loc converts noisy device outputs into structured, reviewable records that help staff make operational decisions. This repository contains a minimal infrastructure scaffold for ingesting medication event data, validating records, storing structured outputs, and supporting operational review workflows.

## Users

Primary users are senior-care providers and staff responsible for medication review and adherence monitoring.

## Architecture

**Data Capture**  
Synthetic medication event data representing device-captured adherence events.

**Processing**  
Python-based validation and transformation pipelines convert raw event rows into structured records.

**Infrastructure**  
Structured records are written into a queryable SQLite database to simulate auditable operational storage.

## Key Features

- Medication event data ingestion  
- Validation and transformation of raw records  
- Queryable and auditable event storage  
- Structured logging of processed records  
- Simple operational summary output  

## Results

- Demonstrates a minimal end-to-end medication event pipeline  
- Converts CSV event data into structured database records  
- Supports auditable storage and basic review summaries  

## Tech Stack

Python  
SQLite  
SQL  

## System Flow

Device Output  
↓  
Data Processing Pipeline  
↓  
Structured Storage  
↓  
Queryable Records  
↓  
Staff Review Workflow  

## Repository Structure

```
mediloc/
├ README.md
├ LICENSE
├ .gitignore
├ data/
├ docs/
├ schemas/
└ src/
```

## Running the Project

Navigate to the repository root:

```
cd mediloc
```

Run the pipeline:

```
python src/main.py
```

This will:

1. Load medication event data  
2. Validate and process records  
3. Store events in a SQLite database  
4. Output a summary of processed events  

## Notes

- All data in this repository is synthetic.  
- This repository represents infrastructure and workflow development for medication adherence monitoring and operational review.
