import sys
import json
from client import KnowledgeMeshValidator

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    req_id = req.get("id")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "validate_cross_docs",
                        "description": "Cross-validates technical specs, PRDs, and playbooks to isolate conflicting invariants.",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "doc_names": {
                                    "type": "array",
                                    "items": {"type": "string"}
                                }
                            }
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        args = params.get("arguments", {})
        validator = KnowledgeMeshValidator()
        res = validator.validate_cross_docs(args.get("doc_names"))
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "content": [{"type": "text", "text": json.dumps(res, indent=2)}]
            }
        }
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}

def main():
    validator = KnowledgeMeshValidator()
    print(json.dumps(validator.validate_cross_docs(), indent=2))

if __name__ == "__main__":
    main()
