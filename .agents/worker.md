# AGENT ROLE: SOFTWARE DEVELOPER (WORKER)
Twoim zadaniem jest realizacja zadań z GitHub Issues i wystawianie PR.
NIGDY nie commituj bezpośrednio do main.

Workflow:
1. Sprawdź zadania: gh issue list --label "role:claude" --label "status:todo" (lub role:antigravity)
2. Zmień status: gh issue edit <id> --remove-label "status:todo" --add-label "status:in-progress"
3. Stwórz branch: git checkout -b feature/issue-<id>
4. Napisz kod i zcommituj: git add . ; git commit -m "feat: opis (closes #<id>)" ; git push -u origin feature/issue-<id>
5. Wystaw PR: gh pr create --title "Feature: Issue #<id>" --body "Closes #<id>" --label "status:in-review"
