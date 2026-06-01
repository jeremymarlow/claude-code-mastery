<!-- GENERATED from meta/cli-reference.json by tools/render-cli-reference — do not hand-edit. Run `tools/render-cli-reference --all` (or `make render`). -->
[Claude Code Mastery](../../README.md) › CLI reference

# Claude Code CLI reference

> ⚙️ **Generated** from `meta/cli-reference.json` by `tools/render-cli-reference` — do not edit by hand; regenerate with `tools/render-cli-reference --all`.
>
> Reflects Claude Code CLI **2.1.159**.

The command tree, flags, and arguments below are introspected directly from `claude --help` (recursively over subcommands). The final sections cover doc-only surface `--help` cannot see — in-REPL slash commands and output styles — sourced from the official docs, with the URL and retrieval date shown.

## Contents

- [What's new](#whats-new)
- [`claude`](#claude)
  - [`claude agents`](#claude-agents)
  - [`claude auth`](#claude-auth)
    - [`claude auth login`](#claude-auth-login)
    - [`claude auth logout`](#claude-auth-logout)
    - [`claude auth status`](#claude-auth-status)
  - [`claude auto-mode`](#claude-auto-mode)
    - [`claude auto-mode config`](#claude-auto-mode-config)
    - [`claude auto-mode critique`](#claude-auto-mode-critique)
    - [`claude auto-mode defaults`](#claude-auto-mode-defaults)
  - [`claude doctor`](#claude-doctor)
  - [`claude install`](#claude-install)
  - [`claude mcp`](#claude-mcp)
    - [`claude mcp add`](#claude-mcp-add)
    - [`claude mcp add-from-claude-desktop`](#claude-mcp-add-from-claude-desktop)
    - [`claude mcp add-json`](#claude-mcp-add-json)
    - [`claude mcp get`](#claude-mcp-get)
    - [`claude mcp list`](#claude-mcp-list)
    - [`claude mcp remove`](#claude-mcp-remove)
    - [`claude mcp reset-project-choices`](#claude-mcp-reset-project-choices)
    - [`claude mcp serve`](#claude-mcp-serve)
  - [`claude plugin`](#claude-plugin)
    - [`claude plugin details`](#claude-plugin-details)
    - [`claude plugin disable`](#claude-plugin-disable)
    - [`claude plugin enable`](#claude-plugin-enable)
    - [`claude plugin init`](#claude-plugin-init)
    - [`claude plugin install`](#claude-plugin-install)
    - [`claude plugin list`](#claude-plugin-list)
    - [`claude plugin marketplace`](#claude-plugin-marketplace)
      - [`claude plugin marketplace add`](#claude-plugin-marketplace-add)
      - [`claude plugin marketplace list`](#claude-plugin-marketplace-list)
      - [`claude plugin marketplace remove`](#claude-plugin-marketplace-remove)
      - [`claude plugin marketplace update`](#claude-plugin-marketplace-update)
    - [`claude plugin prune`](#claude-plugin-prune)
    - [`claude plugin tag`](#claude-plugin-tag)
    - [`claude plugin uninstall`](#claude-plugin-uninstall)
    - [`claude plugin update`](#claude-plugin-update)
    - [`claude plugin validate`](#claude-plugin-validate)
  - [`claude project`](#claude-project)
    - [`claude project purge`](#claude-project-purge)
  - [`claude setup-token`](#claude-setup-token)
  - [`claude ultrareview`](#claude-ultrareview)
  - [`claude update`](#claude-update)
- [In-REPL slash commands](#in-repl-slash-commands)
- [Output styles](#output-styles)

## What's new

Latest CLI changes — full history in [meta/version-changelog.md](../../meta/version-changelog.md).

**2.1.158 → 2.1.159  (retrieved 2026-05-31 from https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)**

The course is now verified against **2.1.159** (refresh 2026-05-31, closing the L9 drift-ahead — the
reference was generated at 2.1.159 during P8 while the recorded anchor was held at 2.1.158 to keep the
upgrade trigger armed until the feature shipped).

- **2.1.159** — Internal infrastructure improvements (no user-facing changes). _Course impact:_ none — the command/flag surface is unchanged (`check-version-drift`: command list unchanged; `render-cli-reference --check` byte-stable), so `cli-reference.json` and every version-data value stand.

## `claude`

Claude Code - starts an interactive session by default, use -p/--print for non-interactive output

**Usage:** `claude [options] [command] [prompt]`

| Argument | Description |
| --- | --- |
| `prompt` | Your prompt |

| Flag | Value | Description |
| --- | --- | --- |
| `--add-dir` | `<directories...>` | Additional directories to allow tool access to |
| `--agent` | `<agent>` | Agent for the current session. Overrides the 'agent' setting. |
| `--agents` | `<json>` | JSON object defining custom agents (e.g. '{"reviewer": {"description": "Reviews code", "prompt": "You are a code reviewer"}}') |
| `--allow-dangerously-skip-permissions` | — | Enable bypassing all permission checks as an option, without it being enabled by default. Recommended only for sandboxes with no internet access. |
| `--allowedTools`, `--allowed-tools` | `<tools...>` | Comma or space-separated list of tool names to allow (e.g. "Bash(git *) Edit") |
| `--append-system-prompt` | `<prompt>` | Append a system prompt to the default system prompt |
| `--bare` | — | Minimal mode: skip hooks, LSP, plugin sync, attribution, auto-memory, background prefetches, keychain reads, and CLAUDE.md auto-discovery. Sets CLAUDE_CODE_SIMPLE=1. Anthropic auth is strictly ANTHROPIC_API_KEY or apiKeyHelper via --settings (OAuth and keychain are never read). 3P providers (Bedrock/Vertex/Foundry) use their own credentials. Skills still resolve via /skill-name. Explicitly provide context via: --system-prompt[-file], --append-system-prompt[-file], --add-dir (CLAUDE.md dirs), --mcp-config, --settings, --agents, --plugin-dir. |
| `--betas` | `<betas...>` | Beta headers to include in API requests (API key users only) |
| `--brief` | — | Enable SendUserMessage tool for agent-to-user communication |
| `--chrome` | — | Enable Claude in Chrome integration |
| `-c`, `--continue` | — | Continue the most recent conversation in the current directory |
| `--dangerously-skip-permissions` | — | Bypass all permission checks. Recommended only for sandboxes with no internet access. |
| `-d`, `--debug` | `[filter]` | Enable debug mode with optional category filtering (e.g., "api,hooks" or "!1p,!file") |
| `--debug-file` | `<path>` | Write debug logs to a specific file path (implicitly enables debug mode) |
| `--disable-slash-commands` | — | Disable all skills |
| `--disallowedTools`, `--disallowed-tools` | `<tools...>` | Comma or space-separated list of tool names to deny (e.g. "Bash(git *) Edit") |
| `--effort` | `<level>` | Effort level for the current session (low, medium, high, xhigh, max) |
| `--exclude-dynamic-system-prompt-sections` | — | Move per-machine sections (cwd, env info, memory paths, git status) from the system prompt into the first user message. Improves cross-user prompt-cache reuse. Only applies with the default system prompt (ignored with --system-prompt). — default: `false` |
| `--fallback-model` | `<model>` | Enable automatic fallback to specified model when the default model is overloaded or not available (only works with --print) |
| `--file` | `<specs...>` | File resources to download at startup. Format: file_id:relative_path (e.g., --file file_abc:doc.txt file_def:img.png) |
| `--fork-session` | — | When resuming, create a new session ID instead of reusing the original (use with --resume or --continue) |
| `--from-pr` | `[value]` | Resume a session linked to a PR by PR number/URL, or open interactive picker with optional search term |
| `-h`, `--help` | — | Display help for command |
| `--ide` | — | Automatically connect to IDE on startup if exactly one valid IDE is available |
| `--include-hook-events` | — | Include all hook lifecycle events in the output stream (only works with --output-format=stream-json) |
| `--include-partial-messages` | — | Include partial message chunks as they arrive (only works with --print and --output-format=stream-json) |
| `--input-format` | `<format>` | Input format (only works with --print): "text" (default), or "stream-json" (realtime streaming input) — choices: `text`, `stream-json` |
| `--json-schema` | `<schema>` | JSON Schema for structured output validation. Example: {"type":"object","properties":{"name":{"type":"string"}},"required":["name"]} |
| `--max-budget-usd` | `<amount>` | Maximum dollar amount to spend on API calls (only works with --print) |
| `--mcp-config` | `<configs...>` | Load MCP servers from JSON files or strings (space-separated) |
| `--mcp-debug` | — | [DEPRECATED. Use --debug instead] Enable MCP debug mode (shows MCP server errors) |
| `--model` | `<model>` | Model for the current session. Provide an alias for the latest model (e.g. 'sonnet' or 'opus') or a model's full name (e.g. 'claude-opus-4-8'). |
| `-n`, `--name` | `<name>` | Set a display name for this session (shown in the prompt box, /resume picker, and terminal title) |
| `--no-chrome` | — | Disable Claude in Chrome integration |
| `--no-session-persistence` | — | Disable session persistence - sessions will not be saved to disk and cannot be resumed (only works with --print) |
| `--output-format` | `<format>` | Output format (only works with --print): "text" (default), "json" (single result), or "stream-json" (realtime streaming) — choices: `text`, `json`, `stream-json` |
| `--permission-mode` | `<mode>` | Permission mode to use for the session — choices: `acceptEdits`, `auto`, `bypassPermissions`, `default`, `dontAsk`, `plan` |
| `--plugin-dir` | `<path>` | Load a plugin from a directory or .zip for this session only (repeatable: --plugin-dir A --plugin-dir B.zip) — default: `[]` |
| `--plugin-url` | `<url>` | Fetch a plugin .zip from a URL for this session only (repeatable: --plugin-url A --plugin-url B) — default: `[]` |
| `-p`, `--print` | — | Print response and exit (useful for pipes). Note: The workspace trust dialog is skipped when Claude is run in non-interactive mode (via -p, or when stdout is not a TTY, e.g. piped or redirected output). Only use this in directories you trust. Settings files that fail validation are silently ignored in this mode (no error dialog is shown). |
| `--prompt-suggestions` | `[value]` | Enable prompt suggestions. In print/SDK mode, emits a prompt_suggestion message after each turn with a predicted next user prompt — choices: `true`, `false`, `1`, `0`, `yes`, `no`, `on`, `off` |
| `--remote-control` | `[name]` | Start an interactive session with Remote Control enabled (optionally named) |
| `--remote-control-session-name-prefix` | `<prefix>` | Prefix for auto-generated Remote Control session names — default: `hostname` |
| `--replay-user-messages` | — | Re-emit user messages from stdin back on stdout for acknowledgment (only works with --input-format=stream-json and --output-format=stream-json) |
| `-r`, `--resume` | `[value]` | Resume a conversation by session ID, or open interactive picker with optional search term |
| `--session-id` | `<uuid>` | Use a specific session ID for the conversation (must be a valid UUID) |
| `--setting-sources` | `<sources>` | Comma-separated list of setting sources to load (user, project, local). |
| `--settings` | `<file-or-json>` | Path to a settings JSON file or a JSON string to load additional settings from |
| `--strict-mcp-config` | — | Only use MCP servers from --mcp-config, ignoring all other MCP configurations |
| `--system-prompt` | `<prompt>` | System prompt to use for the session |
| `--tmux` | — | Create a tmux session for the worktree (requires --worktree). Uses iTerm2 native panes when available; use --tmux=classic for traditional tmux. |
| `--tools` | `<tools...>` | Specify the list of available tools from the built-in set. Use "" to disable all tools, "default" to use all tools, or specify tool names (e.g. "Bash,Edit,Read"). |
| `--verbose` | — | Override verbose mode setting from config |
| `-v`, `--version` | — | Output the version number |
| `-w`, `--worktree` | `[name]` | Create a new git worktree for this session (optionally specify a name) |

### `claude agents`

Manage background agents

**Usage:** `claude agents [options]`

| Flag | Value | Description |
| --- | --- | --- |
| `--add-dir` | `<directory>` | Additional directory to allow tool access to in dispatched sessions (repeatable) |
| `--agent` | `<agent>` | Default agent for sessions dispatched from agent view. Overrides the 'agent' setting. |
| `--allow-dangerously-skip-permissions` | — | Make bypass-permissions mode available to dispatched sessions without defaulting to it |
| `--cwd` | `<path>` | Show only background sessions started under <path> |
| `--dangerously-skip-permissions` | — | Alias for --permission-mode bypassPermissions |
| `--effort` | `<level>` | Default effort level for sessions dispatched from agent view |
| `-h`, `--help` | — | Display help for command |
| `--json` | — | Print live sessions as a JSON array and exit (for scripting; does not require a TTY) |
| `--mcp-config` | `<config>` | MCP server configuration to apply to dispatched sessions (repeatable) |
| `--model` | `<model>` | Default model for sessions dispatched from agent view |
| `--permission-mode` | `<mode>` | Default permission mode for sessions dispatched from agent view |
| `--plugin-dir` | `<path>` | Load plugins from specified directory for the agent view and dispatched sessions (repeatable) |
| `--setting-sources` | `<sources>` | Comma-separated list of setting sources to load (user, project, local). |
| `--settings` | `<file-or-json>` | Settings file or JSON string to apply to the agent view and dispatched sessions |
| `--strict-mcp-config` | — | Only use MCP servers from --mcp-config in dispatched sessions |

### `claude auth`

Manage authentication

**Usage:** `claude auth [options] [command]`

| Flag | Value | Description |
| --- | --- | --- |
| `-h`, `--help` | — | Display help for command |

#### `claude auth login`

Sign in to your Anthropic account

**Usage:** `claude auth login [options]`

| Flag | Value | Description |
| --- | --- | --- |
| `--claudeai` | — | Use Claude subscription (default) |
| `--console` | — | Use Anthropic Console (API usage billing) instead of Claude subscription |
| `--email` | `<email>` | Pre-populate email address on the login page |
| `-h`, `--help` | — | Display help for command |
| `--sso` | — | Force SSO login flow |

#### `claude auth logout`

Log out from your Anthropic account

**Usage:** `claude auth logout [options]`

| Flag | Value | Description |
| --- | --- | --- |
| `-h`, `--help` | — | Display help for command |

#### `claude auth status`

Show authentication status

**Usage:** `claude auth status [options]`

| Flag | Value | Description |
| --- | --- | --- |
| `-h`, `--help` | — | Display help for command |
| `--json` | — | Output as JSON (default) |
| `--text` | — | Output as human-readable text |

### `claude auto-mode`

Inspect auto mode classifier configuration

**Usage:** `claude auto-mode [options] [command]`

| Flag | Value | Description |
| --- | --- | --- |
| `-h`, `--help` | — | Display help for command |

#### `claude auto-mode config`

Print the effective auto mode config as JSON: your settings where set, defaults otherwise

**Usage:** `claude auto-mode config [options]`

| Flag | Value | Description |
| --- | --- | --- |
| `-h`, `--help` | — | Display help for command |

#### `claude auto-mode critique`

Get AI feedback on your custom auto mode rules

**Usage:** `claude auto-mode critique [options]`

| Flag | Value | Description |
| --- | --- | --- |
| `-h`, `--help` | — | Display help for command |
| `--model` | `<model>` | Override which model is used |

#### `claude auto-mode defaults`

Print the default auto mode environment, allow, soft_deny, and hard_deny rules as JSON

**Usage:** `claude auto-mode defaults [options]`

| Flag | Value | Description |
| --- | --- | --- |
| `-h`, `--help` | — | Display help for command |

### `claude doctor`

Check the health of your Claude Code auto-updater. Note: The workspace trust dialog is skipped and stdio servers from .mcp.json are spawned for health checks. Only use this command in directories you trust.

**Usage:** `claude doctor [options]`

| Flag | Value | Description |
| --- | --- | --- |
| `-h`, `--help` | — | Display help for command |

### `claude install`

Install Claude Code native build. Use [target] to specify version (stable, latest, or specific version)

**Usage:** `claude install [options] [target]`

| Flag | Value | Description |
| --- | --- | --- |
| `--force` | — | Force installation even if already installed |
| `-h`, `--help` | — | Display help for command |

### `claude mcp`

Configure and manage MCP servers

**Usage:** `claude mcp [options] [command]`

| Flag | Value | Description |
| --- | --- | --- |
| `-h`, `--help` | — | Display help for command |

#### `claude mcp add`

Add an MCP server to Claude Code. Examples: # Add HTTP server: claude mcp add --transport http sentry https://mcp.sentry.dev/mcp # Add HTTP server with headers: claude mcp add --transport http corridor https://app.corridor.dev/api/mcp --header "Authorization: Bearer ..." # Add stdio server with environment variables: claude mcp add my-server -e API_KEY=xxx -- npx my-mcp-server # Add stdio server with subprocess flags: claude mcp add my-server -- my-command --some-flag arg1

**Usage:** `claude mcp add [options] <name> <commandOrUrl> [args...]`

| Flag | Value | Description |
| --- | --- | --- |
| `--callback-port` | `<port>` | Fixed port for OAuth callback (for servers requiring pre-registered redirect URIs) |
| `--client-id` | `<clientId>` | OAuth client ID for HTTP/SSE servers |
| `--client-secret` | — | Prompt for OAuth client secret (or set MCP_CLIENT_SECRET env var) |
| `-e`, `--env` | `<env...>` | Set environment variables (e.g. -e KEY=value) |
| `-H`, `--header` | `<header...>` | Set WebSocket headers (e.g. -H "X-Api-Key: abc123" -H "X-Custom: value") |
| `-h`, `--help` | — | Display help for command |
| `-s`, `--scope` | `<scope>` | Configuration scope (local, user, or project) — default: `"local"` |
| `-t`, `--transport` | `<transport>` | Transport type (stdio, sse, http). Defaults to stdio if not specified. |

#### `claude mcp add-from-claude-desktop`

Import MCP servers from Claude Desktop (Mac and WSL only)

**Usage:** `claude mcp add-from-claude-desktop [options]`

| Flag | Value | Description |
| --- | --- | --- |
| `-h`, `--help` | — | Display help for command |
| `-s`, `--scope` | `<scope>` | Configuration scope (local, user, or project) — default: `"local"` |

#### `claude mcp add-json`

Add an MCP server (stdio or SSE) with a JSON string

**Usage:** `claude mcp add-json [options] <name> <json>`

| Flag | Value | Description |
| --- | --- | --- |
| `--client-secret` | — | Prompt for OAuth client secret (or set MCP_CLIENT_SECRET env var) |
| `-h`, `--help` | — | Display help for command |
| `-s`, `--scope` | `<scope>` | Configuration scope (local, user, or project) — default: `"local"` |

#### `claude mcp get`

Get details about an MCP server. Unapproved .mcp.json servers are shown as ⏸ Pending approval and not connected to; approved servers are health-checked.

**Usage:** `claude mcp get [options] <name>`

| Flag | Value | Description |
| --- | --- | --- |
| `-h`, `--help` | — | Display help for command |

#### `claude mcp list`

List configured MCP servers. Unapproved .mcp.json servers are shown as ⏸ Pending approval and not connected to; approved servers are health-checked.

**Usage:** `claude mcp list [options]`

| Flag | Value | Description |
| --- | --- | --- |
| `-h`, `--help` | — | Display help for command |

#### `claude mcp remove`

Remove an MCP server

**Usage:** `claude mcp remove [options] <name>`

| Flag | Value | Description |
| --- | --- | --- |
| `-h`, `--help` | — | Display help for command |
| `-s`, `--scope` | `<scope>` | Configuration scope (local, user, or project) - if not specified, removes from whichever scope it exists in |

#### `claude mcp reset-project-choices`

Reset all approved and rejected project-scoped (.mcp.json) servers within this project

**Usage:** `claude mcp reset-project-choices [options]`

| Flag | Value | Description |
| --- | --- | --- |
| `-h`, `--help` | — | Display help for command |

#### `claude mcp serve`

Start the Claude Code MCP server

**Usage:** `claude mcp serve [options]`

| Flag | Value | Description |
| --- | --- | --- |
| `-d`, `--debug` | — | Enable debug mode |
| `-h`, `--help` | — | Display help for command |
| `--verbose` | — | Override verbose mode setting from config |

### `claude plugin`

Manage Claude Code plugins

**Usage:** `claude plugin|plugins [options] [command]`

| Flag | Value | Description |
| --- | --- | --- |
| `-h`, `--help` | — | Display help for command |

#### `claude plugin details`

Show a plugin's component inventory and projected token cost

**Usage:** `claude plugin details [options] <name>`

| Flag | Value | Description |
| --- | --- | --- |
| `-h`, `--help` | — | Display help for command |

#### `claude plugin disable`

Disable an enabled plugin

**Usage:** `claude plugin disable [options] [plugin]`

| Flag | Value | Description |
| --- | --- | --- |
| `-a`, `--all` | — | Disable all enabled plugins |
| `-h`, `--help` | — | Display help for command |
| `-s`, `--scope` | `<scope>` | Installation scope: user, project, local — default: `auto-detect` |

#### `claude plugin enable`

Enable a disabled plugin

**Usage:** `claude plugin enable [options] <plugin>`

| Flag | Value | Description |
| --- | --- | --- |
| `-h`, `--help` | — | Display help for command |
| `-s`, `--scope` | `<scope>` | Installation scope: user, project, local — default: `auto-detect` |

#### `claude plugin init`

Scaffold a new plugin at ~/.claude/skills/<name>/ (auto-loads next session as <name>@skills-dir)

**Usage:** `claude plugin init|new [options] <name>`

| Flag | Value | Description |
| --- | --- | --- |
| `--author` | `<name>` | Author name — default: `git config user.name` |
| `--author-email` | `<email>` | Author email — default: `git config user.email` |
| `--description` | `<text>` | Manifest description |
| `-f`, `--force` | — | Overwrite an existing .claude-plugin/ at the target |
| `-h`, `--help` | — | Display help for command |
| `--with` | `<components...>` | Also scaffold: skills, agents, hooks, mcp, lsp, output-style, channel |

#### `claude plugin install`

Install a plugin from available marketplaces (use plugin@marketplace for specific marketplace)

**Usage:** `claude plugin install|i [options] <plugin>`

| Flag | Value | Description |
| --- | --- | --- |
| `--config` | `<key=value>` | Set a userConfig option declared in the plugin's manifest (repeatable). Values are validated against the schema and stored via the same path as the interactive /plugin configure flow. |
| `-h`, `--help` | — | Display help for command |
| `-s`, `--scope` | `<scope>` | Installation scope: user, project, or local — default: `"user"` |

#### `claude plugin list`

List installed plugins

**Usage:** `claude plugin list [options]`

| Flag | Value | Description |
| --- | --- | --- |
| `--available` | — | Include available plugins from marketplaces (requires --json) |
| `-h`, `--help` | — | Display help for command |
| `--json` | — | Output as JSON |

#### `claude plugin marketplace`

Manage Claude Code marketplaces

**Usage:** `claude plugin marketplace [options] [command]`

| Flag | Value | Description |
| --- | --- | --- |
| `-h`, `--help` | — | Display help for command |

##### `claude plugin marketplace add`

Add a marketplace from a URL, path, or GitHub repo

**Usage:** `claude plugin marketplace add [options] <source>`

| Flag | Value | Description |
| --- | --- | --- |
| `-h`, `--help` | — | Display help for command |
| `--scope` | `<scope>` | Where to declare the marketplace: user (default), project, or local |
| `--sparse` | `<paths...>` | Limit checkout to specific directories via git sparse-checkout (for monorepos). Example: --sparse .claude-plugin plugins |

##### `claude plugin marketplace list`

List all configured marketplaces

**Usage:** `claude plugin marketplace list [options]`

| Flag | Value | Description |
| --- | --- | --- |
| `-h`, `--help` | — | Display help for command |
| `--json` | — | Output as JSON |

##### `claude plugin marketplace remove`

Remove a configured marketplace

**Usage:** `claude plugin marketplace remove|rm [options] <name>`

| Flag | Value | Description |
| --- | --- | --- |
| `-h`, `--help` | — | Display help for command |
| `--scope` | `<scope>` | Remove the marketplace declaration from a specific settings scope: user, project, or local. Omit to remove it from every scope. |

##### `claude plugin marketplace update`

Update marketplace(s) from their source - updates all if no name specified

**Usage:** `claude plugin marketplace update [options] [name]`

| Flag | Value | Description |
| --- | --- | --- |
| `-h`, `--help` | — | Display help for command |

#### `claude plugin prune`

Remove auto-installed dependencies that are no longer needed

**Usage:** `claude plugin prune|autoremove [options]`

| Flag | Value | Description |
| --- | --- | --- |
| `--dry-run` | — | List what would be removed without removing |
| `-h`, `--help` | — | Display help for command |
| `-s`, `--scope` | `<scope>` | Prune at scope: user, project, or local — default: `"user"` |
| `-y`, `--yes` | — | Skip the confirmation prompt (required when stdin or stdout is not a TTY) |

#### `claude plugin tag`

Create a {name}--v{version} git tag for a plugin release, validating that plugin.json and any enclosing marketplace entry agree

**Usage:** `claude plugin tag [options] [path]`

| Flag | Value | Description |
| --- | --- | --- |
| `--dry-run` | — | Print what would be tagged without creating it |
| `-f`, `--force` | — | Skip the dirty-working-tree and tag-already-exists checks |
| `-h`, `--help` | — | Display help for command |
| `-m`, `--message` | `<msg>` | Tag annotation message (use %s for the version) |
| `--push` | — | Push the tag to --remote after creating it |
| `--remote` | `<name>` | Remote to push to with --push — default: `"origin"` |

#### `claude plugin uninstall`

Uninstall an installed plugin

**Usage:** `claude plugin uninstall|remove [options] <plugin>`

| Flag | Value | Description |
| --- | --- | --- |
| `-h`, `--help` | — | Display help for command |
| `--keep-data` | — | Preserve the plugin's persistent data directory (~/.claude/plugins/data/{id}/) |
| `--prune` | — | Also remove auto-installed dependencies that are no longer needed (requires -y in non-interactive contexts) |
| `-s`, `--scope` | `<scope>` | Uninstall from scope: user, project, or local — default: `"user"` |
| `-y`, `--yes` | — | Skip the --prune confirmation prompt (required when stdin or stdout is not a TTY) |

#### `claude plugin update`

Update a plugin to the latest version (restart required to apply)

**Usage:** `claude plugin update [options] <plugin>`

| Flag | Value | Description |
| --- | --- | --- |
| `-h`, `--help` | — | Display help for command |
| `-s`, `--scope` | `<scope>` | Installation scope: user, project, local, managed — default: `user` |

#### `claude plugin validate`

Validate a plugin or marketplace manifest

**Usage:** `claude plugin validate [options] <path>`

| Flag | Value | Description |
| --- | --- | --- |
| `-h`, `--help` | — | Display help for command |
| `--strict` | — | Treat warnings as errors (exit 1). Use in CI to fail on unrecognized fields, missing metadata, and other issues that the runtime tolerates. |

### `claude project`

Manage Claude Code project state

**Usage:** `claude project [options] [command]`

| Flag | Value | Description |
| --- | --- | --- |
| `-h`, `--help` | — | Display help for command |

#### `claude project purge`

Delete all Claude Code state for a project (transcripts, tasks, file history, config entry)

**Usage:** `claude project purge [options] [path]`

| Flag | Value | Description |
| --- | --- | --- |
| `--all` | — | Purge state for every project (mutually exclusive with [path]) |
| `--dry-run` | — | List what would be deleted without deleting anything |
| `-h`, `--help` | — | Display help for command |
| `-i`, `--interactive` | — | Prompt for each item before deleting |
| `-y`, `--yes` | — | Skip confirmation prompt |

### `claude setup-token`

Set up a long-lived authentication token (requires Claude subscription)

**Usage:** `claude setup-token [options]`

| Flag | Value | Description |
| --- | --- | --- |
| `-h`, `--help` | — | Display help for command |

### `claude ultrareview`

Run a cloud-hosted multi-agent code review of the current branch (or a PR number / base branch) and print the findings

**Usage:** `claude ultrareview [options] [target]`

| Flag | Value | Description |
| --- | --- | --- |
| `-h`, `--help` | — | Display help for command |
| `--json` | — | Print the raw bugs.json payload instead of formatted findings |
| `--timeout` | `<minutes>` | Maximum minutes to wait for the review to finish — default: `30` |

### `claude update`

Check for updates and install if available

**Usage:** `claude update|upgrade [options]`

| Flag | Value | Description |
| --- | --- | --- |
| `-h`, `--help` | — | Display help for command |

## In-REPL slash commands

_Doc-sourced — [https://code.claude.com/docs/en/commands](https://code.claude.com/docs/en/commands) (retrieved 2026-05-31)_

Type `/` in a session to see the commands available to you; availability varies by platform, plan, and environment. MCP servers can expose prompts as `/mcp__<server>__<prompt>` commands, discovered dynamically from connected servers. Entries marked "(bundled skill)" / "(bundled workflow)" are prompts Claude can also invoke automatically. Excludes `/vim` (removed v2.1.92) and `/pr-comments` (removed v2.1.91), which are absent from the installed CLI.

| Name | Description |
| --- | --- |
| `/add-dir <path>` | Add a working directory for file access during the current session. |
| `/agents` | Manage agent (subagent) configurations. |
| `/autofix-pr [prompt]` | Spawn a Claude Code on the web session that watches the current branch's PR and pushes fixes when CI fails or reviewers comment. Requires the gh CLI. |
| `/background [prompt]` | Detach the current session to run as a background agent and free the terminal. Alias: /bg. |
| `/batch <instruction>` | (bundled skill) Orchestrate large-scale changes in parallel: decompose into 5–30 units, one background subagent per git worktree. Requires a git repository. |
| `/branch [name]` | Create a branch of the current conversation at this point, preserving the original. Alias: /fork. |
| `/btw <question>` | Ask a quick side question without adding to the conversation. |
| `/chrome` | Configure Claude in Chrome settings. |
| `/claude-api [migrate\|managed-agents-onboard]` | (bundled skill) Load Claude API reference material for your project's language; migrate API code to a newer model, or onboard a Managed Agent. |
| `/clear [name]` | Start a new conversation with empty context; the previous one stays in /resume. Aliases: /reset, /new. |
| `/code-review [low\|medium\|high\|xhigh\|max\|ultra] [--fix] [--comment] [target]` | (bundled skill) Review the current diff for bugs and cleanups; --fix applies findings, --comment posts PR comments, ultra runs a cloud review. |
| `/color [color\|default]` | Set the prompt-bar color for the current session. |
| `/compact [instructions]` | Free up context by summarizing the conversation so far; optional focus instructions. |
| `/config` | Open the Settings interface (theme, model, output style, and other preferences). Alias: /settings. |
| `/context [all]` | Visualize current context usage as a colored grid with optimization suggestions. |
| `/copy [N]` | Copy the last assistant response (or the Nth-latest) to the clipboard. |
| `/cost` | Alias for /usage. |
| `/debug [description]` | (bundled skill) Enable debug logging and troubleshoot by reading the session debug log. |
| `/deep-research <question>` | (bundled workflow) Fan out web searches, fetch and cross-check sources, and synthesize a cited report. |
| `/desktop` | Continue the current session in the Claude Code Desktop app (macOS/Windows, subscription). Alias: /app. |
| `/diff` | Open an interactive diff viewer showing uncommitted changes and per-turn diffs. |
| `/doctor` | Diagnose and verify your Claude Code installation and settings. |
| `/effort [level\|auto]` | Set the model effort level (low/medium/high/xhigh/max/ultracode); auto resets to the model default. |
| `/exit` | Exit the CLI (detaches an attached background session). Alias: /quit. |
| `/export [filename]` | Export the current conversation as plain text. |
| `/fast [on\|off]` | Toggle fast mode on or off. |
| `/feedback [report]` | Submit feedback, report a bug, or share your conversation. Aliases: /bug, /share. |
| `/fewer-permission-prompts` | (bundled skill) Scan transcripts for common read-only calls and add an allowlist to project settings. |
| `/focus` | Toggle the focus view (last prompt, tool-call summary, final response). Fullscreen only. |
| `/goal [condition\|clear]` | Set a goal Claude keeps working toward across turns until met; clear removes it. |
| `/heapdump` | Write a JS heap snapshot and memory breakdown for diagnosing high memory usage. |
| `/help` | Show help and available commands. |
| `/hooks` | View hook configurations for tool events. |
| `/ide` | Manage IDE integrations and show status. |
| `/init` | Initialize the project with a CLAUDE.md guide. |
| `/insights` | Generate a report analyzing your Claude Code sessions. |
| `/install-github-app` | Set up the Claude GitHub Actions app for a repository. |
| `/install-slack-app` | Install the Claude Slack app via the OAuth flow. |
| `/keybindings` | Open or create your keybindings configuration file. |
| `/login` | Sign in to your Anthropic account. |
| `/logout` | Sign out from your Anthropic account. |
| `/loop [interval] [prompt]` | (bundled skill) Run a prompt repeatedly while the session stays open; omit the interval to self-pace. Alias: /proactive. |
| `/mcp` | Manage MCP server connections and OAuth authentication. |
| `/memory` | Edit CLAUDE.md memory files; enable/disable and view auto-memory entries. |
| `/mobile` | Show a QR code to download the Claude mobile app. Aliases: /ios, /android. |
| `/model [model]` | Switch the AI model and save it as the default for new sessions. |
| `/passes` | Share a free week of Claude Code with friends (only if eligible). |
| `/permissions` | Manage allow/ask/deny rules for tool permissions. Alias: /allowed-tools. |
| `/plan [description]` | Enter plan mode directly from the prompt. |
| `/plugin` | Manage Claude Code plugins. |
| `/powerup` | Discover Claude Code features through quick interactive lessons. |
| `/privacy-settings` | View and update your privacy settings (Pro/Max). |
| `/radio` | Open Claude FM lo-fi radio in your browser. |
| `/recap` | Generate a one-line summary of the current session on demand. |
| `/release-notes` | View the changelog in an interactive version picker. |
| `/reload-plugins` | Reload active plugins to apply pending changes without restarting. |
| `/reload-skills` | Re-scan skill and command directories so on-disk changes apply without restarting. |
| `/remote-control` | Make this session available for remote control from claude.ai. Alias: /rc. |
| `/remote-env` | Configure the default remote environment for web sessions. |
| `/rename [name]` | Rename the current session and show the name on the prompt bar. |
| `/resume [session]` | Resume a conversation by ID or name, or open the session picker. Alias: /continue. |
| `/review [PR]` | Review a pull request locally in your current session. |
| `/rewind` | Rewind the conversation and/or code to a previous point, or summarize from a message. Aliases: /checkpoint, /undo. |
| `/run` | (bundled skill) Launch and drive your project's app to see a change working in the running app. |
| `/run-skill-generator` | (bundled skill) Write a per-project skill teaching /run and /verify how to launch and drive your app. |
| `/sandbox` | Toggle sandbox mode (supported platforms only). |
| `/schedule [description]` | Create, update, list, or run routines on Anthropic-managed cloud infrastructure. Alias: /routines. |
| `/scroll-speed` | Adjust mouse-wheel scroll speed interactively (fullscreen only). |
| `/security-review` | Analyze pending changes on the current branch for security vulnerabilities. |
| `/setup-bedrock` | Configure Amazon Bedrock auth, region, and model pins (visible when CLAUDE_CODE_USE_BEDROCK=1). |
| `/setup-vertex` | Configure Google Vertex AI auth, project, region, and model pins (visible when CLAUDE_CODE_USE_VERTEX=1). |
| `/simplify [target]` | (bundled skill) Review changed code for cleanup opportunities and apply fixes; does not hunt for bugs (use /code-review for that). |
| `/skills` | List available skills. |
| `/stats` | Alias for /usage (opens on the Stats tab). |
| `/status` | Open the Settings interface (Status tab): version, model, account, connectivity. |
| `/statusline` | Configure Claude Code's status line. |
| `/stickers` | Order Claude Code stickers. |
| `/stop` | Stop the current background session (only while attached; transcript and worktree are kept). |
| `/tasks` | List and manage background tasks. Also available as /bashes. |
| `/team-onboarding` | Generate a team onboarding guide from your Claude Code usage history. |
| `/teleport` | Pull a Claude Code on the web session into this terminal. Also /tp. |
| `/terminal-setup` | Configure terminal keybindings for Shift+Enter and other shortcuts. |
| `/theme` | Change the color theme (auto/light/dark, daltonized, ANSI, and custom themes). |
| `/tui [default\|fullscreen]` | Set the terminal UI renderer and relaunch into it with your conversation intact. |
| `/ultraplan <prompt>` | Draft a plan in an ultraplan session, review it in your browser, then execute remotely or send it back to your terminal. |
| `/ultrareview [PR]` | Run a deep multi-agent cloud code review; the preferred invocation is now /code-review ultra. |
| `/upgrade` | Open the upgrade page to switch to a higher plan tier. |
| `/usage` | Show session cost, plan usage limits, and activity stats. Aliases: /cost, /stats. |
| `/usage-credits` | Configure usage credits to keep working when you hit a limit (was /extra-usage). |
| `/verify` | (bundled skill) Confirm a code change does what it should by building, running, and observing your app. |
| `/voice [hold\|tap\|off]` | Toggle voice dictation, or enable it in a specific mode (requires a Claude.ai account). |
| `/web-setup` | Connect your GitHub account to Claude Code on the web using your local gh credentials. |
| `/workflows` | Open the workflow progress view to watch, pause, resume, or save workflows. |

## Output styles

_Doc-sourced — [https://code.claude.com/docs/en/output-styles](https://code.claude.com/docs/en/output-styles) (retrieved 2026-05-31)_

Output styles modify Claude Code's system prompt (role, tone, output format). Select one via `/config` → Output style; the choice persists as the `outputStyle` setting in .claude/settings.local.json, and takes effect after /clear or a new session. The standalone `/output-style` command was deprecated in v2.1.73 and removed in v2.1.91. Custom styles can be authored as Markdown files under ~/.claude/output-styles, .claude/output-styles, or a managed-settings directory.

| Name | Description |
| --- | --- |
| **Default** | Claude Code's standard system prompt, designed to complete software-engineering tasks efficiently. |
| **Proactive** | Executes immediately, makes reasonable assumptions instead of pausing for routine decisions, and prefers action over planning (you still see permission prompts). |
| **Explanatory** | Adds educational "Insights" between steps to explain implementation choices and codebase patterns. |
| **Learning** | Collaborative learn-by-doing: shares "Insights" and adds TODO(human) markers for you to implement small pieces of code yourself. |
