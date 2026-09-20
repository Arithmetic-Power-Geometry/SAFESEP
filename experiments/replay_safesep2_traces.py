"""Replay and verify SAFESEP-II controlled experiment traces."""
from __future__ import annotations
import json
from pathlib import Path
from run_safesep2_controlled import scenarios

def verify_trace_file(path, scenario):
    worlds, decisions, probes, initial_authority=scenarios()[scenario]
    rows=json.loads(Path(path).read_text())
    by_world={w:[] for w in worlds}
    for r in rows: by_world[r["world"]].append(r)
    for world, seq in by_world.items():
        C=set(worlds); A=set(initial_authority); unused=set(probes)
        for idx,r in enumerate(seq,1):
            assert r["step"]==idx
            assert r["compatible_before"]==sorted(C)
            assert r["authority_before"]==sorted(A)
            p=probes[r["probe"]]
            assert p.requires <= A
            assert r["probe"] in unused
            o=p.outcomes[world]; assert r["outcome"]==o
            C={w for w in C if p.outcomes[w]==o}
            A=(A|set(p.grants))-set(p.revokes)
            unused.remove(r["probe"])
            assert r["compatible_after"]==sorted(C)
            assert r["authority_after"]==sorted(A)
            vals={decisions[w] for w in C}
            terminal=len(vals)==1
            assert r["terminal"]==terminal
            assert r["decision"]==(next(iter(vals)) if terminal else None)
    return True

def main(base="results/safesep2_traces"):
    base=Path(base)
    for s in scenarios():
        assert verify_trace_file(base/f"{s}.json",s)
    return True

if __name__=="__main__":
    main(); print("SAFESEP-II trace replay: PASS")
