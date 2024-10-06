from src import llm
from tqdm import tqdm

def evaluate_grader(questions, rubrics, answers):
    results = []

    for student in tqdm(answers, desc="Processing Students", unit="student"):
        student_id = student['student_id']
        student_results = {
            "student_id": student_id,
            "questions": []
        }

        for answer in tqdm(student['answers'], desc=f"Evaluating Answers for {student_id}", unit="answer", leave=False):
            question_id = answer['question_id']
            question = next(q for q in questions if q['id'] == question_id)
            max_score = question['max_score']
            relevant_rubrics = [r for r in rubrics if r['question_id'] == question_id]

            # Prepare the input for GetFromLLM
            input_text = (
                f"Here is the question:"
                f"Question: {question['question_text']}\n"
                f"Here is the student's answer:"
                f"Answer: {answer['response_text']}\n"
                f"Here is the rubric for evaluation:"
                f"Rubrics:\n" +
                "\n".join([f"- {rubric['criteria']}: {rubric['points']} points" for rubric in relevant_rubrics])
            )

            # Call GetFromLLM and get the response
            response = llm.get_from_llm(input_text)

            # Assuming response is a dict with 'current_score' and 'reason'
            student_results['questions'].append({
                "question_id": question_id,
                "question_text": question['question_text'],
                "max_score": max_score,
                "current_score": response['current_score'],
                "reason": response['reason'],
                "student_answer": answer['response_text'],  # Added student's answer
            })
        results.append(student_results)

    return results