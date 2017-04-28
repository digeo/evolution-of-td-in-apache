METRICS_ALL = 'accessors,new_technical_debt,blocker_violations,conditions_to_cover,new_it_conditions_to_cover,new_conditions_to_cover,bugs,burned_budget,business_value,class_complexity_distribution,classes,code_smells,comment_lines,commented_out_code_lines,comment_lines_density,comment_lines_data,complexity,class_complexity,file_complexity,function_complexity,complexity_in_classes,complexity_in_functions,branch_coverage,new_it_branch_coverage,new_branch_coverage,conditions_by_line,confirmed_issues,coverage,new_it_coverage,coverage_line_hits_data,new_coverage,covered_conditions_by_line,critical_violations,last_commit_date,directories,duplicated_blocks,new_duplicated_blocks,duplicated_files,duplicated_lines,duplicated_lines_density,new_duplicated_lines,new_duplicated_lines_density,duplications_data,effort_to_reach_maintainability_rating_a,executable_lines_data,false_positive_issues,file_complexity_distribution,files,function_complexity_distribution,functions,generated_lines,generated_ncloc,info_violations,violations,it_conditions_to_cover,it_branch_coverage,it_conditions_by_line,it_coverage,it_coverage_line_hits_data,it_covered_conditions_by_line,it_line_coverage,it_lines_to_cover,it_uncovered_conditions,it_uncovered_lines,line_coverage,new_it_line_coverage,new_line_coverage,lines,ncloc,ncloc_language_distribution,new_lines,lines_to_cover,new_it_lines_to_cover,new_lines_to_cover,sqale_rating,new_maintainability_rating,major_violations,minor_violations,ncloc_data,new_blocker_violations,new_bugs,new_code_smells,new_critical_violations,new_info_violations,new_violations,new_major_violations,new_minor_violations,new_vulnerabilities,open_issues,overall_conditions_to_cover,new_overall_conditions_to_cover,overall_branch_coverage,new_overall_branch_coverage,overall_conditions_by_line,overall_coverage,overall_coverage_line_hits_data,new_overall_coverage,overall_covered_conditions_by_line,overall_line_coverage,new_overall_line_coverage,overall_lines_to_cover,new_overall_lines_to_cover,overall_uncovered_conditions,new_overall_uncovered_conditions,overall_uncovered_lines,new_overall_uncovered_lines,quality_profiles,projects,public_api,public_documented_api_density,public_undocumented_api,quality_gate_details,alert_status,reliability_rating,new_reliability_rating,reliability_remediation_effort,new_reliability_remediation_effort,reopened_issues,security_rating,new_security_rating,security_remediation_effort,new_security_remediation_effort,skipped_tests,development_cost,statements,team_size,sqale_index,sqale_debt_ratio,new_sqale_debt_ratio,uncovered_conditions,new_it_uncovered_conditions,new_uncovered_conditions,uncovered_lines,new_it_uncovered_lines,new_uncovered_lines,test_data,test_execution_time,test_errors,test_failures,test_success_density,tests,vulnerabilities,wont_fix_issues'
METRICS_NOTNULL = 'blocker_violations,bugs,classes,code_smells,comment_lines,comment_lines_density,complexity,class_complexity,file_complexity,function_complexity,complexity_in_classes,complexity_in_functions,confirmed_issues,critical_violations,last_commit_date,directories,duplicated_blocks,duplicated_files,duplicated_lines,duplicated_lines_density,effort_to_reach_maintainability_rating_a,false_positive_issues,file_complexity_distribution,files,function_complexity_distribution,functions,info_violations,violations,lines,ncloc,ncloc_language_distribution,sqale_rating,major_violations,minor_violations,open_issues,quality_profiles,quality_gate_details,alert_status,reliability_rating,reliability_remediation_effort,reopened_issues,security_rating,security_remediation_effort,development_cost,statements,sqale_index,sqale_debt_ratio,vulnerabilities,wont_fix_issues'
METRICS_NOTNULL_NOTSTRING = 'blocker_violations,bugs,classes,code_smells,comment_lines,comment_lines_density,complexity,class_complexity,file_complexity,function_complexity,complexity_in_classes,complexity_in_functions,confirmed_issues,critical_violations,last_commit_date,directories,duplicated_blocks,duplicated_files,duplicated_lines,duplicated_lines_density,effort_to_reach_maintainability_rating_a,false_positive_issues,files,functions,info_violations,violations,lines,ncloc,major_violations,minor_violations,open_issues,reliability_remediation_effort,reopened_issues,security_remediation_effort,development_cost,statements,sqale_index,sqale_debt_ratio,vulnerabilities,wont_fix_issues'
METRICS_NOTNULL_NOTSTRING_NOTLASTITEMVALUE = 'blocker_violations,bugs,classes,code_smells,comment_lines,comment_lines_density,complexity,class_complexity,file_complexity,function_complexity,confirmed_issues,critical_violations,last_commit_date,directories,duplicated_blocks,duplicated_files,duplicated_lines,duplicated_lines_density,effort_to_reach_maintainability_rating_a,false_positive_issues,files,functions,info_violations,violations,lines,ncloc,major_violations,minor_violations,open_issues,reliability_remediation_effort,reopened_issues,security_remediation_effort,development_cost,statements,sqale_index,sqale_debt_ratio,vulnerabilities,wont_fix_issues'
METRICS_ECSA = 'complexity,class_complexity,file_complexity,function_complexity,comment_lines,comment_lines_density,duplicated_blocks,duplicated_files,duplicated_lines,duplicated_lines_density,violations,blocker_violations,critical_violations,major_violations,minor_violations,info_violations,open_issues,code_smells,sqale_index,sqale_debt_ratio,bugs,reliability_remediation_effort,vulnerabilities,security_remediation_effort,classes,directories,files,lines,ncloc,functions,statements'
METRICS = METRICS_ECSA
METRICS_LIST = METRICS.split(',')
metrics_list_length = len(METRICS_LIST)

#esolved=false
resolutions = 'FALSE-POSITIVE,WONTFIX,FIXED,REMOVED'.split(',')
severities = 'INFO,MINOR,MAJOR,CRITICAL,BLOCKER'.split(',')
types = 'CODE_SMELL,BUG,VULNERABILITY'.split(',')

SONARQUBE_PORT = '9000'
REST_API_PORT = '8080'
PS = 500

COMMIT_STATS_API_URL = '/GitHubCommitStatsRest/webresources/commitstatsfiles/repo/'
COMMIT_STATS_API_CACHE_URL = '/GitHubCommitStatsCache/webresources/commitsstats/json/'
COMMIT_STATS_FILES_API_URL = '/api/commitStatsFiles'
COMMIT_STATS_FILES_PER_REPO_API_URL = COMMIT_STATS_FILES_API_URL + '/repo/'
REST_URL = COMMIT_STATS_FILES_PER_REPO_API_URL

PROTOCOL = 'http://'

class GitHubProject:
    def __init__(self, repo_id, owner, repo, language, sonarqube_ip, rest_api_ip = '195.251.210.166'):
        self.repo_id = repo_id
        self.owner = owner
        self.repo = repo
        self.language = language
        self.sonarqube_ip = sonarqube_ip
        self.rest_api_ip = rest_api_ip
        self.sonarqube_project_key = self.owner+':'+self.repo
        self.rest_key = self.owner+'/'+self.repo
        self.timemachine_metrics_url = PROTOCOL + self.sonarqube_ip + ':' + SONARQUBE_PORT + '/api/'+ 'timemachine?' + 'resource=' + self.sonarqube_project_key + '&metrics='
        self.issues_url = PROTOCOL + self.sonarqube_ip + ':' + SONARQUBE_PORT + '/api/'+ 'issues/search?' + 'projectKeys=' + self.sonarqube_project_key + '&languages=' + self.language.lower() + '&ps=' + str(PS)
        self.commit_stats_url = PROTOCOL + self.rest_api_ip + ':' + REST_API_PORT + REST_URL + str(self.repo_id)