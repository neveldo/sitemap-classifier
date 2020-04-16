from scrapy.exceptions import DropItem
import re


class SmscrapperPipeline(object):

    def process_item(self, item, spider):
        if 'article' in item:
            item['article'] = self.remove_html_tags(item['article'])
            item['article'] = self.remove_useless_text(item['article'])
            item['article'] = self.remove_multiple_whitespaces(item['article'])
        else:
            raise DropItem("Missing article in %s" % item)

        return item

    def remove_html_tags(self, text):
        script_re = re.compile(r'<(script|button|footer)\b[^<]*(?:(?!</\1>)<[^<]*)*</\1>')
        text = script_re.sub('', text)

        tag_re = re.compile(r'<[^>]+>')
        return tag_re.sub('', text)

    def remove_multiple_whitespaces(self, text):
        tag_re = re.compile(r'\s{2,}')
        return tag_re.sub(' ', text).strip()

    def remove_useless_text(self, text):
        text = text.replace("Partager cet article", "")
        text = text.replace("Ouest-France.fr", "")
        return text
