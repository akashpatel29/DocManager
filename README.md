<div align="center">
  <h1>🗂️ Smart PDF Document Manager</h1>
  <p>A streamlined, local document management utility designed for uploading, organizing, tracking, and reading lecture notes and PDF files seamlessly in your browser.</p>
</div>

---

## 📖 Overview:

**DocManager** is a Streamlit-based web application designed for students and professionals who have hundreds of PDF files and need a centralized place to index and read them. 

Instead of digging through messy folders, DocManager allows you to **upload PDFs**, instantly **extract metadata**, automatically generate **visual thumbnails**, and even read your documents page-by-page directly inside the app with integrated **progress analytics**.

## ✨ Key Features:

- **Centralized Uploads**: Securely upload your PDFs with custom tags, descriptions, and lecture dates.
- **In-App Reader Mode**: Automatically converts PDF pages to high-quality images allowing you to read them directly inside the Streamlit interface without external viewers.
- **Smart Analytics**: Tracks your reading progress! See exactly which pages you've read, your total completion percentage per document, and daily app visits.
- **Powerful Search**: Instantly filter through your local SQLite database by custom tags or lecture dates.
- **Visual Previews**: Automatically generates a thumbnail of the PDF's first page upon upload.
- **Admin Controls**: Securely wipe the database and clean up storage with password-protected admin actions.

## 🛠 Tech Stack:

- **Frontend/UI**: [Streamlit](https://streamlit.io/)
- **Backend/Logic**: Python 3
- **PDF Processing**: `PyMuPDF` (extracting pages & thumbnails)
- **Database**: SQLite3 (built-in, zero configuration required)
- **Environment Management**: `uv` & `python-dotenv`

## 🚀 Installation & Setup:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/akashpatel29/DocManager.git
   cd DocManager
   ```

2. **Set up the virtual environment:**
   This project uses `uv` for lightning-fast dependency management.
   ```bash
   uv venv
   source .venv/bin/activate
   uv pip sync requirements.txt
   ```
   *(Alternatively, use standard `pip install -r requirements.txt`)*

3. **Configure Environment Variables:**
   Create a `.env` file in the root directory for the Admin dashboard:
   ```ini
   ADMIN_PASSWORD=your_secure_password_here
   ```

4. **Run the Application:**
   ```bash
   streamlit run app/main.py
   ```
   *The application will automatically initialize the SQLite database (`data/documents.db`) and missing storage directories on its first run.*

## 📂 Project Structure

```text
DocManager/
├── app/
│   └── main.py              # Main Streamlit UI/Dashboard entry point
├── core/
│   ├── analytics.py         # Tracks page views & app visits
│   ├── file_manager.py      # Handles saving PDFs physically
│   ├── models.py            # Document OOP Models
│   ├── reader.py            # PDF-to-Image renderer
│   ├── services.py          # Core logic connecting UI & Repo
│   └── thumbnails.py        # Generates front-page cover images
├── data/                    # Contains the SQLite DB (auto-generated)
├── db/
│   ├── database.py          # SQLite connection and schema setup
│   └── repository.py        # SQL commands (Insert, Search, Fetch)
├── storage/                 # Physical file storage (auto-generated)
│   ├── pdfs/                # Saved PDF files & extracted pages
│   └── thumbnails/          # Cover images
└── pyproject.toml           # Project dependencies
```

## 🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/akashpatel29/DocManager/issues).

---
*Built with ❤️ using Python & Streamlit.*
