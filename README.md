# SQL Query ChatBot App

This project is a chatbot application that helps users retrieve SQL queries from a SQLite database. The app uses Google Generative AI (Gemini Pro) to convert natural language questions into SQL queries, which are then executed against a database of student records.

## Demo
https://github.com/user-attachments/assets/043744ad-d1e6-434e-9db0-1e364cfc1cdb

## Features
- Ask questions in natural language, and the app will generate SQL queries to retrieve data from the `STUDENT` table in a SQLite database.
- The database contains information about students including their `NAME`, `CLASS`, `SECTION`, and `MARKS`.
- You can view the results of the query directly in the Streamlit app.

## Requirements
To run this project, you need the following Python packages:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the root directory and add your Google API key like this:

```bash
GOOGLE_API_KEY="PASTE_YOUR_API_KEY_HERE"
```

Run the `sqllite.py` file to create the database and populate it with sample data:

```bash
python sqllite.py
```

## Database Structure
The database `students.db` contains a single table `STUDENT` with the following structure:

| Column Name | Data Type  |
| ----------- | ---------- |
| NAME        | VARCHAR(25)|
| CLASS       | VARCHAR(25)|
| SECTION     | VARCHAR(25)|
| MARKS       | INT        |

## Sample Data

| Name       | Class               | Section | Marks |
|------------|---------------------|---------|-------|
| Charan     | GenAI               | A       | 90    |
| Sushanth   | Web dev             | B       | 100   |
| Veekshith  | Data Science        | A       | 86    |
| Dheeraj    | Content Creation    | A       | 89    |
| Rathan     | Data Science        | A       | 65    |
| Deekshith  | Automation Testing  | B       | 55    |
| Tyson      | Web dev             | B       | 50    |

## Running the App
To start the Streamlit application, use the following command:

```bash
streamlit run app.py
```

This will launch a local server where you can interact with the app.

## How It Works
1. **Enter a question**: You can ask the chatbot questions like "How many students are there?" or "Show me all students in Data Science class."
2. **Query generation**: The app converts your question into an SQL query using the Google Generative AI model.
3. **Execute query**: The generated SQL query is run against the `students.db` database.
4. **Display results**: The app shows the result of the query on the Streamlit interface.

### Example Questions:
- "How many students are there?"
- "Show me the students in Class 'Data Science'."
- "List all the students, who has above 80 MARKS"

## Technologies Used
- **Python**
- **Streamlit**: For building the web interface.
- **SQLite**: For storing and querying student data.
- **Google Generative AI (Gemini Pro)**: For converting natural language questions into SQL queries.
- **dotenv**: For managing environment variables.

## Project Structure
```bash
.
├── sqllite.py           # Script to create and populate the SQLite database
├── app.py               # Streamlit app code
├── students.db          # SQLite database (created after running sqllite.py)
├── requirements.txt     # Python packages required
├── Demo.mp4             # Demo Video
└── README.md            # Project documentation
```