# Medi-Loc Architecture

## Overview

Medi-Loc is a minimal infrastructure scaffold for converting medication adherence event data into structured, queryable records.

## Flow

Device Output  
↓  
CSV Event Ingestion  
↓  
Validation and Transformation  
↓  
Structured SQLite Storage  
↓  
Operational Review Queries  

## Components

### Data Input
Synthetic medication event data stored as CSV rows.

### Processing Layer
Python pipeline validates timestamps, event types, and required fields.

### Storage Layer
Structured events are inserted into a SQLite database to simulate auditable operational storage.

### Review Layer
Basic summaries support operational review of taken, missed, and late medication events.
