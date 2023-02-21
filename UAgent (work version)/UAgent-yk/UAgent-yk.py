#!usr/bin/env python3
# encoding: utf-8

import requests
from cortexutils.analyzer import Analyzer


class UserAgentAnalyzer(Analyzer):
    def __init__(self):
        Analyzer.__init__(self)

    def run(self):
        try:
            if self.data_type == 'user-agent':
                #Input data
                user_agent = self.get_data()
                url = 'https://user-agents.net/parser'
                payload = {'action' : 'parse',
                            'format' : 'json',
                            'string' : user_agent}

                r = requests.post(url, data = payload)
                if not r.ok:
                    self.error('Unable to connect to user-agents.net\n')
                try:
                    result = r.json()
                    
                    url2 = 'https://user-agents.net/string/'
                    user_agent = user_agent.lower()
                    user_agent_new = ''
                    for i in user_agent:
                        if not i.isdigit() and not i.isalpha():
                            user_agent_new += '-'
                        else:
                            user_agent_new += i
                    url2 += user_agent_new.replace('--', '-')
                    if url2[-1] == '-':
                        url2 = url2[:-1]
                    if '--' in url2:
                        url2 = url2.replace('--', '-')

                    result['url'] = url2
                    
                    self.report(result)
                except Exception:
                    self.error('Invalid input data')
            else:
                self.notSupported()
        except Exception as e:
            self.unexpectedError(e)


if __name__ == '__main__':
    UserAgentAnalyzer().run()
