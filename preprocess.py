import os
from pathlib import Path

MARGIN = 70
COMMENTS = ['"""', "'''", "/*", "*/"]

def generate_codes_and_docs(in_dir="code", out_code_dir="_code", out_docs_dir="_docs"):
    for root, _, files in os.walk(in_dir):
        for f in files:
            if not (f.endswith(".py") or f.endswith(".cpp") or f.endswith(".sh") or f.endswith(".java")):
                continue
            if f.endswith(".test.py") or f.endswith(".test.cpp"):
                continue

            in_path = os.path.join(root, f)
            
            rel_path = os.path.relpath(root, in_dir)
            fout_code = os.path.join(out_code_dir, rel_path, f)
            fout_docs = os.path.join(out_docs_dir, rel_path, os.path.splitext(f)[0] + ".md")

            print(f"Processing: {in_path} -> {fout_code}")

            os.makedirs(os.path.dirname(fout_code), exist_ok=True)
            os.makedirs(os.path.dirname(fout_docs), exist_ok=True)

            with open(in_path, "r", encoding="utf-8") as file:
                dat = file.read().splitlines()

            docs = []
            
            with open(fout_code, "w", encoding="utf-8") as out:
                warning = False
                error = False
                last_line_error = False
                is_doc_line = 0
                
                for line in dat:
                    if line.strip() in COMMENTS:
                        is_doc_line = 1 - is_doc_line
                        continue
                    elif is_doc_line == 1:
                        docs.append(line.strip())
                        continue

                    last_line_error = False
                    
                    stripped = line.lstrip(" ")
                    leading_spaces = len(line) - len(stripped)
                    
                    if leading_spaces > 0:
                        stripped = " " + stripped
                        leading_spaces -= 1
                        
                    formatted_line = "-" * leading_spaces + stripped
                    
                    if len(formatted_line) > MARGIN:
                        print(formatted_line, file=out)
                        warning = True
                        last_line_error = True
                        if len(formatted_line) > MARGIN + 4:
                            error = True
                    else:
                        if len(formatted_line) < MARGIN:
                            formatted_line += " "
                        print(formatted_line.ljust(MARGIN, "-"), file=out)

            with open(fout_docs, "w", encoding="utf-8") as out:
                print(" ".join(docs), file=out)

            if last_line_error:
                error = True
            if error:
                print(f"  [ERROR] Code too wide: {in_path}")
            elif warning:
                print(f"  [WARNING] Code (almost) too wide: {in_path}")

if __name__ == "__main__":
    print("--- Preprocessing Started ---")
    generate_codes_and_docs()
    print("--- Preprocessing Finished ---")