# CodeBLEU — README

Short description
- CodeBLEU is a small project for computing code-similarity / CodeBLEU style scores between a candidate implementation and a reference implementation. It contains a simple web client and a server-side toolkit for tokenization, comment cleaning and extension detection.

Folder structure
- /
  - client/
    - index.html — lightweight web UI to upload candidate/reference files and display results.
  - examples/
    - 53e31bb0-0d3f-4ef9-8bab-5854f0fae1fa.py — example candidate file.
    - reference_code_1.py — example reference file.
  - server/
    - comment_cleaner.py — utilities to remove comments from source code before analysis.
    - constants.py — project constants (supported extensions, tokenization settings).
    - extension_extractor.py — logic to extract / detect language/extensions from code.
    - main.py — entrypoint for the server or CLI that wires together tokenization, cleaning and scoring.
    - project.toml — project metadata (if using packaging tools).
    - requirements.txt — Python dependencies for server-side components.
    - tokenizer.py — tokenization logic used for CodeBLEU/token-based comparison.
  - .gitignore

Quick start (Windows)
1. Create and activate a venv:
   - python -m venv .venv
   - .venv\Scripts\activate

2. Install dependencies:
   - pip install -r server\requirements.txt

3. Run server (example):
   - python server\main.py
   - If main.py exposes an HTTP endpoint, open client\index.html in your browser and point uploads to the server endpoint. If main.py is a CLI, run it according to its usage message.

4. Use the client:
   - Open client\index.html in your browser.
   - Upload a candidate file and a reference file and compute scores.



Notes
- The client is a static HTML file that posts files to the server; adapt endpoints in client\index.html if server port/paths differ.
- Review server\requirements.txt and server\constants.py to confirm supported languages/extensions before adding new languages.
- Example files live in examples/ to help validate functionality.

License & contribution
- Add license and contribution guidelines as needed.
