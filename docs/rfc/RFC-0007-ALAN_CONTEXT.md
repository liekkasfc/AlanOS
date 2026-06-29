# RFC-0007: Alan Context

## Status
Draft

## Date
2026-06-29

## Summary
This RFC defines Alan Context: the personal information Alan OS needs in order to choose better opportunities for Alan specifically.

Alan Context is not generic user profiling. It exists to improve MoneyDNA, Today's Bet selection, validation plans, and AlanMemory updates.

The goal is to help Alan move faster from information gap to validated revenue signal by choosing bets he can actually execute.

## Context Principle
Alan OS should only ask for or store Alan Context when it can improve one of these decisions:

- whether Alan can reach the buyer,
- whether Alan can credibly make the offer,
- whether Alan can deliver a manual service before building,
- whether the opportunity fits Alan's skills and constraints,
- whether the validation action can happen today,
- what lesson should update AlanMemory.

Context that does not improve revenue validation should be omitted.

## Required Context Areas

### Skills
Capabilities Alan can use to create value manually.

Examples:

- writing,
- product thinking,
- AI workflow design,
- software prototyping,
- bilingual communication,
- research synthesis,
- customer conversation.

### Networks
People, communities, and channels Alan can reach with low friction.

Examples:

- founders,
- builders,
- operators,
- AI tool users,
- Chinese and English communities,
- past collaborators,
- warm intros.

### Credibility
Reasons a buyer might trust Alan enough to reply, talk, or pay.

Examples:

- relevant experience,
- clear writing,
- public artifacts,
- useful prior work,
- shared community,
- domain fluency.

### Constraints
Limits that affect Today's Bet and validation planning.

Examples:

- available time,
- energy,
- language,
- geography,
- budget,
- preferred channels,
- delivery capacity,
- risk tolerance.

### Service Inventory
Manual offers Alan can deliver before building software.

Examples:

- audit,
- teardown,
- readiness review,
- workflow mapping,
- buyer language rewrite,
- compliance checklist cleanup,
- small implementation sprint.

### Anti-Patterns
Opportunity types that repeatedly waste Alan's time or produce weak signals.

Examples:

- ideas with no reachable buyer,
- topics Alan researches but avoids selling,
- products that require too much building before contact,
- segments with weak urgency,
- channels Alan cannot use consistently.

## Context Use in the Workflow

### During Opportunity Scoring
Alan Context informs MoneyDNA:

- skill fit,
- network fit,
- credibility fit,
- interest fit,
- speed to execute,
- delivery risk,
- personal edge,
- anti-patterns.

### During Today's Bet Selection
Alan Context should bias toward bets that Alan can execute today with real buyer contact.

The system should prefer a slightly smaller bet Alan will execute over a more impressive bet that requires setup, confidence, or product work.

### During Validation Planning
Alan Context should shape:

- target personas,
- outreach channel,
- message language,
- offer framing,
- timebox,
- give-up rule,
- success threshold.

### During Learning
Alan Context should update from results:

- which segments responded,
- which language produced serious replies,
- which offers felt easy or hard to deliver,
- which constraints blocked execution,
- which patterns should be repeated or avoided.

## Privacy and Boundary Rules
Alan Context may include sensitive personal and professional information. It should be treated as private working memory.

The system should:

- store only context that improves validation decisions,
- avoid unnecessary personal detail,
- keep buyer-facing output separate from private reasoning,
- never expose private constraints in outreach scripts unless Alan chooses to,
- prefer explicit AlanMemory updates over vague personality claims.

## Missing Context Rule
When Alan Context is missing, Alan OS should not stall unless the missing fact would change Today's Bet.

Good questions are narrow:

- Can Alan reach this buyer today?
- Can Alan credibly offer this service manually?
- Does Alan have 60 minutes for this validation action?
- Is this segment inside an existing network?

Bad questions create profile-building instead of revenue validation.

## Acceptance Criteria
Alan Context is successful when:

- MoneyDNA scores are more personal and less generic,
- Today's Bet becomes easier for Alan to execute,
- validation plans match Alan's real constraints,
- repeated rejection updates future selection,
- context stays focused on revenue validation rather than identity modeling,
- AlanMemory compounds from actual outcomes.
