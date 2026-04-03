from baseline.run_agent import run_simulation

def inference(request):
    result = run_simulation()
    return {"result": result}