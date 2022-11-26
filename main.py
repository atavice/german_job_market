import pandas as pd
from job_extraction import extract_job_links
from description_extraction import extract_job_descriptions
from lgbtiq_friendly import calculate_lgbt_metric
from description_language import calculate_desc_lang_metric
from required_language import calculate_required_lang_metric

class Metrics:

    scrape_sessions_list: list = [{'city': 'berlin', 'extension_url': '/jobs/search?keywords=Working%20Student&location=Berlin%2C%20Berlin%2C%20Almanya&locationId=&geoId=106967730&f_TPR=r86400&distance=25&position=1&pageNum=0'},
                                  {'city': 'cologne', 'extension_url': '/jobs/search?keywords=Working%20Student&location=K%C3%B6ln%2C%20Kuzey%20Ren-Vestfalya%2C%20Almanya&locationId=&geoId=102426246&f_TPR=r86400&position=1&pageNum=0'}, 
                                  {'city': 'munich', 'extension_url': '/jobs/search?keywords=Working%20Student&location=M%C3%BCnih%2C%20Bavyera%2C%20Almanya&locationId=&geoId=100477049&f_TPR=r86400&distance=25&position=1&pageNum=0'}]

    def __init__(self) -> None:
        self.update_attributes(self)
        
    def update_attributes(self):
        self.berlin_metrics_dict = pd.read_csv('./metrics/berlin/metrics.csv', delimiter=';').iloc[-1].to_dict()
        self.cologne_metrics_dict = pd.read_csv('./metrics/cologne/metrics.csv', delimiter=';').iloc[-1].to_dict()
        self.munich_metrics_dict = pd.read_csv('./metrics/munich/metrics.csv', delimiter=';').iloc[-1].to_dict()
        self.all_metrics_dict = pd.read_csv('./metrics/all/metrics.csv', delimiter=';').iloc[-1].to_dict()

    def update_metrics(self):
        for scrape_session in Metrics.scrape_sessions_list:
            new_day_metrics_dict = {}
            new_day_metrics_dict.update(extract_job_links(scrape_session=scrape_session))
            new_day_metrics_dict.update(extract_job_descriptions(scrape_session=scrape_session))
            new_day_metrics_dict.update(calculate_lgbt_metric(scrape_session=scrape_session))
            new_day_metrics_dict.update(calculate_desc_lang_metric(scrape_session=scrape_session))
            new_day_metrics_dict.update(calculate_required_lang_metric(scrape_session=scrape_session))
            # positions
            # skills
            # dictionary'e tarih ekle 
            # csv'ye kaydet
        self.update_attributes(self)
            
def main():
    metrics = Metrics()

if __name__ == '__main__':
    main()


