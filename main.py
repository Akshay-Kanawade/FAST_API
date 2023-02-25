from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def main():
    return {"page":"get info"}

@app.get('/about')
def about():
    return {"page":"get about info"}

# if __name__ == __main__():