"""Independent exact-solver predictions for controlled SAFESEP-II scenarios."""
from __future__ import annotations
import importlib.util
from pathlib import Path
from safesep.revocation_exact import RevProbe, exact_revocation_resolves

HERE=Path(__file__).resolve().parent

def _load():
    spec=importlib.util.spec_from_file_location("controlled",HERE/"run_safesep2_controlled.py")
    m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

def exact_predictions():
    m=_load(); out={}
    for name,(worlds,decisions,probes,authority) in m.scenarios().items():
        rp=tuple(
            RevProbe(
                p.name,
                tuple((w,p.outcomes[w]) for w in worlds),
                p.requires,p.grants,p.revokes,
            )
            for p in probes.values()
        )
        out[name]=exact_revocation_resolves(
            frozenset(worlds),decisions,rp,frozenset(authority)
        )
    return out

if __name__=="__main__":
    import json
    print(json.dumps(exact_predictions(),indent=2))
