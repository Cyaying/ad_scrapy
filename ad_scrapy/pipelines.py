import json
import codecs


class AdScrapyPipeline:
    def __init__(self):
        self.class_dir = {
            "ADC新闻": 0,
            "认识AD": 1,
            "AD防治": 2,
            "护理康复": 3,
            "AD资讯": 4,
            "政策法规": 5,
        }
        self.fp = None
        self.alls = []
        for i in range(6):
            self.alls.append([])

    def open_spider(self, spider):
        print('********** start ... **********')
        self.fp = codecs.open('./AD_articles.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        item = dict(item)
        id = self.class_dir[item['category']]
        self.alls[id].append(item)
        return item

    def close_spider(self, spider):
        self.fp.write(json.dumps(self.alls, ensure_ascii=False))
        self.fp.close()
        print('**********  end !!!  **********')
