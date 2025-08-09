import frontmatter
import mkdocs_gen_files

from textwrap import dedent


class PostMetaData:
    def __init__(
        self,
        title: str,
        slug: str,
        description: str,
        date_created: str,
        date_modified: str | None = None,
        draft: str = "true",
    ):
        self.title = title
        self.slug = slug
        self.description = description
        self.date_created = date_created
        self.date_modified = date_modified
        self.draft = False if draft == "false" else True

    def get_text_card(self) -> str:
        style = dedent(
            """
        <style>
        .dates {
            font-size: .7rem;
            color: #8b949e;
        }
        </style>
        """
        ).strip()

        text = dedent(
            f"""
            ## [{self.title}](/posts/{self.slug})
            <div class="dates">Created: {self.date_created}</div>
            {self.description}
            <hr style="background-color: #8b949e; border: none; height: 1px;">
            """
        ).strip()

        return style + text


def get_post_metadata(path: str) -> PostMetaData:
    with open(path, "r") as f:
        post = frontmatter.load(f)
        return PostMetaData(**post.metadata)


def get_content() -> str:
    metadata = get_post_metadata("docs/writing/posts/darwin_machines.md")
    style = dedent(
        """
    <style>
    .dates {
        font-size: .7rem;
        color: #8b949e;
    }
    </style>
    """
    ).strip()

    return style + metadata.get_text_card()


def main():
    with mkdocs_gen_files.open("writing/index.md", "w") as f:
        print(get_content(), file=f)


main()
