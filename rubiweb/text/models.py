from django.db import models


#ADMIN
class Language(models.Model):
    code = models.CharField(max_length=2)
    label = models.CharField(max_length=200)
    extension = models.CharField(max_length=3)
    def __str__(self):
        return self.code
    class Meta:
        db_table = "language"

class AppParameters(models.Model):
    last_document_refreshDate = models.DateTimeField('Last Document Refresh Date', blank=True, null=True)
    last_tmpResult_refreshDate = models.DateTimeField('Last Temporary Results Refresh Date', blank=True, null=True)
    last_aggregate_refreshDate = models.DateTimeField('Last Aggregates Refresh Date', blank=True, null=True)

    class Meta:
        db_table = "app_parameters"

class Status(models.Model):
    code = models.CharField(max_length=2)
    label = models.CharField(max_length=200)
    def __str__(self):
        return self.label
    class Meta:
        db_table = "status"

#Classification and basxe objects
class Domain(models.Model):
    label = models.CharField(max_length=255)   
    def __str__(self):
        return self.label
    class Meta:
        db_table = "domain"

class Word(models.Model):
    label = models.CharField(max_length=255)
    ngram = models.IntegerField(blank=True, null=True)   
    def __str__(self):
        return self.label
    class Meta:
        db_table = "word"

# cutom lists
class DomainList(models.Model):
    label = models.CharField(max_length=255)   
    public = models.BooleanField()
    date_creation = models.DateTimeField('Date creation', auto_now_add=True, blank=True, null=True)
    date_modification = models.DateTimeField('Date modification', auto_now=True, blank=True, null=True)
    def __str__(self):
        return self.label
    class Meta:
        db_table = "domain_list"

class FocusList(models.Model):
    label = models.CharField(max_length=255)   
    public = models.BooleanField()
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children',  on_delete=models.CASCADE)
    words = models.ManyToManyField(Word)
    priority = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return self.label
    class Meta:
        db_table = "focus_list"
    

# Primary objects
class Document(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField('Date as in the document Metadata', auto_now_add=True, blank=True, null=True)
    url = models.CharField(max_length=2000)
    content = models.TextField(blank=True, null=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, null=True)
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.title
    class Meta:
        db_table = "document"

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000, blank=True,null=True)
    priority = models.IntegerField(blank=True, null=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, null=True)
    date_creation = models.DateTimeField('Date creation', auto_now_add=True, blank=True, null=True)
    date_modification = models.DateTimeField('Date modification', auto_now=True, blank=True, null=True)
    refresh_rate = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return self.name
    class Meta:
        db_table = "project"




#SEARCH objects
class GenericSearch(models.Model):
    key_word = models.CharField(max_length=200)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, blank=True, null=True)
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE, null=True, blank=True)
    exact_expression = models.BooleanField(default=False)
    date_creation = models.DateTimeField('Date creation', auto_now_add=True, blank=True, null=True)
    date_modification = models.DateTimeField('Date modification', auto_now=True, blank=True, null=True)
    def __str__(self):
        return self.key_word
    class Meta:
        db_table = "generic_search"

class ProjectSearch(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    generic_search = models.ForeignKey(GenericSearch, on_delete=models.CASCADE)
    priority = models.IntegerField(blank=True, null=True)
    date_creation = models.DateTimeField('Date creation', auto_now_add=True, blank=True, null=True)
    date_modification = models.DateTimeField('Date modification', auto_now=True, blank=True, null=True)
    def __str__(self):
        return self.generic_search.key_word + " - " +  self.generic_search.language.code
    class Meta:
        db_table = "project_search"


#SCRAP
class ScrapAction(models.Model):
    key_word = models.CharField(max_length=200)
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE, blank=True, null=True)
    date_creation = models.DateTimeField('Date creation', auto_now_add=True, blank=True, null=True)
    date_modification = models.DateTimeField('Date modification', auto_now=True, blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    nb_results = models.IntegerField(blank=True, null=True)
    nb_duplicates = models.IntegerField(blank=True, null=True)
    nb_existing_other_searches = models.IntegerField(blank=True, null=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, blank=True, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, default=1)
    generic_search = models.ForeignKey(GenericSearch, on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.label
    class Meta:
        db_table = "scrap_action"

#RESULTS OBJECTS        

class GoogleResult(models.Model):
    key_word = models.CharField(max_length=200)
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE, blank=True,null=True)
    rankn = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=2000, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    date_google = models.DateTimeField('Date Google', blank=True, null=True)
    date_scrap = models.DateTimeField('Date Scrapped', auto_now_add=True, blank=True, null=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.key_word
    class Meta:
        db_table = "google_result"

class SearchResult(models.Model):
    date_creation = models.DateTimeField('Date creation', auto_now_add=True, blank=True, null=True)
    generic_search = models.ForeignKey(GenericSearch, on_delete=models.CASCADE)
    google_result = models.ForeignKey(GoogleResult, on_delete=models.CASCADE)
    class Meta:
        db_table = "search_result"

class TmpGoogleResult(models.Model):
    key_word = models.CharField(max_length=200)
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE, null=True)
    action = models.ForeignKey(ScrapAction, on_delete=models.CASCADE, null=True)
    rankn = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=2000, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    date_google = models.DateTimeField('Date Google', blank=True, null=True)
    date_scrap = models.DateTimeField('Date Scrapped', auto_now_add=True, blank=True, null=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.key_word
    class Meta:
        db_table = "tmp_google_result"

#custoom links
class ProjectFocusList(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    focus_list = models.ForeignKey(FocusList, on_delete=models.CASCADE)
    priority = models.IntegerField(blank=True, null=True)
    class Meta:
        db_table = "project_focus_list"




#API
class ExternalAPI(models.Model):
    name = models.CharField(max_length=255)   
    daily_limit = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return self.name
    class Meta:
        db_table = "external_api"

class ExternalAPIProjectQuota(models.Model):
    external_api = models.ForeignKey(ExternalAPI, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    daily_limit = models.IntegerField(blank=True, null=True)
    class Meta:
        db_table = "external_api_project_quota"

class ExternalAPIUsage(models.Model):
    date_creation = models.DateTimeField('Date creation', auto_now_add=True, blank=True, null=True)
    external_api = models.ForeignKey(ExternalAPI, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    nb_calls = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return self.label
    class Meta:
        db_table = "external_api_usage"


#Aggregates - not sure we will neeed this with spark + hadoop