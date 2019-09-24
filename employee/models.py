from mongoengine import Document, EmbeddedDocument, fields

class projects(EmbeddedDocument):
    projectId = fields.IntField(required=True, null=False)
    projectName = fields.StringField(max_length=10, required=True, null=False)
    startDate = fields.DateTimeField()
    endDate = fields.DateTimeField()
    

class skills(EmbeddedDocument):
    technology = fields.StringField(max_length=50, required=True, null=False)
    exp = fields.StringField(max_length=50, required=True)
    level = fields.StringField(max_length=50, required=True)
    

class employees(Document):
    empId = fields.IntField(required=True, null=False)
    empName = fields.StringField(max_length=10, required=True, null=False)
    worklocation = fields.StringField(max_length=10, required=True, null=False)
    projects = fields.EmbeddedDocumentListField(projects)
    skills = fields.EmbeddedDocumentListField(skills)
