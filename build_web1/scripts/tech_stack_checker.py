"""
Seb_DevStudio — Tech Stack Checker
Audits tech stack and generates legacy vs modern report.
"""
import re
import sys
from pathlib import Path
from typing import Any

MODERN_PATTERNS = {
    "react": {"label": "React / Next.js", "modern": True, "score": 9},
    "vue": {"label": "Vue / Nuxt", "modern": True, "score": 8},
    "svelte": {"label": "Svelte / SvelteKit", "modern": True, "score": 8},
    "tailwind": {"label": "Tailwind CSS", "modern": True, "score": 7},
    "typescript": {"label": "TypeScript", "modern": True, "score": 9},
    "vite": {"label": "Vite", "modern": True, "score": 8},
    "python": {"label": "Python", "modern": True, "score": 7},
}

LEGACY_PATTERNS = {
    "jquery": {"label": "jQuery", "modern": False, "score": 2},
    "php": {"label": "PHP", "modern": False, "score": 3},
    "asp.net": {"label": "ASP.NET", "modern": False, "score": 3},
    "bootstrap": {"label": "Bootstrap", "modern": False, "score": 4},
}

def audit(filepath: str) -> dict[str, Any]:
    path = Path(filepath)
    if not path.exists():
        return {"error": f"File not found: {filepath}"}

    content = path.read_text(encoding="utf-8", errors="ignore")
    findings: list[dict[str, Any]] = []
    modern_score = 0
    legacy_score = 0

    for key, spec in MODERN_PATTERNS.items():
        if re.search(rf"\b{key}\b", content, re.IGNORECASE):
            findings.append({**spec, "found": True})
            modern_score += spec["score"]

    for key, spec in LEGACY_PATTERNS.items():
        if re.search(rf"\b{key}\b", content, re.IGNORECASE):
            findings.append({**spec, "found": True})
            legacy_score += spec["score"]

    total = modern_score - legacy_score
    verdict = "Moderno" if total >= 15 else "Mixto" if total >= 5 else "Legacy"

    return {
        "total_score": total,
        "verdict": verdict,
        "findings": findings,
        "recommendations": _recommendations(verdict, findings)
    }

def _recommendations(verdict: str, findings: list[dict[str, Any]]) -> list[str]:
    if verdict == "Moderno":
        return ["Todo en orden. El stack es actual y escalable."]
    recs = []
    for f in findings:
        if not f["modern"]:
            recs.append(f"Migrar {f['label']} a alternativa moderna (score actual: {f['score']}/10)")
    if not recs:
        recs.append("Considerar agregar TypeScript, Vite o Tailwind para mejorar el score de modernidad.")
    return recs

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    result = audit(target)
    print(f"Veredicto: {result['verdict']}")
    print(f"Score total: {result['total_score']}")
    for f in result.get("findings", []):
        status = "\u2705" if f["modern"] else "\u26a0\ufe0f"
        print(f"  {status} {f['label']} ({f['score']}/10)")
    for r in result.get("recommendations", []):
        print(f"  \U0001f4a1 {r}")
