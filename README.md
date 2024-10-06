
# grade.ai

**grade.ai** is an AI-assisted evaluator tool designed to simplify the grading process for educators. This tool leverages advanced AI models to validate student answers, making the assessment process more efficient and accurate. Teachers can use this platform to upload question papers, schema, and relevant batch information. Once student answer PDFs are uploaded, they are converted into text, evaluated against the schema, and presented in a dashboard with detailed scores and analytics.

## Project Overview

The platform includes the following features:
- **Teacher Interface**: Allows educators to add question papers, grading schema, and batch-specific information.
- **Student Answer Evaluation**: Automatically converts uploaded PDFs of student answers into text for AI-based evaluation.
- **Dashboard**: Displays detailed scoring and insightful analytics on student performance.

## Tech Stack
- **Front-end**: React.js
- **Back-end**: Flask and Python
- **API Service**: OpenAI
- **Database**: PostgreSQL

## How It Works
1. **Input Questions and Schema**: Teachers can input questions and define the evaluation schema for each question set.
2. **Upload Student Answers**: PDFs containing student answers are uploaded, converted to text, and stored in the database.
3. **AI-Powered Evaluation**: The tool evaluates student responses based on the schema using OpenAI's language model.
4. **Visualization and Analytics**: Scores are displayed on a dashboard, offering insights and visual representation for easy comprehension.

## Getting Started
To get started with `grade.ai`:
1. Clone the repository.
2. Install the dependencies for both the front-end and back-end.
3. Set up the database and environment variables.
4. Run the React front-end and Flask back-end.
5. Access the dashboard to view evaluation results.

## Installation
```bash
# Clone the repository
git clone https://github.com/your-username/grade.ai.git

# Navigate into the project directory
cd grade.ai

# Install front-end dependencies
cd frontend
npm install

# Install back-end dependencies
cd ../backend
pip install -r requirements.txt
```

## Usage
1. Start the front-end server:
   ```bash
   cd frontend
   npm start
   ```

2. Start the back-end server:
   ```bash
   cd backend
   python app.py
   ```

3. Access the application at `http://localhost:3000`.

## Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License.
