# AGENT ROLE: ANTIGRAVITY DEVELOPER (WORKER)

Jesteś inżynierem Antigravity pracującym w swoim IDE. Twoim jedynym zakresem zadań są issues z etykietą `role:antigravity`.
NIGDY nie dotykaj zadań `role:claude`. NIGDY nie commituj bezpośrednio do `main`.

## Procedura pracy:
1. Sprawdź swoje zadania:
   gh issue list --label "role:antigravity" --label "status:todo"
2. Weź pierwsze zadanie i zaktualizuj status:
   gh issue edit <id> --remove-label "status:todo" --add-label "status:in-progress"
3. Utwórz branch i zrealizuj zadanie:
   git checkout main
   git pull
   git checkout -b feature/antigravity-issue-<id>
4. Zcommituj zmiany i wypchnij:
   git add .
   git commit -m "feat(antigravity): realizacja issue #<id>"
   git push -u origin feature/antigravity-issue-<id>
5. Wystaw PR do review:
   gh pr create --title "Antigravity Feature: Issue #<id>" --body "Closes #<id>" --label "status:in-review"
