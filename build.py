import os
import subprocess
import shutil
import glob
import sys

def run_command(command, description):
    print(f"\n---> {description}")
    try:
        result = subprocess.run(command, text=True)
        if result.returncode != 0:
            print(f"\n[ERROR] {description} failed with exit code {result.returncode}.")
            sys.exit(1)
    except FileNotFoundError:
        print(f"\n[ERROR] Command not found: {command[0]}")
        print("Please ensure it is installed and added to your system PATH.")
        sys.exit(1)


def clean_up():
    print("\n---> Cleaning up temporary files...")

    temp_extensions = ['*.aux', '*.log', '*.toc', '*.out']
    for ext in temp_extensions:
        for file in glob.glob(ext):
            try:
                os.remove(file)
            except OSError:
                pass

    minted_dir = '_minted-notebook'
    if os.path.exists(minted_dir):
        try:
            shutil.rmtree(minted_dir)
        except OSError:
            pass

    print("Cleanup finished.")


def main():
    print("=== Starting Cross-Platform Build ===")

    run_command([sys.executable, 'preprocess.py'], "Running preprocess.py")
    run_command([sys.executable, 'generate_tex.py'], "Running generate_tex.py")

    latex_cmd = ['pdflatex', '-shell-escape', 'notebook.tex']
    run_command(latex_cmd, "Compiling LaTeX (Pass 1)")

    run_command(latex_cmd, "Compiling LaTeX (Pass 2)")
    clean_up()

    print("\n=== Build Complete! Check notebook.pdf ===")


if __name__ == "__main__":
    main()