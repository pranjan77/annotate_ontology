#BEGIN_HEADER
import logging
import os
import shutil
import uuid
from installed_clients.DataFileUtilClient import DataFileUtil
from installed_clients.KBaseReportClient import KBaseReport
#END_HEADER
#BEGIN_CLASS_HEADER
#END_CLASS_HEADER
#BEGIN_CONSTRUCTOR
        self.callback_url = os.environ['SDK_CALLBACK_URL']
        self.shared_folder = config['scratch']
        logging.basicConfig(format='%(created)s %(levelname)s: %(message)s',
                            level=logging.INFO)
#END_CONSTRUCTOR
#BEGIN run_annotate_ontology
        report = KBaseReport(self.callback_url)
        report_name = 'annotate_ontology' + str(uuid.uuid4())

        html_src = "/kb/module/report"
        html_dest = os.path.join(self.shared_folder, "report")

        shutil.copytree(html_src, html_dest)

        dfu = DataFileUtil(self.callback_url)
  
        report_shock_id = dfu.file_to_shock({'file_path': html_dest,
                                            'pack': 'zip'})['shock_id']

        html_file = {
            'shock_id': report_shock_id,
            'name': 'index.html',
            'label': 'index.html',
            'description': 'Ontology HTML report'
            }
        
        report_info = report.create_extended_report({
                        'direct_html_link_index': 0,
                        'html_links': [html_file],
                        'report_object_name': report_name,
                        'workspace_name': params['workspace_name']
                    })
        output = {
            'report_name': report_info['name'],
            'report_ref': report_info['ref'],
        }
#END run_annotate_ontology
#BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
#END_STATUS
