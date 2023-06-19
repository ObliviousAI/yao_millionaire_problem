from fastapi import FastAPI, HTTPException, Header

app = FastAPI()

inputs = {}

@app.post("/income")
async def add_income(
    income: int,
    x_oblv_user_name: str = Header(...)
):
    if x_oblv_user_name not in inputs.keys():
        inputs[x_oblv_user_name] = income
        return "Success"
    else:
        raise HTTPException(400, "Income added for user")

@app.get("/result")
async def result():
    max = 0
    result = []
    for user in inputs.keys():
        if inputs[user]>max:
            max = inputs[user]
            result = [user]
        elif inputs[user]==max:
            result.append(user)
    return ",".join(result)
