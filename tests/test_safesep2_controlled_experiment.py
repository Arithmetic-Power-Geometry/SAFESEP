import importlib.util
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

def load(name,path):
    spec=importlib.util.spec_from_file_location(name,ROOT/path)
    mod=importlib.util.module_from_spec(spec); import sys; sys.modules[name]=mod; spec.loader.exec_module(mod); return mod

def test_controlled_scenarios_and_replay(tmp_path):
    run=load("run_safesep2_controlled","experiments/run_safesep2_controlled.py")
    replay=load("replay_safesep2_traces","experiments/replay_safesep2_traces.py")
    # satisfy replay module's direct import
    import sys; sys.modules["run_safesep2_controlled"]=run
    # reload after dependency injection
    replay=load("replay_safesep2_traces2","experiments/replay_safesep2_traces.py")
    summary=run.main(tmp_path)
    assert summary["destructive"]=={"a": True, "b": False, "c": False}
    assert all(summary["precedence"].values())
    assert all(summary["adaptive"].values())
    assert replay.main(tmp_path)
