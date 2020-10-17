import wikipedia


def print_dict(dict):
    for key, arg in dict.items():
        print(f"{key}: {arg};")


class Wiki():
    def __init__(self, search_keyword):
        self.search_keyword = search_keyword
        self.results_number = 10


    def get_sugestions(self):
        self.sugestions = wikipedia.search(self.search_keyword,
                                          self.results_number,
                                          True)[0] #retunr a tule in wich the first element is a list with the results


    def is_sugestion_empty(self):
        if len(self.sugestions) == 0:
            return True
        else:
            return False


    def organize_sugestions(self):
        self.organized_sugestions = {}
        for sugestion in range(len(self.sugestions)):
            self.organized_sugestions[sugestion+1] = self.sugestions[sugestion]


    def get_page(self, page_number):
        try:
            self.wiki_page = wikipedia.WikipediaPage(self.organized_sugestions[page_number])
        except:
            return "Number out of range"
        else:
            return self.wiki_page.summary



def run():
    search = input("Enter searh: ")
    wiki = Wiki(search)
    wiki.get_sugestions()
    if wiki.is_sugestion_empty():
        print("No search results!!!")
        return None #To end the process...
    else:
        pass
    wiki.organize_sugestions()
    print_dict(wiki.organized_sugestions)
    page = input("Enter page number: ")
    result = wiki.get_page(int(page))
    print(result)


while True:
    run()


#print_dict(a)
