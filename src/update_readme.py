import re
from pathlib import Path
from generate_mermaid_er_diagram import generate_mermaid
from toolmeta_models import ToolGeneric

README = Path("README.md")

def update_readme(mermaid_block):
    content = README.read_text()

    new_content = re.sub(
        r"<!-- BEGIN ERD -->.*?<!-- END ERD -->",
        f"<!-- BEGIN ERD -->\n{mermaid_block}\n<!-- END ERD -->",
        content,
        flags=re.DOTALL,
    )

    README.write_text(new_content)


mermaid = generate_mermaid(ToolGeneric.__table__)
update_readme(mermaid)
