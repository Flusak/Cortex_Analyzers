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

                r = requests.post('https://user-agents.net/parser', data = payload)
                if not r.ok:
                    self.error('Unable to connect to user-agents.net\n')
                try:
                    result = r.json()
                    self.report(result)
                except Exception:
                    self.error('Invalid input data')
            else:
                self.notSupported()
        except Exception as e:
            self.unexpectedError(e)


if __name__ == '__main__':
    UserAgentAnalyzer().run()
