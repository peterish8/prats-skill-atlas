use std::time::{Duration, Instant};

use crate::api::schema::{
    AgentPromptParams, AgentReadParams, AgentRenameParams, AgentSendParams, AgentStartParams,
    AgentTarget, EmptyParams, Method, ReadFormat, ReadSource, Request,
};

pub(super) fn run_agent_command(args: &[String]) -> std::io::Result<i32> {
    let Some(subcommand) = args.first().map(|arg| arg.as_str()) else {
        print_agent_help();
        return Ok(2);
    };

    match subcommand {
        "list" => agent_list(&args[1..]),
        "get" => agent_get(&args[1..]),
        "read" => agent_read(&args[1..]),
        "send" => agent_send(&args[1..]),
        "prompt" => agent_prompt(&args[1..]),
        "rename" => agent_rename(&args[1..]),
        "focus" => agent_focus(&args[1..]),
        "wait" => agent_wait(&args[1..]),
        "attach" => agent_attach(&args[1..]),
        "start" => agent_start(&args[1..]),
        "explain" => agent_explain(&args[1..]),
        "help" | "--help" | "-h" => {
            print_agent_help();
            Ok(0)
        }
        _ => {
            print_agent_help();
            Ok(2)
        }
    }
}

fn agent_explain(args: &[String]) -> std::io::Result<i32> {
    let mut file = None;
    let mut agent = None;
    let mut json = false;
    let mut verbose = false;
    let mut target = None;

    let mut index = 0;
    while index < args.len() {
        match args[index].as_str() {
            "--file" => {
                let Some(value) = args.get(index + 1) else {
                    eprintln!("missing value for --file");
                    return Ok(2);
                };
                file = Some(value.clone());
                index += 2;
            }
            "--agent" => {
                let Some(value) = args.get(index + 1) else {
                    eprintln!("missing value for --agent");
                    return Ok(2);
                };
                agent = Some(value.clone());
                index += 2;
            }
            "--json" => {
                json = true;
                index += 1;
            }
            "--format" => {
                let Some(value) = args.get(index + 1) else {
                    eprintln!("missing value for --format");
                    return Ok(2);
                };
                match value.as_str() {
                    "json" => json = true,
                    "text" => json = false,
                    other => {
                        eprintln!("invalid --format: {other} (expected text or json)");
                        return Ok(2);
                    }
                }
                index += 2;
            }
            "--verbose" | "-v" => {
                verbose = true;
                index += 1;
            }
            "help" | "--help" | "-h" => {
                eprintln!("usage: herdr agent explain <target> [--json|--verbose]");
                eprintln!(
                    "usage: herdr agent explain --file PATH --agent LABEL [--json|--verbose]"
                );
                return Ok(0);
            }
            value if value.starts_with('-') => {
                eprintln!("unknown option: {value}");
                return Ok(2);
            }
            value => {
                if target.is_some() {
                    eprintln!("usage: herdr agent explain <target> [--json]");
                    return Ok(2);
                }
                target = Some(value.to_string());
                index += 1;
            }
        }
    }

    let explain = if let Some(path) = file {
        if target.is_some() {
            eprintln!("usage: herdr agent explain --file PATH --agent LABEL [--json]");
            return Ok(2);
        }
        let Some(agent_label) = agent else {
            eprintln!("herdr agent explain --file requires --agent LABEL");
            return Ok(2);
        };
        let content = std::fs::read_to_string(path)?;
        crate::detect::manifest::explain_to_json_value(&crate::detect::manifest::explain_for_label(
            &agent_label,
            &content,
        ))
    } else {
        let Some(target) = target else {
            eprintln!("usage: herdr agent explain <target> [--json]");
            eprintln!("usage: herdr agent explain --file PATH --agent LABEL [--json]");
            return Ok(2);
        };
        if agent.is_some() {
            eprintln!("--agent is only valid with --file");
            return Ok(2);
        }

        let response = super::send_request(&Request {
            id: "cli:agent:explain".into(),
            method: Method::AgentExplain(AgentTarget {
                target: target.to_owned(),
            }),
        })?;
        if response.get("error").is_some() {
            eprintln!("{}", serde_json::to_string(&response).unwrap());
            return Ok(1);
        }
        response["result"]["explain"].clone()
    };

    if json {
        println!("{explain}");
    } else {
        print_agent_explain_text(&explain, verbose);
    }
    Ok(0)
}

fn print_agent_explain_text(explain: &serde_json::Value, verbose: bool) {
    println!("agent: {}", explain["agent"].as_str().unwrap_or("unknown"));
    println!("state: {}", explain["state"].as_str().unwrap_or("unknown"));
    println!(
        "manifest: {} {}",
        explain["manifest_source"].as_str().unwrap_or("none"),
        explain["manifest_version"].as_str().unwrap_or("unknown")
    );
    if let Some(rule) = explain["matched_rule"].as_object() {
        let rule_id = rule
            .get("id")
            .and_then(|value| value.as_str())
            .unwrap_or("-");
        println!(
            "rule: {} (region={} priority={})",
            rule_id,
            rule.get("region")
                .and_then(|value| value.as_str())
                .unwrap_or("-"),
            rule.get("priority")
                .and_then(|value| value.as_i64())
                .unwrap_or(0),
        );
        if let Some(preview) = matched_rule_region_preview(explain, rule_id) {
            println!("evidence: {preview:?}");
        }
    } else {
        println!("rule: none");
    }
    if let Some(reason) = explain["fallback_reason"].as_str() {
        println!("fallback_reason: {reason}");
    }
    if let Some(reason) = explain["screen_detection_skip_reason"].as_str() {
        println!("screen_detection_skip_reason: {reason}");
    }
    if let Some(reason) = explain["skipped_update_reason"].as_str() {
        println!("skipped_update_reason: {reason}");
    }
    if let Some(warning) = explain["warning"].as_str() {
        println!("warning: {warning}");
    }

    if !verbose {
        return;
    }

    println!(
        "visible: idle={} blocker={} working={}",
        explain["visible_idle"].as_bool().unwrap_or(false),
        explain["visible_blocker"].as_bool().unwrap_or(false),
        explain["visible_working"].as_bool().unwrap_or(false)
    );
    println!(
        "cached_remote_version: {}",
        explain["cached_remote_version"].as_str().unwrap_or("none")
    );
    println!(
        "local_override_shadowing_remote: {}",
        explain["local_override_shadowing_remote"]
            .as_bool()
            .unwrap_or(false)
    );
    if let Some(status) = explain["remote_update_status"].as_str() {
        println!("remote_update_status: {status}");
    }
    if let Some(error) = explain["remote_update_error"].as_str() {
        println!("remote_update_error: {error}");
    }
    if let Some(evaluated_rules) = explain["evaluated_rules"]
        .as_array()
        .filter(|rules| !rules.is_empty())
    {
        println!("evaluated_rules:");
        for rule in evaluated_rules {
            println!(
                "  {} {} priority={} region={} state={}",
                if rule["matched"].as_bool().unwrap_or(false) {
                    "✓"
                } else {
                    "✗"
                },
                rule["id"].as_str().unwrap_or("-"),
                rule["priority"].as_i64().unwrap_or(0),
                rule["region"].as_str().unwrap_or("-"),
                rule["state"].as_str().unwrap_or("unknown")
            );
            let evidence = &rule["evidence"];
            println!(
                "    matchers: contains={:?} regex={:?} line_regex={:?} all={} any={} not={}",
                evidence["contains"],
                evidence["regex"],
                evidence["line_regex"],
                evidence["all_count"].as_u64().unwrap_or(0),
                evidence["any_count"].as_u64().unwrap_or(0),
                evidence["not_count"].as_u64().unwrap_or(0)
            );
            println!(
                "    region: bytes={} preview={:?}",
                evidence["region_bytes"].as_u64().unwrap_or(0),
                evidence["region_preview"].as_str().unwrap_or("")
            );
        }
    }
}

fn matched_rule_region_preview<'a>(
    explain: &'a serde_json::Value,
    rule_id: &str,
) -> Option<&'a str> {
    explain["evaluated_rules"]
        .as_array()?
        .iter()
        .find(|rule| rule["id"].as_str() == Some(rule_id))?["evidence"]["region_preview"]
        .as_str()
        .filter(|preview| !preview.is_empty())
}

fn agent_start(args: &[String]) -> std::io::Result<i32> {
    let Some(name) = args.first() else {
        eprintln!("usage: herdr agent start <name> --kind KIND --pane ID [--timeout MS] [-- <agent-args...>]");
        return Ok(2);
    };
    let separator = args
        .iter()
        .position(|arg| arg == "--")
        .unwrap_or(args.len());
    let mut kind = None;
    let mut pane_id = None;
    let mut timeout_ms = None;
    let mut index = 1;
    while index < separator {
        match args[index].as_str() {
            "--kind" => {
                let Some(value) = args.get(index + 1).filter(|_| index + 1 < separator) else {
                    eprintln!("missing value for --kind");
                    return Ok(2);
                };
                kind = Some(value.clone());
                index += 2;
            }
            "--pane" => {
                let Some(value) = args.get(index + 1).filter(|_| index + 1 < separator) else {
                    eprintln!("missing value for --pane");
                    return Ok(2);
                };
                pane_id = Some(super::normalize_pane_id(value));
                index += 2;
            }
            "--timeout" => {
                let Some(value) = args.get(index + 1).filter(|_| index + 1 < separator) else {
                    eprintln!("missing value for --timeout");
                    return Ok(2);
                };
                timeout_ms = Some(super::parse_u64_flag("--timeout", value)?);
                index += 2;
            }
            other => {
                eprintln!("unknown option: {other}");
                return Ok(2);
            }
        }
    }
    let Some(kind) = kind else {
        eprintln!("missing required --kind");
        return Ok(2);
    };
    let Some(pane_id) = pane_id else {
        eprintln!("missing required --pane");
        return Ok(2);
    };
    let Some(expected_kind) = crate::detect::parse_agent_label(&kind) else {
        eprintln!("unsupported interactive agent kind: {kind}");
        return Ok(2);
    };
    let expected_kind = crate::detect::agent_label(expected_kind).to_string();
    let mut response = super::send_request(&Request {
        id: "cli:agent:start".into(),
        method: Method::AgentStart(AgentStartParams {
            name: name.clone(),
            kind,
            pane_id: pane_id.clone(),
            args: if separator < args.len() {
                args[separator + 1..].to_vec()
            } else {
                Vec::new()
            },
            timeout_ms,
        }),
    })?;
    if response.get("error").is_some() {
        return super::print_response(&response);
    }
    let Some(terminal_id) = response["result"]["agent"]["terminal_id"].as_str() else {
        return super::print_response(&cli_agent_error(
            "cli:agent:start",
            "agent_start_failed",
            "agent start response did not include terminal_id",
        ));
    };
    let terminal_id = terminal_id.to_string();
    let timeout = Duration::from_millis(timeout_ms.unwrap_or(30_000));
    let waited = wait_for_named_agent(
        &terminal_id,
        name,
        Some(timeout),
        AgentWaitMode::Start {
            expected_kind: &expected_kind,
        },
    );
    match waited {
        Ok(Ok(agent)) => {
            response["result"]["agent"] = agent;
            super::print_response(&response)
        }
        Ok(Err(error)) => super::print_response(&error),
        Err(err) => {
            print_agent_transport_error(err, "cli:agent:start", "agent_start_transport_failed")
        }
    }
}

fn agent_list(args: &[String]) -> std::io::Result<i32> {
    if !args.is_empty() {
        eprintln!("usage: herdr agent list");
        return Ok(2);
    }

    super::print_response(&super::send_request(&Request {
        id: "cli:agent:list".into(),
        method: Method::AgentList(EmptyParams::default()),
    })?)
}

fn agent_get(args: &[String]) -> std::io::Result<i32> {
    let Some(target) = args.first() else {
        eprintln!("usage: herdr agent get <target>");
        return Ok(2);
    };
    if args.len() != 1 {
        eprintln!("usage: herdr agent get <target>");
        return Ok(2);
    }

    super::print_response(&super::send_request(&Request {
        id: "cli:agent:get".into(),
        method: Method::AgentGet(AgentTarget {
            target: target.clone(),
        }),
    })?)
}

fn agent_focus(args: &[String]) -> std::io::Result<i32> {
    let Some(target) = args.first() else {
        eprintln!("usage: herdr agent focus <target>");
        return Ok(2);
    };
    if args.len() != 1 {
        eprintln!("usage: herdr agent focus <target>");
        return Ok(2);
    }

    super::print_response(&super::send_request(&Request {
        id: "cli:agent:focus".into(),
        method: Method::AgentFocus(AgentTarget {
            target: target.clone(),
        }),
    })?)
}

fn agent_attach(args: &[String]) -> std::io::Result<i32> {
    let (target, takeover) =
        match super::parse_attach_target(args, "usage: herdr agent attach <target> [--takeover]") {
            Ok(parsed) => parsed,
            Err(code) => return Ok(code),
        };

    let response = resolve_agent_target(&target, "cli:agent:attach:resolve")?;
    if response.get("error").is_some() {
        eprintln!("{}", serde_json::to_string(&response).unwrap());
        return Ok(1);
    }
    let Some(terminal_id) = response["result"]["agent"]["terminal_id"].as_str() else {
        eprintln!("agent attach failed: response did not include terminal_id");
        return Ok(1);
    };
    crate::client::run_terminal_attach(terminal_id.to_owned(), takeover)?;
    Ok(0)
}

fn agent_wait(args: &[String]) -> std::io::Result<i32> {
    let Some(target) = args.first() else {
        eprintln!("usage: herdr agent wait <name> [--timeout MS]");
        return Ok(2);
    };
    let mut timeout_ms = None;
    let mut index = 1;
    while index < args.len() {
        match args[index].as_str() {
            "--timeout" => {
                let Some(value) = args.get(index + 1) else {
                    eprintln!("missing value for --timeout");
                    return Ok(2);
                };
                timeout_ms = Some(super::parse_u64_flag("--timeout", value)?);
                index += 2;
            }
            "help" | "--help" | "-h" => {
                eprintln!("usage: herdr agent wait <name> [--timeout MS]");
                return Ok(0);
            }
            other => {
                eprintln!("unknown option: {other}");
                return Ok(2);
            }
        }
    }
    let initial = resolve_agent_target(target, "cli:agent:wait:resolve")?;
    if initial.get("error").is_some() {
        return super::print_response(&initial);
    }
    let agent = &initial["result"]["agent"];
    if agent["name"].as_str() != Some(target) {
        return super::print_response(&cli_agent_error(
            "cli:agent:wait",
            "agent_name_not_found",
            format!("named agent {target} not found"),
        ));
    }
    match agent["agent_status"].as_str().unwrap_or("unknown") {
        "idle" | "done" | "blocked" => return super::print_response(&initial),
        "unknown" => {
            return super::print_response(&cli_agent_error(
                "cli:agent:wait",
                "agent_not_running",
                "agent is no longer running",
            ))
        }
        _ => {}
    }
    let Some(terminal_id) = agent["terminal_id"].as_str() else {
        return super::print_response(&cli_agent_error(
            "cli:agent:wait",
            "agent_wait_failed",
            "agent response did not include terminal_id",
        ));
    };
    let timeout = timeout_ms.map(Duration::from_millis);
    let waited = match wait_for_named_agent(terminal_id, target, timeout, AgentWaitMode::Current) {
        Ok(waited) => waited,
        Err(err) => {
            return print_agent_transport_error(
                err,
                "cli:agent:wait",
                "agent_wait_transport_failed",
            )
        }
    };
    match waited {
        Ok(agent) => super::print_response(&serde_json::json!({
            "id": "cli:agent:wait",
            "result": { "type": "agent_info", "agent": agent }
        })),
        Err(error) => super::print_response(&error),
    }
}

#[derive(Clone, Copy)]
enum AgentWaitMode<'a> {
    Start { expected_kind: &'a str },
    Current,
    AfterPrompt { baseline_state_change_seq: u64 },
}

fn wait_for_named_agent(
    lookup_target: &str,
    expected_name: &str,
    timeout: Option<Duration>,
    mode: AgentWaitMode<'_>,
) -> std::io::Result<Result<serde_json::Value, serde_json::Value>> {
    let started_at = Instant::now();
    let deadline = timeout.and_then(|timeout| started_at.checked_add(timeout));
    let mut first_poll = true;
    loop {
        if deadline.is_some_and(|deadline| Instant::now() >= deadline) {
            if matches!(mode, AgentWaitMode::Start { .. }) {
                // Let the server reconcile its matching startup deadline before
                // returning so the pending name is immediately reusable.
                let _ = resolve_agent_target_unchecked(lookup_target, "cli:agent:start:timeout");
            }
            return Ok(Err(agent_wait_timeout(mode)));
        }
        let poll_id = match mode {
            AgentWaitMode::Start { .. } => "cli:agent:start",
            AgentWaitMode::Current => "cli:agent:wait",
            AgentWaitMode::AfterPrompt { .. } => "cli:agent:prompt",
        };
        let response = if first_poll {
            first_poll = false;
            resolve_agent_target(lookup_target, poll_id)?
        } else {
            resolve_agent_target_unchecked(lookup_target, poll_id)?
        };
        if response.get("error").is_some() {
            if matches!(mode, AgentWaitMode::Start { .. }) {
                return Ok(Err(cli_agent_error(
                    "cli:agent:start",
                    "agent_start_failed",
                    "agent target disappeared before becoming interactive",
                )));
            }
            return Ok(Err(response));
        }
        let agent = &response["result"]["agent"];
        let status = agent["agent_status"].as_str().unwrap_or("unknown");
        let completed = matches!(status, "idle" | "done" | "blocked");
        if !matches!(mode, AgentWaitMode::Start { .. })
            && agent["name"].as_str() != Some(expected_name)
        {
            return Ok(Err(agent_name_lost_error(poll_id, expected_name)));
        }
        let outcome = match mode {
            AgentWaitMode::Start { expected_kind } => {
                if let Some(actual) = agent["agent"].as_str() {
                    if actual != expected_kind {
                        Some(Err(cli_agent_error(
                            "cli:agent:start",
                            "agent_kind_mismatch",
                            format!("expected {expected_kind}, detected {actual}"),
                        )))
                    } else if agent["name"].as_str() != Some(expected_name) {
                        Some(Err(agent_name_lost_error("cli:agent:start", expected_name)))
                    } else if completed && agent["interactive_ready"].as_bool().unwrap_or(false) {
                        Some(Ok(agent.clone()))
                    } else if !agent["launch_pending"].as_bool().unwrap_or(false) {
                        Some(Err(cli_agent_error(
                            "cli:agent:start",
                            "agent_start_failed",
                            "agent process exited before becoming interactive",
                        )))
                    } else {
                        None
                    }
                } else if !agent["launch_pending"].as_bool().unwrap_or(false) {
                    Some(Err(cli_agent_error(
                        "cli:agent:start",
                        "agent_start_failed",
                        "agent process exited before becoming interactive",
                    )))
                } else {
                    None
                }
            }
            AgentWaitMode::Current => {
                if completed {
                    Some(Ok(agent.clone()))
                } else if status == "unknown" {
                    Some(Err(cli_agent_error(
                        "cli:agent:wait",
                        "agent_not_running",
                        "agent is no longer running",
                    )))
                } else {
                    None
                }
            }
            AgentWaitMode::AfterPrompt {
                baseline_state_change_seq,
            } => {
                let sequence = agent["state_change_seq"].as_u64().unwrap_or(0);
                if sequence > baseline_state_change_seq && completed {
                    Some(Ok(agent.clone()))
                } else if status == "unknown" {
                    Some(Err(cli_agent_error(
                        "cli:agent:prompt",
                        "agent_not_running",
                        "agent exited while waiting for the prompt",
                    )))
                } else {
                    None
                }
            }
        };
        if let Some(outcome) = outcome {
            return Ok(outcome);
        }
        std::thread::sleep(Duration::from_millis(100));
    }
}

fn agent_name_lost_error(request_id: &str, expected_name: &str) -> serde_json::Value {
    cli_agent_error(
        request_id,
        "agent_name_not_found",
        format!("named agent {expected_name} no longer owns the target terminal"),
    )
}

fn print_agent_transport_error(
    err: std::io::Error,
    request_id: &str,
    code: &str,
) -> std::io::Result<i32> {
    if super::protocol_mismatch_was_reported(&err) {
        return Ok(1);
    }
    super::print_response(&cli_agent_error(request_id, code, err.to_string()))
}

fn agent_wait_timeout(mode: AgentWaitMode<'_>) -> serde_json::Value {
    let (id, message) = match mode {
        AgentWaitMode::Start { .. } => ("cli:agent:start", "timed out waiting for agent startup"),
        AgentWaitMode::Current => ("cli:agent:wait", "timed out waiting for agent completion"),
        AgentWaitMode::AfterPrompt { .. } => {
            ("cli:agent:prompt", "timed out waiting for prompted work")
        }
    };
    cli_agent_error(id, "timeout", message)
}

fn cli_agent_error(id: &str, code: &str, message: impl Into<String>) -> serde_json::Value {
    serde_json::json!({
        "id": id,
        "error": { "code": code, "message": message.into() }
    })
}

fn resolve_agent_target(target: &str, request_id: &str) -> std::io::Result<serde_json::Value> {
    super::send_request(&agent_get_request(target, request_id))
}

fn resolve_agent_target_unchecked(
    target: &str,
    request_id: &str,
) -> std::io::Result<serde_json::Value> {
    super::send_request_unchecked(&agent_get_request(target, request_id))
}

fn agent_get_request(target: &str, request_id: &str) -> Request {
    Request {
        id: request_id.into(),
        method: Method::AgentGet(AgentTarget {
            target: target.to_owned(),
        }),
    }
}

fn agent_rename(args: &[String]) -> std::io::Result<i32> {
    let Some(target) = args.first() else {
        eprintln!("usage: herdr agent rename <target> <name>|--clear");
        return Ok(2);
    };
    if args.len() < 2 {
        eprintln!("usage: herdr agent rename <target> <name>|--clear");
        return Ok(2);
    }
    let name = if args.len() == 2 && args[1] == "--clear" {
        None
    } else {
        Some(args[1..].join(" "))
    };

    super::print_response(&super::send_request(&Request {
        id: "cli:agent:rename".into(),
        method: Method::AgentRename(AgentRenameParams {
            target: target.clone(),
            name,
        }),
    })?)
}

fn agent_prompt(args: &[String]) -> std::io::Result<i32> {
    let Some(target) = args.first() else {
        eprintln!("usage: herdr agent prompt <name> <text> [--wait] [--timeout MS]");
        return Ok(2);
    };
    let Some(text) = args.get(1) else {
        eprintln!("agent prompt requires text");
        return Ok(2);
    };
    let mut wait = false;
    let mut timeout_ms = None;
    let mut index = 2;
    while index < args.len() {
        match args[index].as_str() {
            "--wait" => {
                wait = true;
                index += 1;
            }
            "--timeout" => {
                let Some(value) = args.get(index + 1) else {
                    eprintln!("missing value for --timeout");
                    return Ok(2);
                };
                timeout_ms = Some(super::parse_u64_flag("--timeout", value)?);
                index += 2;
            }
            option => {
                eprintln!("unknown option: {option}");
                return Ok(2);
            }
        }
    }
    let mut response = super::send_request(&Request {
        id: "cli:agent:prompt".into(),
        method: Method::AgentPrompt(AgentPromptParams {
            target: target.clone(),
            text: text.clone(),
        }),
    })?;
    if response.get("error").is_some() || !wait {
        return super::print_response(&response);
    }
    let baseline_state_change_seq = response["result"]["baseline_state_change_seq"]
        .as_u64()
        .unwrap_or(0);
    let Some(terminal_id) = response["result"]["agent"]["terminal_id"].as_str() else {
        return super::print_response(&cli_agent_error(
            "cli:agent:prompt",
            "agent_prompt_failed",
            "agent prompt response did not include terminal_id",
        ));
    };
    let waited = match wait_for_named_agent(
        terminal_id,
        target,
        timeout_ms.map(Duration::from_millis),
        AgentWaitMode::AfterPrompt {
            baseline_state_change_seq,
        },
    ) {
        Ok(waited) => waited,
        Err(err) => {
            return print_agent_transport_error(
                err,
                "cli:agent:prompt",
                "agent_prompt_transport_failed",
            )
        }
    };
    match waited {
        Ok(agent) => {
            response["result"]["agent"] = agent;
            super::print_response(&response)
        }
        Err(error) => super::print_response(&error),
    }
}

fn agent_send(args: &[String]) -> std::io::Result<i32> {
    if args.len() < 2 {
        eprintln!("usage: herdr agent send <target> <text>");
        return Ok(2);
    }

    super::print_response(&super::send_request(&Request {
        id: "cli:agent:send".into(),
        method: Method::AgentSend(AgentSendParams {
            target: args[0].clone(),
            text: args[1..].join(" "),
        }),
    })?)
}

fn agent_read(args: &[String]) -> std::io::Result<i32> {
    let Some(target) = args.first() else {
        eprintln!("usage: herdr agent read <target> [--source visible|recent|recent-unwrapped] [--lines N] [--format text|ansi] [--ansi]");
        return Ok(2);
    };

    let mut source = ReadSource::Recent;
    let mut lines = None;
    let mut format = ReadFormat::Text;
    let mut strip_ansi = true;

    let mut index = 1;
    while index < args.len() {
        match args[index].as_str() {
            "--source" => {
                let Some(value) = args.get(index + 1) else {
                    eprintln!("missing value for --source");
                    return Ok(2);
                };
                source = super::parse_read_source(value)?;
                index += 2;
            }
            "--lines" => {
                let Some(value) = args.get(index + 1) else {
                    eprintln!("missing value for --lines");
                    return Ok(2);
                };
                lines = Some(super::parse_u32_flag("--lines", value)?);
                index += 2;
            }
            "--format" => {
                let Some(value) = args.get(index + 1) else {
                    eprintln!("missing value for --format");
                    return Ok(2);
                };
                format = super::parse_read_format(value)?;
                strip_ansi = !matches!(format, ReadFormat::Ansi);
                index += 2;
            }
            "--ansi" => {
                format = ReadFormat::Ansi;
                strip_ansi = false;
                index += 1;
            }
            other => {
                eprintln!("unknown option: {other}");
                return Ok(2);
            }
        }
    }

    super::print_response(&super::send_request(&Request {
        id: "cli:agent:read".into(),
        method: Method::AgentRead(AgentReadParams {
            target: target.clone(),
            source,
            lines,
            format,
            strip_ansi,
        }),
    })?)
}

fn print_agent_help() {
    eprintln!("herdr agent commands:");
    eprintln!("  herdr agent list");
    eprintln!("  herdr agent get <target>");
    eprintln!("  herdr agent read <target> [--source visible|recent|recent-unwrapped] [--lines N] [--format text|ansi] [--ansi]");
    eprintln!("  herdr agent send <target> <text>");
    eprintln!("  herdr agent prompt <name> <text> [--wait] [--timeout MS]");
    eprintln!("  herdr agent rename <target> <name>|--clear");
    eprintln!("  herdr agent focus <target>");
    eprintln!("  herdr agent wait <name> [--timeout MS]");
    eprintln!("  herdr agent attach <target> [--takeover]");
    eprintln!(
        "  herdr agent start <name> --kind KIND --pane ID [--timeout MS] [-- <agent-args...>]"
    );
    eprintln!("  herdr agent explain <target> [--json]");
    eprintln!("  herdr agent explain --file PATH --agent LABEL [--json]");
    eprintln!("  targets accept terminal ids, unique agent names, detected/reported agent labels, and legacy pane ids");
    eprintln!(
        "  agent send writes literal text; use pane run when you want command text plus Enter"
    );
}
