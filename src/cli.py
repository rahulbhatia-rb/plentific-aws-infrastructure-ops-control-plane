import json, sys
from gate import evaluate
with open(sys.argv[1]) as f:
    result=evaluate(json.load(f))
if result['allowed']:
    print('READY'); raise SystemExit(0)
print('BLOCKED')
for finding in result['findings']:
    print('- '+finding)
raise SystemExit(1)
