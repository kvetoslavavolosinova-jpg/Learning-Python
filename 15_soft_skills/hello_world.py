class CodeQualityAnalyzer:
    def __init__(self, filename):
        self.filename = filename

    def generate_ai_prompt_template(self, role, task, format_spec):
        """
        Generates a perfect, structured prompt template for AI models.
        Adheres to the Context-Goal-Format rule.
        """
        prompt = f"""
[AI PROMPT TEMPLATE]
=========================================
ROLE/CONTEXT:
I am a {role}. I am working with supply chain datasets.

GOAL:
I need you to help me with the following task:
{task}

OUTPUT FORMAT:
Please provide the output in this format:
{format_spec}
=========================================
"""
        return prompt


if __name__ == "__main__":
    print("=== CHAPTER 15: CLEAN CODE & AI COLLABORATION ===")
    
    # 1. Demonstrating Clean Code Practices (Docstring & Clear Naming)
    print("\n[INFO] Initializing Clean Code Quality System...")
    analyzer = CodeQualityAnalyzer("supplier_compliance.py")
    
    # Let's inspect our function's documentation (docstring) dynamically!
    print("Function Docstring:")
    print("-" * 50)
    print(analyzer.generate_ai_prompt_template.__doc__.strip())
    print("-" * 50)

    # 2. Creating a Perfect AI Prompt for your future Supplier ESG project!
    role = "Supply Chain Analyst specializing in supplier compliance"
    task = "Write a Pandas script to filter suppliers with an S-Rating below 3.0 and flag them as 'High Risk'."
    format_spec = "Python code using PEP 8 standards, including a short docstring and a sample DataFrame."
    
    perfect_prompt = analyzer.generate_ai_prompt_template(role, task, format_spec)
    print(perfect_prompt)
    
    print("=== LESSON COMPLETED SUCCESSFULLY ===")
