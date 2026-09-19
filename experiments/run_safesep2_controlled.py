"""Controlled SAFESEP-II authority-sensitive evidence experiments.

This is a deterministic systems-realization harness. Capability tokens are explicit
app/controller-owned gates; they are NOT described as Android OS permissions.
"""
from __future__ import annotations
import json
from dataclasses import dataclass, asdict
from pathlib import Path

@dataclass(frozen=True)
class Probe:
    name: str
    outcomes: dict[str, str]
    requires: frozenset[str] = frozenset()
    grants: frozenset[str] = frozenset()
    revokes: frozenset[str] = frozenset()

@dataclass
class TraceRow:
    scenario: str
    world: str
    step: int
    compatible_before: list[str]
    authority_before: list[str]
    probe: str
    outcome: str
    grants: list[str]
    revocations: list[str]
    authority_after: list[str]
    compatible_after: list[str]
    terminal: bool
    decision: str | None
    dead_end: bool

def constant_decision(C, decisions):
    vals={decisions[w] for w in C}
    return next(iter(vals)) if len(vals)==1 else None

def run_policy(scenario, world, worlds, decisions, probes, authority, chooser):
    C=set(worlds); A=set(authority); unused=set(probes); rows=[]; step=0
    while constant_decision(C, decisions) is None:
        executable=[name for name in sorted(unused) if probes[name].requires <= A]
        choice=chooser(C,A,unused,executable)
        if choice is None:
            if rows: rows[-1].dead_end=True
            return rows, False
        if choice not in executable:
            raise RuntimeError(f"policy chose non-executable probe {choice}")
        p=probes[choice]; beforeC=sorted(C); beforeA=sorted(A)
        o=p.outcomes[world]
        C={w for w in C if p.outcomes[w]==o}
        A=(A | set(p.grants))-set(p.revokes)
        unused.remove(choice); step+=1
        d=constant_decision(C,decisions)
        rows.append(TraceRow(
            scenario,world,step,beforeC,beforeA,choice,o,
            sorted(p.grants),sorted(p.revokes),sorted(A),sorted(C),
            d is not None,d,False))
    return rows, True

def scenarios():
    # A: pairwise separators exist initially, but either first destructive probe
    # destroys the authority needed for the unresolved pair.
    A_worlds=("a","b","c"); A_dec={"a":"A","b":"B","c":"C"}
    A_probes={
      "P":Probe("P",{"a":"0","b":"1","c":"1"},frozenset({"X"}),revokes=frozenset({"Y"})),
      "Q":Probe("Q",{"a":"0","b":"0","c":"1"},frozenset({"Y"}),revokes=frozenset({"X"})),
    }
    # B: Q must precede P.
    B_probes={
      "P":Probe("P",{"a":"0","b":"1","c":"1"},frozenset({"X"}),revokes=frozenset({"Y"})),
      "Q":Probe("Q",{"a":"0","b":"0","c":"1"},frozenset({"Y"})),
    }
    # C: root makes only one of two mutually destructive branch probes necessary.
    C_worlds=("0","1","2","3"); C_dec={w:w for w in C_worlds}
    C_probes={
      "R":Probe("R",{"0":"L","1":"L","2":"R","3":"R"}),
      "P":Probe("P",{"0":"0","1":"1","2":"x","3":"x"},frozenset({"X"}),revokes=frozenset({"Y"})),
      "Q":Probe("Q",{"0":"x","1":"x","2":"0","3":"1"},frozenset({"Y"}),revokes=frozenset({"X"})),
    }
    return {
      "destructive":(A_worlds,A_dec,A_probes,{"X","Y"}),
      "precedence":(A_worlds,A_dec,B_probes,{"X","Y"}),
      "adaptive":(C_worlds,C_dec,C_probes,{"X","Y"}),
    }

def chooser_for(name, world):
    if name=="destructive":
        # Deliberately try P first; a and then b/c expose success/dead-end branches.
        return lambda C,A,U,E: "P" if "P" in E else ("Q" if "Q" in E else None)
    if name=="precedence":
        return lambda C,A,U,E: "Q" if "Q" in E else ("P" if "P" in E else None)
    if name=="adaptive":
        def choose(C,A,U,E):
            if "R" in E: return "R"
            if C <= {"0","1"} and "P" in E: return "P"
            if C <= {"2","3"} and "Q" in E: return "Q"
            return None
        return choose
    raise KeyError(name)

def main(out_dir="results/safesep2_traces"):
    out=Path(out_dir); out.mkdir(parents=True,exist_ok=True)
    summary={}
    for name,(worlds,decisions,probes,authority) in scenarios().items():
        allrows=[]; outcomes={}
        for world in worlds:
            rows,ok=run_policy(name,world,worlds,decisions,probes,authority,chooser_for(name,world))
            allrows += [asdict(r) for r in rows]; outcomes[world]=ok
        (out/f"{name}.json").write_text(json.dumps(allrows,indent=2)+"\n")
        summary[name]=outcomes
    (out/"summary.json").write_text(json.dumps(summary,indent=2)+"\n")
    return summary

if __name__=="__main__":
    print(json.dumps(main(),indent=2))
