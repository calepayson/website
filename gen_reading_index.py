import frontmatter
import mkdocs_gen_files
import os

from textwrap import dedent


class PostMetaData:
    def __init__(
        self,
        title: str,
        author: str,
        slug: str,
        description: str,
        date_read: str,
        draft: bool,
    ):
        self.title = title
        self.author = author
        self.slug = slug
        self.description = description
        self.date_read = date_read
        self.draft = draft

    def get_text_card(self) -> str:
        if self.draft:
            return ""
        else:
            return dedent(
                f"""
                ## [{self.title}](posts/{self.slug})
                <div class="dates">{self.author}</div>
                {self.description}
                <hr>
                """
            ).strip()


def get_all_post_paths() -> list[str]:
    files = os.listdir("docs/reading/posts")
    paths = [f"docs/reading/posts/{filename}" for filename in files]
    return paths


def get_post_metadata(path: str) -> PostMetaData:
    with open(path, "r") as f:
        post = frontmatter.load(f)
        return PostMetaData(**post.metadata)


def get_all_cards(paths: list[str]):
    content = ""
    metadata = []

    for path in paths:
        metadata.append(get_post_metadata(path))

    metadata = sorted(metadata, key=lambda x: x.date_read, reverse=True)

    for post in metadata:
        content += post.get_text_card()

    return content


def get_content() -> str:
    style = dedent(
        """
    <style>
    .dates {
        font-size: .7rem;
        color: #8b949e;
    }
    
    hr {
        background-color: #8b949e;
        border: none;
        height: 1px;
    }
    </style>
    """
    ).strip()

    post_paths = get_all_post_paths()
    cards = get_all_cards(post_paths)

    return style + cards


def main():
    with mkdocs_gen_files.open("reading/index.md", "w") as f:
        print(get_content(), file=f)


main()
