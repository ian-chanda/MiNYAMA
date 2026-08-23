# Obsidian ↔ opencode MCP Setup Walkthrough

Goal: let opencode talk to Obsidian live through the **Local REST API** plugin and the **mcp-obsidian** MCP server.

Status legend: ✅ = already done | ⬜ = your manual step

---

## ✅ Step 1 — Global opencode config (DONE 2026-08-23)

Already written to the global opencode config: `~/.config/opencode/opencode.jsonc` (Windows: `%USERPROFILE%\.config\opencode\`). Re-create only if missing:

```jsonc
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "obsidian": {
      "type": "local",
      "command": ["uvx", "mcp-obsidian"],
      "enabled": true,
      "environment": {
        "OBSIDIAN_API_KEY": "{env:OBSIDIAN_API_KEY}",
        "OBSIDIAN_HOST": "127.0.0.1",
        "VERIFY_SSL": "false"
      }
    }
  }
}
```

Notes:
- `VERIFY_SSL=false` is required because the Local REST API plugin serves HTTPS with a self-signed cert.
- `{env:OBSIDIAN_API_KEY}` interpolates the key from your user environment — never hard-code the key into this file.
- Prerequisite: `uvx` must be on PATH (check with `Get-Command uvx`).

## ✅ Step 2 — Package sanity check (DONE)

```powershell
uvx mcp-obsidian
```
Expected behavior: downloads the package, then exits with
`ValueError: OBSIDIAN_API_KEY environment variable required.`
That error confirms the server resolves correctly and is just waiting for the key.

---

## ⬜ Step 3 — Install the Obsidian side of the bridge

In **Obsidian**:
1. Settings → Community plugins → Turn on community plugins (if restricted mode is active)
2. Browse → search **"Local REST API"** (by coddingtonbear) → Install → Enable

## ⬜ Step 4 — Set the API key as a user env var

Copy the key from Obsidian → Settings → **Local REST API**, then in PowerShell:

```powershell
[Environment]::SetEnvironmentVariable('OBSIDIAN_API_KEY','<your-key-here>','User')
```

Verify (new terminal window):
```powershell
$env:OBSIDIAN_API_KEY   # restart terminal first so it picks up the User var
```

## ⬜ Step 5 — Restart opencode

Config is loaded once at startup — quit and relaunch opencode. The `obsidian` MCP server appears among available tools.

---

## Using it

- Obsidian must be **running** whenever you use the tools.
- Typical capabilities: search the vault via the app index, read/patch specific notes, read the currently open note.
- Quick smoke test after restart: ask opencode to fetch the active note or list vault search hits for e.g. `traceability_id`.

## Troubleshooting

| Symptom | Fix |
| :--- | :--- |
| Server exits with `OBSIDIAN_API_KEY ... required` | Env var not visible to opencode → re-check Step 4, open a NEW terminal |
| Connection refused / SSL errors | Obsidian not running, or plugin disabled; confirm port `27124` in plugin settings matches default |
| Tools never appear in opencode | Config typo in `opencode.jsonc`, or opencode wasn't restarted |
| Certificate verification failure | Ensure `"VERIFY_SSL": "false"` survived in the config |
