from client import KnowledgeMeshValidator

validator = KnowledgeMeshValidator()
res = validator.validate_cross_docs()
print("=== Cross-Doc Knowledge Mesh Validator Telemetry ===")
print(f"Indexed Documents: {res['docs_indexed']} | Coherence Index: {res['coherence_index']*100}%")
print("Detected Discrepancies:")
for c in res["conflicts"]:
    print(f"  * [{c['severity']}] {c['topic']}")
    print(f"    - Doc A: {c['doc_a']}")
    print(f"    - Doc B: {c['doc_b']}")
    print(f"    - Recommendation: {c['resolution']}")
