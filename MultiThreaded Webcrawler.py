# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 13:43:35 2023

@author: Yang Cairong
"""
class API:
    def  get_html_content(url):    
            pass
    def  get_links_on_page(html):    
            pass
api=API() 

import time

import threading

import collections   

from concurrent.futures import ThreadPoolExecutor

class MultiThreadedWebcrawler:

    def __init__(self, url):
        self.visited_urls = set()
        self.url_queue = collections.deque()
        self.url_queue.appendleft(url)
        
        self.lock = threading.Lock()
        self.active_futures = []
        self.max_active_jobs_in_pool = 50
                
        
            
    def process_url(self, url):
        try:
            html = api.get_html_content(url) #Interviewer asks which line is the bottleneck. It's this one!
        except ConnectionError:
            return #talk about retries, what to do in this case
        links = api. get_links_on_page(html)
        with self.lock: #this is the same as calling self.lock.acquire()
            for link in links:
                if link not in self.visited_urls:
                    self.visited_urls.add(link)
                    self.url_queue.appendleft(link)
        #and then calling self.lock.release()

    def run(self):
        with ThreadPoolExecutor(max_workers=20) as pool:
            while True:
                with self.lock:
                    num_active_jobs = len(self.active_futures)
                    num_urls_to_crawl = len(self.url_queue)
                    if num_urls_to_crawl == 0 and num_active_jobs == 0:
                        #Termination - you have no urls left to crawl, and all of your 
                        #jobs in the pool are complete.
                        break
                    
#If you have too many jobs still running in the pool, then just let them run again
#Otherwise, if you have a manageable amount, then you can submit more. 
                    # if num_active_jobs <= self.max_active_jobs_in_pool:
                        number_of_jobs_to_submit = min(
                            num_urls_to_crawl, 
                            self.max_active_jobs_in_pool - num_active_jobs
                        )
                        for _ in range(number_of_jobs_to_submit):
                            future = pool.submit(self.process_url, self.url_queue.pop())
                            self.active_futures.append(future)
                #Outside of the lock, you can remove completed futures from the active_futures
                self.active_futures = [future for future in self.active_futures if not future.done()]
                time.sleep(1) #Let someone else take the lock. 
                
        return list(self.visited_urls)



# Define a mock API class for testing
class MockAPI:
    @staticmethod
    def get_html_content(url):
        # Simulate fetching HTML content (you can customize this for your test)
        return f"HTML content for {url}"

    @staticmethod
    def get_links_on_page(html):
        # Simulate extracting links from HTML content (customize as needed)
        return [f"link{i}.com" for i in range(3)]

# Create a test function
def test_webcrawler():
    # Initialize the web crawler with a starting URL
    start_url = "example.com"
    crawler = MultiThreadedWebcrawler(start_url)

    # Set the API instance to the mock API for testing
    crawler.api = MockAPI()
    # html=crawler.api.get_html_content(start_url)
    # links=crawler.api.get_links_on_page(html)
    

    # Run the web crawler
    visited_urls = crawler.run()
    print("Visited URLs:", visited_urls)

    # Verify the results or assert specific conditions based on your test scenario
    assert len(visited_urls) == 4  # Including the starting URL, there should be 4 visited URLs
    assert start_url in visited_urls  # The starting URL should be in the visited URLs

    print("Test passed!")

if __name__ == "__main__":
    # Call the test function
    test_webcrawler()
