from xxlimited import Str
from fastapi import FastAPI
import uvicorn
from dblib.querydb import querydb

app = FastAPI()

@app.get("/")
async def root():
    return {"Do you want to know more?": "You can type 'My choice' in the URL to see the potential health indicators for diabetes"}

@app.get("/My_choices/")
async def My_choices():
    """choises for health indicators"""

    return {"CHOICES": "Diabetes_binary, HighBP, HighChol, CholCheck, BMI, Smoker,Stroke, HeartDiseaseorAttack, PhysActivity, Fruits, Veggies,HvyAlcoholConsump, AnyHealthcare, NoDocbcCost, GenHlth,MentHlth, PhysHlth, DiffWalk, Sex, Age, Education,Income"}

@app.get("/choose/{choice}")
async def choose(choice: Str):
    """choises for health indicators"""
    if choice in ['HighChol','Diffwalk','BMI','HighBP','GenHlth']:
        return{"CORR":"TOP 5"}
    else:
        return {"CORR":"NOT TOP 5"}

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')