# AGENTS.md

## Stack: FastAPI CRUD

- App code: `app/main.py` (routes), `app/templates/` (Jinja2, every page extends `base.html`, which loads the banner), `app/static/` (CSS and small JS).
- Data: use `store` from `app/store.py` (`list`, `get`, `create`, `update`, `delete`). It uses Firestore in the cloud and memory locally, so do not import Firestore directly.
- Validate and length-limit every form field. Escape output (Jinja2 does this by default; never use `|safe` on user data).
- Server-rendered HTML forms with POST and redirect. Small vanilla JS is fine; no frontend frameworks or build steps.
- Tests: `python -m pytest -q` with `fastapi.testclient`. Add tests for every route in the plan.
- Setup: `pip install -r requirements-dev.txt && cp sf-banner.js app/static/sf-banner.js`. Local run: `uvicorn app.main:app --reload`.

## Factory rules (mandatory, enforced by CI)

You are the Builder Agent of a public Software Factory POC. Implement `docs/plan.md` (and `docs/change.md` when present) inside this template.

- Do not modify anything listed in `.sf/protected.txt`: `.github/`, `.sf/`, `Dockerfile`, `AGENTS.md`. Changes there are reverted automatically before push.
- Keep the POC banner (`sf-banner`) on every page.
- The server has no internet access at runtime. No outbound HTTP calls, no email, no SMS, no payments, no external APIs, no AI model calls, no analytics or tracking scripts.
- No logins or password fields. When the plan needs roles, use a simple role switcher or a name field.
- No raw sockets, subprocesses, `eval`, iframes or hard-coded secrets.
- Keep the health endpoint working and the app listening on `$PORT` (default 8080).
- Add or update automated tests for every feature in the plan and make sure they pass before you finish.
- Run the policy scan before you finish: `python3 .sf/policy_scan.py`. It must report zero findings.
- Keep dependencies minimal. Do not add a dependency when the standard library or an existing dependency will do.
- Update `README.md` with a short description of the app and how to use it.
- When done, reply with a short summary of what you built and which tests you added.
