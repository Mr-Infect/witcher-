import argparse
from modules import scraper, domain_handler, utils, progress_bar

def main():
    parser = argparse.ArgumentParser(description='Witcher: An Advanced Web Scraping Tool')
    parser.add_argument('-u', '--url', type=str, help='Target URL or path to scrape')
    parser.add_argument('-k', '--keywords', type=str, nargs='*', help='Keywords to search for (optional)')
    parser.add_argument('-d', '--domain', action='store_true', help='Identify and handle domains automatically')
    
    args = parser.parse_args()

    if args.url:
        urls = [args.url]
        # Handle multiple URLs
        # Fetch domain-specific handlers if needed
        handlers = domain_handler.get_handlers(urls) if args.domain else None

        for url in urls:
            scraper.scrape(url, args.keywords, handlers)
    else:
        print("Please provide a URL or path to scrape.")
    
if __name__ == '__main__':
    main()
