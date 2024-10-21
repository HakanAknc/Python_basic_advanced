from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def merhaba_dunya():
    return {"message": "Merhaba, Dünya!"}

# if __name__ == '__main__':
#     app.run(debug=True)