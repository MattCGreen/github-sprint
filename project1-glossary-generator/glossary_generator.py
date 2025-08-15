# glossary_generator.py
import csv
import json

def load_terms(file_path):
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        return {row[0]: row[1] for row in reader}

def export_markdown(terms, output_path):
    with open(output_path, 'w') as f:
        for term, definition in terms.items():
            f.write(f"## {term}\n{definition}\n\n")

def export_json(terms, output_path):
    with open(output_path, 'w') as f:
        json.dump(terms, f, indent=4)

if __name__ == "__main__":
    terms = load_terms('terms.csv')
    export_markdown(terms, 'glossary.md')
    export_json(terms, 'glossary.json')
