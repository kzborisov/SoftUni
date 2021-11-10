class Document:
    def __init__(self, document_id, category_id, topic_id, file_name):
        self.id = document_id
        self.category_id = category_id
        self.topic_id = topic_id
        self.file_name = file_name
        self.tags = []

    @classmethod
    def from_instances(cls, document_id, category, topic, file_name):
        return cls(document_id, category.id, topic.id, file_name)

    def add_tag(self, tag_content):
        if tag_content in self.tags:
            return
        self.tags.append(tag_content)

    def remove_tag(self, tag_content):
        if tag_content not in self.tags:
            return
        self.tags.remove(tag_content)

    def edit(self, file_name):
        self.file_name = file_name

    def __repr__(self):
        return f"Document {self.id}: {self.file_name}; " \
               f"category {self.category_id}, " \
               f"topic {self.topic_id}, " \
               f"tags: {', '.join(self.tags)}"
