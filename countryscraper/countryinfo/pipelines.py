# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sqlite3

class SQLitePipeline:
    def open_spider(self, spider):
        self.connection = sqlite3.connect("countryinfo.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS countries(
            name TEXT,
            capital TEXT,
            population TEXT,
            area TEXT
            )
        """)
        self.connection.commit()
    def close_spider(self, spider):
        self.connection.close()
    def process_item(self, item, spider):
        self.cursor.execute("INSERT INTO countries(name, capital, population, area) VALUES(?,?,?,?)", (item["name"], item["capital"], item["population"], item["area"]))
        self.connection.commit()
        return item
