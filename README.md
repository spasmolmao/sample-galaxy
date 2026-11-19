# Sample Galaxy

Audio sample organization and acoustic similarity engine built with dimensionality reduction and vector clustering.

## Stack
- Python (Librosa, UMAP, Scikit-learn)
- MongoDB for sample metadata and embedding persistence

## Architecture
- Spectral and MFCC feature extraction pipeline for local audio libraries
- UMAP dimensionality reduction to cluster percussive, melodic, and textural samples by acoustic similarity
- Metadata indexing and nearest-neighbor lookup queries

## Setup & Custom Sample Paths
1. Clone the repository and create a virtual environment (`uv venv` or `python -m venv .venv`).
2. Install dependencies from `requirements.txt`.
3. Set your MongoDB URI and root sample library directory path in `.env` (or update the base directory variable in the indexing script) before running extraction.
