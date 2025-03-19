def parse_documents(documents: list):
    for doc in documents:
        doc["id"] = str(doc["_id"])
    return documents


def parse_document(document):
    if document is None:
        return None
    temp = document.copy()
    temp["id"] = str(temp["_id"])
    return temp
