import importlib.util
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

def load(name,path):
    spec=importlib.util.spec_from_file_location(name,ROOT/path)
    mod=importlib.util.module_from_spec(spec); import sys; sys.modules[name]=mod; spec.loader.exec_module(mod); return mod

def test_exact_solver_predictions_for_controlled_scenarios():
    run=load("run_safesep2_controlled_pred","experiments/run_safesep2_controlled.py")
    sys.modules["run_safesep2_controlled"]=run
    pred=load("predict_safesep2_exact","experiments/predict_safesep2_exact.py")
    got=pred.exact_predictions()
    assert got["destructive"] is False
    assert got["precedence"] is True
    assert got["adaptive"] is True
