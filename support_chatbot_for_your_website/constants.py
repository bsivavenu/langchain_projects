WEBSITE_URL="https://www.decode.com/wp-sitemap-posts-post-1.xml"
# WEBSITE_URL="https://geekflare.com/wp-sitemap-posts-post-1.xml"
# WEBSITE_URL="https://www.indiancounsellingservices.com/job-listing/sitemap-1.xml"
PINECONE_ENVIRONMENT="us-east-1"
PINECONE_INDEX="chatbot"


'''

# this code is to test whether we are able to fetch data from the given sitemap url
from langchain.document_loaders import SitemapLoader

sitemap_url = "https://www.indiancounsellingservices.com/job-listing/sitemap-1.xml"
loader = SitemapLoader(WEBSITE_URL)
docs = loader.load()
print(len(docs))
print(docs[:2])

'''