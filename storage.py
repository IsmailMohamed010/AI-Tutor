class Storage:
    def __init__(self, questions_file="Questions.txt", responses_file="Responses.txt", qna_file="QnA.txt"):
        self.questions_file = questions_file
        self.responses_file = responses_file
        self.qna_file = qna_file

    def save_question(self, question):
        with open(self.questions_file, "a", encoding="utf-8") as f:
            f.write(question + "\n")

    def save_response(self, response):
        with open(self.responses_file, "a", encoding="utf-8") as f:
            f.write(response + "\n")

    def save_qna(self, question, response):
        with open(self.qna_file, "a", encoding="utf-8") as f:
            f.write(f"Q: {question}\nA: {response}\n\n")
