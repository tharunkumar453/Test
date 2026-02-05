import json
class WriteInFile:
    @staticmethod
    def write_in_file(test_case_file):
        with test_case_file.test_cases.open("r") as json_file:
            testcaseJson=json.load(json_file)
            return testcaseJson