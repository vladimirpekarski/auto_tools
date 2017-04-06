from idlelib.AutoComplete import AutoComplete


class CustomAutoComplete(AutoComplete):
    def fetch_completions(self, what, mode):
        if what == "":
            return ['test', 'test2'], ['test', 'test2']
        else:
            return ['sub1', 'sub2'], ['sub2', 'sub3']
