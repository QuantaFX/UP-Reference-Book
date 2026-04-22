import os

def generate_tex_files(structure_dir="structure", out_tex_dir="tex", docs_dir="_docs"):
    for root, _, files in os.walk(structure_dir):
        for f in files:
            if not f.endswith(".md"):
                continue

            in_path = os.path.join(root, f)
            fout_tex = os.path.join(out_tex_dir, f.replace(".md", ".tex"))
            
            print(f"Generating LaTeX layout: {fout_tex}")
            os.makedirs(os.path.dirname(fout_tex), exist_ok=True)

            with open(in_path, "r", encoding="utf-8") as file:
                lines = file.read().splitlines()

            if not lines:
                continue

            with open(fout_tex, "w", encoding="utf-8") as out:
                clean_section_title = lines[0].strip().replace('_', ' ')
                print(f"\\section{{{clean_section_title}}}", file=out)
                for line in lines[1:]:
                    if not line.strip():
                        continue
                        
                    num_spaces = len(line) - len(line.lstrip())
                    depth_level = num_spaces // 2
                    
                    clean_line = line.lstrip(" -*")
                    blocks = [b.strip() for b in clean_line.split("|")]
                    
                    if "comment" in blocks:
                        continue
                        
                    target = blocks[-1]
                    indent_str = " " * num_spaces
                    sub_str = "sub" * depth_level + "section"

                    if target.endswith((".py", ".cpp", ".java", ".sh")):
                        
                        clean_title = target.split('.')[0].replace('_', ' ').title()
                        
                        if "black" in blocks:
                            print(f"{indent_str}\\{sub_str}Black{{{clean_title}}}", file=out)
                        elif "red" in blocks:
                            print(f"{indent_str}\\{sub_str}Red{{{clean_title}}}", file=out)
                        else:
                            print(f"{indent_str}\\{sub_str}{{{clean_title}}}", file=out)
                        # --------------------------------------

                        category_name = f[:-3] 
                        doc_filename = ".".join(target.split(".")[:-1]) + ".md"
                        fdocs = os.path.join(docs_dir, category_name, doc_filename)
                        
                        if os.path.exists(fdocs):
                            with open(fdocs, "r", encoding="utf-8") as fdocs_file:
                                for doc_line in fdocs_file:
                                    if doc_line.strip():
                                        print(f"{indent_str}{doc_line}", end="", file=out)
                        
                        print(f"{indent_str}\\pycode{{{category_name}/{target}}}", file=out)
                        
                    else:
                        if "black" in blocks:
                            print(f"{indent_str}\\{sub_str}Black{{{target}}}", file=out)
                        elif "red" in blocks:
                            print(f"{indent_str}\\{sub_str}Red{{{target}}}", file=out)
                        else:
                            print(f"{indent_str}\\{sub_str}{{{target}}}", file=out)

if __name__ == "__main__":
    print("--- LaTeX Generation Started ---")
    generate_tex_files()
    print("--- LaTeX Generation Finished ---")