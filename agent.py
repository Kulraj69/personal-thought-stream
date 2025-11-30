import os
import datetime
from openai import OpenAI

def get_context():
    try:
        with open("life_context.md", "r") as f:
            return f.read()
    except FileNotFoundError:
        return "No specific context provided."

def generate_entry(context):
    token = os.environ.get("HF_TOKEN")
    if not token:
        raise ValueError("HF_TOKEN environment variable is not set.")

    client = OpenAI(
        base_url="https://router.huggingface.co/v1",
        api_key=token,
    )

    prompt = f"""
    You are a reflective journaling assistant. Based on the following context about my life, generate a thoughtful, introspective journal entry for today.
    
    Context:
    {context}
    
    The entry should be personal, encouraging, and about 150-200 words long. Do not use a greeting or sign-off. Just the entry.
    """

    completion = client.chat.completions.create(
        model="meta-llama/Llama-3.1-8B-Instruct:nebius",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=500,
        temperature=0.7
    )
    
    return completion.choices[0].message.content

def update_journal(entry):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    new_content = f"\n\n## Entry: {timestamp}\n\n{entry}"
    
    with open("journal.md", "a") as f:
        f.write(new_content)

def main():
    print("Reading context...")
    context = get_context()
    
    print("Generating entry...")
    try:
        entry = generate_entry(context)
        print("Entry generated successfully.")
        
        print("Updating journal...")
        update_journal(entry)
        print("Journal updated.")
    except Exception as e:
        print(f"Error: {e}")
        exit(1)

if __name__ == "__main__":
    main()
