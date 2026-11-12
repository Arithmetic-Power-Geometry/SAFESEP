"""Deterministic checks for the eight-world illustration and analytic family."""
import json
from pathlib import Path

W = tuple(range(8))
D = {w: ('R' if w % 2 == 0 else 'W') for w in W}
probes = {
    'q': {w: ('isolated' if w == 0 else 'other') for w in W},
    'bit0': {w: ('0' if w < 4 else '1') for w in W},
}

def counts(probe):
    branches = {}
    for w, o in probe.items():
        branches.setdefault(o, []).append(w)
    return {
        o: {'worlds': v,
            'R': sum(D[w] == 'R' for w in v),
            'W': sum(D[w] == 'W' for w in v),
            'incompatible_pairs': sum(D[w] == 'R' for w in v) * sum(D[w] == 'W' for w in v)}
        for o, v in branches.items()
    }

result = {
    'status': 'independent eight-world illustration; separate from historical stronger-bit experiments',
    'worlds': list(W),
    'decisions': D,
    'costs': {'q': 1, 'bit0': 1},
    'requirements': {'q': [], 'bit0': []},
    'grants': {'q': [], 'bit0': []},
    'probes': {k: counts(v) for k, v in probes.items()},
    'worst_pairs': {k: max(x['incompatible_pairs'] for x in counts(v).values()) for k, v in probes.items()},
}
assert result['worst_pairs'] == {'q': 12, 'bit0': 4}
rows = []
for N in (200, 1000, 2000, 5000, 10000):
    n = N // 2
    rows.append({'worlds': N, 'n': n, 'q_cost': 1, 'worst_pairs': n * (n - 1)})
assert [row['worst_pairs'] for row in rows] == [9900, 249500, 999000, 6247500, 24995000]
result['table1_recalculated'] = rows
assert json.loads(json.dumps(result)) == json.loads((Path(__file__).parent / 'stronger_bit_example.json').read_text())
print('PASS: 8-world example q=12, bit0=4; 5 Table 1 analytic values match')

