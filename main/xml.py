NAME_XML_QUERY = '''<?xml version="1.0"?>
<!DOCTYPE PCT-Data PUBLIC "-//NCBI//NCBI PCTools/EN" "NCBI_PCTools.dtd">
<PCT-Data>
  <PCT-Data_input>
    <PCT-InputData>
      <PCT-InputData_query>
        <PCT-Query>
          <PCT-Query_type>
            <PCT-QueryType>
              <PCT-QueryType_id-exchange>
                <PCT-QueryIDExchange>
                  <PCT-QueryIDExchange_input>
                    <PCT-QueryUids>
                      <PCT-QueryUids_synonyms>
                        {}
                      </PCT-QueryUids_synonyms>
                    </PCT-QueryUids>
                  </PCT-QueryIDExchange_input>
                  <PCT-QueryIDExchange_operation-type value="same"/>
                  <PCT-QueryIDExchange_output-type value="synonyms"/>
                  <PCT-QueryIDExchange_output-method value="file-pair"/>
                  <PCT-QueryIDExchange_compression value="none"/>
                </PCT-QueryIDExchange>
              </PCT-QueryType_id-exchange>
            </PCT-QueryType>
          </PCT-Query_type>
        </PCT-Query>
      </PCT-InputData_query>
    </PCT-InputData>
  </PCT-Data_input>
</PCT-Data>'''  # to send a list of synonyms to the pubchem identifier exchange service

NAME_SMALL = '''<PCT-QueryUids_synonyms_E>{}</PCT-QueryUids_synonyms_E>'''

PUGURL = "https://pubchem.ncbi.nlm.nih.gov/pug/pug.cgi" #where to send xml queries

POLL_QUERY = '''<PCT-Data>
  <PCT-Data_input>
    <PCT-InputData>
      <PCT-InputData_request>
        <PCT-Request>
          <PCT-Request_reqid>{}</PCT-Request_reqid>
          <PCT-Request_type value="status"/>
        </PCT-Request>
      </PCT-InputData_request>
    </PCT-InputData>
  </PCT-Data_input>
</PCT-Data>'''  # a query to ask whether the potentially long-running job has finished yet