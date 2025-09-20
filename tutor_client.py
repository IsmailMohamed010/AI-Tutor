from openai import OpenAI
from config import GITHUB_TOKEN, ENDPOINT, MODEL_NAME
from rate_limiter import RateLimiter

class TutorClient:
    def __init__(self):
        self.client = OpenAI(base_url=ENDPOINT, api_key=GITHUB_TOKEN)
        self.rate_limiter = RateLimiter(min_interval=30)

        self.explanation_levels = {
            1: "like I'm 5 years old",
            2: "like I'm 10 years old",
            3: "like a high school student",
            4: "like a college student",
            5: "like an expert in the field",
            6: "like an Einstein PhD-level mad scientist"
        }

    def ask(self, question, level):
        allowed, wait_time = self.rate_limiter.can_request()
        if not allowed:
            return f"⏳ Please wait {wait_time} seconds before your next question."

        level_description = self.explanation_levels.get(level, "clearly and concisely")
        system_prompt = f"You are a helpful and patient AI Tutor. Explain concepts {level_description}."

        try:
            response = self.client.chat.completions.create(
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": question}
                ],
                model=MODEL_NAME,
                temperature=0.7,
                stream=True
            )

            full_response = ""
            for chunk in response:
                if chunk.choices[0].delta and chunk.choices[0].delta.content:
                    text_chunk = chunk.choices[0].delta.content
                    full_response += text_chunk
                    yield full_response

        except Exception as e:
            error_msg = str(e)
            if "429" in error_msg:
                yield "⚠️ Rate limit reached. Please wait about 60 seconds."
            elif "401" in error_msg:
                yield "❌ Authentication error. Check your GITHUB_TOKEN."
            elif "403" in error_msg:
                yield "❌ Access forbidden. Check API permissions."
            else:
                yield f"❌ Unexpected error: {error_msg}"
