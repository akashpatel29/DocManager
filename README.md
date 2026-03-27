# DocManager
A streamlined local document management utility designed for organizing, tagging, and tracking lecture notes and files.


📂 DocManager: The "Find My PDF" Assistant
DocManager is a Streamlit-based web application designed for people who have hundreds of PDF files scattered across their computer and can never remember which folder they are in.

Instead of digging through Windows Explorer or Mac Finder, DocManager indexes your files into a local SQLite database, allowing you to search by name, date, or custom tags instantly.

✨ Key Features
Centralized Search: Find any PDF by typing a keyword, even if the file is buried 5 folders deep.

Smart Metadata: Track lecture_date, tags, and total_pages for every document.

Visual Previews: See a thumbnail of the PDF before you open it.

One-Click Access: Open the file directly from the Streamlit interface.

🛠 How it Works
Index: Run the indexing script to scan your selected folders.

Store: Metadata and file paths are saved into a lightweight SQLite database.

Search: Use the Streamlit sidebar to filter by category or date.

Retrieve: View the document details and path immediately.
