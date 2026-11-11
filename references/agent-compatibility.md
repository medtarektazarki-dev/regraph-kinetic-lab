# Agent capability and fallback guide

First identify the tools available in this session with a harmless read-only check. Do not assume another agent's commands, APIs, or permission model.

| Capability | Preferred path | Fallback |
| --- | --- | --- |
| Read/write project | Use the project workspace and its conventions | Return a prompt package or storyboard if writing is unavailable |
| Browse reference sites | Open the visible gallery and reference pages | Ask for a link, pasted prompt, or screenshots; label findings as unverified |
| View images/video | Inspect the preview and selected frames | Run technical checks only and state that visual review was unavailable |
| Run shell commands | Use existing project tools and dependencies | Provide commands for the user to run |
| Render video | Use the project's existing renderer | Deliver implementation or prompt package without claiming a render |

Never install an agent plugin, software, package, or skill simply because a reference page mentions it. Ask or follow an already-authorized setup request. Do not lower security settings or expose project files to third-party services. Keep source media local when possible.

Report missing capabilities only when they affect the deliverable. Do not claim to have watched, rendered, measured, or verified anything that was not actually observed.
