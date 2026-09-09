from playwright.sync_api import sync_playwright
import sys

APPS = [
    "https://groundglass-ai-evaluation.streamlit.app/",
    "https://text-to-sql-assay.streamlit.app/",
    "https://signalguard-ai.streamlit.app/",
    "https://financial-services-complaint-analytics-ai-6cxsauwxgm6upvikhdkd.streamlit.app/",
]

failed = []

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    for url in APPS:
        print(f"\nOpening: {url}")

        try:
            page = browser.new_page()

            response = page.goto(
                url,
                wait_until="domcontentloaded",
                timeout=90000
            )

            page.wait_for_timeout(15000)

            if response:
                print(f"HTTP status: {response.status}")
            else:
                print("Page loaded without HTTP response object.")

            print(f"Title: {page.title()}")
            print("SUCCESS")

            page.close()

        except Exception as e:
            print(f"FAILED: {e}")
            failed.append(url)

    browser.close()

if failed:
    print("\nFailed apps:")
    for app in failed:
        print(app)
    sys.exit(1)

print("\nAll Streamlit apps visited successfully.")
