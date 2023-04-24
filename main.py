from fastapi import FastAPI, status, HTTPException, Request

from soup import HTMLScraper

app = FastAPI()


@app.get("/")
async def home(body: Request):
    data = await body.json()
    methode = data.get("selector")
    url = data.get("url")
    pages = data.get("pages")
    value = data.get("value")
    elements = []
    for i in range(pages):
        scraper = HTMLScraper(url, i)
        el = scraper.find_elements(selector=methode, value=value)
        elements.extend(el)
        if el[0] == "Invalid Url!":
            return HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid Url")
    return {
        "code": status.HTTP_200_OK,
        "selector": methode,
        "value": value,
        "data": elements
    }
