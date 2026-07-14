import streamlit as st
import requests
import openpyxl
import re

def scrape_links(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        r = requests.get(url, headers=headers, timeout=10)
        links = []
        for match in re.finditer(r'https?://[^\s"\'<>]+', r.text):
            full = match.group(0)
            if re.search(r'AI|tool|app|platform', full, re.I):
                links.append((full, full))
        return list(set(links))
    except:
        return []
    except:
        return []

st.title("TechSol Scraper")
url = st.text_input("Enter Website URL")
if st.button("Scrape & Add"):
    links = scrape_links(url)
    st.write(f"Found {len(links)} links")
    if links:
        wb = openpyxl.load_workbook("TechSol_Directory_v1_0.xlsx")
        ws = wb["Directory"]
        next_row = ws.max_row + 1
        for i, (u, t) in enumerate(links):
            ws.cell(next_row+i, 4, u)
            ws.cell(next_row+i, 1, f"TSD-{str(next_row+i).zfill(6)}")
            ws.cell(next_row+i, 12, f"Scraped: {t}")
        wb.save("TechSol_Directory_v1_0.xlsx")
        st.success("Added to Directory!")
