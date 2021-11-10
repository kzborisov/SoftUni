class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category):
        if category in self.categories:
            return
        self.categories.append(category)

    def add_topic(self, topic):
        if topic in self.topics:
            return
        self.topics.append(topic)

    def add_document(self, document):
        if document in self.documents:
            return
        self.documents.append(document)

    def edit_category(self, category_id, new_name):
        category = self.__get_object_by_id(self.categories, category_id)
        category.edit(new_name)

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        topic = self.__get_object_by_id(self.topics, topic_id)
        topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id, new_file_name):
        document = self.__get_object_by_id(self.documents, document_id)
        document.edit(new_file_name)

    def delete_category(self, category_id):
        category = self.__get_object_by_id(self.categories, category_id)
        if category not in self.categories:
            return

        self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = self.__get_object_by_id(self.topics, topic_id)
        if topic not in self.topics:
            return

        self.topics.remove(topic)

    def delete_document(self, document_id):
        document = self.__get_object_by_id(self.documents, document_id)
        if document not in self.documents:
            return

        self.documents.remove(document)

    def get_document(self, document_id):
        return self.__get_object_by_id(self.documents, document_id)

    @staticmethod
    def __get_object_by_id(objects, object_id):
        all_object = [x for x in objects if x.id == object_id]
        return all_object[0]

    def __repr__(self):
        return "\n".join([str(x) for x in self.documents])
