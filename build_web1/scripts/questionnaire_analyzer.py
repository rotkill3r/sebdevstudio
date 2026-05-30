"""
Seb_DevStudio — Questionnaire Analyzer
Processes wizard responses and generates project recommendations.
"""
import json
import sys
from typing import Any

RECOMMENDATIONS = {
    "autonomous": {
        "service": "Desarrollo Aut\u00f3nomo con Subagentes",
        "min_budget": 1500,
        "timeline": "2-4 semanas",
        "reason": "Proyecto con alcance definido que se beneficia del pipeline completo de 5 agentes."
    },
    "ai_tools": {
        "service": "Web + AI Tools",
        "min_budget": 800,
        "timeline": "3-7 d\u00edas",
        "reason": "Prototipo r\u00e1pido o MVP ideal para herramienta de IA generativa."
    },
    "consulting": {
        "service": "Consultor\u00eda T\u00e9cnica",
        "min_budget": 2500,
        "timeline": "1-3 meses",
        "reason": "Proyecto existente o arquitectura compleja que requiere auditor\u00eda y plan de migraci\u00f3n."
    }
}

def analyze(data: dict[str, Any]) -> dict[str, Any]:
    has_existing = data.get("existing") == "Proyecto existente"
    is_prototype = data.get("goal") in ["MVP / Prototipo", "No estoy seguro"]
    needs_backend = data.get("backend") not in ["No necesito backend", "No estoy seguro"]
    budget_str = data.get("budget", "")
    budget = 0
    if "$1,000" in budget_str:
        budget = 1000
    elif "$3,000" in budget_str:
        budget = 3000
    elif "10,000" in budget_str:
        budget = 10000

    if has_existing or budget >= 2500:
        recommendation = RECOMMENDATIONS["consulting"]
    elif is_prototype or budget < 1500:
        recommendation = RECOMMENDATIONS["ai_tools"]
    else:
        recommendation = RECOMMENDATIONS["autonomous"]

    return {
        "recommendation": recommendation,
        "scores": {
            "complexity": 7 if needs_backend else 4,
            "urgency": 9 if data.get("timeline", "").startswith("Urgente") else 5,
            "budget_fit": min(10, budget // 300) if budget else 3
        }
    }

if __name__ == "__main__":
    raw = sys.stdin.read()
    data = json.loads(raw) if raw else {}
    result = analyze(data)
    print(json.dumps(result, indent=2))
