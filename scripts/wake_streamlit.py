from playwright.sync_api import sync_playwright
import sys
import time

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
        print("\n======================================")
        print(f"Opening: {url}")
        print("======================================")

        page = browser.new_page()

        try:
            response = page.goto(
                url,
                wait_until="domcontentloaded",
                timeout=90000
            )

            page.wait_for_timeout(5000)

            # Check whether Streamlit is sleeping
            wake_button = page.get_by_text(
                "Yes, get this app back up!",
                exact=False
            )

            if wake_button.count() > 0:

                print("App is sleeping.")
                print("Clicking wake-up button...")

                wake_button.first.click()

                # Give Streamlit time to start the server
                print("Waiting for Streamlit to wake...")

                for attempt in range(18):

                    page.wait_for_timeout(10000)

                    print(
                        f"Wake attempt {attempt + 1}/18"
                    )

                    try:
                        page.reload(
                            wait_until="domcontentloaded",
                            timeout=90000
                        )
                    except:
                        pass

                    page.wait_for_timeout(3000)

                    # If wake button disappeared,
                    # app is likely awake
                    if page.get_by_text(
                        "Yes, get this app back up!",
                        exact=False
                    ).count() == 0:

                        print("Wake page disappeared.")
                        break

                else:
                    raise Exception(
                        "App did not wake within expected time."
                    )

            else:
                print("App was already awake.")

            # Final check
            page.wait_for_timeout(10000)

            title = page.title()

            print(f"Final title: {title}")
            print(f"Final URL: {page.url}")

            content = page.content()

            if "This app has gone to sleep" in content:
                raise Exception(
                    "App is still showing the sleeping page."
                )

            print("SUCCESS - app is awake.")

        except Exception as e:

            print(f"FAILED: {e}")
            failed.append(url)

        finally:
            page.close()

    browser.close()


if failed:

    print("\nFAILED APPS:")

    for app in failed:
        print(app)

    sys.exit(1)


print("\n======================================")
print("ALL STREAMLIT APPS ARE AWAKE")
print("======================================")
