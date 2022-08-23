### _Description_
<!-- 
Add a short summary of your changes below. 
You can also leave notes for code reviewers here.
-->

--- 

### _Pull Request Checklist for dbt models_
- [ ] PR title is prefixed with `[UPDATE]` for changes, `[NEW]` for additions, or `[REMOVE]` for deletions
- [ ] PR title includes descriptive commentary of changes after prefix  
- [ ] PR description includes link or reference to user story, ticket, or work approval  

--- 

### _Style & Structure_  
- [ ] The model is correctly named per the specification in repository wiki  
- [ ] The model adheres to the style guide found in the repository wiki  
- [ ] The model uses `{{ ref('') }}` when referencing existing models  
  - The model is altered in the `_<schema>_models.yml` file
  - The model has a valid `description`, `alias`, and `columns` list  
- [ ] The commits are related to the pull request and do not contain any work from a different work stream  
- [ ] The commits for _**each**_ model have been compiled and tested in a pre-production environment:  
  - Run `dbt compile -m [MODEL_NAME_HERE]`
  - Run `dbt run -m [MODEL_NAME_HERE]`
  - Run `dbt test -m [MODEL_NAME_HERE]`
- [ ] The `dbt_project.yml` configuration has not been altered without repository owner approval  
- [ ] The `_<schema>_sources.yml` configuration has not been altered without repository owner approval  
