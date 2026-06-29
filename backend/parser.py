import frontmatter

def parse_problem_file(filepath):
    with open(filepath) as f:
        post = frontmatter.load(f)

    title = post['title']
    body = post.content

    if "## Problem" in body and "## Solution" in body:
       problem = body.split("## Solution")[0].replace("## Problem", "").strip()
       solution = body.split("## Solution")[1].strip()
       return title, problem, solution
    else:
        return 'Check the .md file again!'
