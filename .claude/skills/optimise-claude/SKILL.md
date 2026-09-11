---
name: optimise-claude
description: >
  Use this skill when the goal is to minimize Claude token usage,
  avoid hitting limits, and maximize efficiency during long or complex sessions.
  Applies best practices like batching, fresh chats, and minimal verbosity.
  Triggers on: "optimize tokens", "reduce usage", "save credits", "claude limit",
  "token efficiency", "long conversation", "agent cost reduction".
---

# Claude Token Optimizer Skill

**Description:**  
Use this skill to minimize Claude token usage, avoid hitting limits, and maximize efficiency during long or complex sessions.

--

## Triggers
- optimize tokens  
- reduce usage  
- save credits  
- claude limit  
- token efficiency  
- long conversation  
- agent cost reduction  

--

## Rules

### 1. Avoid Follow-Up Messages
Do NOT continue conversations with corrective follow-ups.  
Instead, rewrite and improve the original prompt before sending.  
Prefer editing over appending.

--

### 2. Reset Context Regularly
After 15–20 messages, summarize the conversation and start a new chat.  
Use the summary as the first message to preserve context while reducing tokens.

--

### 3. Batch Multiple Tasks
Combine multiple related tasks into a single prompt.  
Avoid splitting tasks across multiple messages.  

**Example:**  
Instead of:
- summarize this  
- list key points  
- suggest a title  

Use:
- summarize this, list key points, and suggest a title  

--

### 4. Reduce Response Length
Prefer concise, direct answers.  
Avoid explanations unless explicitly requested.  
Remove fluff.

--

### 5. Think in Tokens, Not Messages
Optimize both input and output length.  
Keep prompts short but precise.  
Avoid unnecessary context or repeated instructions.

--

### 6. Avoid Repeated Data
Do not resend large files or repeated context.  
Reference summaries instead of raw data.

--

### 7. Use Persistent Preferences
Store user preferences (style, role, format) once.  
Avoid repeating setup instructions in every prompt.

--

### 8. Avoid Unnecessary Features
Do not use tools (web, connectors, advanced reasoning) unless required.  
Keep execution minimal.

--

### 9. Use Lightweight Models
Use cheaper/faster models for simple tasks:
- formatting  
- grammar  
- short answers  

Use powerful models only for complex reasoning.

--

### 10. Spread Usage Over Time
Avoid consuming all tokens in one session.  
Distribute work across multiple time windows.

--

### 11. Prefer Off-Peak Execution
Run heavy tasks during off-peak hours to reduce limits and improve efficiency.

--

## Execution Guidelines

- **Verbosity:** Minimal  
- **Style:** Direct  
- **Priority:**  
  1. Reduce tokens  
  2. Maintain accuracy  
  3. Avoid redundancy  

--

## Constraints

- Do not repeat context  
- Do not expand unnecessarily  
- Do not split tasks across multiple turns if one is enough  

--

## Examples

### ❌ Bad
Summarize this.  
Now give key points.  
Now suggest a title.  

### ✅ Good
Summarize this, list key points, and suggest a title.

--

### ❌ Bad
No, that's wrong. I meant this instead.

### ✅ Good
Edit the original prompt with correct instructions.

--

## Goal
Maximize efficiency and avoid hitting Claude usage limits.# Claude Token Optimizer

Operate in maximum token-efficiency mode for the entire session.

--

## Core Rules

### 1. No Follow-Up Messages
**Do NOT** send corrective follow-ups. Rewrite and improve the original prompt instead.
Prefer editing over appending.

**Bad:** "Summarize this." → "Now give key points." → "Now suggest a title."
**Good:** "Summarize this, list key points, and suggest a title."

### 2. Reset Context Regularly
After 15–20 messages, summarize the conversation and start a new chat.
Use the summary as the first message to preserve context while reducing tokens.

### 3. Batch Multiple Tasks
Combine related tasks into a single prompt. Never split tasks across multiple messages.

### 4. Minimize Output
- Concise, direct answers only
- No explanations unless explicitly requested
- Compact formatting, no fluff
- No trailing summaries

### 5. Optimize Both Directions
Keep prompts short but precise. Avoid unnecessary context or repeated instructions.
Output tokens are expensive — keep answers tight.

### 6. Avoid Repeated Data
Do not resend large files or repeated context. Reference prior summaries instead of raw data.

### 7. Store Preferences Once
Capture user preferences (style, role, format) in memory once.
Never repeat setup instructions in every prompt.

### 8. Minimal Tooling
Do not use tools (web search, connectors, advanced reasoning) unless explicitly required.
Keep execution minimal.

### 9. Use Lightweight Models for Simple Tasks
- Formatting, grammar, short answers → cheaper/faster model
- Complex reasoning only → powerful model
Reserve powerful models for when they're truly needed.

### 10. No Subagents Unless Essential
Never spawn agents for tasks solvable in a single pass.
Each agent call starts cold and re-derives context — expensive.

### 11. Spread Usage Over Time
Avoid consuming all tokens in one session. Distribute heavy work across time windows.

### 12. Off-Peak for Heavy Tasks
Run long or intensive tasks during off-peak hours to reduce rate limiting.

---

## Execution Mode

| Setting | Value |
|---|---|
| Verbosity | Minimal |
| Reasoning | Efficient |
| Style | Direct |
| Follow-ups | Forbidden |
| Subagents | Avoid |

**Priority order:** reduce_tokens → maintain_accuracy → avoid_redundancy

---

## What Wastes Tokens (Avoid)

- Long explanations when a short answer works
- Repeating the problem back before solving it
- Multiple refinement passes when one-shot is possible
- Exploring the codebase more than needed
- Generating code blocks that won't be used
- Verbose storytelling or preamble

---

## Mode Persistence

Stay in this mode for the entire conversation unless explicitly disabled.
