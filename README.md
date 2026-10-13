
# RouteDrop

RouteDrop is a delivery-driver optimization project designed to help drivers choose delivery offers that align with their earnings goals and desired destination.

## Problem

Traditional delivery workflows can make it difficult for drivers to control delivery distance or finish a shift near a preferred destination.

## Current Features

- REST API built with FastAPI
- Delivery offer filtering by maximum delivery distance
- Ranking based on estimated earnings per hour
- Detour time incorporated into delivery time estimates
- Interactive API documentation through Swagger UI

## Technology Stack

- Python
- FastAPI
- Pydantic
- Uvicorn

## Getting Started

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
cd routedrop/backend
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install "fastapi[standard]"
```

### 4. Run the API

```bash
python -m uvicorn main:app --reload
```

Open http://127.0.0.1:8000/docs to explore the API.

## Roadmap

- [ ] Improve delivery recommendation scoring
- [ ] Incorporate destination-aware route optimization
- [ ] Integrate mapping and routing data
- [ ] Build a mobile-friendly React frontend
- [ ] Add PostgreSQL persistence
- [ ] Explore predictive analytics for delivery times and earnings

## Disclaimer

RouteDrop is an independent portfolio project. It is not affiliated with or endorsed by Uber Eats. All current delivery offers are fictional examples.