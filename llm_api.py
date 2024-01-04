import guardrails as gd
from pydantic_class import ApplicantInfo
import cohere
import json
import openai


class LLMApi:
    def __init__(self) -> None:
        self.prompt = """
            Given the following resume about an applicant, please extract a dictionary that contains the applicants skill and experience

            ${resume_text}

            ${gr.complete_json_suffix_v2}
            """

    def call_llm(self,text):
        guard = gd.Guard.from_pydantic(output_class=ApplicantInfo, prompt=self.prompt)
        cohere_client = cohere.Client(api_key="fNVIubcfeafrzEkgoybBAJAnQmA4Hk6uIsrmwIrs")
        res = guard(
            cohere_client.generate,
            prompt_params={"resume_text": text},
            model="command-nightly",
            max_tokens=8000,
        )

        return json.dumps(res.validated_output, indent=2)


